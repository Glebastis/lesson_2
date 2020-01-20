#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# stroka = '00000'
# for i in range(5):
#     print(i, stroka)
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# summ = 0
# for i in range(10):
#     vvod = input('enter digit')
#     if vvod == '5':
#         summ += 1
# print(summ)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# sum = 1
#
# for i in range(1,11):
#     sum*=i
# print(sum)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 2129
# summa = 0
# while integer_number>0:
#     summa+=integer_number%10
#     integer_number = integer_number//10
# print(summa)

'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 2129
# summa = 1
# while integer_number>0:
#     summa*=integer_number%10
#     integer_number = integer_number//10
# print(summa)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# maxima = 0
# integer_number = 2129
# while integer_number>0:
#     if integer_number%10>maxima:
#         maxima = integer_number%10
#     integer_number = integer_number//10
# print(maxima)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# kolvo = 0
# integer_number = 2559
# while integer_number>0:
#     if integer_number%10==5:
#         kolvo+=1
#     integer_number = integer_number//10
# print(kolvo)