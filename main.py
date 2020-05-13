from defiwar.dex.aave import Aave
from defiwar.dex.compound import Compound
from defiwar.dex.dydx import DyDx
from defiwar.dex.one_inch import OneInch
from defiwar.dex.radar_relay import RadarRelay
from defiwar.dex.kyber import Kyber
from defiwar.dex.uniswap import Uniswap
from defiwar.dex.zero_x import ZeroX

from web3 import HTTPProvider
from defiwar.dex.common import *

if __name__ == "__main__":

    web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/2f91050e6c9c4b888d3b722c752766bc'))
    aave_dex = Aave()
    compound_dex = Compound()
    dydx_dex = DyDx()
    one_inch_dex = OneInch(web3)
    radar_relay_exchange = RadarRelay()
    kyber_exchange = Kyber()
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
    # print(zero_x_exchange.get_swap_tokens())

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

    # Kyber API
    print(kyber_exchange.get_buy_rate(
        'id=0xdd974D5C2e2928deA5F71b9825b8b646686BD200',
        'qty=300',
        'id=0xd26114cd6EE289AccF82350c8d8487fedB8A0C07',
        'qty=10.1'
    ))
    print(kyber_exchange.get_change24h(only_official_reserve=False))
    print(kyber_exchange.get_currencies())
    print(kyber_exchange.get_gas_limit_config())
    print(kyber_exchange.get_market())
    print(kyber_exchange.get_quote_amount(
        'base=0xdd974d5c2e2928dea5f71b9825b8b646686bd200',
        'quote=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        'base_amount=10', 'type=sell'
    ))
    print(kyber_exchange.get_gas_limit(
        'source=0x6b175474e89094c44da98b954eedeac495271d0f',
        'dest=0xd26114cd6ee289accf82350c8d8487fedb8a0c07',
        'amount=10000'
    ))
    print(kyber_exchange.get_users_currencies('0x8fA07F46353A2B17E92645592a94a0Fc1CEb783F'))
