---
title: Programovanie v jazyku Python
layout: default
---

# {{ page.title }}

## Uhádni číslo, ktoré si myslím

```python
#!/usr/bin/env python3

from random import randint


def play_game(secret:int = 7):
    print('Myslím si číslo od "1" do \'20\'')
    tip = None
    attempts = 0
    
    while (secret != tip) and (attempts < 5):
        answer = input('Tvoj tip: ')
        tip = int(answer)
        
        if secret > tip:
            print('Hmm... Moje číslo je väčšie ako tvoje.')

        elif secret < tip:
            print('Hmm... Moje číslo je menšie ako tvoje.')

        else:
            print('Ta ty genius.')
            break

        attempts += 1
    else:
        print('si lama')


new_game = 'a'

while new_game == 'a':
    play_game(randint(1, 20))
    new_game = input('Chceš hrať znova? (a/n) ')
        
print('Díky, že si si zahral. Stav sa aj nabudúce.')
```


## Konzolové aplikácie s Curses

* ak pracujete v OS Windows, musíte si doinštalovať balík `windows-curses`:

  ```bash
  $ pip3 install windows-curses
  ```
* kniznica [curses](https://docs.python.org/3/library/curses.html) v jazyku Python

```python
from curses import wrapper, window
import curses
import time

def main(stdscr: window):
    # setup
    curses.curs_set(0)
    x = 70
    y = 0
    dx = 1
    dy = 1
    text = 'ahoj jano'


    while True:
        stdscr.clear()

        # update
        x += dx
        y += dy

        # get width and height
        height, width = stdscr.getmaxyx()
        if x + len(text) >= width - 1:
            x -= 1
            dx *= -1
        if x <= 0:
            x = 0
            dx *= -1
        if y >= height - 1:
            y -= 1
            dy *= -1
        if y <= 0:
            y = 0
            dy *= -1

        # render
        stdscr.addstr(y, x, text)
        stdscr.refresh()
        time.sleep(0.2)

    stdscr.getch()



wrapper(main)
```


## Hra Hadík v knižnici Curses

* [Snake Game In Python - Python Beginner Tutorial](https://www.python-engineer.com/posts/snake-game-in-python/)

```python
import curses
from random import randint

# setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0) # y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], '#')
# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, f' Score {score} ')
    # increase speed
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) 

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, 
                   curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) # append O(n)

    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # if snake runs over itself
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
print(f"Final score = {score}")
```


## Pygame Zero: Arkanoid

### Ako nainštalovať

* Ak používate *Raspberry Pi OS*, tak Pygame Zero je tam už nainštalované.

* Ak používate niektorú linuxovú distribúciu, nainštalujte si balíček `pgzero`.

* Všetci ostatní môžu nainštalovať Pygame Zero prostredníctvom správcu balíčkov jazyka Python s názvom `pip3`:

  ```bash
  $ pip3 install pgzero
  ```

**Poznámka:** Knižnica závisí od knižnice `sdl`. V linuxových distribúciách sa nainštaluje spolu s balíčkom `pgzero` ako závislosť. V prípade inštalácie cez `pip3` som si nie istý :-/


### Dokumentácia

* [Pygame Zero homepage](https://pygame-zero.readthedocs.io/) ([sk](https://pgzero-slovak.readthedocs.io/sk/latest/index.html))

* [Wireframe](https://wireframe.raspberrypi.org/) Magazine, [MagPi](https://www.raspberrypi.org/magpi/) Magazine

* [Mission Python](https://nostarch.com/missionpython) ([YouTube Video](https://www.youtube.com/watch?time_continue=2&v=_2aglIeW1kQ))

* [Tvorba počítačových hier s Pygame Zero](https://legacy.gitbook.com/book/bletvaska/tvorba-pocitacovych-hier-s-pygame-zero/details) - poznámky ku tvorivej dielni

* [Retro Gaming with Raspberry Pi](https://magpi.raspberrypi.org/books/retro-gaming) - 164 pages of Video Game Projects (ebook)

* [Pygame Zero: snadno použitelný nástroj určený pro výuku programování](https://www.root.cz/clanky/pygame-zero-snadno-pouzitelny-nastroj-urceny-pro-vyuku-programovani/) - časť seriálu [Jazyky pro výuku programování](https://www.root.cz/serialy/jazyky-pro-vyuku-programovani/) na portáli [root.cz](https://www.root.cz)

