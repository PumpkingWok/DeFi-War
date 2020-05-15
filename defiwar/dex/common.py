import requests
from web3 import Web3

# ERC-20 Token Addresses

ant_token = Web3.toChecksumAddress('0x960b236A07cf122663c4303350609A66A7B288C0')
bat_token = Web3.toChecksumAddress('0x0D8775F648430679A709E98d2b0Cb6250d2887EF')
dai_token = Web3.toChecksumAddress('0x6b175474e89094c44da98b954eedeac495271d0f')
eth_token = Web3.toChecksumAddress('0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE')
knc_token = Web3.toChecksumAddress('0xdd974D5C2e2928deA5F71b9825b8b646686BD200')
link_token = Web3.toChecksumAddress('0x514910771AF9Ca656af840dff83E8264EcF986CA')
loom_token = Web3.toChecksumAddress('0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0')
mkr_token = Web3.toChecksumAddress('0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2')
sai_token = Web3.toChecksumAddress('0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359')
usdc_token = Web3.toChecksumAddress('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48')
weth_token = Web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
zrx_token = Web3.toChecksumAddress('0xE41d2489571d322189246DaFA5ebDe1F4699F498')

# ERC-20 Uniswap V1 Token Addresses

uni_bat_token = Web3.toChecksumAddress('0x2E642b8D59B45a1D8c5aEf716A84FF44ea665914')
uni_ant_token = Web3.toChecksumAddress('0x077d52B047735976dfdA76feF74d4d988AC25196')
uni_link_token = Web3.toChecksumAddress('0xF173214C720f58E03e194085B1DB28B50aCDeeaD')
uni_loom_token = Web3.toChecksumAddress('0x417CB32bc991fBbDCaE230C7c4771CC0D69daA6b')
uni_mkr_token = Web3.toChecksumAddress('0x2C4Bd064b998838076fa341A83d007FC2FA50957')
uni_sai_token = Web3.toChecksumAddress('0x09cabEC1eAd1c0Ba254B09efb3EE13841712bE14')
uni_knc_token = Web3.toChecksumAddress('0x49c4f9bc14884f6210F28342ceD592A633801a8b')
uni_weth_token = Web3.toChecksumAddress('0xA2881A90Bf33F03E7a3f803765Cd2ED5c8928dFb')
uni_zrx_token = Web3.toChecksumAddress('0xaE76c84C9262Cdb9abc0C2c8888e62Db8E22A0bF')

# Curve_fi Addresses

curve_fi_params = {
    'compound': {
        'swap': {
            'address': Web3.toChecksumAddress('0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56')
        },
        'curve': {
            'address': Web3.toChecksumAddress('0x845838DF265Dcd2c412A1Dc9e959c7d08537f8a2')
        }
    },
    'usdt': {
        'swap': {
            'address': Web3.toChecksumAddress('0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C')
        },
        'curve': {
            'address': Web3.toChecksumAddress('0x9fC689CCaDa600B6DF723D9E47D84d76664a1F23')
        }
    },
    'y': {
        'swap': {
          'address': Web3.toChecksumAddress('0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51')
        },
        'curve': {
          'address': Web3.toChecksumAddress('0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8')
        }
    },
    'busd': {
        'swap': {
            'address': Web3.toChecksumAddress('0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27')
        },
        'curve': {
            'address': Web3.toChecksumAddress('0x3B3Ac5386837Dc563660FB6a0937DFAa5924333B')
        }
    },
    'susdv2': {
        'swap': {
            'address': Web3.toChecksumAddress('0xA5407eAE9Ba41422680e2e00537571bcC53efBfD')
        },
        'curve': {
            'address': Web3.toChecksumAddress('0xC25a3A3b969415c80451098fa907EC722572917F')
        }
    },
    'pax': {
        'swap': {
            'address': Web3.toChecksumAddress('0x06364f10B501e868329afBc005b3492902d6C763')
        },
        'curve': {
            'address': Web3.toChecksumAddress('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
        }
    }
}

base_account = Web3.toChecksumAddress('Your address')


def append_params(url, *args):
    if len(args) > 0:
        url += '?' + args[0]
    for param in args[1:]:
        url += '&' + param
    return url


def execute_request(url):
    r = requests.get(url=url)
    data = r.json()
    return data
