import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.stock import Stock
from models.price import Price
from models.calculate import Calculate

DB_URL = 'sqlite:///warren.db'
db_engine = create_engine(DB_URL)
Session = sessionmaker(bind=db_engine)
session = Session()


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    Base.metadata.create_all(db_engine, checkfirst=True)


@cli.command()
@click.option('-f', '--filepath')
def init_kospi_200(filepath):
    """
    :param filepath: canonical path for kospi-200 .xls file
    :return:
    """
    from collectors.kospi_200 import insert_kospi_200_from_file
    # https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage
    insert_kospi_200_from_file(filepath, session)


@cli.command()
def load_price():
    from collectors.stock_price import load_price
    load_price(session)


@cli.command()
def calc_mean_sd():
    from collectors.calc_mean_sd import cal_mean_sd
    cal_mean_sd(session)


@cli.command()
def show_result():
    from collectors.calc_result import show_result
    show_result(session)


if __name__ == '__main__':
    cli()
