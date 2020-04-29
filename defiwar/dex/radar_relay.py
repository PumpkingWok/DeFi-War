from .common import append_params
from .common import execute_request


class RadarRelay(object):

    base_endpoint = 'https://api.radarrelay.com/v3'
    ws_endpoint = 'wss://ws.radarrelay.com/v3'

    book = '/book'
    candles = '/candles'
    fills = '/fills'
    history = '/history'
    markets = '/markets/'
    orders = '/orders/'
    ticker = '/ticker'
    tokens = '/tokens'
    stats = '/stats'
    validate = '/validate'

    # Orders API

    def get_order(self, order_hash):
        url = self.base_endpoint + self.orders + order_hash
        return execute_request(url)

    def validate_order(self, order_hash):
        url = self.base_endpoint + self.orders + order_hash + self.validate
        return execute_request(url)

    # Markets API

    def list_markets(self, *args):
        url = self.base_endpoint + self.markets
        url = append_params(url, *args)
        return execute_request(url)

    def get_market(self, *args):
        url = self.base_endpoint + self.markets
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_market_ticker(self, market_id=None):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.ticker
        return execute_request(url)
    
    def get_market_stats(self, market_id=None):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.stats
        return execute_request(url)
    
    def get_market_history(self, market_id=None):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.history
        return execute_request(url)

    def list_market_fills(self, market_id=None, *args):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.fills
        url = append_params(url, *args)
        return execute_request(url)

    def list_market_candles(self, market_id=None, *args):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.candles
        url = append_params(url, *args)
        return execute_request(url)

    def get_market_book(self, market_id=None):
        url = self.base_endpoint + self.markets
        if market_id is not None:
            url += market_id + self.book
        return execute_request(url)

    # Tokens API

    def list_tokens(self):
        url = self.base_endpoint + self.tokens
        return execute_request(url)
    
    def get_order_book(self, base_token, quote_token):
        url = self.base_endpoint + self.orders + base_token + '-' + quote_token + self.book
        return execute_request(url)
