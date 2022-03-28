#int целое число
#number = 5

#float дробь
#fnumber = 5.7

#str строка
#name = "Sid"
#age = 34

#bool true or false
#Status=True

#вывод комментарий

#Экранирование
#print ("Он \"плохой\" человек!")

#либо чередовать "" и ''
#print ('Он "плохой" человек!')

#перевод строки
#print ('Привет\nмир')

#Конкатенация
#print ('Привет, меня зовут '+ name)
#print ("Мне " + str(age) + " года!")

#Input (Оператор Str() не нужен, т.к. Input всё выводит в Str)
#name = input ("Введите своё имя: ")
#age = input ("Укажите свой возраст: ")

#print ('Привет, '+ name + "!")
#print ("Тебе уже " + age + " года!")

# +, -, *, /, **, %, 
#a=5
#b=10
#c=a**2
#print (c)

#унарный минус
#a=10

#a=-a
#print (a)

#округление обычное
#a=5.65

#print (round (a))

#округление вниз
#import math
#a=5.65

#print (math.floor (a))

#округление вверх
#import math
#a=5.25

#print (math.ceil (a))

# Пи

#import math

#print (math.pi)

#Калькулятор 
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print(Back.CYAN)

what = input("Что делаем? (+, -): ")

print(Back.MAGENTA)

a=float(input ("Введи первое число: "))
b=float(input ("Введи второе число: "))

print(Back.YELLOW)

if what == "+":
	c=a+b
	print("Результат: " + str (c))	
elif what == "-":
	c=a-b
	print("Результат: " + str (c))
else:
	print("Выбрана неверная операция!")

input()