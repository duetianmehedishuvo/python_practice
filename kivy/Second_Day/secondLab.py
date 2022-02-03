from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('my.kv')

class MyGridLayout(Widget):
    
    def press(self):
        name=self.ids.name.text
        food=self.ids.food.text
        #self.checkValue=False
        checkValue=str(self.ids.checkValue.active)
        print("Hello "+name+" , your favourite food is "+food+" Check Value "+checkValue)
        self.ids.name.text=""
        self.ids.food.text=""
        
    def checkbox_click(self,instance,value):
        print(value)

class Visual(App):
    def build(self):
        return MyGridLayout()
    
if __name__=="__main__":
    Visual().run()