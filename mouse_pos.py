import pyautogui
import time
import sys


def mouse():
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


if __name__ == "__main__":
    mouse()
