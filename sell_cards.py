import pyautogui
import time
from progress.bar import Bar

waittime = 1.5


class Sell_Bot():

    def __init__(self):
        self.cards = int
        print("\nSteam Trading Card Bot V1\n")

    def locate_button(self, image):
        x, y = pyautogui.locateCenterOnScreen(image, confidence=.7)
        pyautogui.click(x=x, y=y)
        time.sleep(waittime)

    def cards_to_gems(self):
        try:
            self.cards = int(
                input("\nHow many cards do you want to turn into gems?\n"))
            bar = Bar('\nProcessing', max=self.cards)
            for _ in range(self.cards):
                pyautogui.moveTo(x=226, y=361)
                pyautogui.click()
                time.sleep(waittime)
                self.locate_button("capture.png")
                self.locate_button("green-ok.png")
                self.locate_button("grey-ok.png")
                bar.next()
            bar.finish()

            repeat = input("\nWould you like to convert more?\nY/N\n").upper()
            if "Y" in repeat:
                self.cards_to_gems()

            else:
                print("\nShutting Down...")
                pass
        except KeyboardInterrupt:
            print("\nShutting Down...")
            pass


bot = Sell_Bot()
bot.cards_to_gems()
