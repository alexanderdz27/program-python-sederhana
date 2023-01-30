from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
#window size
w,h=Window.size
#class for first screen
class Display(FloatLayout):
   string=""
   def __init__(self,*args):
      super().__init__(*args)
      self.text_field=TextInput(font_size=15,hint_text="Enter the values here",text="",size_hint=(0.5,0.05),pos_hint={'x':0.1,'y':0.85})
      self.add_widget(self.text_field)
      
      btn_list=['C','(',')','/','7','8','9','*','4','5','6','+','1','2','3','-','0','','.','=']
      Y=0.5
      X=0.025
      n=1
      for i in range(20):
       if n==18:
        pass
       else:
        self.btn=Button(text=btn_list[i],size_hint=(0.2,0.1),pos_hint={'x':X,'y':Y},)
        self.add_widget(self.btn)
        self.btn.background_color = (1, 1, 1, 1)
        self.btn.color=(0,0,0,1)
        self.btn.font_size=w*0.05
        self.btn.bind(on_press=self.calculation)
        
       if n%4==0:
        Y-=0.125
        X=0.025
        self.btn.background_color=(1,0.49,0.31,1)
        self.btn.color=(1,1,1,1)
       else: 
        X+=0.25
        
       if n==17:
        self.btn.size_hint_x=0.45 
       if n==20:
          self.btn.background_color=(0,1,0,1)
        
       n+=1
   def calculation(self,instance):
      a=instance.text
      if a=="=":
         try:
           self.string=self.text_field.text
           self.text_field.text=str(eval(self.string))
           self.string=self.text_field.text
         except  SyntaxError:
           self.text_field.text="syntax error!"
           self.string=""
         except TypeError:
            self.text_field.text="pass wrong input!"
            self.string=""
         except NameError:
           self.text_field.text="syntax error!"
           self.string=""
         except:
            self.text_field.text="syntax error!"
            self.string=""
      elif a=="C":
         self.string=self.string[0:-1]
         self.text_field.text=self.string
      else:
         self.string+=a
         self.text_field.text=self.string 
      
#Main class       
class calci(App):
   def build(self):
      return Display()
      
calci().run()