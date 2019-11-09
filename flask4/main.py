from flask import Flask
from flask4.config import run_config
from flask4.hotel import api_hotel_bp
from flask4.hotel.db_utils import create_db

app = Flask(__name__)
app.config.from_object(run_config())
app.register_blueprint(api_hotel_bp)


@app.route('/')
def home():
    return f'You are using {app.config["NAME"]} configurations'


if __name__ == '__main__':
    create_db()
    app.run(debug=app.config['DEBUG'])
