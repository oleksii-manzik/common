import os
import uuid
from flask import (Blueprint, render_template, request,
                   redirect, url_for, session)
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, IntegerField
from werkzeug.utils import secure_filename
from flask3.utils import get_data, update_data

supermarkets = Blueprint('supermarkets', __name__,
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='/supermarkets_blueprint/static')

DATA_STORAGE = 'supermarkets_blueprint/supermarket_data.json'


@supermarkets.route('/supermarket')
def get_all_supermarkets_page():
    data = get_data(DATA_STORAGE)

    if request.args:
        selected_supermarkets = []

        for supermarket in data:
            for key, value in request.args.items():
                if not supermarket.get(key) == value:
                    break
            else:
                selected_supermarkets.append(
                    (supermarket["id"], supermarket["name"]))
    else:
        selected_supermarkets = [(supermarket["id"], supermarket["name"])
                                 for supermarket in data]
    return render_template('all_supermarkets.html',
                           selected_supermarkets=selected_supermarkets)


@supermarkets.route('/supermarket/<supermarket_id>')
def get_supermarket_page(supermarket_id):
    session[supermarket_id] = 'clicked'
    data = get_data('supermarkets_blueprint/supermarket_data.json')
    supermarket_data = [x for x in data if x["id"] == supermarket_id][0]
    return render_template('supermarket.html',
                           supermarket_data=supermarket_data)


@supermarkets.route('/supermarket/add_supermarket', methods=['GET', 'POST'])
def get_add_supermarket_page():
    form = AddNewSupermarket()
    if request.method == 'POST':
        filename = secure_filename(form.image.data.filename)
        file_path = f'{os.getcwd()}/supermarkets_blueprint/static/{filename}'
        form.image.data.save(file_path)
        form_data = {
            'id': str(uuid.uuid1()),
            'name': form.name.data,
            'location': form.location.data,
            'img_name': form.image.data.filename
        }
        update_data(DATA_STORAGE, form_data)
        return redirect(url_for('supermarkets.get_all_supermarkets_page'))
    return render_template('add_supermarket.html', form=form)


class AddNewSupermarket(FlaskForm):
    name = StringField('Name')
    location = StringField('Location')
    image = FileField()
    submit = SubmitField('Add supermarket')
