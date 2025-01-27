from pygame import *
import os


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("data/block.gif")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("data/kol.png")


class BlockAct(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("data/knopka.png")


class END(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("data/p0.gif")




#class Door(Platform):
 #   def __init__(self, x, y):
 #       Platform.__init__(self, x, y)
  #      self.image = image.load("data/knopka.png")