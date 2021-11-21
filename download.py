# coding: utf-8
import json
import requests

with open('data/arknightsdraw_ch.json', 'r', encoding='utf-8') as f:
    arknightsDraw_data = json.loads(f.read())
for i in range(0, len(arknightsDraw_data)):
    star = arknightsDraw_data[i]['star']
    name = arknightsDraw_data[i]['name']
    class_ch = arknightsDraw_data[i]['class']
    url = arknightsDraw_data[i]['url_half']
    res = requests.get(url)
    # 发出请求，并把返回的结果放在变量res中
    pic = res.content
    # 把Reponse对象的内容以二进制数据的形式返回
    photo = open(r'image/'+star+'/'+class_ch+'_'+name+'.png', 'wb')
    # 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
    # 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
    photo.write(pic)
    # 获取pic的二进制内容
    photo.close()
    print(class_ch, star, name, url)
print("下载成功！")
