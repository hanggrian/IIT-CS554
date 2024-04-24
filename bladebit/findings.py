"""
Generate SVG representation of SVG files.
"""

from matplotlib import pyplot
from pandas import read_csv
from seaborn import lineplot, barplot

NAME = 'Name'
PHASE = 'Phase'
MINUTES = 'Minutes'


def line_plot(ksize):
    """Export plot and clear canvas."""
    filename_without_extension = f'k{ksize}_time'
    ksize_time = read_csv(f'{filename_without_extension}.csv')

    axes = lineplot(ksize_time, x=PHASE, y=MINUTES, hue=NAME, palette='Set1')
    pyplot.title(f'k{ksize} plotting time', fontweight='bold')
    pyplot.xticks(range(1, 6))
    pyplot.grid(True)
    pyplot.legend()
    for phase, minutes in zip(ksize_time[PHASE], ksize_time[MINUTES]):
        axes.annotate(str(minutes), xy=(phase, minutes))
    pyplot.tight_layout()
    pyplot.savefig(f'{filename_without_extension}.svg')
    pyplot.clf()


line_plot('25')
line_plot('32')

average_by_ksize = read_csv('average_by_ksize.csv')

axes2 = barplot(average_by_ksize, x=PHASE, y=MINUTES, hue=NAME, palette='Set2')
pyplot.title('Average by k-size', fontweight='bold')
pyplot.legend()
for phase2, minutes2 in zip(average_by_ksize[PHASE], average_by_ksize[MINUTES]):
    axes2.annotate(str(minutes2), xy=(phase2 - 1, minutes2))
pyplot.tight_layout()
pyplot.savefig('average_by_ksize.svg')
