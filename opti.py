from action import Action, initAction
import matplotlib.pyplot as plt
import time
import random
from math import floor, ceil
import csv
from trend_curve import getTrend2d, trend_curve

def main():
    print("Dataset 1 - Algorithme Sac a dos")
    list_action = getDataExcel("dataset1.csv")
    res = []
    profit = sacADos2(list_action,500, res)
    print("Resultat dataSet 1 : \n  Profit = " + str(profit))
    r = 0
    best_set = []
    for action in res:
        r += action.price
        best_set.append(action.id)
    print("  Cout total des action = " + str(r))
    print("Liste des actions de la combinaison : ")
    print(best_set)
    print("\n\nDataset 2 - Algorithme Sac a dos")
    list_action = getDataExcel("dataset2.csv")
    res = []
    t1 = time.time()
    profit = sacADos2(list_action,500, res)
    t2 = time.time()
    print("Temps execution = " + str(t2 - t1))
    print("Resultat dataSet 2 : \n  Profit = " + str(profit))
    r = 0
    best_set = []
    for action in res:
        r += action.price
        best_set.append(action.id)
    print("  Cout total des action = " + str(r))
    print("Liste des actions de la combinaison : ")
    print(best_set)
    print("\n\nAnalyse temporelle sur 500 action")
    fig, ax = plt.subplots()
    res = SacAdowInRange(200)
    ax.plot([x for x in range(len(res))], getTrend2d(res), color="red")
    ax.plot([x for x in range(len(res))], res, ".")
    plt.show()

def SacADow(tab_action, max_price):
    res = [0] * (max_price + 1)
    list_comb = []
    for action in tab_action:
        for index in range(max_price, round(action.price) - 1, -1):
            res[index] = max(res[index], res[round(index-action.price)] + action.profit() - action.price)

    return res[max_price]

def sacADos2(tab_action, max_price, final_comb):
    matrice = [[0 for x in range(max_price + 1)] for x in range(len(tab_action) + 1)]
    for index_ligne in range(1, len(tab_action) + 1):
        for index_col in range(1, max_price + 1):
            if tab_action[index_ligne - 1].price <= index_col and tab_action[index_ligne - 1].price != 0:
                matrice[index_ligne][index_col] = max(tab_action[index_ligne - 1].profit() + 
                                                      matrice[index_ligne - 1][index_col - round(tab_action[index_ligne-1].price)] - 
                                                      tab_action[index_ligne - 1].price,
                                                      matrice[index_ligne-1][index_col])
            else:
                matrice[index_ligne][index_col] = matrice[index_ligne - 1][index_col]
    index_price = max_price
    index = len(tab_action)
    for index_l in range(len(tab_action)):
        chaine = "| "
        for index_c in range(max_price):
            chaine += str(matrice[index_l][index_c]) +  " | "
        print( chaine + "\n")
    r = 0
    while index_price >= 0 and index >= 0:
        action = tab_action[index - 1]
        if floor(matrice[index][floor(index_price)]) - floor((matrice[index - 1][floor(index_price) == floor(action.price)]) + 
                 action.profit()) and action.price != 0 and r + action.price <= 500:
            final_comb.append(action)
            r += action.price
            index_price -= action.price
        index -= 1
    return matrice[-1][-1]

def SacAdowInRange(n):
    list_action = []
    res = []
    for index in range(n):
        list_action.append(Action(index,random.randint(5, 120), random.randint(1, 21)))
        t1 = time.time()
        SacADow(list_action.copy(), 500)
        t2 = time.time()
        res.append(t2-t1)
    return res

def getDataExcel(file_name):
    list_action = []
    with open(file_name,"r") as csvfile:
        sheet = csv.reader(csvfile)
        for index, row in enumerate(sheet):
            if index != 0:
                list_action.append(Action(row[0],float(row[1]), float(row[2])))
    return list_action

if __name__ == "__main__":
    main()