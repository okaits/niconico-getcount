import requests as request
import time
import datetime
import sys
from xml.etree import ElementTree as et
url = "https://ext.nicovideo.jp/api/getthumbinfo/" + str(sys.argv[1])
max = 0
while True:
  responce = request.get(url)
  tree = et.fromstring(request.get(url).content)
  response = request.get(url, stream=True)
  response.raw.decode_content = True
  events = et.iterparse(response.raw)
  for event, elem in events:
    if str(elem.tag) == "view_counter":
      if int(elem.text) > max:
        if int(elem.text) > 9900000 and int(elem.text) < 10000000:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 神話入りまで残り" + str(10000000 - int(elem.text)) + "回")
        if int(elem.text) > 10000000 and int(elem.text) < 10000300:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 神話入り達成！！！！")
        if int(elem.text) > 990000 and int(elem.text) < 1000000:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 伝説入りまで残り" + str(1000000 - int(elem.text)) + "回")
        if int(elem.text) > 1000000 and int(elem.text) < 1000050:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 伝説入り達成！！！！")
        if int(elem.text) > 95000 and int(elem.text) < 100000:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 殿堂入りまで残り" + str(100000 - int(elem.text)) + "回")
        if int(elem.text) > 100000 and int(elem.text) < 100025:
          print("UP" + str(max - int(elem.text)) + ": " + str(elem.text) + ", " + str(datetime.datetime.now()) + ", 殿堂入り達成！！！！")
        max = int(elem.text)
      elif int(elem.text) == max:
        print("Equal: " + str(elem.text))
  time.sleep(7)
