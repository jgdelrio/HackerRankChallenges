import sys
from pandas import read_csv


def get_top_n(filename, n=5):
    print(filename)
    data = read_csv(filename, header=None)
    # spaces are already removed...

    # Select top n and print it
    topn = data.iloc[:, 0].value_counts().index[:n]
    print('\n'.join(map(str, topn)))


if __name__ == '__main__':
    total = len(sys.argv)
    arguments = sys.argv

    if total == 0:
        raise ValueError('The filename is required as argument')
    if total > 2:
        n = arguments[2]
    else:
        n = 5
    get_top_n(arguments[1], n)
