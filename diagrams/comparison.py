import matplotlib.pyplot as plt
import Common
import matplotlib.ticker as ticker

from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import NullFormatter
from Run import Category

def next_power_of_10(value):
    power = 0
    divisor = pow(10, power)

    while value / divisor > 1:
        power = power + 1
        divisor = pow(10, power)

    return divisor


def draw(data, configs, only_correct=True):
    x = []
    y = []
    legend = [Common.labels[configs[0]], Common.labels[configs[1]]]

    for index in range(0, len(data[configs[0]])):
        first = data[configs[0]][index]
        second = data[configs[1]][index]

        assert first.name == second.name

        if only_correct:
            if first.category == Category.wrong or second.category != Category.wrong:
                continue

        x.append(first.time)
        y.append(second.time)

    plt.rc('text', usetex=True)
    plt.rcParams.update({'font.size': 11})
    plt.rcParams['xtick.major.pad'] = '5'

    fig, ax = plt.subplots(figsize=(5,5))

    # plt.yscale('log')
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.scatter(x, y, s=2, color=Common.colors[1])

    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
    ax.yaxis.set_minor_formatter(NullFormatter())

    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
    ax.xaxis.set_minor_formatter(NullFormatter())

    ax.set_xlim(min(x), next_power_of_10(max(x)))
    ax.set_ylim(min(y), next_power_of_10(max(y)))

    ax.plot([0, 1], [0, 1], '--', alpha=0.5, transform=ax.transAxes, color='black', lw=1)

    y = ax.set_ylabel(
        'CPU Time [s] for ' + Common.labels[configs[0]]['label'],
        rotation=0,
        loc='bottom'
    )
    ax.yaxis.set_label_coords(-0.1, 1.03)
    ax.set_xlabel('CPU Time [s] for ' + Common.labels[configs[1]]['label'], labelpad=5)

    # legend = ax.legend(
    #    legend,
    #    frameon=False,
    #    bbox_to_anchor=(1.0, 1.01),
    #    loc='lower right',
    #    handletextpad=-0.2
    # )
    # plt.setp(legend.get_texts(), va='center')
    # for handle in legend.legendHandles:
    #     handle.set_sizes([20])
    # for text in legend.get_texts():
    #     text.set_y(2)

    fig.tight_layout()
    plt.show()

    fig.savefig('out/comparison.svg', format='svg')

def create_comparison(data, configs):
    result = {}

    for config in configs:
        runs = data[config].copy()
        runs.sort(key=lambda run: run.name)
        result[config] = runs

    draw(result, configs)


