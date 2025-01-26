from pygame import *
import os
import sys
import argparse
import pyganim

import Lov
import block
import monsters


MOVE_SPEED = 4.5
WIDTH = 30
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 7
GRAVITY = 0.35
dead = False
WIN_WIDTH = 1000
WIN_HEIGHT = 608
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
data = open('data/xvel yvel.txt', 'w')
data.write('55 55')
data.close()
NEXT = False


class Player(sprite.Sprite):
    def __init__(self, x, y):
        self.imagesr = [(image.load('player/r0.png')), (image.load('player/r1.png')), (image.load('player/r2.png')),
                        (image.load('player/r3.png')), (image.load('player/r4.png'))]
        self.imagesl = [(image.load('player/l1.png')), (image.load('player/l2.png'))]
        self.images_stop = [(image.load('player/1s.gif'))]
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
        self.screen = display.set_mode(DISPLAY)
        self.f1 = font.Font(None, 150)
        self.text1 = self.f1.render('DEAD', True,
                      (0, 0, 0))


    def update(self, left, right, up, platforms):


        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER

        if left:
            self.xvel = -MOVE_SPEED
            self.index += 1
            if self.index >= 5 * len(self.imagesl):
                self.index = 0
            self.image = self.imagesl[self.index // 5]

        if right:
            self.xvel = MOVE_SPEED
            self.index += 1
            if self.index >= 7 * len(self.imagesr):
                self.index = 0
            self.image = self.imagesr[self.index // 7]


        if not (left or right):
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

        s = str(self.rect.x) + ' ' + str(self.rect.y)
        data = open('data/xvel yvel.txt', 'w')
        data.write(s)
        data.close()



    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, block.BlockDie) or isinstance(p,
                                                                monsters.Monster) or isinstance(p, Lov.Lovushka):
                    self.die()
                if isinstance(p, block.END):
                    global NEXT
                    NEXT = True

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
        time.wait(1000)
        self.teleporting(self.startX, self.startY)