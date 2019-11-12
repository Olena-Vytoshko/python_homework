"""
Обчислення функції в залежності від значення введеної змінної.
"""

import re
def returning_float(text):
    return bool(re.match(r'^[+-]?(\d*[.])?\d+$', text))

def validator_float(prompt):
    abc=input(prompt)
    while not returning_float(abc):
        abc = input(prompt)
    return float(abc)

print("Введіть аргумент")
x = validator_float('x = ')
if x<=7:
    y=-3*x+9
if x>7:
    y=1/(x-7)
print("Результат:", y)