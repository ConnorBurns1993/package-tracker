from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
    name = StringField("From", validators=[DataRequired()])
    recipient = StringField("To", validators=[DataRequired()])
    origin = SelectField("Origin", validators=[DataRequired()], choices = map.items())
    destination = SelectField("Destination", validators=[DataRequired()])
    express_shipping = BooleanField("Express Shipping")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
