# coding: utf-8
# 下载相关相关素材
import os
import json
import requests

with open('data/arknightsdraw_ch.json', 'r', encoding='utf-8') as f:
    arknightsDraw_data = json.loads(f.read())
for i in range(0, len(arknightsDraw_data)):
    star = arknightsDraw_data[i]['star']
    name = arknightsDraw_data[i]['name']
    class_ch = arknightsDraw_data[i]['class']
    url = arknightsDraw_data[i]['url_half']
    road = 'image/arknightsdraw/' + star + '/'
    if not os.path.exists(road):
        os.makedirs(road)
    if not os.path.exists(r'image/arknightsdraw/' + star + '/' + class_ch + '_' + name + '.png'):
        res = requests.get(url)
        # 发出请求，并把返回的结果放在变量res中
        pic = res.content
        # 把Response对象的内容以二进制数据的形式返回
        photo = open(r'image/arknightsdraw/' + star + '/' + class_ch + '_' + name + '.png', 'wb')
        # 图片内容需要以二进制wb读写
        photo.write(pic)
        # 获取pic的二进制内容
        photo.close()
        print('下载', class_ch, star, name, url)
    else:
        print('已存在')

print("下载成功！")
