from typing import List

from sqlalchemy.orm import Session

from models.calculate import Calculate


def show_result(session: Session):
    calc_list: List[Calculate] = session.query(Calculate).all()
    high_sum = 0
    for calc in calc_list:
        sd = calc.sd
        low = (calc.mean - (sd * 1))
        high = (calc.mean + (sd * 1))
        result = f'종목: {calc.stock.name} | 코드: {calc.stock.code} | 최저: {low} | 최고: {high}'
        print(result + '\n')

