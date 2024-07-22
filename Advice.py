from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class One(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_name = Label(text="Введіть імя", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.01})
        but_car=Button(text="Машини",
                       size_hint=(0.1,0.1),pos_hint={"x":0.1,"y":0.1})
        but_film=Button(text="Фільми",
                       size_hint=(0.1,0.1),pos_hint={"x":0.45,"y":0.1})
        but_game=Button(text="Ігри",
                       size_hint=(0.1,0.1),pos_hint={"x":0.8,"y":0.1})
        line.add_widget(lab_name)
        line.add_widget(but_car)
        line.add_widget(but_film)
        line.add_widget(but_game)
        self.add_widget(line)
        but_car.on_press=self.next
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="car"

class Car(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_name = Label(text="Ви вибрали машини", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.01})
        line.add_widget(lab_name)
        self.add_widget(line)

class MyApp(App):
    def build(self):
        main_screen= ScreenManager()
        main_screen.add_widget(One(name='one'))
        main_screen.add_widget(Car(name='car'))
        return main_screen


app = MyApp()
app.run()
