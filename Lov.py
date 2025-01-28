from pygame import *
import os


LOVUSHKA_WIDTH = 32
LOVUSHKA_HEIGHT = 32
LOVUSHKA_COLOR = "#5110FF"


class Lovushka(sprite.Sprite):
    def __init__(self, x, y, left, maxLengthLeft):
        sprite.Sprite.__init__(self)
        self.image = Surface((LOVUSHKA_WIDTH, LOVUSHKA_HEIGHT))
        self.rect = Rect(x, y, LOVUSHKA_WIDTH, LOVUSHKA_HEIGHT)
        self.images = [(image.load('player/e0.gif')), (image.load('player/e1.gif'))]
        self.imagesr = [(image.load('player/e2.gif')), (image.load('player/e3.gif')), (image.load('player/e2.gif'))]
        self.index = 0
        self.colob = 0
        self.image = self.images[self.index]
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLengthLeft
        self.l = left
        self.xvel = left
        self.stop = False

    def update(self, platforms):
        self.index += 1
        self.colob += 1

        if self.colob >= 200:
            self.stop = True
        if self.colob >= 300:
            self.stop = False
            self.colob = 0
        if self.stop == True:
            self.rect.x += 0
            if self.index >= 7 * len(self.images):
                self.index = 0
            self.image = self.images[self.index // 7]
        if self.stop == False:
            self.rect.x += self.xvel
            if self.index >= 3 * len(self.imagesr):
                self.index = 0
            self.image = self.imagesr[self.index // 3]
        self.collide(platforms)
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel


    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                self.xvel = - self.xvel
