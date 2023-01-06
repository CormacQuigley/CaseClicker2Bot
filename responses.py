import random
import CaseClicker
from pynput.mouse import Button, Controller, Listener
import time

mouse = Controller()


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '1':
        return CaseClicker.case_clicker()

    if p_message == '2':
        return CaseClicker.autoclick()

    if p_message == '3':
        return CaseClicker.bot_cycle()

    if p_message == '4':
        return CaseClicker.buy_max()

    if p_message == '5':
        return CaseClicker.buy_min()

    if p_message == '6':
        return CaseClicker.buy_case()

    if p_message == '7':
        return CaseClicker.mouse_position()
