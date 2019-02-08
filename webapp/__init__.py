from flask import Flask, render_template, request

from webapp.model import db
from webapp.forms import SubmitForm
from webapp.parser import export_to_json

notice_urls = []

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/submit_links', methods=['GET','POST'])
    def links_submission():
        title = "Добавление ссылок в БД"
        
        submit_a_link_form = SubmitForm()
        if submit_a_link_form.validate_on_submit():
            if request.method == 'POST':
                if request.form['action'] == 'one_more': 
                    notice_urls.append(submit_a_link_form.a_link.data)
                    print(notice_urls)
                elif request.form['action'] == 'submit_all':
                    notice_urls.append(submit_a_link_form.a_link.data)
                    print(export_to_json(notice_urls))



	       		
        return render_template('links_submission.html', page_title=title, form=submit_a_link_form)

    



    return app