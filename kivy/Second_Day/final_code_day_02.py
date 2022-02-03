# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:47:21 2022

@author: Mehedi Hasan Shuvo
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('final_design.kv')

class CustomGridLayout(Widget):
    
    def checkbox_click(self,instance,value):
        print(value)
        
    def submit(self):
        name=self.ids.name.text
        email=self.ids.email.text
        age=self.ids.age.text
        password=self.ids.password.text
        if self.ids.gender.active:
            self.gender="Male"
        else:
            self.gender="Female"
            
        print("Name : "+name+" Email: "+email+" Age: "+age+" Password: "+password+" Gender: "+self.gender)
        


class MyApp(App):
    def build(self):
        self.title="Login Screen"
        return CustomGridLayout()

if __name__=="__main__":
    MyApp().run()