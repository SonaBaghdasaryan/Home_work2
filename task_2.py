# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

def calc_fraction_operations(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    fraction_obj1 = Fraction(numerator1, denominator1)
    fraction_obj2 = Fraction(numerator2, denominator2)

    sum_fraction = fraction_obj1 + fraction_obj2
    product_fraction = fraction_obj1 * fraction_obj2

    return sum_fraction, product_fraction


fraction1 = input("Введите первую дробь (формат a/b): ")
fraction2 = input("Введите вторую дробь (формат a/b): ")

sum_result, product_result = calc_fraction_operations(fraction1, fraction2)
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)