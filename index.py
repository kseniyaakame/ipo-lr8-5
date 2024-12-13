import json

def save(date):
    with open("city.json", "w", encoding = "utf-8") as file:
        json.dump(date, "city.json", indent=5)

def all_rec(date):
    for record in date:
        print(f'Номер записи: {record["id"]}')
        print(f"Название города: {record['name']}")
        print(f"Название страны: {record['country']}")
        print(f"Является ли население города больше 100 000 человек: {record['is_big']}")
        print(f"Население города: {record['people_count']}\n")

def rec_field(date, field):
    for record in date:
        if record['id'] == field:
            print(f"Название города: {record['name']}")
            print(f"Название страны: {record['country']}")
            print(f"Является ли население города больше 100 000 человек: {record['is_big']}")
            print(f"Население города: {record['people_count']}")
            return
    print("Записи нет")

def add_rec(date):
    newcity = {}
    newcity['id'] = str(max(int(city['id']) for city in date) + 1 if date else 1)
    newcity['name'] = input("Введите название города: ")
    newcity['country'] = input("Введите название страны: ")
    while True:
        peop_count = input("Введите население города: ")
        if peop_count.isdigit():
            newcity['people_count'] = int(peop_count)
            break
        else:
            print("Ошибка: население города должно быть числом.")
    newcity['is_big'] = newcity['people_count'] > 100000
    date.append(newcity)
    print("Запись добавлена")

def delete(date, field):
    for city  in date:
        if city['id'] == field:
            date.remove(city)
            print("Запись удалена")
            return
    print("Запись не найдена")

def main():
    with open("city.json", "r", encoding = "utf-8") as file:
        date = json.load(file)
    count = 0
    while True:
        print("1. Вывести все записи  \n2. Вывести запись по полю  \n3. Добавить запись  \n4. Удалить запись по полю \n5. Выйти из программы ")
        num=int(input('Выберите пункт '))
        if num == 1:
            all_rec(date)
            count +=1
        elif num == 2:
            field = input('Введите поле для поиска: ')
            rec_field(date, field)
            count +=1
        elif num == 3:
            add_rec(date)
            save(date)
            count +=1
        elif num == 4:
            delete(date, field)
            save(date)
            count +=1
        elif num == 5:
            print(f"{count} выполненных операций")
            break
        else:
            print('нет такого пункта')
main()