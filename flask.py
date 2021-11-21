# coding: utf-8

from flask import Flask, Response

app = Flask(__name__)


@app.route("/arknightsdraw/<imageId>.png")
def get_frame(imageId):
    # 图片上传保存的路径
    with open(r'./image/arknightsdraw/{}.png'.format(imageId), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/png")
        return resp


if __name__ == '__main__':
    app.run()
