# Tu napíšte svoj kód :-)
WIDTH = 288
HEIGHT = 512
TITLE = 'flap.py'
GRAVITY = 0.3
KICK = -6.5

flappy = Actor('flappy')
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
flappy.vy = 0

horna_trubka = Actor('pipe.upper')
horna_trubka.left = WIDTH

def update():
    flappy.vy = flappy.vy + GRAVITY
    flappy.y = flappy.y + flappy.vy

    if flappy.bottom > HEIGHT:
        print('oskrel si si brusko')
        quit()

    if flappy.top <= 0:
        print('otrepal si si hlavicku')
        quit()

    horna_trubka.x = horna_trubka.x - 1
    if horna_trubka.right <= 0:
        horna_trubka.left = WIDTH

    if flappy.colliderect(horna_trubka):
        print('ta hlavou trubku neprerazis')
        quit()Z

def draw():
    screen.blit('background', (0,0))

    horna_trubka.draw()
    flappy.draw()


def on_key_down():
    flappy.vy = KICK


