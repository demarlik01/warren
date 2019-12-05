from sqlalchemy.orm import Session

from models.stock import Stock
import xlrd


def insert_kospi_200_from_file(filepath: str, session: Session):
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)

    stock_list = []

    for row_idx in range(1, sheet.nrows):
        name = sheet.cell_value(row_idx, 0)
        code = f'{str(sheet.cell_value(row_idx, 1))}'
        stock_list.append(Stock(name=name, code=code))

    session.add_all(stock_list)
    session.commit()

