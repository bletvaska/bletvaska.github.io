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