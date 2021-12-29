from parse import parse
from diagrams.categories import create_categories
import pickle

if __name__ == '__main__':
    try:
        with open('data.txt', 'rb') as file:
            data = pickle.load(file)
    except:
        data = parse()
        with open('data.txt', 'wb') as file:
            file.write(pickle.dumps(data))

    create_categories(data, [
        'baseline-predicateAnalysis',
        'baseline-predicateAnalysis-backwards',
        'all-blocks+reuse+redundancy-checks',
        'all-blocks+reuse+no-redundancy-checks',
        'program-entry+reuse+redundancy-checks',
        'program-entry+reuse+no-redundancy-checks'
    ])


