from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notice_id = db.Column(db.Integer, nullable=False)
	vendee_definition_method = db.Column(db.Integer, nullable=False)
	tender_system = db.Column(db.String, nullable=False)
	start_max_price = db.Column(db.String, nullable=False)
    application_dates_end = db.Column(db.DateTime, nullable=False)
    e_auction_date = db.Column(db.DateTime, nullable=False)
    date_printed_notice = db.Column(db.DateTime, nullable=False)

    vendees = db.relationship('offer', backref = 'notice_author') #Это ок?
    


    def __repr__(self):
            return '<Notice {} {}>'.format(self.notice_id)


class Vendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notice_id = db.Column(db.Integer, nullable=False, db.ForeignKey('notice_id')) #Это ок? Хочу, чтобы notice_id связывал все таблицы
	postal_address = db.Column(db.Integer, nullable=False)
	vendee = db.Column(db.String, nullable=False)

    def __repr__(self):
            return '<Vendee {} {}>'.format(self.notice_id, self.vendee)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notice_id = db.Column(db.Integer, nullable=False, db.ForeignKey('notice_id')) #Это ок? Хочу, чтобы notice_id связывал все таблицы
	name = db.Column(db.Integer, nullable=False)
    quantity = = db.Column(db.Integer, nullable=False)
	price = db.Column(db.String, nullable=False)

    def __repr__(self):
            return '<Offer {} {}>'.format(self.notice_id, self.name, self.quantity)


    
    
			
			
#Извещение:			
#Номер извещения - notice_id
#Способ определения поставщика (подрядчика, исполнителя) - vendee_definition_method
#Организация, осуществляющая размещение - vendee
#Адрес электронной площадки в информационно-телекоммуникационной сети «Интернет» - tender_system
#Начальная (максимальная) цена контракта - start_max_price
#Дата и время окончания подачи заявок - application_dates_end
#Дата проведения аукциона в электронной форме - e_auction_date
#Дата и время подписания печатной формы извещения - date_printed_notice

#Организация:
#Номер извещения - notice_id
#Почтовый адрес - postal_address
#Организация, осуществляющая размещение - vendee

#Товар:
#Номер извещения - notice_id
#Наименование товара, работы, услуги - name
#Количество - quantity
#Цена за ед.изм. - price