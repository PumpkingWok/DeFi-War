import requests


class Synthetix(object):
    http_subgraph = 'https://api.thegraph.com/subgraphs/name/synthetixio-team/synthetix'
    ws_subgraph = 'wss://api.thegraph.com/subgraphs/name/synthetixio-team/synthetix'

    query_objects = {
        'synthetixes': ['id', 'issuers', 'snxHolders'],
        'transfers': ['id', 'from', 'to', 'value', 'timestamp', 'block', 'source'],
        'issueds': ['id', 'account', 'value', 'source', 'timestamp', 'gasPrice', 'block'],
        'issuers': ['id'],
        'snxholders': [
            'id',
            'block',
            'timestamp',
            'balanceOf',
            'collateral',
            'transferable',
            'initialDebtOwnership',
            'debtEntryAtIndex'
        ],
        'synthholders': ['id', 'source', 'block', 'timestamp', 'balanceOf'],
        'burneds': ['id', 'account', 'value', 'source', 'timestamp', 'gasPrice', 'block'],
        'contractUpdateds': ['id', 'source', 'target', 'block', 'timestamp'],
        'rewardEscrowHolders': ['id', 'balanceOf'],
        'feesClaimeds': ['id', 'account', 'value', 'rewards', 'block', 'timestamp']
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


