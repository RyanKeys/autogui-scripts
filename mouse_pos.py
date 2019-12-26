import pyautogui
import time
import sys


def show_mouse():
    title = "\n\nGetting current mouse position: \nPress CONTROL-C to quit."
    print(title)
    running = True
    while running:
        try:
            pos = pyautogui.position()
            print(f"{pos}", end='\r')

            time.sleep(.1)

        except KeyboardInterrupt:
            print(f"Shutting Down \nFinal mouse position:{pos}")
            break


def save_mouse_on_close(prompt):

    print(prompt)
    running = True
    while running:
        try:
            pos = pyautogui.position()
            print(f"{pos}", end='\r')

            time.sleep(.1)

        except KeyboardInterrupt:
            print(f"\nShutting Down \nFinal mouse position:{pos}\n")
            return pos.x, pos.y


if __name__ == "__main__":
    save_mouse_on_close("\nTest Script for mouse_pos.py!\n")
