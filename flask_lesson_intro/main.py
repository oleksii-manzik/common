from flask import Flask, render_template, abort
from json.decoder import JSONDecodeError
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/author')
def get_author_page():
    return render_template("author.html")


@app.route('/<item>')
def get_item_page(item):
    try:
        data = get_data()
    except (FileNotFoundError, JSONDecodeError):
        return render_template('data_problems.html')

    if item in [x['title'].replace(' ', '_').lower() for x in data]:
        for x in data:
            if item == x['title'].replace(' ', '_').lower():
                return render_template("base_product.html",
                                       title=x['title'],
                                       image=f"{item}.jpg",
                                       text=x['text'],
                                       count=len(x['text']))
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
