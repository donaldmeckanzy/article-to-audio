import pyttsx3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.linkedin.com/pulse/how-coffee-reduces-depression-donald-meckanzy-okaragba/?trackingId=DLnnTKc9TruGSIfZ0i0OgQ%3D%3D")
data = response.text
#print(data)
article = "How Coffee Reduces Depression! Studies have found that drinking coffee could be associated with an 8% lower risk of depression. One study on more than 200,000 people showed that drinking coffee was linked to a lower risk of death by suicide. Drinking coffee may not automatically reduce depression, but in this article, I will show you how you can use it to reduce depression. Where can I get coffee? Walk to a local beverage shop or search online. What are some coffee name brands? Nescafé, Starbucks. How Can Coffee Lower the Risk of Depression? Coffee contains caffeine. Caffeine boosts energy. When your energy is boosted after taking coffee, you can use it to do some good work, take that dance class you've been putting aside, etc. The reward (mentally) you get from the work you did adds to your confidence. It's the same as the sense of accomplishment from working on and completing a task. You can improve your general well-being by using your energy to work towards improving aspects of your life. One of the symptoms of depression is a lack of energy. Do you see how you can boost your energy and use it for something good? What amount of coffee is okay? 1 - 4 cups of coffee a day is considered good. Written by Donald Meckanzy Okaragba"

engine = pyttsx3.init()
#voices = engine.getProperty('voice', voice.id)
engine.save_to_file(article, 'How Coffee Reduces Depression by Donald.mp3')
#for r in res:
#    print("Article Name: " + r.find('a').text) I am trying to get the text from the exact Url
engine.say(article)
engine.runAndWait()