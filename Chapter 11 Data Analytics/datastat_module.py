
import numpy as np
import matplotlib.pyplot as plt

def datastat(xdata, ydata, xname, yname, dispOption):
    """
    Input:
    - xdata: data for x-axis (e.g., days)
    - ydata: data for y-axis (e.g., temperature values for cities)
    - xname: name for x-axis data (e.g., 'Days')
    - yname: name for y-axis data (e.g., 'Temperature')
    - dispOption: display option ('NONE', 'CW', 'PLOT')
    
    Output:
    - statisticVal: array containing mean, variance, median, max, and min
    """

    N = ydata.shape[1]  # Number of columns (cities)
    statisticVal = np.zeros((5, N))

    # Compute statistics
    statisticVal[0, :] = np.mean(ydata, axis=0)
    statisticVal[1, :] = np.var(ydata, axis=0)
    statisticVal[2, :] = np.median(ydata, axis=0)
    statisticVal[3, :] = np.max(ydata, axis=0)
    statisticVal[4, :] = np.min(ydata, axis=0)

    # Handle display options
    if dispOption == 'NONE':
        pass
    elif dispOption == 'CW':
        dispdata(statisticVal, yname)
    elif dispOption == 'PLOT':
        dispdata(statisticVal, yname)
        plotdata(xdata, ydata, xname, yname)
    else:
        print("DISPLAY OPTION IS NOT VALID")

    return statisticVal

def dispdata(stat, yname):
    """
    Display the statistical data for each dataset.
    """
    N = stat.shape[1]  # Number of datasets (cities)
    overall = [
        np.mean(stat[0, :]),  # Average
        np.mean(stat[1, :]),  # Variance
        np.median(stat[2, :]),  # Median
        np.max(stat[3, :]),  # Max
        np.min(stat[4, :])   # Min
    ]

    print(f"{yname} data:-")
    print('              Average  Variance    Median       Max       Min')

    for i in range(N):
        print(f"Dataset {i+1} :{stat[0, i]:10.2f}{stat[1, i]:10.2f}{stat[2, i]:10.2f}{stat[3, i]:10.2f}{stat[4, i]:10.2f}")

    print("Overall   :", end="")
    for val in overall:
        print(f"{val:10.2f}", end="")
    print()

def plotdata(x, y, xlabel, ylabel):
    """
    Plot the x and y data with labels, legend, and title. The y-axis is adjusted to accommodate the legend.
    """
    plt.plot(x, y[:, 0], '-o', label='City A')
    plt.plot(x, y[:, 1], '-o', label='City B')
    plt.plot(x, y[:, 2], '-o', label='City C')

    # Adjust y-axis limit by adding an arbitrary increase to the max value
    plt.ylim([np.min(y) - 2, np.max(y) + 10])  # Adds extra space above and below

    # Set labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Temperature Reading over a Month for 3 Cities')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()
