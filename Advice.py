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
        lab_name = Label(text="Доброго дня!Я порадник.\n(Вибиріть категорію яку вам порадити)", 
                         size_hint=(0.9,1), pos_hint={"y":0.1,"x":0.05})
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
        lab_name = Label(text="Ви вибрали машини,давайте виберем цінову категорію ", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.6,"x":0.4})
        btn1=Button(text="1000$-10000$",size_hint=(0.15,0.15),pos_hint={"x":0.1,"y":0.1})
        btn2=Button(text="10000$-50000$",size_hint=(0.15,0.15),pos_hint={"x":0.45,"y":0.1})
        btn3=Button(text="50000$-100000$",size_hint=(0.15,0.15),pos_hint={"x":0.8,"y":0.1})
        line.add_widget(lab_name)
        line.add_widget(btn1)
        line.add_widget(btn2)
        line.add_widget(btn3)
        self.add_widget(line)
        btn1.on_press=self.next
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="car1"

class Car1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_name = Label(text="Ви вибрали цінову категорію 1000$-10000$.Знизу результат", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        lanos = Label(text="1)Daewoo lanos б/у-середня ціна-2000$", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.7,"x":0.09})
        passat= Label(text="2)Volkswagen Passat б/у-середня ціна 11000$", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.6,"x":0.11})
        golf= Label(text="3)Volkswagen Golf 2001-середня ціна 3700$", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.08})
        audi= Label(text="4)Audi A4 1999-середня ціна 3500$", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.09})
        #golf= Label(text="3)Volkswagen Golf 2001-середня ціна 3700$", 
                         #size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.09})
        line.add_widget(lab_name)
        line.add_widget(lanos)
        line.add_widget(audi)
        line.add_widget(golf)
        line.add_widget(passat)
        self.add_widget(line)

class MyApp(App):
    def build(self):
        main_screen= ScreenManager()
        main_screen.add_widget(One(name='one'))
        main_screen.add_widget(Car(name='car'))
        main_screen.add_widget(Car1(name="car1"))
        return main_screen


app = MyApp()
app.run()
