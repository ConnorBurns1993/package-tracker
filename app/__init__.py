from flask import Flask, render_template
from .config import Config
from .shipping_form import ShippingForm

import psycopg2

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return "<h1>Package Tracker</h1>"

@app.route('/new-package', methods = ['GET, POST'])
def new_package():
    form = ShippingForm()

    if form.validate_on_submit():
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                    '''
                    INSERT INTO packages(name, recipient, origin, destination, express_shipping)
                    VALUES (%(name)s, %(recipient)s, %(origin)s, %(destination)s, %(express_shipping)s)
                    ''',
                    {
                    'name': form.name.data,
                    'recipient': form.recipient.data,
                    'origin': form.origin.data,
                    'destination': form.destination.data,
                    'express_shipping': form.express_shipping.data
                    }
                )
                return redirect('/')

    return render_template('shipping_request.html')
