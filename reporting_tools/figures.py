from altair_saver import save
from .utils import fix_label
import pathlib

def create_tex_file(label, caption, path_tex, path_figure_reporting, width, position):
    text = ("\\begin{{figure}}[{position}]\n\\centering\n\\includegraphics[{width}]{{{path}}}\n\\caption{{{caption}}}" +
            "\n\\label{{{label}}}\n\\end{{figure}}") \
        .format(position=position, width=width, path=path_figure_reporting,
                caption=caption, label=label)
    with open(path_tex, 'w+') as f:
        f.write(text)

def create_paths(name, path_tex, path_figure, path_figure_reporting):

    path_tex = pathlib.Path(path_tex) / (name + '.tex')
    path_fig_tex = pathlib.Path(path_figure_reporting) / (name + '.pdf')
    path_fig = pathlib.Path(path_figure) / (name + '.pdf')

    return path_tex, path_fig_tex, path_fig


def create_tex(label, caption, path_tex, path_figure, path_figure_reporting='figures/charts', width='width=0.8\\textwidth', position='h'):
    label = fix_label(label, 'figure')
    path_tex, path_fig_tex, path_figure = create_paths(label.split(':')[-1], path_tex, path_figure, path_figure_reporting)
    create_tex_file(label, caption, path_tex, path_figure_reporting, width, position)

    return path_figure.as_posix()

def alt_to_latex(chart, label, caption, path_tex, path_figure, path_figure_reporting='figures/charts', width='width=0.8\\textwidth', position='h'):
    path_figure = create_tex(label, caption, path_tex, path_figure, path_figure_reporting, width, position)

    save(chart, path_figure)
    return chart


def sns_to_latex(chart, label, caption, path_tex, path_figure, path_figure_reporting='figures/charts', width='width=0.8\\textwidth', position='h'):
    path_figure = create_tex(label, caption, path_tex, path_figure, path_figure_reporting, width, position)
    chart.savefig(path_figure, bbox_inches='tight')
    return chart