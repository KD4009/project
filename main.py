import pygame
from pygame.constants import KEYDOWN, K_SPACE, K_RETURN, K_ESCAPE
from player import *
from block import *
from bullet import *
from monsters import *
from Lov import *
import sqlite3
from money import *


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
lvl = ''
data2 = open('level/obuchenie.txt', encoding='utf-8').read()
table2 = [r.split('\t') for r in data2.split('\n')]
level_num = 1


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

def rez():
    smallfont = pygame.font.SysFont('TimesNewRoman', 50)
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Green hat")
    bg = pygame.image.load("data/back.png")
    screen.blit(bg, (0, 0))
    timer = pygame.time.Clock()

    button = pygame.Rect(55, 55, WIN_WIDTH - 110, 50)
    text = smallfont.render('Level                          Score', True, (0, 0, 0))

    button4 = pygame.Rect(50, 50, WIN_WIDTH - 100, WIN_HEIGHT -100)
    button5 = pygame.Rect(49, 49, WIN_WIDTH - 98, WIN_HEIGHT - 98)



    while 1:
        timer.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sc()



        pygame.draw.rect(screen, [255, 255, 255], button5)
        pygame.draw.rect(screen, [0, 0, 0], button4)
        pygame.draw.rect(screen, [255, 255, 0], button)
        screen.blit(text, (55, 50))
        for i in range(2):
            con = sqlite3.connect("BD.sqlite")
            cur = con.cursor()
            result = cur.execute(f"""SELECT lvl FROM score
                                                    WHERE lvl == {i + 1}""").fetchall()
            result1 = cur.execute(f"""SELECT score FROM score
                                                                WHERE lvl == {i + 1}""").fetchall()
            for elem in result:
                lvl = elem[0]
            for elem1 in result1:
                lvl1 = elem1[0]
            con.close()
            text1 = smallfont.render(f'{str(lvl)}                 {str(lvl1)}', True, (255, 255, 0))
            screen.blit(text1, (70, 55 + 60 * (i + 1)))
        pygame.display.update()


def sc():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Green hat")
    bg = pygame.image.load("data/back.png")
    screen.blit(bg, (0, 0))
    timer = pygame.time.Clock()

    button = pygame.Rect(WIN_WIDTH // 2 - 150, 300, 300, 50)
    smallfont = pygame.font.SysFont('Corbel', 40)
    text = smallfont.render('Новая игра', True, (0, 0, 0))

    button2 = pygame.Rect(WIN_WIDTH // 2 - 150, 375, 300, 50)
    text2 = smallfont.render('Результаты', True, (0, 0, 0))

    button3 = pygame.Rect(WIN_WIDTH // 2 - 150, 450, 300, 50)
    text3 = smallfont.render('Обучение', True, (0, 0, 0))

    smallfont1 = pygame.font.SysFont('TimesNewRoman', 85)
    text4 = smallfont1.render('МЕНЮ', True, (0, 0, 0))
    button4 = pygame.Rect(WIN_WIDTH // 2 - 140, 30, 300, 100)

    while 1:
        timer.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mouse_pos = e.pos
                global level_num
                if button.collidepoint(mouse_pos):
                    level_num = 1
                    main()
                if button2.collidepoint(mouse_pos):
                    rez()
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
        pygame.draw.rect(screen, [200, 200, 255], button4)
        screen.blit(text4, (WIN_WIDTH / 2 - 130, 40))
        pygame.display.update()


def ob():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND_COLOR))
    timer = pygame.time.Clock()
    bg = pygame.image.load("data/back.png")
    screen.blit(bg, (0, 0))
    bg1 = pygame.image.load("data/prav.png")
    screen.blit(bg1, (100, 75))
    while 1:
        timer.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sc()
        pygame.display.update()


def main():
    global level_num
    global lvl
    score = 0

    con = sqlite3.connect("data/BD.sqlite")
    cur = con.cursor()
    result = cur.execute(f"""SELECT lvl FROM level
                                            WHERE num == {level_num}""").fetchall()
    for elem in result:
        lvl = elem[0]
    con.close()
    data = open(lvl, encoding='utf-8').read()
    table = [r.split('\t') for r in data.split('\n')]
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    bull = Bullet(55, 55)
    left = right = False
    turn = ''
    shot = False
    up = False
    game_time = 0

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

                if i == "@":
                    rq = END(x, y)
                    entities.add(rq)
                    platforms.append(rq)

                if i == '%':
                    mn = Monster(x, y, 2, 2, 50, 15)
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)

                if i == '&':
                    mn = Money(x, y, 2, 2, 50, 15)
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

        game_time += 1
        screen.blit(bg, (0, 0))
        smallfont = pygame.font.SysFont('TimesNewRoman', 20)
        text = smallfont.render(f'time: {game_time}', True, (0, 0, 0))
        screen.blit(text, (50, 50))
        death = smallfont.render(f'deaths: {deaths}', True, (0, 0, 0))
        screen.blit(death, (WIN_WIDTH - 150, 50))
        hero.update(left, right, up, platforms)
        bull.update(shot, platforms, turn)
        monsters.update(platforms)
        Lov.update(platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()
        nex = open('data/next.txt', encoding='utf-8').readline()
        if nex == 'NEXT':

            data = open('data/next.txt', 'w')
            data.write('')
            data.close()
            level_num += 1
            main()


monsters = pygame.sprite.Group()
Lov = pygame.sprite.Group()

if __name__ == "__main__":
    sc()