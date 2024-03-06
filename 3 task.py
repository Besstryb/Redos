#Создание двух переменных типа bool.
bool1 = True
bool2 = False

#Вывод типов переменных.
print (type(bool1))
print (type(bool2))

#Вывод логических операций Конъюкция, дизъюкция, инверсия.
list = ["1", "2", "3"]
if input ("введите число из списка или больше :") in list and "2" in list:
    print ("Конъюкция") 
elif input("Введите число :") in list or "4" in list:
    print ("дизъюкция")
else:
    print (not bool1)

#Создание двух неравных перменных int.
a = int(input("Введите значение a :"))
b = int(input("Введите значение b :"))

#Печать операций сравнения.
if a == b:
    print("Они равны")
else:
    print ("Они не равны")
if a > b:
    print("a больше b")
else:
    print ("a меньше b")
if b >= a:
    print ("b Больше или равно a")
else:
    print("b меньше или равно a")

#Печать арифметических операций
c = a+b
print (c)
d = a-b
print(d)
e = a*b
print (e)
f = a/b
print (f)
r = a**b
print (r)
w = a//b
print (w)
t = a%b
print (t)




