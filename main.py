import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherits Kivy's Apps class which represent the window
# for this widget 
# HelloKivy inherits all the fields and method
# from kivy
class HelloKivy(App):
    #This returns the content that we want in the window
    def build(self):
        return Label(text="Hello World ")

helloKivy =HelloKivy()
helloKivy.run()
