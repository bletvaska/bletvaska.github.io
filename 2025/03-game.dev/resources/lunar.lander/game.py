HEIGHT = 708
WIDTH = 400
GRAVITY = 0.01
THRUST = 0.03

lander = Actor('lander2')
lander.x = WIDTH // 2
lander.vy = 0
lander.fuel = 100

thruster = Actor('thruster')
thruster.x = lander.x

def draw():
    screen.clear()
    altitude = int(HEIGHT - lander.y)
    velocity = abs(int(lander.vy * 100))
    screen.draw.text(f'Altitude: {altitude} m', (10, 10))
    screen.draw.text(f'Fuel: {lander.fuel} l', (10, 30))
    screen.draw.text(f'Velocity: {velocity} m/s', (10, 50))
    lander.draw()

    if keyboard.space and lander.fuel > 0:
        thruster.top = lander.bottom
        thruster.draw()


def update():
    lander.vy += GRAVITY
    lander.y += lander.vy

    if keyboard.space and lander.fuel > 0:
        lander.vy -= THRUST
        lander.fuel -= 0.5

    if HEIGHT - 5 <= lander.bottom < HEIGHT + 5:
        if lander.vy < 0.5:
            print('landed')
        else:
            print('crash')
        print(lander.vy)
        quit()

