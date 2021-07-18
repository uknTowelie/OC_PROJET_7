import csv
from math import sqrt
from action import Action



def getTrend2d(list_point):
    n = len(list_point)
    x_average = 0
    y_average = 0
    for x, y in enumerate(list_point):
        x_average += x + 1
        y_average += y
    x_average /= n
    y_average /= n 

    sigma_x_y = 0
    for x, y in enumerate(list_point):
        sigma_x_y += (x+1) * y - x_average * y_average
    sigma_x_y /= n 

    sigma_x = 0
    for x, y in enumerate(list_point):
        sigma_x += (x + 1)**2 - x_average**2
    sigma_x /= n
    sigma_x = sqrt(sigma_x)

    sigma_y = 0
    for x, y in enumerate(list_point):
        sigma_y += y**2 - y_average**2
    sigma_y /= n
    sigma_y = sqrt(sigma_y)

    r = sigma_x_y / (sigma_x * sigma_y)
    print('r = ' + str(r))
    print("r > 0,75 ==> Coorélation linéaire")
    print("equation courbe de tendance : y = ax + b")
    

    beta = sigma_x_y / (sigma_x**2)
    alpha = y_average - ((sigma_x_y / (sigma_x**2)) * x_average)
    res = []
    print("alpha = " + str(round(alpha,4)) +"\nbeta = " + str(round(beta,4)))
    
    for index in range(0,n):
        res.append(alpha * (index) + beta)
    return res


def trend_curve(tab_time):
    last_time = 0
    coeff = 0
    list_coeff = []
    for index,time in enumerate(tab_time):
        if index != 0 and time > 0.1:
            list_coeff.append(time / last_time)
            last_time = time
        else:
            last_time = time
    r = 0
    for x in list_coeff:
        r += x
    r /= len(list_coeff)

    print("\n Un+1 / Un = " + str(round(r,2)))
    