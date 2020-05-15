import requests


class Synthetix(object):
    http_subgraph = 'https://api.thegraph.com/subgraphs/name/synthetixio-team/synthetix'
    ws_subgraph = 'wss://api.thegraph.com/subgraphs/name/synthetixio-team/synthetix'

    def post_request(self, query):
        r = requests.post(self.http_subgraph, json={'query': query})
        return r.text
