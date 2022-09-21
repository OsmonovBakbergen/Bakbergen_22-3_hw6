import random


def stavka(amount, lot):
    win_lot = random.randint(1, 30)
    if win_lot == lot:
        print('вы выиграли')
        return amount*2
    else:
        print('Вы проиграли')
        return -amount