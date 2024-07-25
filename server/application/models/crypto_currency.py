from safrs import SAFRSBase, jsonapi_rpc
import datetime
from application.db import db
from application.const import *

ALL_CURRENCIES = "BTC,ETH,BNB,ADA,DOGE,XRP,USDT,DOT,ICP,HEX,LTC,LINK,VET,MATIC,XMR,AAVE,NEO,SHIB,TRX,LUNA,BCH"


class CryptoCurrency(SAFRSBase, db.Model):
    """
        description: This is CryptoCurrency
    """
    __tablename__ = "CryptoCurrency"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    name = db.Column(db.String)
    logo_url = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.String)
    price_timestamp = db.Column(db.DateTime(timezone=False))
    circulating_supply = db.Column(db.String)
    max_supply = db.Column(db.String)
    market_cap = db.Column(db.String)
    market_cap_dominance = db.Column(db.String)
    num_exchanges = db.Column(db.String)
    num_pairs = db.Column(db.String)
    num_pairs_unmapped = db.Column(db.String)
    first_trade = db.Column(db.DateTime(timezone=False))
    first_order_book = db.Column(db.DateTime(timezone=False))
    high = db.Column(db.String)
    high_timestamp = db.Column(db.DateTime(timezone=False))
    volume = db.Column(db.String)
    price_change = db.Column(db.String)
    price_change_pct = db.Column(db.String)

    @classmethod
    @jsonapi_rpc()
    def get_date_range(cls, **kwargs):
        """
            description: Get currencies from time range
            args:
                date1: date 1
                date2: date 2
        """
        date1 = datetime.datetime.strptime(kwargs['date1'], "%Y-%m-%d %H:%M:%S")
        date2 = datetime.datetime.strptime(kwargs['date2'], "%Y-%m-%d %H:%M:%S")
        prices = db.session.query(CryptoCurrency).filter(CryptoCurrency.price_timestamp.between(date1, date2)).all()
        return {RESULT: prices}

    @classmethod
    @jsonapi_rpc()
    def add_list_of_currencies(cls, **kwargs):
        """
            description: Get message
            args:
                crypto_data: cryptocurrencies data
        """
        crypto_data = kwargs['crypto_data']
        for c in crypto_data:
            max_supply = c['max_supply'] if 'max_supply' in c else "unknown"
            pr_timestamp = datetime.datetime.strptime(c['price_timestamp'], "%Y-%m-%dT%H:%M:%SZ")
            fr_trade = datetime.datetime.strptime(c['first_trade'], "%Y-%m-%dT%H:%M:%SZ")
            fr_order_book = datetime.datetime.strptime(c['first_order_book'], "%Y-%m-%dT%H:%M:%SZ")
            hi_timestamp = datetime.datetime.strptime(c['high_timestamp'], "%Y-%m-%dT%H:%M:%SZ")

            local_object = db.session.merge(
                CryptoCurrency(
                    code=c['id'],
                    name=c['name'],
                    logo_url=c['logo_url'],
                    status=c['status'],
                    price=c['price'],
                    price_timestamp=pr_timestamp,
                    circulating_supply=c['circulating_supply'],
                    max_supply=max_supply,
                    market_cap=c['market_cap'],
                    market_cap_dominance=c['market_cap_dominance'],
                    num_exchanges=c['num_exchanges'],
                    num_pairs=c['num_pairs'],
                    num_pairs_unmapped=c['num_pairs_unmapped'],
                    first_trade=fr_trade,
                    first_ordered_book=fr_order_book,
                    high=c['high'],
                    high_timestamp=hi_timestamp,
                    volume=c['1d']['volume'],
                    price_change=c['1d']['price_change'],
                    price_change_pct=c['1d']['price_change_pct']
                )
            )
            db.session.add(local_object)
            db.session.commit()

        return {RESULT: DB_UPDATED}

    @classmethod
    @jsonapi_rpc()
    def get_cryptocurrencies_by_code(cls, **kwargs):
        """
            description: Get message
            args:
                currencies_list: list of currencies
        """
        currencies_list = kwargs['currencies_list'].split(",")
        currencies = []
        for c in currencies_list:
            currencies.append(db.session.query(CryptoCurrency).filter(CryptoCurrency.code == c)
                              .order_by(CryptoCurrency.price_timestamp.desc()).first())

        return {RESULT: currencies}

    @classmethod
    @jsonapi_rpc()
    def get_cryptocurrency_history(cls, **kwargs):
        """
            description: Get cryptocurrency historical data
            args:
                cryptocurrency_code: code of cryptocurrency
        """
        code = kwargs['cryptocurrency_code']

        currency_history = db.session.query(CryptoCurrency).filter(CryptoCurrency.code == code).order_by(CryptoCurrency.price_timestamp.asc()).all()

        return {RESULT: currency_history}

    @classmethod
    @jsonapi_rpc()
    def get_hot_currencies(cls):
        """
            description: Get hostest cryptocurrencies
        """
        kwargs = {'currencies_list': ALL_CURRENCIES}
        res = CryptoCurrency.get_cryptocurrencies_by_code(**kwargs)['result']
        res.sort(key=lambda x: float(x.price_change_pct), reverse=True)

        return {RESULT: res[:10]}
