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
        btn2.on_press=self.next1
        btn3.on_press=self.next7
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="car1"
        
    def next1(self):
        self.manager.transition.direction="up"
        self.manager.current="car2"
    def next7(self):
        self.manager.transition.direction="up"
        self.manager.current="car5"
    

class Car1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_name = Label(text="Ви вибрали цінову категорію 1000$-10000$.Знизу результат", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        lanos = Label(text="1)Daewoo Lanos 2007 1 покоління ціна 2.000$-пробіг 171 тис. км.Паливо Бензин.Об'єм двигуна 1.35 л\nКоробка механіка.Знаходиться в Жидачів, Львівська обл.Номер продавця-(096)6971441", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.7,"x":0.345})
        passat= Label(text="2)Volkswagen Passat 2014 1 покоління ціна 10.900$-пробіг 194 тис. км.Паливо Бензин.Об'єм двигуна 1.8 л\nКоробка типтронік.Знаходиться в м.Одесі.Номер продавця-(098)1998711", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.6,"x":0.365})
        golf= Label(text="3)Volkswagen Golf 1999 ціна 2.999$-пробіг 237 тис. км.Паливо Бензин.Об'єм двигуна 1.39 л\nКоробка механіка.Знаходиться м.Львів.Номер продавця-(097)4363177",
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.3})
        audi= Label(text="4)Audi A4 2003 ціна 5.900$-пробіг 153 тис. км.Паливо Бензин.Об'єм двигуна 2.0 л\nКоробка автомат.Знаходиться в Сміла, Черкаська обл.Номер продавця-(066)1320826", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.4,"x":0.28})
        mitsubishi= Label(text="5)Mitsubishi Outlander 2008 ціна 7.600$-пробіг 153 тис. км.Паливо Газ/Бензин.Обєм двигуна 2.4л\nКоробка автомат.Знаходиться в м.Одеса.Номер продавця-(093)6043502",
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
class Car2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        
        lab_name = Label(text="Ви вибрали цінову категорію 10000$-50000$.Виберіть тип машини.", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.4})
        sedan=Button(text="Седан",size_hint=(0.2,0.2),pos_hint={"x":0.2,"y":0.01})
        krosover=Button(text="Кроссовер",size_hint=(0.2,0.2),pos_hint={"x":0.6,"y":0.01})
       
        line.add_widget(lab_name)
        line.add_widget(sedan)
        line.add_widget(krosover)

        self.add_widget(line)
        sedan.on_press=self.next2
        krosover.on_press=self.next3

    def next2(self):
        self.manager.transition.direction="up"
        self.manager.current="car3"
    def next3(self):
        self.manager.transition.direction="down"
        self.manager.current="car4"
    def next4(self):
        self.manager.transition.direction="right"
        self.manager.current="car5"
