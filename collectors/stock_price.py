from typing import List
from datetime import datetime

import requests
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup
from models.stock import Stock
from models.price import Price


def _fetch_price(stock: Stock):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)' \
         'Chrome/78.0.3904.97 Safari/537.36'
    url = f'https://finance.naver.com/item/sise_day.nhn?code={stock.code}'
    price_list = []

    for idx in range(1, 3):
        response = requests.get(
            headers={'user-agent': ua},
            url=f'{url}&page={idx}'
        )
        soup = BeautifulSoup(response.text, features='html.parser')
        tr_list = soup.find_all('tr')
        for tr in tr_list:
            if 'onmouseover' in tr.attrs:
                tds = tr.find_all('td')
                date_str = tds[0].find('span').text
                date = datetime.strptime(date_str, '%Y.%m.%d')
                price_str = tds[1].find('span').text
                price = int(price_str.replace(',', ''))
                price_list.append(Price(price=price, stock=stock, created_at=date))

    return price_list


def load_price(session: Session):
    stock_list: List[Stock] = session.query(Stock).all()
    price_list = []
    for stock in stock_list:
        price_list_by_stock = _fetch_price(stock)
        price_list = price_list + price_list_by_stock

    session.add_all(price_list)
    session.commit()
