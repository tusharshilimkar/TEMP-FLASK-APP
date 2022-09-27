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
    base_url=f"http://api.weatherstack.com/current?access_key=1ce59aaa2916843340954d6807ef368b&query={n}"
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
