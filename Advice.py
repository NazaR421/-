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
        lab_name = Label(text="Доброго дня!Я порадник і я допоможу вам вибрати машину\n(натисніть далі щоб обрати цінову категорію)", 
                         size_hint=(0.9,1), pos_hint={"y":0.1,"x":0.05})
        but_car=Button(text="Далі",
                       size_hint=(0.3,0.2),pos_hint={"x":0.33,"y":0.1})
        line.add_widget(lab_name)
        line.add_widget(but_car)
        self.add_widget(line)
        but_car.on_press=self.next
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="car"

class Car(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_name = Label(text="Давайте виберем цінову категорію ", 
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
        lanos = Label(text="1)Daewoo Lanos 2007 1 покоління ціна 2000$-пробіг 171 тис. км.Паливо Бензин.Об'єм двигуна 1.35 л\nКоробка механіка.Знаходиться в Жидачів, Львівська обл.Номер продавця-(096)6971441", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.7,"x":0.345})
        passat= Label(text="2)Volkswagen Passat 2014 1 покоління ціна 10900$-пробіг 194 тис. км.Паливо Бензин.Об'єм двигуна 1.8 л\nКоробка типтронік.Знаходиться в м.Одесі.Номер продавця-(098)1998711", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.6,"x":0.365})
        golf= Label(text="3)Volkswagen Golf 1999 ціна 2999$-пробіг 237 тис. км.Паливо Бензин.Об'єм двигуна 1.39 л\nКоробка механіка.Знаходиться м.Львів.Номер продавця-(097)4363177",
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.3})
        audi= Label(text="4)Audi A4 2003 ціна 5900$-пробіг 153 тис. км.Паливо Бензин.Об'єм двигуна 2.0 л\nКоробка автомат.Знаходиться в Сміла, Черкаська обл.Номер продавця-(066)1320826", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.4,"x":0.28})
        mitsubishi= Label(text="5)Mitsubishi Outlander 2008 ціна 7600$-пробіг 153 тис. км.Паливо Газ/Бензин.Обєм двигуна 2.4л\nКоробка автомат.Знаходиться в м.Одеса.Номер продавця-(093)6043502",
                         size_hint=(0.2,0.05), pos_hint={"y":0.3,"x":0.325})
        btnresset=Button(text="Повернутися на першу сторінку",size_hint=(0.3,0.2),pos_hint={"x":0.33,"y":0.01})
        line.add_widget(lab_name)
        line.add_widget(lanos)
        line.add_widget(audi)
        line.add_widget(golf)
        line.add_widget(passat)
        line.add_widget(mitsubishi)
        line.add_widget(btnresset)
        self.add_widget(line)
        btnresset.on_press=self.next
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="one"
class MyApp(App):
    def build(self):
        main_screen= ScreenManager()
        main_screen.add_widget(One(name='one'))
        main_screen.add_widget(Car(name='car'))
        main_screen.add_widget(Car1(name="car1"))
        return main_screen


app = MyApp()
app.run()
