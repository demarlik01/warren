from typing import List
import statistics

from sqlalchemy.orm import Session

from models.price import Price

from models.calculate import Calculate


def cal_mean_sd(session: Session):
    price_list: List[Price] = session.query(Price).all()

    # this wii be {stock_id: {stock: stock, price_list:[]}, ...}
    stock_price_map = {}
    for price in price_list:
        if price.stock_id in stock_price_map:
            _price_list = stock_price_map[price.stock_id].get('price_list')
            _price_list.append(price.price)
        else:
            stock_price_map[price.stock_id] = {'stock': price.stock, 'price_list': [price.price]}

    calc_list = []

    for _stock_price in stock_price_map.values():
        _stock = _stock_price.get('stock')
        _price_list = _stock_price.get('price_list')
        mean = statistics.mean(_price_list)
        sd = statistics.pstdev(_price_list)

        calc_list.append(Calculate(mean=mean, sd=sd, stock=_stock))

    session.add_all(calc_list)
    session.commit()
