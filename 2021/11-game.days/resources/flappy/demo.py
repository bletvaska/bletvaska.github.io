# Tu napíšte svoj kód :-)

import random
from time import sleep

TITLE = 'Flappy'
WIDTH = 288
HEIGHT = 512 + 100
GRAVITY = 0.3
KICK = -6.5
GAP = 130
GAME_SPEED = 2

# ground
ground1 = Actor('ground')
ground1.bottom = HEIGHT
ground2 = Actor('ground')
ground2.bottom = HEIGHT

# background
bg_x = 0

# ako flappy vyzera
flappy = Actor('flappy')
# pozicia flappyho
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
# flappyho rychlost
flappy.vy = 0
flappy.score = 0

pipe_upper = Actor('pipe.upper')
pipe_upper.left = WIDTH
pipe_upper.bottom = random.randint(72, 300)

pipe_lower = Actor('pipe.lower')
pipe_lower.left = WIDTH
pipe_lower.top = pipe_upper.bottom + GAP


def update():
    global bg_x
    # make parallax background
    bg_x -= GAME_SPEED / 10
    if bg_x == -WIDTH:
        bg_x = 0

    # make parallax ground
    ground1.x -= GAME_SPEED
    if ground1.right == 0:
        ground1.left = 0
    ground2.left = ground1.right

    # update flappy
    flappy.vy += GRAVITY
    flappy.y += flappy.vy

    if flappy.top <= 0:
        print('You are dead - contact with head!')
        quit()

    if flappy.bottom >= HEIGHT:
        print('You are dead - contact with zobak!')
        quit()

    pipe_upper.x -= GAME_SPEED
    pipe_lower.x -= GAME_SPEED
    if pipe_upper.right <= 0:
        # prehram zvuk
        sounds.ding.play()

        # pripocitam skore
        flappy.score += 1
        print(flappy.score)

        # presuniem trubky vpravo za okraj
        pipe_upper.left = WIDTH
        pipe_lower.left = WIDTH

        # nova vyska
        pipe_upper.bottom = random.randint(72, 300)
        pipe_lower.top = pipe_upper.bottom + GAP

    if flappy.colliderect(pipe_upper):
        print('You are dead - contact with horna  trubka!')
        quit()

    if flappy.colliderect(pipe_lower):
        print('You are dead - contact with dolna trubka!')
        quit()

def draw():
    global bg_x
    # draw background
    screen.blit('background', (bg_x,0))
    screen.blit('background', (bg_x + WIDTH, 0))

    # draw actors
    flappy.draw()
    pipe_upper.draw()
    pipe_lower.draw()

    # draw slider
    ground1.draw()
    ground2.draw()


def on_key_down():
    sounds.jump.play()
    flappy.vy = KICK
