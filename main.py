from parse import parse
from diagrams.categories import create_categories
from diagrams.quantile import create_quantile
from diagrams.comparison import create_comparison
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
    ], 'categories.svg')

    # Spawn Strategy
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'all-blocks+reuse+redundancy-checks'
    ], [
        (97/255, 61/255, 193/255),
        (237/255, 33/255, 124/255)
    ], 'spawn-strategy-quantile.svg', False)
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'all-blocks+reuse+redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'spawn-strategy-quantile-both-correct.svg', True)

    create_comparison(data, [
        'program-entry+reuse+redundancy-checks',
        'all-blocks+reuse+redundancy-checks'
    ], 'spawn-strategy-comparison.svg')

    # Component Reuse
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+no-reuse+redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'component-reuse-quantile.svg', False)
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+no-reuse+redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'component-reuse-quantile-both-correct.svg', True)
    create_comparison(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+no-reuse+redundancy-checks'
    ], 'component-reuse-comparison.svg')

    # Redundancy Checks
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+reuse+no-redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'redundancy-checks-quantile.svg', False)
    create_quantile(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+reuse+no-redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'redundancy-checks-quantile-both-correct.svg', True)

    create_comparison(data, [
        'program-entry+reuse+redundancy-checks',
        'program-entry+reuse+no-redundancy-checks'
    ], 'redundancy-checks-comparison.svg')

    # Redundancy Checks
    create_quantile(data, [
        'baseline-predicateAnalysis',
        'program-entry+reuse+redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'comparison-with-predicate.svg', False)
    create_quantile(data, [
        'baseline-predicateAnalysis',
        'program-entry+reuse+redundancy-checks'
    ], [
        (97 / 255, 61 / 255, 193 / 255),
        (237 / 255, 33 / 255, 124 / 255)
    ], 'comparison-with-predicate-both-correct.svg', True)



