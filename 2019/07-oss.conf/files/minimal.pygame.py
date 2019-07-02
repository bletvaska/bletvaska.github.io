import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()

# game loop
while running:
    # process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

    # update

    # render
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
