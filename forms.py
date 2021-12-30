from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClusterSearchForm(FlaskForm):
    name = StringField('ClusterName', validators=[DataRequired()])
    submit = SubmitField('Go')


