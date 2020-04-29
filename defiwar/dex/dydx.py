from .common import append_params
from .common import execute_request


class DyDx(object):

    base_endpoint = 'https://api.dydx.exchange/'

    fills = 'v2/fills'
    orderbook = 'v1/orderbook/'
    orders = 'v2/orders'
    trades = 'v2/trades'
    stats_markets = 'v1/stats/markets'
    candles = 'v1/candles/'
    markets = 'v2/markets/'
    accounts = 'v1/accounts/'
    perpetual_markets = 'v1/perpetual-markets'
    perpetual_accounts = 'v1/perpetual-accounts/'
    perpetual_balance_updates = 'v1/perpetual-balance-updates'
    standard_actions = 'v1/standard-actions'

    # Trading API

    def get_orderbook(self, market):
        url = self.base_endpoint + self.orderbook + market
        return execute_request(url)

    def get_orders(self, *args):
        url = self.base_endpoint + self.orders
        url = append_params(url, *args)
        return execute_request(url)

    def get_trades(self, *args):
        url = self.base_endpoint + self.orders
        url = append_params(url, *args)
        return execute_request(url)

    def get_fills(self, *args):
        url = self.base_endpoint + self.fills
        url = append_params(url, *args)
        return execute_request(url)

    def get_stats_markets(self):
        url = self.base_endpoint + self.stats_markets
        return execute_request(url)

    def get_candles(self, *args):
        url = self.base_endpoint + self.candles
        url = append_params(url, *args)
        return execute_request(url)

    # Solo API

    def get_markets(self, market=None):
        url = self.base_endpoint + self.markets
        if market:
            url += market
        return execute_request(url)

    def get_accounts(self, address, number=None):
        url = self.base_endpoint + self.accounts + address
        if number:
            url += '?number=' + number
        return execute_request(url)

    # Perpetual API

    def get_perpetual_markets(self):
        url = self.base_endpoint + self.perpetual_markets
        return execute_request(url)

    def get_perpetual_balance_updates(self, *args):
        url = self.base_endpoint + self.perpetual_balance_updates
        url = append_params(url, *args)
        return execute_request(url)

    def get_standard_actions(self, *args):
        url = self.base_endpoint + self.stats_markets
        url = append_params(url, *args)
        return execute_request(url)

    def get_perpetual_accounts(self, wallet_address):
        url = self.base_endpoint + self.perpetual_accounts + wallet_address
        return execute_request(url)
