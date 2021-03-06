# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544'
# введена строка
# 2,3,5,4,4        #вивело в консолі.
#
# numbers = []
# for i in st:
#     if i.isdigit():
#         numbers.append(int(i))
#
# print(numbers)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#st = 'as 23 fdfdg544 34'  # введена строка
#   23, 544, 34              #вивело в консолі

# numbers = []
# n = ''
# for i in st:
#     if i.isdigit():
#         n = n + i
#     else:
#         if n != '':
#             numbers.append(int(n))
#             n = ''
# if n != '':
#         numbers.append(int(n))
#
# print(numbers)

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting_new = [i.upper() for i in greeting]
# print(greeting_new)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# squares = [i ** 2 for i in range(50) if i % 2 != 0]
# print(squares)

# function
#
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - створити функцію яка виводить ліст

def show_list():
    print(list)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def three_min(a, b, c):
    print(a, b, c)
    return (min(a, b, c))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def three_max(a, b, c):
    print(a, b, c)
    return (max(a, b, c))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def func4(*args):
    print(max(args))
    return (min(args))

# - створити функцію яка повертає найбільше число з ліста

def list_max(list):
    return (max(list))

# - створити функцію яка повертає найменьше число з ліста

def list_min(list):
    return (min(list))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_list(list):
    summa = 0
    for i in list:
        summa += i
    return (summa)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
def average(list):
    ave = 0
    for i in list:
        ave += i
    return (ave/len(list))
#
#
#
#
#
# #################################################################################################
# 1)Дан лист:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - найти min число в листе

# print(min(list))

#   - удалить все дубликаты в листе

# list_new = set(list)
# print(list_new)

#   - заменить каждое четвертое значение на "Х"

# list_new1 = []
# for i in list:
#     if list.index(i) % 4 == 0:
#         list_new1.append('X')
#     else:
#         list_new1.append(i)
#
# print(list_new1)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# number = 10
# space = number - 4
# print('*' * number)
# for i in range(number):
#     print('*', ' ' * space, '*')
# print('*' * number)

# 3) вывести табличку умножения с помощью цикла while

# i = 0
# while i < 10:
#     i += 1
#     j = 0
#     while j < 10:
#         j += 1
#         c = i * j
#         print(c, end = ' ')
#     print()

# 4) переделать первое задание под меню с помощью цикла

while True:
    print('1) найти min число в листе')
    print('2) удалить все дубликаты в листе')
    print("3) заменить каждое четвертое значение на 'Х'")
    print('4) выход')

    choice = input('Сделайте свой выбор: ')
    print(list)

    if choice == '1':
        print(min(list))
    elif choice == '2':
        list_new = set(list)
        print(list_new)
    elif choice == '3':
        list_new1 = []
        for i in list:
            if list.index(i) % 4 == 0:
                list_new1.append('X')
            else:
                list_new1.append(i)

        print(list_new1)
    elif choice == '4':
        break



# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# l = [-1, -2, 3, 4, 555]
#
# l_new = sorted(l)
# for i in l_new:
#     print(l_new[len(l_new)//2])
