import json
import csv
import pandas as pd

#Вывод контакта#
with open("users.json", "r+", encoding='utf-8') as json_file:
    a = json.load(json_file)
    
x = 1
for k, v in a.items():
    print(x, k, v)
    x+=1
print(f"\n")    
  
go = int(input("1-Добавить контакт \n2-Удалить контакт \n3-Найти в контактах \n4-Экспорт данных в CSV \nУкажите цифрой что бы вы хотели: "))
    
if go == 1:
    #Добавление контакта#
    print("Вы можете добавить контакт")
    name = input("name: ")
    phone = input("phone: ")
    data = {"name": name, "phone": phone}    
    a[name] = f"{phone}"  

    with open("users.json", "r+", encoding='utf-8') as json_file:
        json.dump(a, json_file, indent=4)
    print(f"Контакт успешно записан \n")

if go == 2:
    #Удаление контакта#
    nameDel = input("Вы можете удалить контакт указав имя: ")
    try:
        del a[f'{nameDel}']
        json.dumps(a)
        with open("users.json", "w") as json_file:
            json.dump(a, json_file)
    except KeyError as e:
        print("У вас нет такого в контактах")
        

if go == 3:
    #Поиск по контактам#
    namePoisc = input("Вы можете удалить контакт указав имя: ")
    print(f"Номер: {namePoisc}",  a[f"{namePoisc}"])
    

if go == 4:
    #Экспорт в CSV#
    pdObj = pd.read_json('users.json', orient="index")
    print(pdObj)
    pdObj.to_csv('contacts.csv', index=True)