#!/usr/bin/env python
import arcade

WIDTH = 640
HEIGHT = 600
TITLE = 'Arkanoid'


class Arkanoid(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        
        # create ball
        self.ball = arcade.Sprite('images/ball.png')
        self.ball.center_x = WIDTH / 2
        self.ball.center_y = HEIGHT / 2
        self.ball.dx = 1
        self.ball.dy = 1
        self.ball.speed = 7
        
        # create bricks
        self.bricks = []
        for row in range(5):
            for col in range(10):
                brick = arcade.Sprite('images/brick.red.png')
                brick.left = col * brick.width
                brick.top = HEIGHT - row * brick.height
                self.bricks.append(brick)
                
        # create paddle
        self.paddle = arcade.Sprite('images/paddle.png')
        self.paddle.bottom = 0
        self.paddle.center_x = WIDTH / 2
        self.paddle.speed = 10
        self.paddle.dx = 0
           
    def on_draw(self):
        self.clear()
        self.ball.draw()
        for brick in self.bricks:
            brick.draw()
        self.paddle.draw()

    def on_update(self, dt):
        # update ball
        self.ball.center_x += self.ball.dx * self.ball.speed
        self.ball.center_y += self.ball.dy * self.ball.speed
        
        if self.ball.top > HEIGHT:
            self.ball.dy *= -1
        if self.ball.right > WIDTH:
            self.ball.dx *= -1
        if self.ball.bottom < 0:
            #self.ball.dy *= -1
            print('>> game over')
            quit()
        if self.ball.left < 0:
            self.ball.dx *= -1
            
        # collision detection
        for brick in self.bricks:
            if self.ball.collides_with_sprite(brick):
                self.bricks.remove(brick)
                self.ball.dy *= -1
                
        # success
        if len(self.bricks) == 0:
            print('>> well done')
            quit()
            
        # paddle update
        self.paddle.center_x += self.paddle.dx * self.paddle.speed
        if self.paddle.right > WIDTH:
            self.paddle.right = WIDTH
        if self.paddle.left < 0:
            self.paddle.left = 0
            
        if self.paddle.collides_with_sprite(self.ball):
            self.ball.dy *= -1
            self.ball.bottom = self.paddle.top
            
        # god mode
        self.paddle.center_x = self.ball.center_x
            
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.paddle.dx = -1
        if symbol == arcade.key.RIGHT:
            self.paddle.dx = 1
            
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.paddle.dx = 0
        if symbol == arcade.key.RIGHT:
            self.paddle.dx = 0

        
window = Arkanoid()
arcade.run()

