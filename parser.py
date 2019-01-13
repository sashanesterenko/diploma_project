import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

def get_html(url, headers):
    try:
        result = requests.get(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=81135264', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        return False

def get_relevant_info():
    html = get_html(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=81135264', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
    if html: 
        soup = bs(html, 'html.parser')
        
        all_tr = soup.find_all('tr')
        param_value_dict = {}
        for tr in all_tr:
            param = tr.find('p', class_='parameter')
            param_value = tr.find('p', class_='parameterValue')
            if param and param_value:
                param = param.text
                param_value = param_value.text
                param_value_pair = {param:param_value}
                param_value_dict.update(param_value_pair)
        # print(param_value_dict)

        
        table_body = soup.find_all('table', class_='table font9')
        for tb in table_body:
            tbody_tr = tb.find_all('tr', class_=False)  
            # print(tbody_tr)           
        table_param_value_dict = {}
        table_param_value_list = []
        for tr in tbody_tr:
            try_th = tr.find_all('th')
            if try_th:
                tbody_th = []
                for every_th in try_th:
                    every_th_text = every_th.text
                    if every_th_text != 'Характеристики товара, работы, услуги':
                        # print(every_th_text)
                        tbody_th.append(every_th_text)
                    else:
                        pass
                # print(tbody_th)
            else:
                try_td = tr.find_all('td', style=False)
                # print(try_td)

                if try_td: 
                    tbody_td = []           
                    for every_td in try_td:
                        every_td_text = every_td.text
                        # print(every_td_text)
                        if every_td_text != '':
                            tbody_td.append(every_td_text)
                    # print(tbody_td)
                    table_param_value_dict = dict(zip(tbody_th, tbody_td))
                # print(table_param_value_dict)
                    table_param_value_list.append(table_param_value_dict)
        # print(table_param_value_list)

        needed_keys = ['Способ определения поставщика (подрядчика, исполнителя)', 
                'Адрес электронной площадки в информационно-телекоммуникационной сети «Интернет»', 
                'Организация, осуществляющая размещение', 
                'Почтовый адрес', 
                'Дата и время окончания подачи заявок', 
                'Дата проведения аукциона в электронной форме', 
                'Начальная (максимальная) цена контракта', 
                'Дата и время подписания печатной формы извещения (соответствует дате направления на контроль по ч.5 ст.99 Закона 44-ФЗ либо дате размещения в ЕИС, в случае отсутствия контроля, по местному времени организации, осуществляющей размещение)']
        needed_param_value_dict = {}
        for key in param_value_dict.keys():
            if key in needed_keys:
                # print(needed_param_value_dict)
                needed_param_value_dict.update({key: param_value_dict[key]})
                # print(needed_param_value_dict)
            else:
                pass
        # print(needed_param_value_dict)


        needed_table_keys = {'Наименование товара, работы, услуги по КТРУ',
                            'Количество', 
                            'Цена за ед.изм.'}
        needed_table_param_value_list = []
        for a_dict in table_param_value_list:
            needed_table_dict = {}
            for key in a_dict.keys():
                if key in needed_table_keys:
                    needed_table_dict.update({key: a_dict[key]})
                else:
                    pass
            needed_table_param_value_list.append(needed_table_dict)
        # print(needed_table_param_value_list)


        fields = ['Способ определения поставщика (подрядчика, исполнителя)', 
                'Организация, осуществляющая размещение',
                'Почтовый адрес',
                'Наименование товара, работы, услуги по КТРУ',
                'Количество', 
                'Цена за ед.изм.',                
                'Адрес электронной площадки в информационно-телекоммуникационной сети «Интернет»', 
                'Начальная (максимальная) цена контракта', 
                'Дата и время окончания подачи заявок', 
                'Дата проведения аукциона в электронной форме', 
                'Дата и время подписания печатной формы извещения (соответствует дате направления на контроль по ч.5 ст.99 Закона 44-ФЗ либо дате размещения в ЕИС, в случае отсутствия контроля, по местному времени организации, осуществляющей размещение)']
        column_range = [3, 4, 5, 12, 13, 14, 15, 16]
        wb = load_workbook(filename='test_table.xlsx')
        sheet = wb.active
        # print(sheet.cell(column=5, row=50))
        first_columns_len = len(sheet['A'])
        print(first_columns_len)
        last_index_number = sheet.cell(column=1, row=first_columns_len).value
        # print(last_index_number)
        index_number = last_index_number + 1

        sheet.cell(column=1, row=sheet.max_row+1, value=index_number)
        column_range_index = 0
        # решить, как итерировать -- строки внутри ключей или ключи внутри строк
        for row in wb.rows: 
            for key in needed_table_param_value_dict.keys():
                    if key in fields: 
                        sheet.cell(column=column_range[column_range_index], row=ws.max_row, value=a_dict[key])
                        column_range_index = column_range_index + 1



#         with open('', 'w', encoding='utf-8') as f:
          
          



        # with open('param_value.json', w, encoding='utf8') as f:
        #     json.dump(the_dict, f, skipkeys=True)
# def write_to_excel(needed_param_value_dict, needed_table_param_value_list):

    # fields = ['Способ определения поставщика (подрядчика, исполнителя)', 
    #             'Организация, осуществляющая размещение',
    #             'Почтовый адрес',
    #             'Наименование товара, работы, услуги по КТРУ',
    #             'Количество', 
    #             'Цена за ед.изм.',                
    #             'Адрес электронной площадки в информационно-телекоммуникационной сети «Интернет»', 
    #             'Начальная (максимальная) цена контракта', 
    #             'Дата и время окончания подачи заявок', 
    #             'Дата проведения аукциона в электронной форме', 
    #             'Дата и время подписания печатной формы извещения (соответствует дате направления на контроль по ч.5 ст.99 Закона 44-ФЗ либо дате размещения в ЕИС, в случае отсутствия контроля, по местному времени организации, осуществляющей размещение)']
    # column_range = [3, 4, 5, 12, 13, 14, 15, 16]
    # wb = load_workbook(filename='test_table.xlsx')
    # sheet = wb.active
    # first_column_len = len(wb['A'])
    # last_index_number = wb.cell(column=1, row=first_column_len).value
    # index_number = int(last_index_number) + 1

    # ws.cell(column=1, row=ws.max_row+1, value=index_number)
    # column_range_index = 0
    # # решить, как итерировать -- строки внутри ключей или ключи внутри строк
    # for row in wb.rows: 
    #     for key in needed_table_param_value_dict.keys():
    #             if key in fields: 
    #                 ws.cell(column=column_range[column_range_index], row=ws.max_row, value=a_dict[key])
    #                 column_range_index = column_range_index + 1



       

get_relevant_info()
# write_to_excel(needed_param_value_dict, needed_table_param_value_list)
#как сделать, чтобы одна функция передавала переменные другой 



