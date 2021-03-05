import random

TITLE = 'Flappy'
WIDTH = 288
HEIGHT = 512
GRAVITY = 0.3
KICK = -6.5
GAP = 125 

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
    flappy.vy += GRAVITY
    flappy.y += flappy.vy
    
    if flappy.top <= 0:
        print('You are dead - contact with head!')
        quit()
        
    if flappy.bottom >= HEIGHT:
        print('You are dead - contact with zobak!')
        quit()
        
    pipe_upper.x -= 1
    pipe_lower.x -= 1
    if pipe_upper.right <= 0:
        # presuniem trubky vpravo za okraj
        pipe_upper.left = WIDTH
        pipe_lower.left = WIDTH
        
        # nova vyska
        pipe_upper.bottom = random.randint(72, 300)
        pipe_lower.top = pipe_upper.bottom + GAP
        
        # pripocitam skore
        flappy.score += 1
        print(flappy.score)
        
    if flappy.colliderect(pipe_upper):
        print('You are dead - contact with horna  trubka!')
        quit()
        
    if flappy.colliderect(pipe_lower):
        print('You are dead - contact with dolna trubka!')
        quit()
    
def draw():
    screen.blit('background', (0,0))
    flappy.draw()
    pipe_upper.draw()
    pipe_lower.draw()  
    
def on_key_down():
    flappy.vy = KICK