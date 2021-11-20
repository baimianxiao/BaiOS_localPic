from flask import Flask, Response

app = Flask(__name__)


@app.route("/photo/<imageId>.png")
def get_frame(imageId):
    # 图片上传保存的路径
    with open(r'./image/{}.png'.format(imageId), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/png")
        return resp


if __name__ == '__main__':
    app.run()
