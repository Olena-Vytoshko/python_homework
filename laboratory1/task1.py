"""
Користувач уводить ціни 1 кг цукерок і 1 кг печива. Знайти вартість:
а) однієї покупки з 300 г цукерок і 400 г печива;
б) трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок.
"""
import re
def returning_float(text):
    return bool(re.match(r'^(\d*[.])?\d+$', text))

def validator_float(prompt):
    abc=input(prompt)
    while not returning_float(abc):
        abc = input(prompt)
    return float(abc)


cost1=validator_float("Введіть вартість 1кг цукерок:")
cost2=validator_float("Введіть вартість 1кг печива:")
The_purchase_price1=cost1*0.3+cost2*0.4
The_purchase_price2=3*(cost2*2+cost1*1.8)
print("Вартість першої покупки:",The_purchase_price1)
print("Вартість другої покупки:",The_purchase_price2)