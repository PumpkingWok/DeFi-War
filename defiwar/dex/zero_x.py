from .common import append_params
from .common import execute_request


class ZeroX(object):

    base_endpoint = 'https://api.0x.org/'
    ws_endpoint = 'wss://api.0x.org/sra/v3'

    swap_base = 'swap/v0/'
    swap_quote = 'quote'
    swap_tokens = 'tokens'
    swap_prices = 'prices'

    meta_tx_base = 'meta_transaction/v0/'
    meta_tx_price = 'price'
    meta_tx_quote = 'quote'

    sra_base = 'sra/v3/'
    sra_asset_pairs = 'asset_pairs'
    sra_orders = 'orders'
    sra_order_hash = 'order'
    sra_orderbook = 'orderbook'
    sra_fee_recipients = 'fee_recipients'

    # Swap API

    def get_swap_quote(self, *args):
        url = self.base_endpoint + self.swap_base + self.swap_quote
        url = append_params(url, *args)
        return execute_request(url)

    def get_swap_tokens(self):
        url = self.base_endpoint + self.swap_base + self.swap_tokens
        return execute_request(url)

    def get_swap_prices(self, sell_token=None):
        url = self.base_endpoint + self.swap_base + self.swap_prices
        if sell_token is not None:
            url += '?sellToken=' + sell_token
        return execute_request(url)

    # Meta Transactions API

    def get_meta_tx_price(self, *args):
        url = self.base_endpoint + self.meta_tx_base + self.meta_tx_price
        url = append_params(url, *args)
        return execute_request(url)

    def get_meta_tx_quote(self, *args):
        url = self.base_endpoint + self.meta_tx_base + self.meta_tx_quote
        url = append_params(url, *args)
        return execute_request(url)

    # SRA PAI
    
    def get_sra_asset_pairs(self, *args):
        url = self.base_endpoint + self.sra_base + self.sra_asset_pairs
        url = append_params(url, *args)
        return execute_request(url)

    def get_sra_orders(self, *args):
        url = self.base_endpoint + self.sra_base + self.sra_orders
        url = append_params(url, *args)
        return execute_request(url)

    def get_sra_order_hash(self, order_hash):
        url = self.base_endpoint + self.sra_base + self.sra_order_hash + '/' + order_hash
        return execute_request(url)

    def get_sra_orderbook(self, base_asset_data, quote_asset_data):
        url = self.base_endpoint + self.sra_base + self.sra_orderbook
        if base_asset_data:
            url += '?baseAssetData=' + base_asset_data
        if quote_asset_data:
            url += '&quoteAssetData=' + quote_asset_data
        return execute_request(url)

    def get_sra_fee_recipient(self):
        url = self.base_endpoint + self.sra_base + self.sra_fee_recipients
        return execute_request(url)
