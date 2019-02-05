from webapp import create_app
import json
from webapp.parser import  export_to_json, notice_urls
from webapp.model import Notice

def save_notice(json_export):
    for json_object in json_export:
        print('a')
        # Читаем JSON-файл.
        notice = json.loads(json_object)
        # Проходим по данным и добавляем их в базу.
        for new_notice in notice:
            print('b')
            new_notice = Notice(zakupkigov_id=notice['zakupkigov_id'], vendee_definition_method=notice['vendee_definition_method'], tender_system=notice['tender_system'], start_max_price=notice['start_max_price'], application_dates_end=notice['application_dates_end'],  e_auction_date=notice['e_auction_date'], date_printed_notice=notice['date_printed_notice'])
            session.add(new_notice)
            session.commit()

app = create_app()
with app.app_context():
    a=export_to_json(notice_urls)
    save_notice(a)