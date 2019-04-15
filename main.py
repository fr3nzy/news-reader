from kivy.config import Config
Config.set('graphics', 'resizable', 0)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder

class MainLayout(FloatLayout):
	pass

class NewsReader(App):
	def build(self):
		return Builder.load_file('news.kv')

NewsReader().run()
