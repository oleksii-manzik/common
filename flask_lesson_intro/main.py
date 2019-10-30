from flask import Flask, render_template, url_for
from utils import get_data

app = Flask(__name__)

data = get_data()


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/author')
def get_author_page():
    return render_template("author.html")


@app.route('/alarm_clock')
def get_alarm_clock_page():
    return render_template("alarm_clock.html",
                           title=data[0]['title'],
                           text=data[0]['text'],
                           count=len(data[0]['text']))


@app.route('/battery_charger')
def get_battery_charger_page():
    return render_template("battery_charger.html",
                           title=data[5]['title'],
                           text=data[5]['text'],
                           count=len(data[5]['text']))


@app.route('/calculator')
def get_calculator_page():
    return render_template("calculator.html",
                           title=data[3]['title'],
                           text=data[3]['text'],
                           count=len(data[3]['text']))


@app.route('/coffeemaker')
def get_coffeemaker_page():
    return render_template("coffeemaker.html",
                           title=data[4]['title'],
                           text=data[4]['text'],
                           count=len(data[4]['text']))


@app.route('/headphones')
def get_headphones_page():
    return render_template("headphones.html",
                           title=data[1]['title'],
                           text=data[1]['text'],
                           count=len(data[1]['text']))


@app.route('/ipod')
def get_ipod_page():
    return render_template("ipod.html",
                           title=data[2]['title'],
                           text=data[2]['text'],
                           count=len(data[2]['text']))


if __name__ == "__main__":
    app.run(debug=True)
