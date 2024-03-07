from kivy.app import App
from kivy.uix.widget import Widget

"""
「xxx.kv」のxxx部分はclassの「XxxApp」の「Xxx」に対応している
 name "Pmk" is short name in ProjectManagement Kun
"""


class PmkGame(Widget):
    pass


class PmkApp(App):
    def build(self):
        return PmkGame()


if __name__ == "__main__":
    PmkApp().run()
