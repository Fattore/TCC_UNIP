import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import ObjectProperty, StringProperty
import hashlib
import sqlite3
Builder.load_string(open("login\gui.kv", encoding="utf-8").read(),rulesonly = True)
class MenuScreen(Screen):
	lbl_saida = ObjectProperty(None)
class AppScreen(Screen):
	pass
class UserScreen(Screen):
	pass
class AlterarScreen(Screen):
	pass
class CadastrarScreen(Screen):
	pass
class LoginScreen(App):
	sm = ScreenManager()
	sm.add_widget(MenuScreen(name="menu"))
	sm.add_widget(AppScreen(name="app"))
	sm.add_widget(UserScreen(name="verificar"))
	sm.add_widget(AlterarScreen(name="alterar"))
	sm.add_widget(CadastrarScreen(name="cadastrar"))
	usuario = ''
	def login_usuario(self):
		pass
	def cadastrar_usuario(self):
		txt_usuario = ObjectProperty(None)
		txt_email = ObjectProperty(None)
		txt_senha = ObjectProperty(None)
		lbl_saida = ObjectProperty(None) 
	def verificar_usuario(self):
		pass
	def alterar_senha(self):
		pass
	def build(self):
		App.title = "League of Lost Impact"
		Window.size = (320,480)
		self.db = sqlite3.connect("tcc.db")
		self.db.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT, email TEXT, senha TEXT)")
		self.cursor = self.db.cursor()
		self.sm.current = "cadastrar"
		return self.sm

LoginScreen().run()