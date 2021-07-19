class Action:
    def __init__(self, i_id, i_price, i_benefit):
        self.id = i_id
        self.price = i_price
        self.benefit = i_benefit
    
    def profit(self):
        return self.price * (1 + self.benefit / 100)


def initAction():
    list_action = []
    list_action.append(Action(1, 20, 5))
    list_action.append(Action(2, 30, 10))
    list_action.append(Action(3, 50, 15))
    list_action.append(Action(4, 70, 20))
    list_action.append(Action(5, 60, 17))
    list_action.append(Action(6, 80, 25))
    list_action.append(Action(7, 22, 7))
    list_action.append(Action(8, 26, 11))
    list_action.append(Action(9, 48, 13))
    list_action.append(Action(10, 34, 27))
    list_action.append(Action(11, 42, 17))
    list_action.append(Action(12, 110, 9))
    list_action.append(Action(13, 38, 23))
    list_action.append(Action(14, 14, 1))
    list_action.append(Action(15, 18, 3))
    list_action.append(Action(16, 8, 8))
    list_action.append(Action(17, 4, 12))
    list_action.append(Action(18, 10, 14))
    list_action.append(Action(19, 22, 21))
    list_action.append(Action(20, 114, 18))
    return list_action