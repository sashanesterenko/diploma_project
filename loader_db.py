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
        vendee = json.loads(json_object)
        vendee_data = vendee['vendee_info']
        offers = json.loads(json_object)
        #offers_data = offers['goods']
        # Проходим по данным и добавляем их в базу.
        for new_notice in notice:
            print('b')
            new_notice = Notice(zakupkigov_id=notice['zakupkigov_id'], vendee_definition_method=notice['vendee_definition_method'], tender_system=notice['tender_system'], start_max_price=notice['start_max_price'], application_dates_end=datetime.strptime(notice['application_dates_end'], '%d.%m.%Y %H:%M'),  e_auction_date=datetime.strptime(notice['e_auction_date'], '%d.%m.%Y'), date_printed_notice=datetime.strptime(notice['date_printed_notice'], '%d.%m.%Y %H:%M'))
        for new_vendee in vendee:
            print('c')    
            new_vendee = Vendee(postal_address=vendee_data['postal_address'], vendee=vendee_data['vendee'], notice_id=vendee_data['notice_id'])
        
        for new_offer in offers['goods']:
            print('d')
            new_offer = Offer(name=new_offer['name'], quantity=new_offer['quantity'], price=new_offer['price'])    
            
            #created_at = datetime.strptime(json_export['created_at'], '%d.%m.%Y %H:%M')   
        print(new_vendee)
        print(new_offer)   

        db.session.add(new_notice)
        db.session.add(new_vendee)
        db.session.add(new_offer)
        db.session.commit()
        
app = create_app()
with app.app_context():
    a=export_to_json(notice_urls)
    save_notice(a)




