# Example file showing a circle moving on screen
import pygame, sys, os, random, pyautogui, time, win32api, keyboard, win32con









time.sleep(2)
is_running = True


def click(x, y):
    
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    


while is_running:
    if keyboard.is_pressed('H'):
        is_running = False

    if pyautogui.pixel(2386, 423) [0] == 74:
        click(2386, 423)
    if pyautogui.pixel(2569, 423) [0] == 74:
        click(2569,423)
    if pyautogui.pixel(2741, 423) [0] == 74:
        click(2741, 423)
    if pyautogui.pixel(2938, 423) [0] == 74:
        click(2938, 423)
###############################################################
    if pyautogui.pixel(2386, 600) [0] == 74:
        click(2386, 600)
    if pyautogui.pixel(2569, 600) [0] == 74:
        click(2569,600)
    if pyautogui.pixel(2741, 600) [0] == 74:
        click(2741, 600)
    if pyautogui.pixel(2938, 600) [0] == 74:
        click(2938, 600)
   #####################################################
    if pyautogui.pixel(2386, 800) [0] == 74:
        click(2386, 800)
    if pyautogui.pixel(2569, 800) [0] == 74:
        click(2569,800)
    if pyautogui.pixel(2741, 800) [0] == 74:
        click(2741, 800)
    if pyautogui.pixel(2938, 800) [0] == 74:
        click(2938, 800)
   ############################################################
    if pyautogui.pixel(2386, 1000) [0] == 74:
        click(2386, 1000)
    if pyautogui.pixel(2569, 1000) [0] == 74:
        click(2569,1000)
    if pyautogui.pixel(2741, 1000) [0] == 74:
        click(2741, 1000)
    if pyautogui.pixel(2938, 1000) [0] == 74:
        click(2938, 1000)