from pygame import *
import pyganim
import os


LOVUSHKA_WIDTH = 32
LOVUSHKA_HEIGHT = 32
LOVUSHKA_COLOR = "#5110FF"


class Lovushka(sprite.Sprite):
    def __init__(self, x, y, left, maxLengthLeft, maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((LOVUSHKA_WIDTH, LOVUSHKA_HEIGHT))
        self.image = image.load("data/player.jpg")
        self.rect = Rect(x, y, LOVUSHKA_WIDTH, LOVUSHKA_HEIGHT)
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLengthLeft
        self.maxLengthUp = maxLengthUp
        self.xvel = left

    def update(self, platforms):
        self.rect.x += self.xvel
        self.collide(platforms)
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel


    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                self.xvel = - self.xvel
