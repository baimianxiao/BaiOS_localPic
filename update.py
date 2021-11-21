# coding: utf-8
# 更新数据
import json
import re
import urllib
import urllib.request


def get_url(name):
    url = "https://prts.wiki/w/PRTS:%E6%96%87%E4%BB%B6%E4%B8%80%E8%A7%88/%E5%B9%B2%E5%91%98%E7%B2%BE%E8%8B%B10%E5%8D%8A%E8%BA%AB%E5%83%8F "
    request = urllib.request.Request(url)
    # 模拟Mozilla浏览器进行爬虫
    request.add_header("user-agent", "Mozilla/5.0")
    response2 = urllib.request.urlopen(request)
    html_str = str(response2.read(), encoding="utf-8")
    pic_url = re.findall(
        r'/images/thumb/[0-9a-z]+/[0-9a-z]+/%E5%8D%8A%E8%BA%AB%E5%83%8F_' + urllib.parse.quote(name) + '_1.png',
        html_str, re.I)
    return url_change(pic_url[0], name)


def url_change(url, name):
    url_data = re.findall(r'/[0-9a-z]+/[0-9a-z]+/%E5%8D%8A%E8%BA%AB%E5%83%8F_' + urllib.parse.quote(name) + '_1.png',
                          url, re.I)
    return "https://prts.wiki//images" + url_data[0]


with open('data/arknightsdraw_ch(v2).json', 'r', encoding='utf-8') as f:
    arknightsDraw_data = json.loads(f.read())
for i in range(0, len(arknightsDraw_data)):
    name = arknightsDraw_data[i]['name']
    arknightsDraw_data[i]['url_half'] = get_url(name)
    print(arknightsDraw_data[i]['name'], arknightsDraw_data[i]['url_half'])
with open('data/arknightsdraw_ch.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(arknightsDraw_data, ensure_ascii=False, indent=2))
    print("获取完毕!")
