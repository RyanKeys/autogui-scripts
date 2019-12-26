import pyautogui
import time
from progress.bar import Bar
import mouse_pos

waittime = 1.5


class Sell_Bot():
    # Prompts
    card_prompt = "\nHow many cards do you want to turn into gems?\n"
    coord_prompt = "\n\nDisplaying mouse coordinates.\nWhen hovered over starting card, press CONTROL-C to start selling!\n\n"

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
                input(self.card_prompt))
            x_coord, y_coord = mouse_pos.save_mouse_on_close(self.coord_prompt)

            bar = Bar('Processing', max=self.cards)

            for _ in range(self.cards):
                pyautogui.moveTo(x=int(x_coord), y=int(y_coord))
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
