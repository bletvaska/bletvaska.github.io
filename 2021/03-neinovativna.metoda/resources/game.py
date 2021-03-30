HEIGHT = 400
WIDTH = 640
TITLE = "Arkanoid"

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.speed = 5
ball.dx = 1
ball.dy = -1

paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 4

bricks = []
for i in range(10):
    brick = Actor('brick.red')
    brick.left = brick.width * i
    bricks.append(brick)

def update():
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.right >= WIDTH:
        ball.dx = -1

    if ball.top <= 0:
        ball.dy = +1

    if ball.left <= 0:
        ball.dx = +1

    if ball.bottom >= HEIGHT:
        print('Game over')
        quit()
        #ball.dy = -1

    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball.dy *= -1
            break

    if len(bricks) == 0:
        print('Well done')
        quit()

    # god mode
    paddle.x = ball.x

    if keyboard.left == True:
        paddle.x = paddle.x - paddle.speed
        if paddle.left <= 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x = paddle.x + paddle.speed
        if paddle.right >= WIDTH:
            paddle.right = WIDTH

    if paddle.colliderect(ball):
        ball.dy *= -1
        ball.bottom = paddle.top


def draw():
    screen.clear()

    for brick in bricks:
        brick.draw()

    ball.draw()
    paddle.draw()
