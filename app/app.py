from flask import Flask,request,render_template,jsonify
import os
import yaml
import urllib.parse
from converter.convert import Converter
from k_util.utilities import Utilities
import datetime
import json

app = Flask(__name__, static_folder="templates/index")
f = open("app/config.yml")
configuration = yaml.full_load(f)
converter = Converter()
util = Utilities()

# Fetch Config yaml file parameters
# ------
config_location = configuration["config"]["credentials_location"]
project_id = configuration["config"]["project_id"]
article_folder = configuration["config"]["article_folder"]
# ------


@app.route('/')
def index():
  return render_template('index/index.html')

@app.route('/api/convert', methods=["POST"])
def convert_article():
  incoming = request.get_json()
  url = incoming["url"]
  now = datetime.datetime.now().strftime("%d-%Y_%H-%M%S")
  random_id = util.randomString()
  article_path = os.path.join(article_folder, random_id)

  if not os.path.exists(article_path):
    os.mkdir(article_path)
  res = converter.convert(
    url=urllib.parse.unquote(url),
    project_id=project_id,
    config_location=config_location,
    out_dir=os.path.join(article_path)
  )

  return jsonify({"response": str(res)})

@app.route('/api/articles', methods=["GET"])
def articles():
  pass
if __name__ == "__main__":
  app.run(port="8000")