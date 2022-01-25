from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class FunCLass(App):
    
    def build(self):
        
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={'center_x':0.5,'center_y':0.5}
        
        # add Widget to window
        self.image=Image(source="image.jfif")
        self.window.add_widget(self.image)
        
        # for Name
        self.nameGretting=Label(text="Enter your name?",font_size=18,color='#00FFCE')
        self.window.add_widget(self.nameGretting)
        self.nameInput=TextInput(
            multiline=False,
            padding_y=(10,10),
            size_hint=(1,0.5),
            hint_text= 'name...',
            font_size= '17dp'
            )
        self.window.add_widget(self.nameInput)
        
        
        
        # for Age
        self.ageGretting=Label(text="Enter your Age?",font_size=18,color='#00FFCE')
        self.window.add_widget(self.ageGretting)
        self.ageInput=TextInput(
            multiline=False,
            padding_y=(10,10),
            size_hint=(1,0.5),
            hint_text= 'age...',
            font_size= '17dp'
            )
        self.window.add_widget(self.ageInput)
        
        
        # for display Button
        self.displayButton=Button(text="DISPLAY",
                                  size_hint=(1,0.5),
                                  bold=True,
                                  background_color="#00FFCE",
                                  background_normal=""
                                  )
        self.displayButton.bind(on_press=self.displayButtonResponse)
        self.window.add_widget(self.displayButton)
        
        # for display Result
        self.result=Label(text="",font_size=18,color='#00FFCE')
        self.window.add_widget(self.result)
        
        
        return self.window
        
    
    def displayButtonResponse(self,instance):
        self.result.text="Result\nName: "+self.nameInput.text+"\nAge: "+self.ageInput.text+""
    
    
if __name__=="__main__":
    FunCLass().run()