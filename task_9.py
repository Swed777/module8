print('Задача 9. Выражение')
print('---------------------------------')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

numberl = 1
denominator = 1

x = int(input('Введите число х: '))

for i in range(1, 6):
  numberl *= x - (2 ** i - 1)
  denominator *= x - 2 ** i

print('Результат вычислений = ', numberl / denominator)

print('=============+++++++==============')