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

