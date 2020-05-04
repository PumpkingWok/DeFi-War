from .compound import append_params
from .common import execute_request
from .common import base_account
from web3 import Web3
import json
import os


class OneInch(object):

    base_endpoint = 'https://api.1inch.exchange/v1.1/'
    tokens = 'tokens'
    exchanges = 'exchanges'
    quote = 'quote'
    swap = 'swap'
    swap_quote = 'swapQuote'

    one_inch_split_address = Web3.toChecksumAddress('0xC586BeF4a0992C495Cf22e1aeEE4E446CECDee0E')

    current_path = os.path.dirname(os.path.abspath(__file__))
    one_inch_split_abi = json.load(open(os.path.join(current_path, 'abi/one_inch_split.abi'), 'r'))
    one_inch_split_contract = None

    web3 = None

    def __init__(self, web3=None):
        if web3:
            self.web3 = web3
            self.one_inch_split_contract = self.web3.eth.contract(
                address=self.one_inch_split_address,
                abi=self.one_inch_split_abi)

    # Off-chain API

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

    # On-chain API

    def get_expected_return(self, from_token, to_token, amount, parts, disable_flags):
        contract_response = self.one_inch_split_contract.functions.getExpectedReturn(
            from_token,
            to_token,
            amount,
            parts,
            disable_flags
        ).call({'from': base_account})
        return contract_response
