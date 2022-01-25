from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class SayHello(App):
    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        
        # 0.7 mean top+bottom margins are 30%
        # 0.6 mean left and right margins are 40%
        
        self.window.size_hint=(0.6,0.7)
        
        # for Position
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        
        
        # add widget to window
        
        # image widget
        self.window.add_widget(Image(source="ehajj.png"))
        
        # Label Widget
        self.greeting=Label(
            text="What's your name?",
            font_size=18,
            color='#00FFCE'
            )
        self.window.add_widget(self.greeting)
        
        # text input Widget
        self.user=TextInput(
            multiline=False,
            padding_y=(20,20),
            size_hint=(1,0.5)
            )
        self.window.add_widget(self.user)
        
        #button Widget
        self.button=Button(
            text="GREET",
            size_hint=(1,0.5),
            bold=True,
            background_color='#00FFCE',
            background_normal=""
            )
        self.button.bind(on_press=self.callBackMethod)
        self.window.add_widget(self.button)
        
        return self.window
    
    def callBackMethod(self,instance):
        self.greeting.text="Hello "+self.user.text+"!"

if __name__=="__main__":
    SayHello().run()