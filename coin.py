from pygame import *
import os
from bullet import MyGlobals



MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#5110FF"
ICON_DIR = os.path.dirname(__file__)

class Mon(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.images = [(image.load('data/m0.gif')), (image.load('data/m1.gif'))]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.startX = x
        self.startY = y


    def update(self, platforms):
        self.image.set_alpha(255)
        self.index += 1
        if self.index >= 7 * len(self.images):
            self.index = 0
        self.image = self.images[self.index // 7]
        data2 = MyGlobals.MONEY
        if data2 == 1:
            self.image.set_alpha(0)
            self.rect.y -= 1000