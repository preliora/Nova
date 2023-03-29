import pyautogui
import os


def switchTab():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')


def press(button):
    pyautogui.keyDown(button)
    pyautogui.keyDown(button)
    pyautogui.keyUp(button)
    pyautogui.keyUp(button)



