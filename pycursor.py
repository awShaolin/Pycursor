import pyautogui as pg
import random
import schedule
import time

def positions ():
    # sWidth, sHeight = pg.size()
    posX, posY = pg.position()
    return(posX, posY)


def movement ():
    r = int(random.randint(4, 10))

    for i in range (1, int(r)):
        step = random.randint(50, 100)
        time = 0.5 + random.uniform(0, 0.1)
        x = random.randrange(100, 1800, step)
        y = random.randrange(100, 900, step)
        pg.moveTo(x, y, time)
    

def main ():
    schedule.every(15).seconds.do(movement)

    while True:
        schedule.run_pending()
        time.sleep(1)
   

if __name__ == '__main__':
    main()