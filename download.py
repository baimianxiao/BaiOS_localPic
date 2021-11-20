from requests_html import HTMLSession
import json
session = HTMLSession()
with open('data/arknightsdraw_ch(v2).json', 'rb') as f:
    arknightsDraw_data = json.loads(f.read())
for i in range(0, len(arknightsDraw_data)):
    star=arknightsDraw_data[i]['star']
    name=arknightsDraw_data[i]['name']
    print(i, arknightsDraw_data[i]['name'])
