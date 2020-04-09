import matplotlib.pyplot as plt
plt.style.use('ggplot')
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = 'Ubuntu'

def chart(dic_list, kind='plot', name='title', x_name='month', y_name='values', legend=None):
    x = list(dic_list[0].keys())
    fig, ax = plt.subplots(figsize=(16,8))
    if kind == 'plot':
        for dic in dic_list:
            y = list(dic.values())
            ax.plot(x, y)  
    elif kind == 'bar':
        ax = fig.add_axes([0,0,1,1])
        y = list(dic_list[0].values())
        y1 = [v[0] for v in y]
        y2 = [v[1] for v in y]
        ax.bar(x, y1, color='darkgreen')
        ax.bar(x, y2, bottom=y1, color='lightgreen', alpha=.7)
    #elif kind
    if legend:
        ax.legend(legend, fontsize=30)
    ax.set_title(name, size=25)
    ax.set_xlabel(x_name, size=20)
    ax.set_ylabel(y_name, size=20)
    fig.autofmt_xdate() 
    fig.tight_layout()
        #print (y1)

    

def plot_bar(dic, name='title', x_name='month', y_name='values'):
    x = arr_list[0]
    #y = 
    return

