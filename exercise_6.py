# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


from time import sleep

def percents(money: float):  # Комиссия на снятие наличных
    percent = money * 1.5 / 100
    if percent < 30:
        percent = 30.0
    elif percent > 600:
        percent = 600.0
    else:
        percent = percent
    print(f"Комиссия = {percent}")
    return percent


def round_summ(summa: float) -> float:  # Округление суммы до 50
    if summa % 50 > 0:
        summa = round(summa / 50) * 50
        print(f"Сумма округленна до: {summa}")
    return summa


def withdraw(summa: float = 0):  # Операция снятия
    print("На снятие наличных вводится комиссия 1.5%\n"
          "Min: 30\nMax: 600")
    # sleep(1)
    print(f'Вам доступно: {summa}\n')
    # sleep(1)
    choose_a_sum = round_summ(float(input("Введите сумму снятия, кратную {50} или \n"
                                          "для отмены операции введите ноль {0}: ")))
    if choose_a_sum == 0:
        return summa
    if summa - (choose_a_sum + percents(choose_a_sum)) < 0:
        print("На вашем счете недостаточно средств")
    else:
        summa -= (choose_a_sum + percents(choose_a_sum))
    return summa


def enter(summa: int = 0):
    choose_a_sum = round_summ(float(input("Введите сумму пополнения, кратную {50} или \n"
                                          "{0} ноль для отмены операции: ")))
    if choose_a_sum == 0:
        return summa
    else:
        return summa + choose_a_sum


def choice_selection(summa: float = 0, count=[]):
    # print('cmd =', count)
    if len(count) >= 3:
        count.clear()
        bonus = round(0.03 * summa, 2)
        summa += bonus
        print(f"Вам начислен бонус в 3% = {bonus}!!!")
        print(f'\nДоступно средств: {summa}\n')
    cmd = (input('Выберите действие:\n'
                 '1 - Снять\n'
                 '2 - Пополнить\n'
                 '3 - Показать баланс\n'
                 '0 - Выйти\n'
                 ':'))
    commands = ['1', '2', '3', '0']
    if cmd not in commands:
        print(f"вы ввели не верную команду {cmd}!\n"
              f"Попробуйте снова.")
        return choice_selection(summa)
    while True:
        if int(cmd) == 1:
            summa = withdraw(summa)
            print(f'\nДоступно средств: {summa}\n')
            count.append(1)
            return choice_selection(summa, count)

        elif int(cmd) == 2:
            summa = enter(summa)
            print(f'\nДоступно средств: {summa}\n')
            count.append(2)
            return choice_selection(summa, count)

        elif int(cmd) == 3:
            print(f'\nДоступно средств: {summa}\n')
            return choice_selection(summa)

        elif int(cmd) == 0:
            print("Exit. Good bye!")
            return False

print("Банкомат 5000")
print()
choice_selection(5000)