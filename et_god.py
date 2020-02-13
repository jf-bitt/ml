import pandas as pd
from collections import deque

best_chain = None
best_value = 0.0

def build_rates_dict(data):
    rates_dict = dict.fromkeys(data['Quote'].unique())
    for ccy1 in rates_dict:
        rates = []
        for row in data[data['Quote'] == ccy1][['Base', 'Rate']].itertuples(index=False, name=None):
            rates.append(row)

        rates_dict[ccy1] = rates

    return rates_dict


def build_chain(start_ccy, current_ccy, rates_dict, depth, max_depth, chain=None, value=1):
    global best_value, best_chain

    if max_depth < 2:
        return

    if chain is None:
        chain = deque()
        chain.append(current_ccy)

    if depth != max_depth:
        for dest_ccy, rate in rates_dict[current_ccy]:
            if dest_ccy not in chain:  # check if a currency is not part of a chain yet
                chain.append(dest_ccy)
                build_chain(start_ccy, dest_ccy, rates_dict, depth + 1, max_depth, chain, value * rate)
                chain.pop()
    else:
        # final conversion, thus find currency that matches with start_ccy
        currencies, rates = zip(*rates_dict[current_ccy])
        if start_ccy in list(currencies):
            idx = currencies.index(start_ccy)
            chain.append(start_ccy)
            final_chain = ' -> '.join(chain)
            value *= rates[idx]

            print('Max Depth: {}, Chain: {}, Final Value: {}'.format(max_depth, final_chain, value))

            if value > best_value:
                best_value = value
                best_chain = final_chain

            chain.pop()


def optimize_conversion(data):
    rates_dict = build_rates_dict(data)

    for max_depth in range(2, 15):
        print('Analyzing chain depth {}...'.format(max_depth))
        for ccy in rates_dict:
            build_chain(ccy, ccy, rates_dict, 1, max_depth)


def main():
    data = pd.read_csv('JPM Case - FX Rates.csv')
    optimize_conversion(data)

    print('Best Chain: {}'.format(best_chain))
    print('Best Value: {}'.format(best_value))


if __name__ == '__main__':
    main()
