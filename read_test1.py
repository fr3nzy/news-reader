import bs4, requests, os
from gtts import gTTS
# requires mp123, bs4, gtts
os.system('rm -rf cache')
os.mkdir('cache')

res = requests.get("https://futurism.com/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

headlines = soup.select('.ImageColumn')

for i in range(len(headlines)):
	section = headlines[i].parent
	headline = section.select('h4')[0].getText()
	tts = gTTS(text=headline, lang='en').save('cache/{}.mp3'.format(i))
	os.system('mpg123 cache/{}.mp3'.format(i))
	
	print(headline)
	print(section.get('href'), '\n')
	
tts = gTTS(text=""" For the first time, doctors are preparing to test a brain-computer interface that can be implanted onto a human brain, no open surgery required.The Stentrode, a neural implant that can let paralyzed people communicate, can be delivered to a patient’s brain through the jugular vein — and the company that developed it, Synchron, just got approval to begin human experimentation.By leaving the skull sealed shut, patients could receive their neural implants without running as great a risk of seizures, strokes, or permanent neural impairments, all of which can be caused by open-brain surgery.In the coming months, five participants with paralyzed hands or mouths that prevent them from communicating will have Stentrodes implanted into their brains.“We’ve commenced recruitment over the last several weeks,” Synchron founder and CEO Thomas Oxley, a physician in New York City, told Futurism. That’s the goal.”One Step At A TimeA permanent neural implant that reads brain activity and churns out text could prove to be a valuable medical tool, but it also could provide doctors with an unprecedented 24/7 stream of neural data.Oxley recognizes that an endless feed of brain activity could be invaluable to medical researchers, but he doesn’t have plans to tap into that yet.“[The Stentrode is] going to show us information that we hadn’t had before. """, lang='en').save('cache/x.mp3')
os.system('mpg123 cache/x.mp3')
	
	
