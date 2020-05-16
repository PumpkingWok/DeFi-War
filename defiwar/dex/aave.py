import requests


class Aave(object):
    http_subgraph = 'https://api.thegraph.com/subgraphs/name/aave/protocol-raw'
    ws_subgraph = 'wss://api.thegraph.com/subgraphs/name/aave/protocol-raw'

    query_objects = {
        'lendingPoolConfigurationHistoryItems': [],
        'lendingPoolConfigurations': [],
        'priceHistoryItems': [],
        'usdEthPriceHistoryItems': [],
        'chainlinkAggregators': [],
        'priceOracleAssets': [],
        'priceOracles': [],
        'aTokens': [],
        'referrers': [],
        'deposits': [],
        'redeemUnderlyings': [],
        'borrows': [],
        'swaps': [],
        'usageAsCollaterals': [],
        'rebalanceStableBorrowRates': [],
        'repays': [],
        'flashLoans': [],
        'liquidationCalls': [],
        'originationFeeLiquidations': [],
        'reserveConfigurationHistoryItems': [],
        'reserveParamsHistoryItems': [],
        'reserves': [],
        'aTokenBalanceHistoryItems': [],
        'userBorrowHistoryItems': [],
        'userReserves': [],
        'users': [],
        'lendingPoolAddressProviders': [],
        'userTransactions': []
    }

    def post_request(self, query):
        r = requests.post(self.http_subgraph, json={'query': query})
        return r.text

    def graph_request(self, query_object, parameters=None):
        if query_object in self.query_objects:
            query = """ 
                    {\n""" + query_object + """ {
            """
            if parameters and len(parameters) > 0:
                for parameter in parameters:
                    query += parameter + ','
                query += """
                    }}
                """
            else:
                query += """
                    id }}
                """
            r = requests.post(self.http_subgraph, json={'query': query})
            return r.text
