coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
def for_dict(coin, code):
    s = dict(zip(coin, code))
    return s
print(for_dict(coin, code))