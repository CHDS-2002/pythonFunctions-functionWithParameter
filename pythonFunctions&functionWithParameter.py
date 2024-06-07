# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')


# get_matrix - функция, создающая матрицу
def get_matrix(n, m, value):
    # Создание матрицы
    matrix = [[value for _ in range(m)]
              for _ in range(n)]
    return matrix


# Создадим матрицы
result1 = get_matrix(2, 2, 10)
# result1 - первая матрица
result2 = get_matrix(3, 5, 42)
# result2 - вторая матрица
result3 = get_matrix(4, 2, 13)
# result3 - третья матрица

# ВЫВОД МАТРИЦ
print('\nМАТРИЦЫ\n')
print('Первая матрица:')
print(result1, end='\n\n')
print('Вторая матрица:')
print(result2, end='\n\n')
print('Третья матрица:')
print(result3, end='\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
