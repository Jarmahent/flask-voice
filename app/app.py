from flask import Flask,request,render_template,jsonify
import os
import urllib.parse
from converter.convert import Converter
import datetime
import json

app = Flask(__name__, static_folder="templates/index/index")
converter = Converter()

@app.route('/')
def index():
  return render_template('index/index/index.html')

@app.route('/api/convert', methods=["POST"])
def convert_article():
  incoming = request.get_json()
  url = incoming["url"]
  print(incoming["url"])
  print("\n")
  now = datetime.datetime.now().strftime("%d-%Y_%H-%M%S")

  # Move everything in between these lines to a config file (yml)
  # ---------------
  config_location = "app/config.json"
  project_id = "ttsapi-259817"
  article_folder = \
    f"/Users/kevinhernandez/Documents/flask-voice/app/templates/index/index/articles/{now}"
  # ---------------

  if not os.path.exists(article_folder):
    os.mkdir(article_folder)
  res = converter.convert(url=urllib.parse.unquote(url),project_id=project_id,config_location=config_location,out_dir=os.path.join(article_folder, "test.mp3"))

  return jsonify({"response": str(res)})




if __name__ == "__main__":
  app.run(port="8000")