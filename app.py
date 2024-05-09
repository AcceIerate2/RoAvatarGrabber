from flask import Flask, request
from get_image_url import avatar_img_url

app = Flask(__name__)

@app.route('/<id>', methods = ["GET"])
def index(id):

    if request.method == "GET":
        print(id)
        
        return avatar_img_url(id=id)


if __name__ == "__main__":
    app.run()