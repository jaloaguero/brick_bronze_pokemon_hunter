#Deals with automating movement

import time
import pyautogui as pg
import pydirectinput as pd


def move_mouse(target_coordinates):
    x=target_coordinates[0]
    y=target_coordinates[1]

    #does it twice because no harm, and sometimes the window is not focused so this helps
    pd.move(x,y, duration=1)
    pd.click(x,y, duration=1)
    pd.click()
    #pd.move(x,y, duration=1)

def idle_game():
    while True:
        x = 100
        y = 100

        pd.move(x,y, duration=2)
        pd.click(x,y, duration=2)
        pd.click()
        time.sleep(8)
        pd.move(x+200,y, duration=2)
        pd.click(x+200,y, duration=2)
        pd.click()
        time.sleep(8)

def press_keys(key_press, hold_time):
    start = time.time()

    while time.time() - start < hold_time:
        pd.press(key_press)

def get_screen_size():
    return pg.size()