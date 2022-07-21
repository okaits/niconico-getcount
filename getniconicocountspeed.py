import requests as request
import time
import sys
from xml.etree import ElementTree as et
url = "https://ext.nicovideo.jp/api/getthumbinfo/" + str(sys.argv[1])
max = 0
history = []
first = True
while True:
  responce = request.get(url)
  tree = et.fromstring(request.get(url).content)
  response = request.get(url, stream=True)
  response.raw.decode_content = True
  events = et.iterparse(response.raw)
  for event, elem in events:
    if str(elem.tag) == "view_counter":
      if first == True:
        print("INIT " + str(elem.text) + ", speed=0counts/min")
        before = int(elem.text)
        first = False
      else:
        history.append(int(int(elem.text) - before))
        print("SPEED " + str(int(elem.text) - before) + "c/m")
        print("AVG " + str(sum(history)/len(history)) + "c/m")
        before = int(elem.text)
  time.sleep(60)
