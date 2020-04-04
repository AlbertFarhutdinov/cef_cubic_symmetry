import matplotlib.pyplot as plt
from cef_object_scripts import common

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.linewidth'] = 2


def get_plot(x_data=None, y_data_set=None, x_label='x_label', y_label='y_label', y_legend_set=None, color_set=None,
             x_min=None, x_max=None, y_min=None, y_max=None, size=(10, 10), graph_title=None, graph_name='graph',
             mode='show', tick_label_size=14, tick_major_length=6, tick_minor_length=3, axis_label_size=14,
             axis_label_pad=0, legend_font_size=14, left=0.19, bottom=0.11, right=0.98, top=0.90,
             x_major_locator=None, x_minor_locator=None, y_major_locator=None, y_minor_locator=None,
             text_x=0, text_y=0, text_string='Test text'):
    size_inches = tuple(i / 2.54 for i in size)
    x_min = min(x_data) if x_min is None else x_min
    x_max = max(x_data) if x_max is None else x_max
    y_min = min([min(value) for value in y_data_set.values()]) if y_min is None else y_min
    y_max = max([max(value) for value in y_data_set.values()]) if y_max is None else y_max
    dpi = 100 if mode == 'show' else 500
    fig, ax = plt.subplots(figsize=size_inches, dpi=dpi)
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=None, hspace=None)
    ax.set_title(graph_title)
    ax.set_xlabel(x_label, labelpad=axis_label_pad, fontsize=axis_label_size)
    ax.set_ylabel(y_label, labelpad=axis_label_pad, fontsize=axis_label_size)
    x_major_locator = (x_max - x_min) // 5 if x_major_locator is None else x_major_locator
    x_minor_locator = x_major_locator / 5 if x_minor_locator is None else x_minor_locator
    y_major_locator = (y_max - y_min) // 5 if y_major_locator is None else y_major_locator
    y_minor_locator = y_major_locator / 5 if y_minor_locator is None else y_minor_locator
    ax.xaxis.set_major_locator(plt.MultipleLocator(x_major_locator))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(x_minor_locator))
    ax.yaxis.set_major_locator(plt.MultipleLocator(y_major_locator))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(y_minor_locator))
    ax.set_xlim(xmin=x_min, xmax=x_max)
    ax.set_ylim(ymin=-y_minor_locator, ymax=y_max)
    ax.tick_params(which='both', direction='in', width=2, top=True, right=True, labelsize=tick_label_size)
    ax.tick_params(which='major', length=tick_major_length)
    ax.tick_params(which='minor', length=tick_minor_length)
    for key, y_data in y_data_set.items():
        ax.plot(x_data, y_data, color=color_set[key], label=y_legend_set[key], linewidth=2)
    ax.legend(fontsize=legend_font_size, frameon=False)
    plt.text(text_x, text_y, text_string, size=14)
    if mode == 'show':
        plt.show()
    elif mode == 'eps':
        fig.savefig(f'{graph_name}.eps')
    elif mode == 'png':
        fig.savefig(f'{graph_name}.png')
    else:
        print(f'Mode {mode} is not supported.')
    plt.close('all')


def get_energy_transfer_plot(crystal, rare_earth, w, x, temperature_1, temperature_2,
                             x_data, y_data_set, y_legend_set, color_set, mode,
                             x_min=None, x_max=None, y_min=None, y_max=None,
                             x_major_locator=None, x_minor_locator=None, y_major_locator=None, y_minor_locator=None,
                             text_x=0, text_y=0):
    file_name = common.get_paths(common.path_to_graphs, 'graph', mode,
                                 crystal, rare_earth, w, x, f'{temperature_1}-{temperature_2}')
    common.check_path(file_name)
    get_plot(x_data=x_data, y_data_set=y_data_set, x_label='Energy Transfer, meV',
             y_label=r'$S(\omega)$, arb.u.', color_set=color_set, y_legend_set=y_legend_set, mode=mode,
             x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, graph_name=file_name.rstrip(f'.{mode}'),
             text_x=text_x, text_y=text_y, text_string=fr'$W={w: .3f}$' + '\n' + fr'$x = {x: .3f}$',
             x_major_locator=x_major_locator, x_minor_locator=x_minor_locator, y_major_locator=y_major_locator,
             y_minor_locator=y_minor_locator)


if __name__ == '__main__':
    maximum = 11
    x_array = [i for i in range(maximum)]
    y_array = {
        '4': [i ** 4 for i in range(maximum)],
        '3': [i ** 3 for i in range(maximum)],
        '2': [i ** 2 for i in range(maximum)],
        '1': [i ** 1 for i in range(maximum)],
    }
    colors = {
        '4': 'black',
        '3': 'red',
        '2': 'green',
        '1': 'blue',
    }
    legend = {
        '4': '$x^4$',
        '3': '$x^3$',
        '2': '$x^2$',
        '1': '$x^1$',
    }
    get_plot(x_data=x_array, y_data_set=y_array, x_label='Energy Transfer, meV', y_label=r'$S(\omega)$, arb.u.',
             color_set=colors, y_legend_set=legend, mode='show')
