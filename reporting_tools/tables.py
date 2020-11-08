from .utils import fix_label
import pathlib


def to_latex(df, label, caption, path, **kwargs):
    df.to_latex(buf=pathlib.Path(path) / (label.split(':')[-1] + '.tex'),
                label=fix_label(label, 'table'), caption=caption, escape=False, **kwargs)

    return df
