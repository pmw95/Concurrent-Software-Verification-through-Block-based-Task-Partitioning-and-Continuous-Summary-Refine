import matplotlib.pyplot as plt

from Run import Category
import numpy as np

def draw(data):
    plt.rc('text', usetex=True)
    plt.rcParams.update({'font.size': 11})

    colors = [
        (27/255, 153/255, 139/255),
        (97/255, 61/255, 193/255),
        (237/255, 33/255, 124/255)
    ]

    # (27/255, 153/255, 139/255),
    # (97/255, 61/255, 193/255),
    # (146/255, 20/255, 12/255)

    labels = [
        '\\textbf{Predicate Analysis}',
        '\\textbf{Predicate Analysis}\n\\textbf{(backwards)}',
        '\\textbf{Concurrent Analysis}\nSpawn on All Blocks\nWith Redundancy Checks',
        '\\textbf{Concurrent Analysis}\nSpawn on All Blocks\nNo Redundancy Checks',
        '\\textbf{Concurrent Analysis}\nSpawn on Program Entry\nWith Redundancy Checks',
        '\\textbf{Concurrent Analysis}\nSpawn on Program Entry\nNo Redundancy Checks',
    ]
    x = np.arange(len(data)) * 2
    width = 0.35

    correct = list(map(lambda key: data[key][Category.correct], data))
    error = list(map(lambda key: data[key][Category.error], data))
    wrong = list(map(lambda key: data[key][Category.wrong], data))

    fig, ax = plt.subplots(figsize=(13,5))
    bars_correct = ax.bar(x - 1 * width, correct, width, label='Correct', color=colors[0])
    bars_error = ax.bar(x, error, width, label='Error', color=colors[1])
    bars_wrong = ax.bar(x + 1 * width, wrong, width, label='Wrong', color=colors[2])

    y = ax.set_ylabel(
        'Number of Corresponding Results',
        rotation=0
    )
    ax.yaxis.set_label_coords(0.05, 1.06)

    ax.legend(
        frameon=False,
        bbox_to_anchor=(1.0, 1.01),
        loc='lower right'
        # bbox_to_anchor=(1.11, 0.6)
    )

    ax.tick_params(axis='x', pad=7)
    ax.set_xticks(x, labels, multialignment='center', linespacing=1.65)

    fig.tight_layout()
    plt.show()

    fig.savefig('out/categories.svg', format='svg')

def create_categories(data, configs):
    result = {}

    for config in configs:
        correct = 0
        wrong = 0
        error = 0

        runs = data[config]
        for run in runs:
            if run.category is Category.correct:
                correct = correct + 1
            elif run.category is Category.wrong:
                wrong = wrong + 1
            elif run.category is Category.error:
                error = error + 1
            else:
                assert False

        result[config] = {
            Category.correct: correct,
            Category.error: error,
            Category.wrong: wrong,
        }

    draw(result)


