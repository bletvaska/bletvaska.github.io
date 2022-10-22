import random

WIDTH=288
HEIGHT=512
TITLE='Flap.py'

GRAVITY = 0.3
KICK = -6.5
GAP = 130


flappy = Actor('flappy')
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
flappy.vy = 0

pipe_upper = Actor('pipe.upper')
pipe_upper.left = WIDTH
pipe_upper.bottom = random.randint(72, 300)

pipe_lower = Actor('pipe.lower')
pipe_lower.left = WIDTH
pipe_lower.top = pipe_upper.bottom + GAP

def update():
    flappy.vy = flappy.vy + GRAVITY
    flappy.y = flappy.y + flappy.vy

    if flappy.top <= 0:
        print('Ta si si rozbil hlavicku')
        quit()

    if flappy.bottom >= HEIGHT:
        print('Ta si si osuchal brusko')
        quit()

    pipe_upper.x = pipe_upper.x - 1
    pipe_lower.x = pipe_lower.x - 1
    if pipe_upper.right <= 0:
        pipe_upper.left = WIDTH
        pipe_lower.left = WIDTH
        pipe_upper.bottom = random.randint(72, 300)
        pipe_lower.top = pipe_upper.bottom + GAP

    if flappy.colliderect(pipe_upper) or flappy.colliderect(pipe_lower):
        print('Hlavou trubku neprerazis.')
        quit()


def draw():
    screen.blit('background', (0, 0))

    pipe_upper.draw()
    pipe_lower.draw()
    flappy.draw()


def on_key_down():
    flappy.vy = KICK

