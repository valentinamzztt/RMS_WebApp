# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import signal
import numpy as np
from numpy import polyval
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import pandas as pd

def cooling():


    path = r"C:\Users\valen\Desktop\Sustaingineering"
    filename = r"\long_cooling.csv"
    filename = path + filename
    fname = filename
    data = np.loadtxt(fname, delimiter=',', comments='#', usecols=(0, 1, 2, 3))

    # access the data columns and assign variables x,y  and  uncetainty in y y_sigma
    x = data[:, 0]
    y = data[:, 2]
    y_sigma = data[:, 3]

    ###############################################################################
    # FIRST STEP: Solve the IVP from Newton's Law of Cooling: dT/dt = -K(T_obj-T_out),T(0)=356.25K
    ###############################################################################
    xtheory = list(range(0, int(x[-1]) + 5, 50))
    # Define initial conditions of the system
    T_out = 297.15
    dt = 0.0021  # (in s) in Arduino: delay(50000ms)
    period = math.floor(x[-1])  # seconds
    t_cup_pred = range(period)  # minutes
    T_cup_pred = [y[0]]  # Celsius
    print(y[0])
    K = 0.020416

    # Implement iterative solution
    for t in range(1, xtheory[-1]):
        dT = -K * (T_cup_pred[t - 1] - T_out) * dt  # Change in temperature of object
        T_cup_pred_update = T_cup_pred[t - 1] + dT  # New temperature for current time step
        T_cup_pred.append(T_cup_pred_update)

    T_cup_obs = y
    t_cup_obs = x

    plt.figure(figsize=(8, 5))
    plt.plot(t_cup_pred, T_cup_pred, '--r', label="predicted by NL")
    plt.plot(t_cup_obs, T_cup_obs, 'ok', label="actual")
    plt.xlabel('Time (s)', size=16)
    plt.ylabel('Temperature (K)', size=16)
    plt.title("Fitting of the Cooling process using Newton's Law of Cooling")
    plt.legend(loc='best', numpoints=1)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cooling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
