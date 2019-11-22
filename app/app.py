from flask import Flask,request,render_template,jsonify

app = Flask(__name__, static_folder="templates/")

@app.route('/')
def index():
    return render_template('index/index.html')




if __name__ == "__main__":
    app.run(port="8000")