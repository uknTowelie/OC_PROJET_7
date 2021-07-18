from action import Action, initAction
import time
import random
import matplotlib.pyplot as plt
from trend_curve import getTrend2d, trend_curve

def main():
    basic_20_action()      #Execution de l'algorithme pour set de 20 action
    #timeAnalyse()      #Etudes temporelle de l'algorithme

def timeAnalyse():
    n = 23
    time_list = getTimeInRange(n)
    fig, ax = plt.subplots()
    ax.plot([x for x in range(1,n)], time_list)
    trend_curve(time_list)
    plt.show()
    
def basic_20_action():
    list_action = []
    list_action = initAction()
    all_combination = []
    t = time.time()
    for index in range(1,20):
        for comb in combination(list_action, index):
            all_combination.append(comb)
    tab_comb_viable = getViable(all_combination)
    comb_finale = []
    print("Maximum profit : " + str(getBestSet(tab_comb_viable, comb_finale)))
    t2 = time.time()
    print("Execution time : " + str(round(t2-t, 2)))

def getTimeInRange(n):
    res = []
    list_action = []
    for index in range(1, n):
        all_comb_list = []
        comb_final = []
        list_action.append(Action(index,random.randint(5, 120),random.randint(1, 21)))
        t1 = time.time()
        for index_comb in range(1, index):
            for comb in combination(list_action, index_comb):
                all_comb_list.append(comb)
        viable_comb = getViable(all_comb_list)
        getBestSet(viable_comb, comb_final)
        t2 = time.time()
        res.append(t2-t1)
        print("Iteration : " + str(index + 1) + "\n Execution time :" + str(round(t2-t1, 2)))
    return res

def getViable(list_combination):
    res = []
    for combination in list_combination:
        tab_temp = []
        summ = 0
        profit = 0
        cond = True
        for action in combination:
            if summ + action.price <= 500:
                summ += action.price
            else:
                cond = False
                break
        if cond:
            res.append(combination)
    return res

def getBestSet(viable_comb_list, comb_finale):
    max_profit = None
    for comb in viable_comb_list:
        summ = 0
        profit = 0
        for action in comb:
            summ += action.price
            profit += action.profit()
        if max_profit == None or profit - summ > max_profit:
            max_profit = profit - summ
            comb_finale.clear()
            comb_finale += comb
    return max_profit
    

def combination(tab, size):
    if size==0:
        yield []
    else:
        for index in range( len(tab) - size + 1 ):
            for res_temp in combination( tab[index+1:], size - 1):
                yield [tab[index]] + res_temp

if __name__ == "__main__":
    main()