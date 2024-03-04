#8 разных переменных
var_none = None
var_int = 10
var_float = 3.14
var_str = "3.14"
var_list = [1,2,3,4,5]
var_tuple = (6,7,8,9,10)
var_dict = {"name": "Vasiliy", "age": "22", "country": "RF"}
var_set = {1,2,3,4,5}

#функция для печати типа переменной и ее размера (если возможно)
def print_variable_info (variable):
    print (f"Тип переменной : {type(variable).__name__}")
    if isinstance (variable, (str, list, tuple, dict, set)):
        print (f"Размер: {len(variable)}")

#Печать типа каждой переменной
print_variable_info(var_none)
print_variable_info(var_int)
print_variable_info(var_float)
print_variable_info(var_str)
print_variable_info(var_list)
print_variable_info(var_tuple)
print_variable_info(var_dict)
print_variable_info(var_set)

#Изменение типа переменной int на float и обратно
var_int = float(var_int)
var_float = int(var_float)

#Изменение типа переменной float на str и обратно
var_float = str(var_float)
var_str = float(var_str)

#Печать размера и элементов для переменных str, list, tuple
if isinstance(var_str, (str, list, tuple)):
    print(f"Первый элемент: {var_str[0]}")
    print(f"Последний элемент: {var_str[-1]}")
    print(f"Элементы без первого и последнего: {var_str[1:-1]}")

#печать размера и значения для переменной dict
    if isinstance(var_dict, dict):
        print(f"Значение одного из ключей: {var_dict['name']}")
