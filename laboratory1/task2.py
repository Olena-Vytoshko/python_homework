"""
import re
def returning_float(text):
    return bool(re.match(r'^[+-]?(\d*[.])?\d+$', text))
"""
import re
def returning_float(text):
    return bool(re.match(r'^[+-]?(\d*[.])?\d+$', text))

def validator_float(prompt):
    abc=input(prompt)
    while not returning_float(abc):
        abc = input(prompt)
    return float(abc)

print("Введіть координати точки (В першому рядку - х, в наступному - у)")
x = validator_float('координата x = ')
y = validator_float('координата y = ')
if x>0 and y>0:
   print("Точка знаходиться в першій чверті")
if x<0 and y>0:
   print("Точка знаходиться в другій чверті")
if x<0 and y<0:
   print("Точка знаходиться в третій чверті")
if x>0 and y<0:
   print("Точка знаходиться в четвертій чверті")
if x==0 and y==0:
   print("Точка знаходиться на перетині ОХ і OY")
if x==0 and y!=0:
   print("Точка лежить на OY")
if x!=0 and y==0:
   print("Точка лежить на OX")
