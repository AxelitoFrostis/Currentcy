import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

import requests
import json
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
#import string

class Currency ():
    def __init__(self, currency, display):
        self.currency = str(currency) #Ex. usd
        self.display = str(display)#Ex. sek
        if not hasattr(self, "value"):
            self.fetchCurrency()

    def fetchCurrency (self):
        url = f"https://free.currconv.com/api/v7/convert?q={self.currency.upper()}_{self.display.upper()}&compact=ultra&apiKey=04191b9ff33b80ab3791"
        r = requests.request("GET", url)
        rawJSON = r.text
        parsedJSON = json.loads(rawJSON)
        self.value = parsedJSON[f"{self.currency.upper()}_{self.display.upper()}"]
        print(self.value)

usdtosek = Currency("usd", "sek")


class currentcy(App):
    def build(self):
        usdtosek = Currency("usd", "sek")
        return Label(text=usdtosek.value)

if __name__ == "__main__":
    currentcy().run()