import cv2
import numpy as np
import requests
import io
import json
from googletrans import Translator


path = input("Enter the path of the image\n")
l = input("Enter the language\n")
img = cv2.imread(path)

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".png", img)
file_bytes = io.BytesIO(compressedimage)
results = requests.post(url_api, files = {path: file_bytes}, data = {"apikey": "6ee0015c5488957", "language": l})
results = results.content.decode()

result = json.loads(results)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

translator = Translator()  # initalize the Translator object
translation = translator.translate(text_detected, dest='hi')  # translate two phrases to Hindi
print(translation.text)

