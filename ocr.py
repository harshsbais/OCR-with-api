# [Optional] OCR code for lang
# Arabic=ara
# Bulgarian=bul
# Chinese(Simplified)=chs
# Chinese(Traditional)=cht
# Croatian = hrv
# Czech = cze
# Danish = dan
# Dutch = dut
# English = eng
# Finnish = fin
# French = fre
# German = ger
# Greek = gre
# Hungarian = hun
# Korean = kor
# Italian = ita
# Japanese = jpn
# Polish = pol
# Portuguese = por
# Russian = rus
# Slovenian = slv
# Spanish = spa
# Swedish = swe
# Turkish = tur


#   [OPTIONAL] Google Trans  code for lang
#  'af': 'afrikaans',
#     'sq': 'albanian',
#     'am': 'amharic',
#     'ar': 'arabic',
#     'hy': 'armenian',
#     'az': 'azerbaijani',
#     'eu': 'basque',
#     'be': 'belarusian',
#     'bn': 'bengali',
#     'bs': 'bosnian',
#     'bg': 'bulgarian',
#     'ca': 'catalan',
#     'ceb': 'cebuano',
#     'ny': 'chichewa',
#     'zh-cn': 'chinese (simplified)',
#     'zh-tw': 'chinese (traditional)',
#     'co': 'corsican',
#     'hr': 'croatian',
#     'cs': 'czech',
#     'da': 'danish',
#     'nl': 'dutch',
#     'en': 'english',
#     'eo': 'esperanto',
#     'et': 'estonian',
#     'tl': 'filipino',
#     'fi': 'finnish',
#     'fr': 'french',
#     'fy': 'frisian',
#     'gl': 'galician',
#     'ka': 'georgian',
#     'de': 'german',
#     'el': 'greek',
#     'gu': 'gujarati',
#     'ht': 'haitian creole',
#     'ha': 'hausa',
#     'haw': 'hawaiian',
#     'iw': 'hebrew',
#     'he': 'hebrew',
#     'hi': 'hindi',
#     'hmn': 'hmong',
#     'hu': 'hungarian',
#     'is': 'icelandic',
#     'ig': 'igbo',
#     'id': 'indonesian',
#     'ga': 'irish',
#     'it': 'italian',
#     'ja': 'japanese',
#     'jw': 'javanese',
#     'kn': 'kannada',
#     'kk': 'kazakh',
#     'km': 'khmer',
#     'ko': 'korean',
#     'ku': 'kurdish (kurmanji)',
#     'ky': 'kyrgyz',
#     'lo': 'lao',
#     'la': 'latin',
#     'lv': 'latvian',
#     'lt': 'lithuanian',
#     'lb': 'luxembourgish',
#     'mk': 'macedonian',
#     'mg': 'malagasy',
#     'ms': 'malay',
#     'ml': 'malayalam',
#     'mt': 'maltese',
#     'mi': 'maori',
#     'mr': 'marathi',
#     'mn': 'mongolian',
#     'my': 'myanmar (burmese)',
#     'ne': 'nepali',
#     'no': 'norwegian',
#     'or': 'odia',
#     'ps': 'pashto',
#     'fa': 'persian',
#     'pl': 'polish',
#     'pt': 'portuguese',
#     'pa': 'punjabi',
#     'ro': 'romanian',
#     'ru': 'russian',
#     'sm': 'samoan',
#     'gd': 'scots gaelic',
#     'sr': 'serbian',
#     'st': 'sesotho',
#     'sn': 'shona',
#     'sd': 'sindhi',
#     'si': 'sinhala',
#     'sk': 'slovak',
#     'sl': 'slovenian',
#     'so': 'somali',
#     'es': 'spanish',
#     'su': 'sundanese',
#     'sw': 'swahili',
#     'sv': 'swedish',
#     'tg': 'tajik',
#     'ta': 'tamil',
#     'te': 'telugu',
#     'th': 'thai',
#     'tr': 'turkish',
#     'uk': 'ukrainian',
#     'ur': 'urdu',
#     'ug': 'uyghur',
#     'uz': 'uzbek',
#     'vi': 'vietnamese',
#     'cy': 'welsh',
#     'xh': 'xhosa',
#     'yi': 'yiddish',
#     'yo': 'yoruba',
#     'zu': 'zulu',


import cv2
import requests
import io
import json
from googletrans import Translator
import webbrowser
from bs4 import BeautifulSoup
import smtplib
import time
from lxml import html
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class Client(QWebEnginePage): 
    def __init__(self, url): 
        self.app = QApplication(sys.argv) 
        QWebEnginePage.__init__(self) 
        self.html = '' 
        self.loadFinished.connect(self._on_load_finished) 
        self.load(QUrl(url)) 
        self.app.exec_() 
    def _on_load_finished(self): 
        self.html = self.toHtml(self.Callable) 
    def Callable(self, html_str): 
        self.html = html_str 
        self.app.quit() 

def run():
    path = input("Enter the path of the image\n")
    choice = int(input("Enter \n 1. OCR of the image \n 2. OCR of the image and translate it to other language \n 3. Do a sentiment analysis on the text \n 4. Do a Reverse Google Image serach on the image \n "))
    if (choice == 1 or choice == 2 or choice == 3):
        l = input("Enter the language in which the image is\n")
        img = cv2.imread(path)
        url_api = "https://api.ocr.space/parse/image"
        _, compressedimage = cv2.imencode(".png", img)
        file_bytes = io.BytesIO(compressedimage)
        results = requests.post(url_api, files = {path: file_bytes}, data = {"apikey": "6ee0015c5488957", "language": l})
        results = results.content.decode()
        result = json.loads(results)
        text_detected = result.get("ParsedResults")[0].get("ParsedText")
        if(text_detected == ""):
            print("NO TEXT!!")
        else:
            print("Original Text :- \n")
            print(text_detected)
            if choice == 2:
                translator = Translator()  # initalize the Translator object
                d = input("Enter the destination language :- ")
                translation = translator.translate(text_detected, dest = d)  # translate two phrases to other language
                print("Translated Text :- \n")
                print(translation.text)
            if choice == 3:
                print("Senitment Analysis would be added soon")
    elif choice == 4:
        searchUrl = 'http://www.google.co.in/searchbyimage/upload'
        multipart = {'encoded_image': (path, open(path, 'rb')), 'image_content': ''}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers['Location']
        client_response = Client(fetchUrl)
        source = client_response.html
        soup = BeautifulSoup(source, 'html.parser')
        title=soup.find('div', attrs={'class':'r5a77d'})
        print("The Reverse image search brings up this result")
        print(title.find('a').contents[0])
        print("Kindly check the below URL to get more results!!")
        print(fetchUrl)
    else:
        print("WRONG CHOICE!!")

run()
