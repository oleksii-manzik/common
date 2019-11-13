from flask import Flask, render_template
from flask3.products_blueprint.main import products
from flask3.supermarkets_blueprint.main import supermarkets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret key'
app.register_blueprint(products)
app.register_blueprint(supermarkets)


@app.route('/')
def get_home_page():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_page.html')


if __name__ == '__main__':
    app.run(debug=True)
