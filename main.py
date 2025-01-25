import pygame
from pygame.constants import KEYDOWN, K_SPACE, K_RETURN, K_ESCAPE
import player
from player import *
from block import *
from bullet import *
from monsters import *
from Lov import *


import os
import sys
import argparse


FPS = 60
WIN_WIDTH = 1000
WIN_HEIGHT = 608
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#f2ebac"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6265"
direc = 'right'
shot = False
data = open('data/lvl1.txt', encoding='utf-8').read()
table = [r.split('\t') for r in data.split('\n')]

data2 = open('data/obuchenie.txt', encoding='utf-8').read()
table2 = [r.split('\t') for r in data2.split('\n')]


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def sc():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Sh")
    bg = pygame.image.load("data/back.png")
    screen.blit(bg, (0, 0))
    timer = pygame.time.Clock()

    button = pygame.Rect(WIN_WIDTH // 2 - 150, 300, 300, 50)
    smallfont = pygame.font.SysFont('Corbel', 40)
    text = smallfont.render('Новая игра', True, (0, 0, 0))

    button2 = pygame.Rect(WIN_WIDTH // 2 - 150, 375, 300, 50)
    text2 = smallfont.render('Продолжить', True, (0, 0, 0))

    button3 = pygame.Rect(WIN_WIDTH // 2 - 150, 450, 300, 50)
    text3 = smallfont.render('Обучение', True, (0, 0, 0))


    while 1:
        timer.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mouse_pos = e.pos
                if button.collidepoint(mouse_pos):
                    main()
                if button2.collidepoint(mouse_pos):
                    pass
                if button3.collidepoint(mouse_pos):
                    ob()


        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [150, 150, 150], button)
        elif not button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [255, 255, 255], button)

        if button2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [150, 150, 150], button2)
        elif not button2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [255, 255, 255], button2)

        if button3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [150, 150, 150], button3)
        elif not button3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, [255, 255, 255], button3)

        screen.blit(text, (WIN_WIDTH / 2 - 90, WIN_HEIGHT / 2))
        screen.blit(text2, (WIN_WIDTH / 2 - 105, 380))
        screen.blit(text3, (WIN_WIDTH / 2 - 85, 457))

        pygame.display.update()


def ob():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Jumper")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    bull = Bullet(55, 55)
    left = right = False
    turn = ''
    shot = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    entities.add(bull)

    timer = pygame.time.Clock()
    x = y = 0
    for row in table2:
        for col in row:
            for i in col:
                if i == "#":
                    rt = BlockAct(x, y)
                    entities.add(rt)
                    platforms.append(rt)

                if i == "<":
                    a = Lovushka(x, y, 2, 50, 15)
                    entities.add(a)
                    platforms.append(a)
                    Lov.add(a)

                if i == "*":
                    bd = BlockDie(x, y)
                    entities.add(bd)
                    platforms.append(bd)

                if i == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)

                if i == '%':
                    mn = Monster(x, y, 2, 2, 50, 15)
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

    total_level_width = len(table2[0][0]) * PLATFORM_WIDTH
    total_level_height = (len(table2))* PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == pygame.K_a:
                left = True
                turn = 'left'
            if e.type == KEYDOWN and e.key == pygame.K_d:
                right = True
                turn = 'right'
            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == pygame.KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYDOWN and e.key == K_RETURN:
                shot = True
            if e.type == pygame.KEYUP and e.key == K_RETURN:
                shot = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sc()
        screen.blit(bg, (0, 0))
        hero.update(left, right, up, platforms)
        bull.update(shot, platforms, turn)
        monsters.update(platforms)
        Lov.update(platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()


def main():
    f1 = pygame.font.Font(None, 50)
    text1 = f1.render('Hello Привет', True,
                      (0, 0, 0))
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Sh")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    bull = Bullet(55, 55)
    left = right = False
    turn = ''
    shot = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    entities.add(bull)

    timer = pygame.time.Clock()
    x = y = 0
    for row in table:
        for col in row:
            for i in col:
                if i == "#":
                    rt = BlockAct(x, y)
                    entities.add(rt)
                    platforms.append(rt)

                if i == "<":
                    a = Lovushka(x, y, 3, 100)
                    entities.add(a)
                    platforms.append(a)
                    Lov.add(a)

                if i == "*":
                    bd = BlockDie(x, y)
                    entities.add(bd)
                    platforms.append(bd)

                if i == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)

                if i == '%':
                    mn = Monster(x, y, 2, 2, 50, 15)
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

    total_level_width = len(table[0][0]) * PLATFORM_WIDTH
    total_level_height = len(table) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if dead:
                print('sdf')
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == pygame.K_a:
                left = True
                turn = 'left'
            if e.type == KEYDOWN and e.key == pygame.K_d:
                right = True
                turn = 'right'
            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == pygame.KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYDOWN and e.key == K_RETURN:
                shot = True
            if e.type == pygame.KEYUP and e.key == K_RETURN:
                shot = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sc()


        screen.blit(bg, (0, 0))


        hero.update(left, right, up, platforms)
        bull.update(shot, platforms, turn)
        monsters.update(platforms)
        Lov.update(platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()





monsters = pygame.sprite.Group()
Lov = pygame.sprite.Group()

if __name__ == "__main__":
    sc()