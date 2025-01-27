from pygame import *
import pyganim
import os

import bullet
from bullet import bullets

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#5110FF"
ICON_DIR = os.path.dirname(__file__)

class Mon(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.images = [(image.load('player/m0.gif')), (image.load('player/m1.gif')), (image.load('player/m2.gif'))]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.startX = x
        self.startY = y


    def update(self, platforms):
        self.index += 1
        if self.index >= 7 * len(self.images):
            self.index = 0
        self.image = self.images[self.index // 7]
        self.collide(platforms)


    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                if isinstance(p, bullet.Bullet):
                    print('sd')