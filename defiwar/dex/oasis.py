from .common import append_params
from .common import execute_request


class Oasis(object):
    base_endpoint = 'https://api.oasisdex.com/v2'

    markets = '/markets'
    orders = '/orders'
    pairs = '/pairs'
    prices = '/prices'
    trades = '/trades'
    volumes = '/volumes'

    def get_markets(self, base=None, quote=None):
        url = self.base_endpoint + self.markets
        if base and quote:
            url += '/' + base + '/' + quote
        return execute_request(url)
    
    def get_orders(self, base=None, quote=None):
        url = self.base_endpoint + self.orders
        print(url)
        if base and quote:
            url += '/' + base + '/' + quote
        return execute_request(url)
    
    def get_pairs(self, base=None, quote=None):
        url = self.base_endpoint + self.pairs
        if base and quote:
            url += '/' + base + '/' + quote
        return execute_request(url)
    
    def get_prices(self, base=None, quote=None):
        url = self.base_endpoint + self.prices
        if base and quote:
            url += '/' + base + '/' + quote
        return execute_request(url)
    
    def get_trades(self, base, quote, *args):
        url = self.base_endpoint + self.trades + '/' + base + '/' + quote
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_volumes(self, base=None, quote=None):
        url = self.base_endpoint + self.volumes
        if base and quote:
            url += '/' + base + '/' + quote
        return execute_request(url)
