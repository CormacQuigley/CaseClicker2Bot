import time
import bot
from pynput.mouse import Button, Controller

if __name__ == '__main__':
    bot.run_discord_bot()

mouse = Controller()


def mouse_position():
    print(mouse.position)


def auto_click():
    mouse.position = (231, 410)
    mouse.click(Button.left, 1)


def buy_factory():
    mouse.position = (1331, 590)
    mouse.click(Button.left, 2)


def buy_upgrades():
    mouse.position = (1242, 234)
    mouse.click(Button.left, 2)


def biggest_upgrades():
    mouse.position = (1356, 760)
    mouse.click(Button.left, 2)


def secondbiggest_upgrades():
    mouse.position = (1341, 710)
    mouse.click(Button.left, 2)


def bank_upgrades():
    mouse.position = (1329, 650)
    mouse.click(Button.left, 2)


def case_clicker():
    mouse.click(Button.left, 1)
