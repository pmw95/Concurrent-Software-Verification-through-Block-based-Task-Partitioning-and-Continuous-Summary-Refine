from parse import parse
from diagrams.categories import create_categories
from diagrams.quantile import create_quantile
import pickle

if __name__ == '__main__':
    try:
        with open('data.txt', 'rb') as file:
            data = pickle.load(file)
    except:
        data = parse()
        with open('data.txt', 'wb') as file:
            file.write(pickle.dumps(data))

    # create_categories(data, [
    #     'baseline-predicateAnalysis',
    #     'baseline-predicateAnalysis-backwards',
    #     'all-blocks+reuse+redundancy-checks',
    #     'all-blocks+reuse+no-redundancy-checks',
    #     'program-entry+reuse+redundancy-checks',
    #     'program-entry+reuse+no-redundancy-checks'
    # ])

    create_quantile(data, [
        'baseline-predicateAnalysis',
        'program-entry+reuse+no-redundancy-checks',
        'program-entry+reuse+redundancy-checks'
    ], [
        (97/255, 61/255, 193/255),
        (237/255, 33/255, 124/255),
        (27 / 255, 153 / 255, 139 / 255)
    ])
