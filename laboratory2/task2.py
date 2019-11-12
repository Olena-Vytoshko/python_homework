"""
5) Необхідно підсумувати всі непарні цілі числа в діапазоні, який введе користувач з клавіатури.
"""

import re
def returning_int(text):
    return bool(re.match(r'^\d+$', text))

def validator_int(prompt):
    abc=input(prompt)
    while not returning_int(abc):
        abc = input(prompt)
    return int(abc)


result = 0
lower_limit_of_range=validator_int("Введіть нижню межу діапазону (ціле число):")
upper_limit_of_range=validator_int("Введіть верхню межу діапазону (ціле число):")
while lower_limit_of_range <= upper_limit_of_range:
    if lower_limit_of_range % 2 == 1:
        result += lower_limit_of_range
    lower_limit_of_range+=1
print(result)
