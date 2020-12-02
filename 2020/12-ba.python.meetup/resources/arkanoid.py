# https://codeshare.io/5wp86p
# import pgzrun
import random
WIDTH = 640
HEIGHT = 480
TITLE = 'Mocna hra'

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.dx = 1
ball.dy = -1
ball.speed = 5

paddle = Actor('paddle')
paddle.x = WIDTH / 2
paddle.bottom = HEIGHT
paddle.speed = 8

bricks = []
colors = ['red', 'purple', 'blue', 'yellow', 'green', 'grey']
for y in range(4):
    for x in range(10):
        color = random.choice(colors)
        brick = Actor(f'brick.{color}')
        brick.left = x * brick.width
        brick.top = y * brick.height
        bricks.append(brick)


def draw():
    #screen.clear()
    screen.blit('arkanoid.background', (0, 0))
    for brick in bricks:
        brick.draw()
    ball.draw()
    paddle.draw()

def update():
    ball.x = ball.x + ball.dx * ball.speed
    ball.y = ball.y + ball.dy * ball.speed

    if ball.right > WIDTH:
        ball.dx = -1

    elif ball.left < 0:
        ball.dx = +1

    if ball.top < 0:
        ball.dy = +1

    elif ball.bottom > HEIGHT:
        ball.dy = -1
        print('Looser')
        #quit()

    for  brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball.dy = -ball.dy
            break


    paddle.x = ball.x
    if keyboard.left == True:
        paddle.x -= paddle.speed

        if paddle.left < 0:
            paddle.left = 0

    if keyboard.right == True:
        paddle.x += paddle.speed

        if paddle.right > WIDTH:
            paddle.right = WIDTH

    if ball.colliderect(paddle):
        ball.dy *= -1

    if len(bricks) == 0:
        print('Well Done')
        quit()

    #print(ball.x, ball.y)

# pgzrun.go()
