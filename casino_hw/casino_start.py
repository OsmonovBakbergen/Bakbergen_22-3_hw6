from functional_casino import stavka

balance = 1000
while True:
    command = input(f'Введите команду')
    if command == 'exit':
        break
    elif balance == 0:
        print("Вы обнокротились")
        break
    else:
        amount = int(input(f'Введите сумму ставки'))
        if amount > balance or amount <= 0:
            print(f'Вы ввели неправильную ставку')
            continue
        lot = int(input(f'Введите лот'))
        if lot > 30 or lot <= 0:
            print(f'Вы ввели неправильный лот')
        win_amount = stavka(amount, lot)
        balance += win_amount