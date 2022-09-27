from flask import Flask, render_template, url_for , flash , redirect
from flask import request
from flask import jsonify
import requests
app = Flask(__name__)
@app.route('/', methods=["GET"])
def welcome():
    return render_template("home.html")

@app.route('/hello')
def hello_world():
    n = request.args.get('city')
    base_url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=3272cb87863583623e3e36a813b81447'
    x=requests.get(base_url.format(n)).json()
    try:
        return render_template('response.html', posts=x)
    except:
        return "<h1>----------Something goes wrong----------<h1> Please check city name is correct or not <h1><a href='/'>Back</a><h1>"
@app.route('/trial')
def trial():
    return render_template("trial.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
