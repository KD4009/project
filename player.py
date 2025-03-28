from pygame import *
import os
import sys
import argparse

import monsters_2
import block
import coin
import monsters
from bullet import Poz


MOVE_SPEED = 4.5
WIDTH = 30
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 7
GRAVITY = 0.35
WIN_WIDTH = 1000
WIN_HEIGHT = 608
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


class Deaths():
    deaths = 0


class Next():
    NEXT = False


class Player(sprite.Sprite):
    def __init__(self, x, y):
        self.imagesr = [(image.load('player/r0.gif')), (image.load('player/r1.gif')),
                        (image.load('player/r2.gif')), (image.load('player/r3.gif'))]
        self.imagesl = [(image.load('player/l0.gif')), (image.load('player/l1.gif')),
                        (image.load('player/l2.gif')), (image.load('player/l3.gif'))]
        self.images_stop = [(image.load('player/s0.gif')), (image.load('player/s1.gif'))]
        self.images_jump = [(image.load('player/j.gif'))]
        self.index = 0
        self.image = self.imagesr[self.index]
        self.image_s = self.images_stop[self.index]
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = 55
        self.startY = 55
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False


    def update(self, left, right, up, platforms):

        if up:
            self.index += 1
            if self.index >= 5 * len(self.images_jump):
                self.index = 0
                self.image = self.images_jump[self.index // 5]
            if self.onGround:
                self.yvel = -JUMP_POWER

        if left:
            self.xvel = -MOVE_SPEED
            if not up:
                self.index += 1
                if self.index >= 5 * len(self.imagesl):
                    self.index = 0
                self.image = self.imagesl[self.index // 5]

        if right:
            self.xvel = MOVE_SPEED
            if not up:
                self.index += 1
                if self.index >= 4 * len(self.imagesr):
                    self.index = 0
                self.image = self.imagesr[self.index // 4]

        if not (left or right) and not up:
            self.xvel = 0
            self.index += 1
            if self.index >= 10 * len(self.images_stop):
                self.index = 0
            self.image = self.images_stop[self.index // 10]

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

        Poz.poz = str(self.rect.x) + ' ' + str(self.rect.y)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, block.BlockDie) or isinstance(p,
                                                                monsters.Monster) or isinstance(p, monsters_2.Lovushka)\
                        and not isinstance(p, coin.Mon):
                    self.die()
                elif isinstance(p, block.END):
                    Next.NEXT = True

                else:

                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY


    def die(self):
        global deaths
        Deaths.deaths += 1
        time.wait(500)
        self.teleporting(self.startX, self.startY)
