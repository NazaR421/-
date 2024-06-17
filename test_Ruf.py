from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from inst import *
p1,p2,p3=0,0,0


class One(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = instruct, 
                         size_hint=(1,0.45), pos_hint={"y":0.55})
        line.add_widget(lab_inst)
        lab_name = Label(text="Введіть імя", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.35,"x":0.1})
        lab_age = Label(text="Введіть вік", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.25,"x":0.1})
        name_input = TextInput(multiline=False, 
                         size_hint=(0.3,0.05), pos_hint={"y":0.35,"x":0.3})
        age_input = TextInput(multiline=False, 
                         size_hint=(0.3,0.05), pos_hint={"y":0.25,"x":0.3})
        but_go=Button(text="Почати",size_hint=(0.3,0.1), pos_hint={"y":0.02,"x":0.3})

        line.add_widget(lab_name)
        line.add_widget(lab_age)
        line.add_widget(name_input)
        line.add_widget(age_input)
        line.add_widget(but_go)

        self.add_widget(line)
        but_go.on_press=self.next
    def next(self):
        self.manager.transition.direction="up"
        self.manager.current="two"

class Two(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = instruct2, 
                         size_hint=(1,0.45), pos_hint={"y":0.55})
        line.add_widget(lab_inst)
        lab_name = Label(text="Введіть результат", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.35,"x":0.1})
        self.res_input = TextInput(multiline=False, 
                         size_hint=(0.3,0.05), pos_hint={"y":0.35,"x":0.3})
        but_go=Button(text="Продовжити",size_hint=(0.3,0.1), pos_hint={"y":0.02,"x":0.3})

        line.add_widget(lab_name)
        
        line.add_widget(self.res_input)
        line.add_widget(but_go)
        
        self.add_widget(line)
    
        but_go.on_press=self.next
    def next(self):
        global p1
        p1=int(self.res_input.text)
        self.manager.transition.direction="right"
        self.manager.current="three"

class Three(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = instruct3, 
                         size_hint=(1,0.45), pos_hint={"y":0.55})
        line.add_widget(lab_inst)
        
        but_go=Button(text="Продовжити",size_hint=(0.3,0.1), pos_hint={"y":0.02,"x":0.3})


        line.add_widget(but_go)
        
        self.add_widget(line)
    
        but_go.on_press=self.next
    def next(self):
        self.manager.transition.direction="right"
        self.manager.current="four"

class Four(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_inst = Label(text = instruct4, 
                         size_hint=(1,0.45), pos_hint={"y":0.55})
        line.add_widget(lab_inst)
        lab_name = Label(text="Результат", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.35,"x":0.1})
        lab_age = Label(text="Результат після відпочинку", 
                         size_hint=(0.2,0.05), pos_hint={"y":0.25,"x":0.1})
        res2_input = TextInput(multiline=False, 
                         size_hint=(0.3,0.05), pos_hint={"y":0.35,"x":0.3})
        res3_input = TextInput(multiline=False, 
                         size_hint=(0.3,0.05), pos_hint={"y":0.25,"x":0.3})
        but_go=Button(text="Завершити",size_hint=(0.3,0.1), pos_hint={"y":0.02,"x":0.3})

        line.add_widget(lab_name)
        line.add_widget(lab_age)
        line.add_widget(res2_input)
        line.add_widget(res3_input)
        line.add_widget(but_go)

        self.add_widget(line)
        but_go.on_press=self.next

    def next(self):
        self.manager.transition.direction="down"
        self.manager.current="five"

class Five(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_inst = Label(text = instruct5, 
                         size_hint=(1,0.45), pos_hint={"y":0.55})
        line.add_widget(lab_inst)

       
        self.add_widget(line)

class MyApp(App):
    def build(self):
        main_screen= ScreenManager()
        main_screen.add_widget(One(name='one'))
        main_screen.add_widget(Two(name='two'))
        main_screen.add_widget(Three(name='three'))
        main_screen.add_widget(Four(name='four'))
        main_screen.add_widget(Five(name='five'))
        return main_screen
    
app = MyApp()
app.run()
