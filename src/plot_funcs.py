import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_chart(dic_list, name='title', x_name='month', y_name='values'):
    x = list(dic.keys())
    y = list(dic.values())
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(x, y)
    ax.set_title(name, size=25)
    ax.set_xlabel(x_name, size=20)
    ax.set_ylabel(y_name, size=20)
    fig.autofmt_xdate()
    fig.tight_layout()