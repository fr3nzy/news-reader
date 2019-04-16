# requires mp123, bs4, gtts, (sumy - sumy,python3 -c "import nltk; nltk.download('punkt')",numpy)
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

import bs4	, requests, os
from gtts import gTTS


#TODO greet with 'hello x', display 'loading' while downloading first headline - once downloaded, display headline sequentially as info is read out. defer the reading out to a seperate thread, leaving the main thread to update the text. use another thread to download the data for the next headline so that the spaces in between the reading out of headlines can be consistent

class MainLayout(FloatLayout):
	pass
	
class Output(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
			
		# lambda is conceptually identical to a function but it doesn't need to be defined THEN called - it is defined and callable on its creation, so you can pass the definition as callable function argument 
		# here it is called because that is running directly. if function was used, would require function -
		# - defnition containing the self.text_loader call to be defined elsewhere, because you're not calling the function in the parameters, you can only pass it for calling in schedule_once()
		Clock.schedule_once(lambda dt: self.text_loader('hello, lain'), 2) 
		
	# load the text letter by letter to create a more dynamic aura
	def text_loader(self, text): 
		def display_letter(ctr):
			try:
				self.text += text[ctr]
			except IndexError:
				return
			ctr+=1
			Clock.schedule_once(lambda dt: display_letter(ctr), 1/8) # every 8th frame
			
		display_letter(0)
		
	
class NewsReader(App):
	def build(self):
		return Builder.load_file('news.kv')

NewsReader().run()
