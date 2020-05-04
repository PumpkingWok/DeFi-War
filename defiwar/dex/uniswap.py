from .common import base_account
import os
import json


class Uniswap(object):

    current_path = os.path.dirname(os.path.abspath(__file__))
    erc_20_abi = json.load(open(os.path.join(current_path, 'abi/erc20.abi'), 'r'))
    uniswap_abi = json.load(open(os.path.join(current_path, 'abi/uniswap.abi'), 'r'))
    uniswap_factory_address = '0xe2f197885abe8ec7c866cFf76605FD06d4576218'
    uniswap_contract = None
    web3 = None

    def __init__(self, web3):
        self.web3 = web3

    def get_eth_balance(self, token_address):
        return self.web3.eth.getBalance(token_address)

    def get_token_balance(self, token_address, uni_ex_address):
        token = self.web3.eth.contract(address=token_address, abi=self.erc_20_abi)
        return token.functions.balanceOf(uni_ex_address).call({'from': base_account})

    def get_eth_token_input_price(self, token_address, qty):
        token = self.web3.eth.contract(address=token_address, abi=self.erc_20_abi)
        return token.getEthToTokenInputPrice(qty).call({'from': base_account})
