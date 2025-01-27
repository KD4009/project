from pygame import *
from pygame.display import update

import block

MOVE_SPEED = 8
WIDTH = 25
HEIGHT = 25
COLOR = "#888888"
bullets = []
Bul = False



class Bullet(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_alpha(0)
        self.yvel = 0
        self.shot = False
        self.open = False


    def update(self, shot, platforms, turn):
        global Bul
        data = open('data/xvel yvel.txt', encoding='utf-8').read()
        t = data.split()

        if shot and turn == 'right':
            self.image = image.load("player/zr.gif")
            self.rect.y = int(t[-1])
            self.rect.x = int(t[0])
            self.image.set_alpha(255)
            self.xvel = +MOVE_SPEED
            Bul = True
        if shot and turn == 'left':
            self.image = image.load("player/zl.gif")
            self.rect.y = int(t[-1])
            self.rect.x = int(t[0])
            self.image.set_alpha(255)
            self.xvel = -MOVE_SPEED
            Bul = True


        self.shot = False

        if not Bul:
            self.image.set_alpha(0)
            self.rect.y = int(t[-1])
            self.rect.x = int(t[0])

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)




    def collide(self, xvel, yvel, platforms):
        global Bul
        data = open('data/xvel yvel.txt', encoding='utf-8').read()
        t = data.split()
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, block.BlockAct):
                    self.rect.y = int(t[-1])
                    self.rect.x = int(t[0])
                    Bul = False

                else:
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.rect.y = int(t[-1])
                        self.rect.x = int(t[0])
                        Bul = False

                    if xvel < 0:
                        self.rect.left = p.rect.right
                        Bullet(int(t[0]), int(t[-1]))
                        self.rect.y = int(t[-1])
                        self.rect.x = int(t[0])
                        Bul = False
