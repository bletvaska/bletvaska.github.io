# Tu napíšte svoj kód :-)
HEIGHT = 480
WIDTH = 640
TITLE = "Arkanoid.py"

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.dx = 1
ball.dy = -1
ball.speed = 5

paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 7

bricks = []
for i in range(10):
    brick = Actor('brick.red')
    brick.left = i * brick.width
    bricks.append(brick)

def update():
    # process input
    if keyboard.left == True:
        paddle.x = paddle.x - paddle.speed

        if paddle.left < 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x = paddle.x + paddle.speed

        if paddle.right > WIDTH:
            paddle.right = WIDTH

    # update game
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.right >= WIDTH:
        ball.dx = -1
    elif ball.left <= 0:
        ball.dx = 1

    if ball.top <= 0:
        ball.dy = 1
    elif ball.bottom >= HEIGHT:
        # ball.dy = -1
        print('Game Over')
        quit()

    # collision detection paddle vs ball
    if paddle.colliderect(ball) == True:
        ball.bottom = paddle.top
        ball.dy = -1

    # collision detection brick vs ball
    for brick in bricks:
        if ball.colliderect(brick) == True:
            ball.top = brick.bottom
            ball.dy = 1
            bricks.remove(brick)
            break

    # well done?
    if len(bricks) == 0:
        print('Well Done')
        quit()


def draw():
    # screen.clear()
    screen.blit('background', (0, 0))
    ball.draw()
    paddle.draw()

    for brick in bricks:
        brick.draw()

