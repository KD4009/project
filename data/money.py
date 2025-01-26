from pygame import *
import player
import os


MONEY_WIDTH = 32
MONEY_HEIGHT = 32
MONEY_COLOR = "#5110FF"
ICON_DIR = os.path.dirname(__file__)

class Money(sprite.Sprite):
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


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, player.Player):
                    print('df')
