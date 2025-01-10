"""
Creating a custom library to use for assignments, forking from datastat_module in Chapter 11
"""

import numpy as np
import matplotlib.pyplot as plt

def datastats(xdata, ydata, xname, yname, disp, title):
    '''
    Input:
    - xdata:    data for x-axis (exp days)
    - ydata:    data for y-axis (exp temperature values)
    - xname:    name for x-axis
    - yname:    name for y-axis

    Output:
    - statistic_val: array containing mean, variance, median, max and min
    '''

    num = ydata.shape[1]      # Number of colums (cities)
    statistic_val = np.zeros((5,num))

    # Compute statistics
    statistic_val[0, :] = np.mean(ydata, axis=0)
    statistic_val[1, :] = np.var(ydata, axis=0)
    statistic_val[2, :] = np.median(ydata, axis=0)
    statistic_val[3, :] = np.max(ydata, axis=0)
    statistic_val[4, :] = np.min(ydata, axis=0)

    # Handle display options
    if disp == 'NONE':
        pass
    elif disp == 'CW':
        disp_data(statistic_val, yname)
    elif disp == 'PLOT':
        disp_data(statistic_val, yname)
        plot_data(xdata, ydata, xname, yname, title)
    else:
        print('Display option not valid bro')
    return statistic_val


def disp_data(stat, yname):
    '''
    Display the statistics for each dataset
    '''
    num = stat.shape[1]  # Number of datasets (cities)
    overall = [
        np.mean(stat[0, :]),    # Average
        np.mean(stat[1, :]),    # Variance
        np.median(stat[2, :]),  # Median
        np.max(stat[3, :]),     # Max
        np.min(stat[4, :])     # Min
    ]
    print(f'{yname} data:')
    print('             Average  Variance      Median      Max     Min')

    for i in range(num):
        print(f'Dataset {i+1} : {stat[0, i]:10.2f}{stat[1, i]:10.2f}{stat[2, i]:10.2f}{stat[3, i]:10.2f}{stat[4, i]:10.2f}')
    
    print("Overall   :", end="")
    for val in overall:
        print(f"{val:10.2f}", end="")
    print()


def plot_data(x, y, xlabel, ylabel, title):
    '''
    Plot the x and y data with labels, legend, and title.
    The y-axis is adjusted to accomodate the legend.
    '''

    plt.plot(x, y[:, 0], 'forestgreen', label='City A')
    plt.plot(x, y[:, 1], 'dodgerblue', label='City B')
    plt.plot(x, y[:, 2], 'rebeccapurple', label='City C')

    # Adjust y-axis limit by adding an arbitrary increase to the max value
    plt.ylim([np.min(y) -2, np.max(y) + 10])        # Adds extra space above and below

    # Set labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
