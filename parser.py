import requests
from bs4 import BeautifulSoup as bs

def get_html(url, headers):
    try:
        result = requests.get(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=82173485', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        return False

# def has_class(tag):
#     return tag.has_attr('class')

def get_relevant_info():
    html = get_html(url='http://zakupki.gov.ru/epz/order/notice/printForm/view.html?printFormId=82173485', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
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
        print(param_value_dict)

       

get_relevant_info()