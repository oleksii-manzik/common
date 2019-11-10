import os
import uuid
from flask import (Blueprint, render_template, request,
                   redirect, url_for, session)
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, IntegerField
from werkzeug.utils import secure_filename
from flask3.utils import get_data, update_data

products = Blueprint('products', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/products_blueprint/static')

DATA_STORAGE = 'products_blueprint/product_data.json'


@products.route('/product')
def get_all_products_page():
    data = get_data(DATA_STORAGE)

    if request.args:
        selected_products = []

        for product in data:
            for key, value in request.args.items():
                if not product.get(key) == value:
                    break
            else:
                selected_products.append((product["id"], product["name"]))
    else:
        selected_products = [(product["id"], product["name"])
                             for product in data]
    return render_template('all_products.html',
                           selected_products=selected_products)


@products.route('/product/<product_id>')
def get_product_page(product_id):
    session[product_id] = 'clicked'
    data = get_data(DATA_STORAGE)
    product_data = [x for x in data if x["id"] == product_id][0]
    return render_template('product.html', product_data=product_data)


@products.route('/product/add_product', methods=['GET', 'POST'])
def get_add_product_page():
    form = AddNewProduct()
    if request.method == 'POST':
        filename = secure_filename(form.image.data.filename)
        file_path = f'{os.getcwd()}/products_blueprint/static/{filename}'
        form.image.data.save(file_path)
        form_data = {
            'id': str(uuid.uuid1()),
            'name': form.name.data,
            'description': form.description.data,
            'img_name': form.image.data.filename,
            'price': str(form.price.data)
        }
        update_data(DATA_STORAGE, form_data)
        return redirect(url_for('products.get_all_products_page'))
    return render_template('add_product.html', form=form)


class AddNewProduct(FlaskForm):
    name = StringField('Name')
    description = StringField('Descriprion')
    image = FileField()
    price = IntegerField('Price')
    submit = SubmitField('Add product')
