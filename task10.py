# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

n=int(input("Введи сколько всего  монеток на столе:"))
a=int(input("Введи сколько  монеток лежат решкой вверх:"))
b=n-a
print("Монеток лежат гербом вверх:",b)   
if(a>b):
   print(b)
else:
   print(a)

