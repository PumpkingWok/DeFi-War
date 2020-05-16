from .common import curve_fi_params
from .common import base_account

import os
import json


class CurveFi(object):

    current_path = os.path.dirname(os.path.abspath(__file__))

    curve_fi = curve_fi_params
    web3 = None

    def __init__(self, web3=None):
        if web3:
            self.web3 = web3

            for token, params in curve_fi_params.items():
                self.curve_fi[token]['swap']['abi'] = json.load(open(os.path.join(
                    self.current_path, 'abi/curve_fi/' + str(token) + '_swap.abi'), 'r')
                )
                self.curve_fi[token]['curve']['abi'] = json.load(open(os.path.join(
                    self.current_path, 'abi/curve_fi/' + str(token) + '_curve.abi'), 'r')
                )

            # compound
            self.curve_fi['compound']['swap']['contract'] = self.web3.eth.contract(
                address=self.curve_fi['compound']['swap']['address'],
                abi=self.curve_fi['compound']['swap']['abi']
            )
            self.curve_fi['compound']['curve']['contract'] = self.web3.eth.contract(
                address=self.curve_fi['compound']['curve']['address'],
                abi=self.curve_fi['compound']['curve']['abi']
            )

            # usdt
            self.curve_fi['usdt']['swap']['contract'] = self.web3.eth.contract(
                address=self.curve_fi['usdt']['swap']['address'],
                abi=self.curve_fi['usdt']['swap']['abi']
            )
            self.curve_fi['usdt']['curve']['contract'] = self.web3.eth.contract(
                address=self.curve_fi['usdt']['curve']['address'],
                abi=self.curve_fi['usdt']['curve']['abi']
            )

            # y
            self.curve_fi['y']['swap']['address'] = self.web3.eth.contract(
                address=self.curve_fi['y']['swap']['address'],
                abi=self.curve_fi['y']['swap']['abi']
            )
            self.curve_fi['y']['curve']['address'] = self.web3.eth.contract(
                address=self.curve_fi['y']['curve']['address'],
                abi=self.curve_fi['y']['curve']['abi']
            )

            # busd
            self.curve_fi['busd']['swap']['address'] = self.web3.eth.contract(
                address=self.curve_fi['busd']['swap']['address'],
                abi=self.curve_fi['busd']['swap']['abi']
            )
            self.curve_fi['busd']['curve']['address'] = self.web3.eth.contract(
                address=self.curve_fi['busd']['curve']['address'],
                abi=self.curve_fi['busd']['curve']['abi']
            )

            # susdv2
            self.curve_fi['susdv2']['swap']['address'] = self.web3.eth.contract(
                address=self    .curve_fi['susdv2']['swap']['address'],
                abi=self.curve_fi['susdv2']['swap']['abi']
            )
            self.curve_fi['susdv2']['curve']['address'] = self.web3.eth.contract(
                address=self.curve_fi['susdv2']['curve']['address'],
                abi=self.curve_fi['susdv2']['curve']['abi']
            )

            # pax
            self.curve_fi['pax']['swap']['address'] = self.web3.eth.contract(
                address=self.curve_fi['pax']['swap']['address'],
                abi=self.curve_fi['pax']['swap']['abi']
            )
            self.curve_fi['pax']['curve']['address'] = self.web3.eth.contract(
                address=self.curve_fi['pax']['curve']['address'],
                abi=self.curve_fi['pax']['curve']['abi']
            )

    # Swap token methods

    def get_virtual_price(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.get_virtual_price().call({'from': base_account})
        return response

    def calc_token_amount(self, token, amounts, deposit):
        response = self.curve_fi[token]['swap']['contract'].functions.calc_token_amount(
            amounts,
            deposit
        ).call({'from': base_account})
        return response

    def get_dy(self, token, i, j, dx):
        response = self.curve_fi[token]['swap']['contract'].functions.get_dy(
            i,
            j,
            dx
        ).call({'from': base_account})
        return response

    def get_dx(self, token, i, j, dy):
        response = self.curve_fi[token]['swap']['contract'].functions.get_dx(
            i,
            j,
            dy
        ).call({'from': base_account})
        return response

    def get_dy_underlying(self, token, i, j, dx):
        response = self.curve_fi[token]['swap']['contract'].functions.get_dy_underlying(
            i,
            j,
            dx
        ).call({'from': base_account})
        return response

    def get_dx_underlying(self, token, i, j, dy):
        response = self.curve_fi[token]['swap']['contract'].functions.get_dx_underlying(
            i,
            j,
            dy
        ).call({'from': base_account})
        return response

    def coins(self, token, arg0):
        response = self.curve_fi[token]['swap']['contract'].functions.coins(arg0).call({'from': base_account})
        return response

    def underlying_coins(self, token, arg0):
        response = self.curve_fi[token]['swap']['contract'].functions.coins(arg0).call({'from': base_account})
        return response

    def balances(self, token, arg0):
        response = self.curve_fi[token]['swap']['contract'].functions.balances(arg0).call({'from': base_account})
        return response

    def a(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.A().call({'from': base_account})
        return response

    def fee(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.fee().call({'from': base_account})
        return response

    def admin_fee(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.admin_fee().call({'from': base_account})
        return response

    def owner(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.owner().call({'from': base_account})
        return response

    def admin_actions_deadline(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.admin_actions_deadline().call(
            {'from': base_account}
        )
        return response

    def transfer_ownership_deadline(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.transfer_ownership_deadline().call(
            {'from': base_account}
        )
        return response

    def future_a(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.future_a().call({'from': base_account})
        return response

    def future_fee(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.future_fee().call({'from': base_account})
        return response

    def future_admin_fee(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.future_admin_fee().call({'from': base_account})
        return response

    def future_owner(self, token):
        response = self.curve_fi[token]['swap']['contract'].functions.future_owner().call({'from': base_account})
        return response

    # Curve token methods

    def total_supply(self, token):
        response = self.curve_fi[token]['curve']['contract'].functions.totalSupply().call({'from': base_account})
        return response

    def allowance(self, token,  _owner, _spender):
        response = self.curve_fi[token]['curve']['contract'].functions.allowance().call({'from': base_account})
        return response

    def name(self, token):
        response = self.curve_fi[token]['curve']['contract'].functions.name().call({'from': base_account})
        return response

    def symbol(self, token):
        response = self.curve_fi[token]['curve']['contract'].functions.name().call({'from': base_account})
        return response

    def decimals(self, token):
        response = self.curve_fi[token]['curve']['contract'].functions.decimals().call({'from': base_account})
        return response

    def balance_of(self, token, arg0):
        response = self.curve_fi[token]['curve']['contract'].functions.balanceOf(arg0).call({'from': base_account})
        return response
