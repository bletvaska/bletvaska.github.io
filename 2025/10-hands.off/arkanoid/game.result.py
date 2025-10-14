#!/usr/bin/env pgzrun
WIDTH = 640
HEIGHT = 480
TITLE = 'Arkanoid.py'

# create paddle
paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 3

# create ball
ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.dy = -1
ball.dx = 1
ball.speed = 5

# create bricks
bricks = []
for idx in range(10):
    brick = Actor('brick.red')
    brick.top = 0
    brick.left = idx * brick.width
    bricks.append(brick)

def update():
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.top <= 0:
        ball.dy *= -1
    elif ball.right >= WIDTH:
        ball.dx *= -1
#    elif ball.bottom >= HEIGHT:
#       ball.dy *= -1
    elif ball.left <= 0:
        ball.dx *= -1

    # god mode
    paddle.x = ball.x

    # colision detection
    for brick in bricks:
        if ball.colliderect(brick):
            ball.dy *= -1
            ball.top = brick.bottom
            bricks.remove(brick)
            break

    # are there any bricks?
    if len(bricks) == 0:
        print('Well Done!')
        quit()

    # ball at the bottom?
    if ball.bottom >= HEIGHT:
        print('Looser')
        quit()

    # move paddle
    if keyboard.left == True:
        paddle.x -= paddle.speed

        # test left border
        if paddle.left < 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x += paddle.speed

        # test right border
        if paddle.right > WIDTH:
            paddle.right = WIDTH

    # is paddle colision with ball?
    if paddle.colliderect(ball) == True:
        ball.bottom = paddle.top
        ball.dy *= -1

def draw():
    # screen.clear()
    screen.blit('background', (0, 0))
    for brick in bricks:
        brick.draw()
    ball.draw()
    paddle.draw()

