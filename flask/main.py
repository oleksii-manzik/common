from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_r():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables_r():
    vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', vegetables=vegetables)


@app.route('/fruits')
def fruits_r():
    fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', fruits=fruits)


if __name__ == '__main__':
    app.run(debug=True)
