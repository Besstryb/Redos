# вывод значений от 1 до 10 цикл for
print("for")
for i in range(0,11,1):
    print(i)

# цикл while вывод значений от 1 до 10
print ("while")
k = 0
while k < 11:
    print (k)
    k = k +1

# в цикле for печатает в командную строку каждую букву ФИО;
print ("fio")
fio = input('')
for fio in list(fio):
    print (fio)

#Список содержащий имена друзей
friend = ["Максим", "Андрей", "Слава", "Саша"]
for friend in (friend):
    print (friend)

#Словарь с именами друзей и датами рождения
import datetime
friendDict ={
                'maks'   : datetime.date(2001,3,10),
                'andrey' : datetime.date(2003,7,20), 
                'slava'  : datetime.date(1998,2,19), 
                'Pasha'  : datetime.date(2000,9,4)}
for friendName, friendDate in friendDict.items(): 
    if friendDate.month <= 8 and friendDate.month >=6:
        print ("Родились летом")
        print(friendName + ":", friendDate)     
    elif friendDate.month >=1 and friendDate.month <=2 or friendDate.month ==12:
        print ("Родились зимой")
        print(friendName + ":", friendDate)  