class Car3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        self.add_widget(line)
        lab_name = Label(text="Ви вибрали седани, цінова категорія 10000$-50000$.Результат знизу.", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        bmw = Label(text="1)Bmw 3 Series 320i Steptronic ціна 48.830$.Пробіг-234000тис.км.Паливо бензин,2.0\nКоробка автомат. Знаходиться в м.Харків.Номер продавця-(0631068780)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.75,"x":0.27})
        Toyota = Label(text="2)Toyota Camry 2019 ціна 31.900$.Пробіг-107000тис.км.Паливо гібрид,2.5\nКоробка автомат. Знаходиться в м.Одеса.Номер продавця-(0950040409)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.63,"x":0.23})
        audi = Label(text="3)Audi A4 2018 ціна 20.999$Пробіг-128000тис.км.Паливо бензин,2.0\nКоробка автомат. Знаходиться в м.Тернопіль.Номер продавця-(0977610018)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.48,"x":0.24})
        volskwagen = Label(text="4)Volkswagen Passat 2021 ціна 27.900$.Пробіг-200000тис.км.Паливо дизель,2.0\nКоробка автомат.Знаходиться в м.Стрий.Номер продавця-(0664445555)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.33,"x":0.25})
        lexus = Label(text="5)Lexus ES 2021 ціна 38.000$.Пробіг-98000тис.км.Паливо гібрид,2.5\nКоробка варіатор.Знаходиться в м.Харків.Номер продавця-(0677298175)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.23,"x":0.221})
        return1=Button(text="Назад",size_hint=(0.3,0.2),pos_hint={"x":0.40,"y":0.01})
        line.add_widget(lab_name)
        line.add_widget(bmw)
        line.add_widget(Toyota)
        line.add_widget(audi)
        line.add_widget(volskwagen)
        line.add_widget(lexus)
        line.add_widget(return1)
        return1.on_press=self.next5
    def next5(self):
        self.manager.transition.direction="left"
        self.manager.current="one"

class Car4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        self.add_widget(line)
        lab_name = Label(text="Ви вибрали кросовери, цінова категорія 10000$-50000$.Результат знизу.", 
                                        size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        bmw = Label(text="1)BMW X5 2015 ціна 27.500$.Пробіг-256000тис.км.Паливо дизель 3.0\nКоробка автомат.Знаходиться в м.Чернівці.Номер продавця-(0505669106)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.75,"x":0.24 })
        Tesla = Label(text="2)Tesla Model X 2017 ціна 25.900$.Пробіг-121000тис.км.Паливо електрична 245кВт\nКоробка автомат.Знаходиться в м.Київ.Номер продавця-(0938218471)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.63,"x":0.27})
        audi = Label(text="3)Audi Q7 2018 ціна 35.000$.Пробіг-283000тисю.км.Паливо Дизель 3.0\nКоробка автомат. Знаходиться в Стрий,Львівська обл.Номер продавця-(0963649000)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.48,"x":0.282})
        Toyota = Label(text="4)Toyota Land Cruiser Prado 2010 ціна 25.000$.Пробіг-215000тис.км.Паливо дизель 3.0\nКоробка автомат. Знаходиться в м.Одеса.Номер продавця-(0955833367)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.33,"x":0.281})
        mazda = Label(text="5)Mazda CX-5 2020 ціна 21.399$.Пробіг 58000тис.км.Паливо бензин 2.5\nКоробка автомат.Знаходиться в м.Вінниця.Номер продавця-(0937314642)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.23,"x":0.23})
        return1=Button(text="Назад",size_hint=(0.3,0.2),pos_hint={"x":0.3,"y":0.01})
        line.add_widget(lab_name)
        line.add_widget(bmw)
        line.add_widget(Toyota)
        line.add_widget(audi)
        line.add_widget(Tesla)
        line.add_widget(mazda)
        line.add_widget(return1)
        return1.on_press=self.next5
    def next5(self):
        self.manager.transition.direction="down"
        self.manager.current="one"
class Car5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        
        lab_name = Label(text="Ви вибрали цінову категорію 10000$-50000$.Виберіть тип машини.", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.5,"x":0.4})
        sedan1=Button(text="Седан",size_hint=(0.2,0.2),pos_hint={"x":0.2,"y":0.01})
        krosover1=Button(text="Кроссовер",size_hint=(0.2,0.2),pos_hint={"x":0.6,"y":0.01})
       
        line.add_widget(lab_name)
        line.add_widget(sedan1)
        line.add_widget(krosover1)
        self.add_widget(line)
        sedan1.on_press=self.next6
        krosover1.on_press=self.next8
    def next6(self):
        self.manager.transition.direction="right"
        self.manager.current="car6"
    def next8(self):
        self.manager.transition.direction="left"
        self.manager.current="car7"

class Car6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        self.add_widget(line)
        lab_name = Label(text="Ви вибрали кросовери, цінова категорія 50000$-100000$.Результат знизу.", 
                                        size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        bmw = Label(text="1)BMW 5 Series 2021 ціна 60.000$.Пробіг-33000тис.км.Паливо бензин 3.0\nКоробка автомат.Знаходиться в м.Київ.Номер продавця-(0664440600) ", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.75,"x":0.23 })
        mercedes = Label(text="2)Mercedes-Benz E-Class 2022 ціна 65.000$.Пробіг-8000тис.км.Паливо гібрид 2.0\nКоробка автомат.Знаходиться в м.Київ.Номер продавця-(0678811555)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.63,"x":0.261})
        bmw2 = Label(text="3)BMW M3 2021 ціна 82.500$.Пробіг-32000тис.км.Паливо бензин 3.0\nКоробка автомат.Знаходиться в м.Київ.Номер продавця(0634814138)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.48,"x":0.211})
        Tycan = Label(text="4)Porsche Taycan 2022 ціна 78.000$тис.км.Електро.Коробка автомат.Знаходиться в м.Київ\nНомер продавця-(0960300013)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.33,"x":0.3})
        audi = Label(text="5)Audi S6 3.0 TDI Tiptronic Quattro S-Line 2024 ціна 94.000$.Нова\nПаливо дизель 3.0.Знаходиться в м.Одеса.Номер продавця(0632784598)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.23,"x":0.23})
        return1=Button(text="Назад",size_hint=(0.3,0.2),pos_hint={"x":0.3,"y":0.01})
        line.add_widget(lab_name)
        line.add_widget(bmw)
        line.add_widget(mercedes)
        line.add_widget(Tycan)
        line.add_widget(bmw2)
        line.add_widget(audi)
        line.add_widget(return1)
        return1.on_press=self.next9
    def next9(self):
        self.manager.transition.direction="down"
        self.manager.current="one"


class Car7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line=FloatLayout()
        self.add_widget(line)
        lab_name = Label(text="Ви вибрали кросовери, цінова категорія 50000$-100000$.Результат знизу.", 
                                        size_hint=(0.2,0.05), pos_hint={"y":0.9,"x":0.4})
        bmw = Label(text="1)BMW X5 2019 ціна 79.900$.Пробіг-118000тис.км.Паливо дизель 3.0\nКоробка автомат.Знаходиться в м.Одеса.Номер продавця-(0950040409)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.75,"x":0.22 })
        mercedes = Label(text="2)Mercedes-Benz G-Class 2012 ціна 71.000$.Пробіг-90000тис.км.Паливо бензин 5.5\nКоробка автомат.Знаходиться в м.Дніпро.Номер продавця(0973333080)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.63,"x":0.261})
        volkswagen = Label(text="3)Volkswagen Touareg 2018 ціна 56.000$.Пробіг-60000тис.км.Паливо дизель 3.0\nКоробка автомат.Знаходитьсяв м.Одеса.Номер продавця-(0950040409)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.48,"x":0.25})
        Tycan = Label(text="4)Toyota Land Cruiser 2017 ціна 61.500.Пробіг-82000тис.км.Паливо дизель 4.5\nКоробка автомат.Знаходиться м.Київ.Номер продавця-(0681970707)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.33,"x":0.24})
        audi = Label(text="5)Audi Q8 2020 ціна 75.000$.Пробіг-53000тис.км.Паливо дизель 3.0\nКоробка автомат.Знаходиться в м.Луцьк.Номер продавця(0506026605)", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.23,"x":0.223})
        return1=Button(text="Назад",size_hint=(0.3,0.2),pos_hint={"x":0.3,"y":0.01})
        line.add_widget(lab_name)
        line.add_widget(bmw)
        line.add_widget(mercedes)
        line.add_widget(Tycan)
        line.add_widget(volkswagen)
        line.add_widget(audi)
        line.add_widget(return1)
        return1.on_press=self.next11
    def next11(self):
        self.manager.transition.direction="down"
        self.manager.current="one"
class MyApp(App):
    def build(self):
        main_screen= ScreenManager()
        main_screen.add_widget(One(name='one'))
        main_screen.add_widget(Car(name='car'))
        main_screen.add_widget(Car1(name="car1")) 
        main_screen.add_widget(Car2(name="car2"))
        main_screen.add_widget(Car3(name="car3"))
        main_screen.add_widget(Car4(name="car4"))
        main_screen.add_widget(Car5(name="car5"))
        main_screen.add_widget(Car6(name="car6"))
        main_screen.add_widget(Car7(name="car7"))
        return main_screen
    


app = MyApp()
app.run()
