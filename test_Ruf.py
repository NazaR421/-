from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from inst import *

class One(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_inst = Label(text=instruct,size_hint=(1,0.45),pos_hint={"y":0.55})
        line.add_widget(lab_inst)

        lab_name=Label(text="Введіть імя",size_hint=(0.2,0.05),pos_hint={"y":0.35,"x":0.1})
        lab_age=Label(text="Введіть вік",size_hint=(0.2,0.05),pos_hint={"y":0.25,"x":0.1})
        line.add_widget(lab_name)
        line.add_widget(lab_age)

        name_input=TextInput(multiline=False,size_hint=(0.3,0.05),pos_hint={"y":0.35,"x":0.3})
        line.add_widget(name_input)


        self.add_widget(line)
class MyApp(App):
    def build(self):
        main_screen=ScreenManager()
        main_screen.add_widget(One(name="one"))
        return main_screen
    
app=MyApp()
app.run()
