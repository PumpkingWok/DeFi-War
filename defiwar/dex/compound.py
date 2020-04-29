from .common import append_params
from .common import execute_request


class Compound(object):

    base_endpoint = 'https://api.compound.finance/api/v2/'

    account = 'account'
    ctoken = 'ctoken'
    graph = 'market_history/graph'
    gov_proposals = 'governance/proposals'
    gov_proposal_vote_receipts = 'governance/proposal_vote_receipts'
    gov_accounts = 'governance/accounts'
    gov_history = 'governance/history'
    gov_profile = 'governance/profile'

    def get_account(self, *args):
        url = self.base_endpoint + self.account
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_ctoken(self, *args):
        url = self.base_endpoint + self.ctoken
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_graph(self, *args):
        url = self.base_endpoint + self.graph
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gov_proposals(self, *args):
        url = self.base_endpoint + self.gov_proposals
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gov_proposal_vote_receipts(self, *args):
        url = self.base_endpoint + self.gov_proposal_vote_receipts
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gov_accounts(self, *args):
        url = self.base_endpoint + self.gov_accounts
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_gov_history(self, *args):
        url = self.base_endpoint + self.gov_history
        url = append_params(url, *args)
        return execute_request(url)

    # TODO
    # def post_gov_profile(self, *args):
