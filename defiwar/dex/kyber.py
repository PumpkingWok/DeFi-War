from .common import append_params
from .common import execute_request


class Kyber(object):
    base_endpoint = 'https://api.kyber.network'

    buy_rate = '/buy_rate'
    change24h = '/change24h'
    currencies = '/currencies'
    enable_data = '/enable_data'
    gas_limit = '/gas_limit'
    gas_limit_config = '/gasLimitConfig'
    market = '/market'
    quote_amount = '/quote_amount'
    sell_rate = '/sell_rate'
    trade_data = '/trade_data'
    transfer_data = '/transfer_data'
    users = '/users'

    def get_buy_rate(self, *args):
        url = self.base_endpoint + self.buy_rate
        url = append_params(url, *args)
        return execute_request(url)

    def get_change24h(self, only_official_reserve=True):
        url = self.base_endpoint + self.change24h
        if not only_official_reserve:
            url += '?only_official_reserve=' + str(only_official_reserve)
        print(url)
        return execute_request(url)
    
    def get_currencies(self, *args):
        url = self.base_endpoint + self.currencies
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gas_limit(self, *args):
        url = self.base_endpoint + self.gas_limit
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gas_limit_config(self):
        url = self.base_endpoint + self.gas_limit_config
        return execute_request(url)
    
    def get_market(self):
        url = self.base_endpoint + self.market
        return execute_request(url)
    
    def get_quote_amount(self, *args):
        url = self.base_endpoint + self.quote_amount
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_sell_rate(self, *args):
        url = self.base_endpoint + self.sell_rate
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_trade_data(self, *args):
        url = self.base_endpoint + self.sell_rate
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_transfer_data(self, *args):
        url = self.base_endpoint + self.transfer_data
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_users_currencies(self, user_address):
        url = self.base_endpoint + self.users + '/' + user_address + self.currencies
        return execute_request(url)
    
    def get_users_currencies_enable_data(self, *args, user_address, currency_id):
        url = self.base_endpoint + self.users + '/' + user_address + self.currencies + '/' + currency_id + self.enable_data
        url = append_params(url, *args)
        return execute_request(url)

    

    


