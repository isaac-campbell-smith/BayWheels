import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
def chart(s_list, kind='plot', name='title', x_name='', y_name='', n=1, b=None, legend=None, line=None, fmt=True):
    fig, ax = plt.subplots(figsize=(16,8))

    if kind == 'scatter':
        ax.scatter(s_list[0], s_list[1], alpha=0.09)
        ax.set_xlim([0, 1300])
        ax.set_ylim([0, 6])

    if type(s_list[0].index[0]) == tuple:
        x = [' '.join(char) for char in s_list[0].index]
    else:
        x = s_list[0].index
    
    for s in s_list:
        y = s.values
        if kind == 'plot':
            ax.plot(x, y, color='mediumpurple') 
        elif kind == 'bar':
            ax.bar(x, y, color='teal') 
        elif kind == 'hist':
            ax.hist(y, bins=b[0], color='lightseagreen')
            ax.set_xlim([b[1], b[2]])
    if line:
        for n in line:
            ax.axvline(n, color='black', linestyle='--')
    if legend:
        ax.legend(legend, fontsize=20)
    ax.set_title(name, size=22)
    ax.set_xlabel(x_name, size=20, labelpad=10)
    ax.set_ylabel(y_name, size=20, labelpad=20)
    if fmt:
        fig.autofmt_xdate() 
    fig.tight_layout()
