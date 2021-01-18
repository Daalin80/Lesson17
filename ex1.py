coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

def new_dict():
    new_dict = {}
    for i in code:
        new_idx = code.index(i)
        i2 = coin[new_idx]
        new_dict[i2] = i
    return new_dict

print(new_dict())