#!/usr/bin/env pgzrun

# window's attributes
TITLE = 'Arkanoid.py'
WIDTH = 640
HEIGHT = 400

# ball's attributes
ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.dx = 1
ball.dy = -1
ball.speed = 3

# paddle's attributes
paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 3

# creating bricks
bricks = []
for i in range(10):
    brick = Actor('brick.red')
    brick.left = brick.width * i
    bricks.append(brick)


def update():
    # update ball
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.top <= 0:
        ball.dy = 1

    if ball.right >= WIDTH:
        ball.dx = -1

    if ball.bottom >= HEIGHT:
        #ball.dy = -1
        print('You are Loser')
        quit()

    if ball.left <= 0:
        ball.dx = 1

    if ball.colliderect(paddle):
        ball.dy = ball.dy * -1

    # update brick
    for brick in bricks:
        if ball.colliderect(brick) == True:
            bricks.remove(brick)
            ball.dy = ball.dy * -1
            break

    # well done
    if len(bricks) == 0:
        print('weel done')
        quit()

    # update paddle
    if keyboard.left == True:
        paddle.x = paddle.x - paddle.speed
        if paddle.left <= 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x = paddle.x + paddle.speed
        if paddle.right >= WIDTH:
            paddle.right = WIDTH

    paddle.x = ball.x


def draw():
    screen.clear()

    for brick in bricks:
        brick.draw()

    ball.draw()

    paddle.draw()
