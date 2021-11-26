HEIGHT = 512
WIDTH = 288
TITLE = 'Flap.py'
GRAVITY = 0.3

flappy = Actor('flappy')
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
# flappyho rychlost
flappy.vy = 0

# horna trubka
pipe_upper = Actor('pipe.upper')
pipe_upper.left = WIDTH


def update():
    # aktualizacia flappyho
    flappy.vy = flappy.vy + GRAVITY
    flappy.y = flappy.y + flappy.vy

    # aktualizacia trubky
    pipe_upper.x = pipe_upper.x - 1
    if pipe_upper.right <= 0:
        pipe_upper.left = WIDTH

    # osetrenie kolizii
    if flappy.colliderect(pipe_upper):
        print('Ta si mrtvy')
        quit()


def draw():
    screen.blit('background', (0, 0))
    pipe_upper.draw()

    flappy.draw()


def on_key_down():
    sounds.jump.play()
    flappy.vy = -6.5
