import requests
from bs4 import BeautifulSoup as bs

def get_html(url, headers):
    try:
        result = requests.get(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=82066963', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        return False

def get_relevant_info():
    html = get_html(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=82066963', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
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
                    tbody_th.append(every_th.text)
            else:
                try_td = tr.find_all('td')
                # print(try_td)
                # print('1')
                if try_td: 
                    tbody_td = []           
                    for every_td in try_td:
                        tbody_td.append(every_td.text)
                        # print(tbody_td)
                    table_param_value_dict = dict(zip(tbody_th, tbody_td))
                    table_param_value_list.append(table_param_value_dict)

        print(table_param_value_list)


       

get_relevant_info()