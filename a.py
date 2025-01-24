def ob():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Shut")
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

    total_level_width = len(table[0][0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(table) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(60)

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
                main()

            if e.type == pygame.KEYUP and e.key == K_RETURN:
                shot = False
            #if e.type == KEYDOWN and e.key == pygame.K_k:
                #pygame.draw.rect(screen, (0, 255, 0), (xvel, yvel,
                #                                       text_w + 20, text_h + 20), 1)
            #if e.type == pygame.KEYUP and e.key == pygame.K_k:
               # blud = False


        screen.blit(bg, (0, 0))

        hero.update(left, right, up, platforms)
        bull.update(shot, platforms, turn)
        monsters.update(platforms)
        Lov.update(platforms)
        camera.update(hero) # центризируем камеру относительно персонажа# передвижение
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()