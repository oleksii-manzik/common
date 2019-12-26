from flask import Flask
from config import run_config
from hotel import api_hotel_bp
from hotel.model import db

app = Flask(__name__)
app.config.from_object(run_config())
app.register_blueprint(api_hotel_bp)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return f'You are using {app.config["NAME"]} configurations'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
