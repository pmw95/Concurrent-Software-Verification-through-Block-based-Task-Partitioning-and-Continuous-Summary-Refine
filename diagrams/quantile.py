import matplotlib.pyplot as plt
import numpy as np
import Common

from Run import Category

def draw(data, colors, only_correct=True):
    entries = []
    legend = []

    max_count = 0
    for key in data:
        if only_correct:
            data[key] = list(filter(lambda run: run.category == Category.correct, data[key]))
        data[key].sort(key=lambda run: run.time)
        entries.append(list(map(lambda run: run.time, data[key])))
        max_count = max(max_count, len(data[key]))
        legend.append(Common.labels[key]['label'])

    for index in range(0, len(entries)):
        entry = entries[index]
        if len(entry) < max_count:
            entry.extend([-1000] * (max_count - len(entry)))

    plt.rc('text', usetex=True)
    plt.rcParams.update({'font.size': 11})
    plt.rcParams['xtick.major.pad'] = '5'

    x = np.arange(max_count)

    fig, ax = plt.subplots(figsize=(11,5))

    plt.yscale('log')
    ax.set_yscale('log')

    plt.grid(visible=True, which='both', alpha=0.3)

    index = 0
    for entry in entries:
        ax.scatter(x, entry, s=1, zorder=3, color=colors[index])
        index = index + 1

    plt.xlim(left=0)

    y = ax.set_ylabel(
        'CPU Time [s]',
        rotation=0
    )
    ax.yaxis.set_label_coords(0.01, 1.02)
    ax.set_xlabel('Run Index', labelpad=8)

    legend = ax.legend(
        legend,
        frameon=False,
        bbox_to_anchor=(1.0, 1.01),
        loc='lower right',
        handletextpad=-0.2
    )
    plt.setp(legend.get_texts(), va='center')
    for handle in legend.legendHandles:
        handle.set_sizes([20])
    for text in legend.get_texts():
        text.set_y(2.3)

    fig.tight_layout()
    plt.show()

    fig.savefig('out/quantile.svg', format='svg')

def create_quantile(data, configs, colors):
    result = {}

    for config in configs:
        runs = data[config].copy()
        runs.sort(key=lambda run: run.time)
        result[config] = runs

    draw(result, colors)


