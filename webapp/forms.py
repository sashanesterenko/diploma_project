from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    a_link = StringField('Ссылка на печатную форму извещения:', validators=[DataRequired()])
    # submit_link = SubmitField('Отправить ссылки')
    # submit_another_link = SubmitField('Добавить ещё одну ссылку')
