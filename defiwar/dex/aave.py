import requests


class Aave(object):
    http_subgraph = 'https://api.thegraph.com/subgraphs/name/aave/protocol-raw'
    ws_subgraph = 'wss://api.thegraph.com/subgraphs/name/aave/protocol-raw'

    def post_request(self, query):
        r = requests.post(self.http_subgraph, json={'query': query})
        return r.text
