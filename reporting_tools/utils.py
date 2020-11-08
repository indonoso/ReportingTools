def fix_label(label, kind):
    if kind == 'table':
        if not label.startswith('tab'):
            return 'tab:' + label
    elif kind == 'figure':
        if not label.startswith('fig'):
            return 'fig:' + label
    return label
