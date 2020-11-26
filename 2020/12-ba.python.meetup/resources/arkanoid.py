from time import sleep

WIDTH = 640
HEIGHT = 480
TITLE = 'GVPT SPST Arkanoid MT'

ball = Actor('ball')
ball.x = WIDTH / 2 - 100
ball.y = HEIGHT / 2

ball.dx = 1
ball.dy = -1
ball.speed = 3

bricks = []
for x in range(10):
    brick = Actor('brick.red')
    brick.left = brick.width * x
    bricks.append(brick)

def update():
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.top <= 0:
        ball.dy *= -1
    elif ball.bottom >= HEIGHT:
        ball.dy *= -1
    elif ball.left <= 0:
        ball.dx *= -1
    elif ball.right >= WIDTH:
        ball.dx *= -1

    for brick in bricks:
        if ball.colliderect(brick) == True:
            ball.dy *= -1
            bricks.remove(brick)


def draw():
    screen.clear()
    ball.draw()

    for brick in bricks:
        brick.draw()
