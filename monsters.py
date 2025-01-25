from pygame import *
import pyganim
import os


MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#5110FF"
ICON_DIR = os.path.dirname(__file__)

class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft, maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.images = [(image.load('player/m0.gif')), (image.load('player/m1.gif')), (image.load('player/m2.gif'))]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLengthLeft
        self.maxLengthUp = maxLengthUp
        self.xvel = left
        self.yvel = up


    def update(self, platforms):

        self.index += 1
        if self.index >= 7 * len(self.images):
            self.index = 0
        self.image = self.images[self.index // 7]

        self.rect.y += self.yvel
        self.rect.x += self.xvel

        self.collide(platforms)

        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel  # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                self.xvel = - self.xvel
                self.yvel = - self.yvel