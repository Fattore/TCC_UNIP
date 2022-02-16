import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class CrudKivy(App):
	def build(self):
		Window.size = (320,480)
		return Label(text = 'CRUD Kivy SQLite')
CrudKivy().run()