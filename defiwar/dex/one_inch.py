from .compound import append_params
from .common import execute_request


class OneInch(object):

    base_endpoint = 'https://api.1inch.exchange/v1.1/'
    tokens = 'tokens'
    exchanges = 'exchanges'
    quote = 'quote'
    swap = 'swap'
    swap_quote = 'swapQuote'

    def get_tokens(self):
        url = self.base_endpoint + self.tokens
        return execute_request(url)
    
    def get_exchanges(self):
        url = self.base_endpoint + self.exchanges
        return execute_request(url)
    
    def get_quote(
            self,
            amount,
            from_token_symbol=None,
            from_token_address=None,
            to_token_symbol=None,
            to_token_address=None,
            disabled_exchanges_list=None
    ):
        url = self.base_endpoint + self.quote

        if from_token_address:
            url += '?fromTokenAddress=' + from_token_address
        else:
            url += '?fromTokenSymbol=' + from_token_symbol
        if to_token_address:
            url += '&toTokenAddress=' + to_token_address
        else:
            url += '&toTokenSymbol=' + to_token_symbol
        url += '&amount=' + amount

        if disabled_exchanges_list:
            url += '&disabledExchangesList=' + disabled_exchanges_list

        return execute_request(url)

    def get_swap(self, *args):

        url = self.base_endpoint + self.swap
        url = append_params(url, *args)
        return execute_request(url)

    def get_swap_quote(self, *args):

        url = self.base_endpoint + self.swap_quote
        url = append_params(url, *args)
        return execute_request(url)
