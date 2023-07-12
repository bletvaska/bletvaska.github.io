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
        print('>> ta odrel si si brusko')
        quit()

    if flappy.top < 0:
        print('>> ta si si otrepal hlavicku')
        quit()

    horna_trubka.x = horna_trubka.x - 1
    if horna_trubka.right < 0:
        horna_trubka.left = WIDTH

    if flappy.colliderect(horna_trubka):
        print('>> hlavickou trubku neprerazis')
        quit()

def draw():
    screen.blit('background', (0,0))
    flappy.draw()
    horna_trubka.draw()

def on_key_down():
    flappy.vy = KICK
