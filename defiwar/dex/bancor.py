from .common import append_params
from .common import execute_request


class Bancor(object):
    base_endpoint = 'https://api.bancor.network/0.1/currencies'

    convertible_pairs = '/convertiblePairs'
    ticker = '/ticker'
    value = '/value'
    volume_history = '/volumeHistory'

    def get_available_pairs(self):
        url = self.base_endpoint + self.convertible_pairs
        return execute_request(url)

    def get_historical_volume(self, to_currency_code, from_currency_code, time_frame, start_date=None, end_date=None):
        url = self.base_endpoint + \
              self.volume_history + \
              '?toCurrencyCode=' + to_currency_code + \
              '&fromCurrencyCode=' + from_currency_code + \
              '&timeFrame=' + time_frame
        if start_date:
            url += '&startDate=' + start_date
        if end_date:
            url += '&endDate=' + end_date
        return execute_request(url)

    def get_price_discovery(self, from_currency_code, to_currency_code, amount):
        url = self.base_endpoint + '/' +\
              from_currency_code + \
              self.value + \
              '?toCurrencyCode=' + to_currency_code + \
              '&toAmount=' + amount
        return execute_request(url)

    def get_price_ticker(self, to_token, from_token, display_currency):
        url = self.base_endpoint + '/' + \
              to_token + \
              self.ticker +\
              '?fromCurrencyCode=' + from_token +\
              '&displayCurrencyCode=' + display_currency
        return execute_request(url)

    def get_token_data(self, *args):
        url = self.base_endpoint
        url += append_params(url, *args)
        return execute_request(url)
