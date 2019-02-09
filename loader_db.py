from webapp import create_app
import json
from webapp.parser import  export_to_json, notice_urls
from webapp.model import db, Notice, Vendee, Offer
from datetime import datetime





def save_notice(json_export):
    for json_object in json_export:
        print('a')
        # Читаем JSON-файл.
        notice = json.loads(json_object)
        # Проходим по данным и добавляем их в базу.
        for new_notice in notice:
            print('b')
            new_notice = Notice(zakupkigov_id=notice['zakupkigov_id'], vendee_definition_method=notice['vendee_definition_method'], tender_system=notice['tender_system'], start_max_price=notice['start_max_price'], application_dates_end=datetime.strptime(notice['application_dates_end'], '%d.%m.%Y %H:%M'),  e_auction_date=datetime.strptime(notice['e_auction_date'], '%d.%m.%Y %H:%M'), date_printed_notice=datetime.strptime(notice['date_printed_notice'], '%d.%m.%Y %H:%M'))
            #created_at = datetime.strptime(json_export['created_at'], '%d.%m.%Y %H:%M')
            db.session.add(new_notice)
            db.session.commit()

def save_vendee(json_export):
    for json_object in json_export:
        print('a')
        # Читаем JSON-файл.
        vendee = json.loads(json_object)
        # Проходим по данным и добавляем их в базу.
        for new_vendee in vendee:
            print('b')
            new_vendee = Vendee(postal_address=vendee['postal_address'], vendee=vendee['vendee'], notice_id=vendee['notice_id'])
            #created_at = datetime.strptime(json_export['created_at'], '%d.%m.%Y %H:%M')
            db.session.add(new_vendee)
            db.session.commit()

def save_offer(json_export):
    for json_object in json_export:
        print('a')
        # Читаем JSON-файл.
        offer = json.loads(json_object)
        # Проходим по данным и добавляем их в базу.
        for new_offer in offer:
            print('b')
            new_offer = Offer(name=offer['name'], quantity=offer['quantity'], price=offer['price'], price=offer['price'], notice_id=offer['notice_id'])
            #created_at = datetime.strptime(json_export['created_at'], '%d.%m.%Y %H:%M')
            db.session.add(new_offer)
            db.session.commit()

app = create_app()
with app.app_context():
    a=export_to_json(notice_urls)
    save_notice(a)




