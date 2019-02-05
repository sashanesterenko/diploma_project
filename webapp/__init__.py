from flask import Flask, render_template, request

from webapp.model import db
from webapp.forms import SubmitForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/submit_links', methods=['GET','POST'])
    def links_submission():
        title = "Добавление ссылок в БД"
        submit_a_link_form = SubmitForm()
        if submit_a_link_form.validate_on_submit():
            if request.form.post == submit_link: 
                print(submit_a_link_form.a_link.data)
	       		
        return render_template('links_submission.html', page_title=title, form=submit_a_link_form)



    return app