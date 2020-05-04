from defiwar.dex.aave import Aave
from defiwar.dex.compound import Compound
from defiwar.dex.dydx import DyDx
from defiwar.dex.one_inch import OneInch
from defiwar.dex.radar_relay import RadarRelay
from defiwar.dex.uniswap import Uniswap
from defiwar.dex.zero_x import ZeroX

from web3 import Web3, HTTPProvider
from defiwar.dex.common import *

if __name__ == "__main__":

    web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/2f91050e6c9c4b888d3b722c752766bc'))
    aave_dex = Aave()
    compound_dex = Compound()
    dydx_dex = DyDx()
    one_inch_dex = OneInch(web3)
    radar_relay_exchange = RadarRelay()
    uniswap = Uniswap(web3)
    zero_x_exchange = ZeroX()

    # Compound API Calls
    '''print(compound_dex.get_account('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588', 'block_number=0'))
    print(compound_dex.get_ctoken('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588'))
    print(compound_dex.get_graph('asset=0xf5dce57282a584d2746faf1593d3121fcac444dc'))
    print(compound_dex.get_gov_proposals())
    print(compound_dex.get_gov_proposal_vote_receipts('proposal_id=2'))
    print(compound_dex.get_gov_accounts('page_size=1'))
    print(compound_dex.get_gov_history())

    # One1inch API Calls
    print(one_inch_dex.get_quote('100', from_token_symbol='DAI', to_token_symbol='ETH'))
    print(one_inch_dex.get_tokens())
    print(one_inch_dex.get_exchanges())

    # Radar Relay API Calls
    print(radar_relay_exchange.list_markets())
    print(radar_relay_exchange.get_market('marketId=ZRX-WETH'))
    print(radar_relay_exchange.get_market_ticker('ZRX-WETH'))
    print(radar_relay_exchange.get_market_stats('ZRX-WETH'))
    print(radar_relay_exchange.get_market_history('ZRX-WETH'))'''

    # ZeroX API Calls
    #print(zero_x_exchange.get_swap_tokens())

    # Aave GraphQl API
    query = """
        {
            lendingPoolConfigurationHistoryItems(first: 5) {
                id
                provider {
                    id
                }
                lendingPool
                lendingPoolCore
            }
            lendingPoolConfigurations(first: 5) {
                id
                lendingPool
                lendingPoolCore
                lendingPoolParametersProvider
            }
        }
        """
    print(aave_dex.post_request(query))

    # DyDx API
    print(dydx_dex.get_markets())
    print(one_inch_dex.get_expected_return(dai_token, usdc_token, 100, 100, 0))
    print(uniswap.get_eth_balance(uni_bat_token))
    print(uniswap.get_token_balance(bat_token, uni_bat_token))
