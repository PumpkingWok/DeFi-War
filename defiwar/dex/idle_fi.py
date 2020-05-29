from .common import idle_fi_params
from .common import base_account
from web3 import Web3

import json
import os


class IdleFi(object):

    current_path = os.path.dirname(os.path.abspath(__file__))

    idle_fi = idle_fi_params
    web3 = None

    def __init__(self, web3=None):
        if web3:
            self.web3 = web3

            for token, params in idle_fi_params.items():
                self.idle_fi[token]['max']['abi'] = json.load(open(os.path.join(
                    self.current_path, 'abi/idle_fi/' + str(token) + '_max.abi'), 'r')
                )
                self.idle_fi[token]['risk']['abi'] = json.load(open(os.path.join(
                    self.current_path, 'abi/idle_fi/' + str(token) + '_risk.abi'), 'r')
                )
            
            # DAI
            self.idle_fi['dai']['max']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['dai']['max']['address'],
                abi=self.idle_fi['dai']['max']['abi']
            )
            self.idle_fi['dai']['risk']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['dai']['risk']['address'],
                abi=self.idle_fi['dai']['risk']['abi']
            )

            # USDC
            self.idle_fi['usdc']['max']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['usdc']['max']['address'],
                abi=self.idle_fi['usdc']['max']['abi']
            )
            self.idle_fi['usdc']['risk']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['usdc']['risk']['address'],
                abi=self.idle_fi['usdc']['risk']['abi']
            )

            # USDT
            self.idle_fi['usdt']['max']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['usdt']['max']['address'],
                abi=self.idle_fi['usdt']['max']['abi']
            )
            self.idle_fi['usdt']['risk']['contract'] = self.web3.eth.contract(
                address=self.idle_fi['usdt']['risk']['address'],
                abi=self.idle_fi['usdt']['risk']['abi']
            )

    def all_available_tokens(self, token, y_type, index):
        response = self.idle_fi[token][y_type]['contract'].functions.allAvailableTokens(index).call(
            {'from': base_account}
        )
        return response
    
    def allowance(self, token, y_type, owner, spender):
        owner = Web3.toChecksumAddress(owner)
        spender = Web3.toChecksumAddress(spender)
        response = self.idle_fi[token][y_type]['contract'].functions.allowance(owner, spender).call(
            {'from': base_account}
        )
        return response
    
    def balance_of(self, token, y_type, address):
        address = Web3.toChecksumAddress(address)
        response = self.idle_fi[token][y_type]['contract'].functions.balance_of(address).call({'from': base_account})
        return response
    
    def decimals(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.decimals().call({'from': base_account})
        return response
    
    def fee(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.fee().call({'from': base_account})
        return response
    
    def fee_address(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.feeAddress().call({'from': base_account})
        return response
    
    def get_aprs(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.getAPRs().call({'from': base_account})
        return response
    
    def get_avg_apr(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.getAvgAPR().call({'from': base_account})
        return response
    
    def get_current_allocations(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.getCurrentAllocations().call(
            {'from': base_account}
        )
        return response
    
    def gst2(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.gst2().call({'from': base_account})
        return response

    def i_token(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.iToken().call({'from': base_account})
        return response
    
    def is_new_protocol_delayed(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.isNewProtocolDelayed().call({'from': base_account})
        return response
    
    def is_owner(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.isOwner().call({'from': base_account})
        return response
    
    def is_pauser(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.isPauser().call({'from': base_account})
        return response
    
    def is_risk_adjusted(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.isRiskAdjusted().call({'from': base_account})
        return response
    
    def last_allocations(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.lastAllocations().call({'from': base_account})
        return response
    
    def last_token_price(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.lastTokenPrice().call({'from': base_account})
        return response
    
    def manual_play(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.manualPlay().call({'from': base_account})
        return response
    
    def name(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.name().call({'from': base_account})
        return response
    
    def owner(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.owner().call({'from': base_account})
        return response
    
    def paused(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.paused().call({'from': base_account})
        return response
    
    def price_calculator(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.priceCalculator().call({'from': base_account})
        return response
    
    def protocol_wrappers(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.protocolWrappers().call({'from': base_account})
        return response
    
    def rebalancer(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.rebalancer().call({'from': base_account})
        return response
    
    def release_times(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.releaseTimes().call({'from': base_account})
        return response

    def symbol(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.symbol().call({'from': base_account})
        return response
    
    def token(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.token().call({'from': base_account})
        return response
    
    def token_decimals(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.tokenDecimals().call({'from': base_account})
        return response
    
    def token_price(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.tokenDecimals().call({'from': base_account})
        return response

    def total_supply(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.totalSupply().call({'from': base_account})
        return response
    
    def user_avg_prices(self, token, y_type):
        response = self.idle_fi[token][y_type]['contract'].functions.userAvgPrices().call({'from': base_account})
        return response
