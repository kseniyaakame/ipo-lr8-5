import json
count = 0
while True:
    print("1. Вывести все записи  \n2. Вывести запись по полю  \n3. Добавить запись  \n4. Удалить запись по полю \n5. Выйти из программы ")
    num=int(input('Выберите пункт '))
    with open("city.json", "r", encoding = "utf-8") as file:
        text = json.load(file)
    if num == 1:
        count+=1
        for write in text:
            print(f'Номер записи: {write['id']}')
            print(f"Название города: {write['name']} \nНазвание страны в котором находится город: {write['country']} \nЯвляется ли население города больше 100 000 человек: {write['is_big']} \nНаселение города: {write['people_count']}")
    elif num ==2:
        count+=1
        field = input('Введите поле ')
        found=False
        for write in text:
            if write['id']==field:
                print(f"Название города: {write['name']} \nНазвание страны в котором находится город: {write['country']} \nЯвляется ли население города больше 100 000 человек: {write['is_big']} \nНаселение города: {write['people_count']}")
                found = True
                break
        if not found:
            print("Записи нет")
    elif num==3:
        count+=1
        new = {}
        new['id'] = str(max(int(city['id']) for city in text) + 1 if text else 1)
        new['name'] = input("Введите название города: ")
        new['country'] = input("Введите название страны: ")   
        while True:
            people_count = input("Введите население города: ")
            if people_count.isdigit():
                new['people_count'] = int(people_count)
                break
            else:
                print("Ошибка: население города должно быть числом.")   
        new['is_big'] = (True if new['people_count'] > 100000 else False)
        text.append(new)  
        with open("city.json", "w", encoding="utf-8") as file:
            json.dump(text, file, indent=5)
        print("Запись добавлена")
    elif num == 4:
        count += 1
        field = input("Введите поле для удаления: ")
        found = False
        for city in text:
            if city['id'] == field:
                text.remove(city)
                found = True
                break
        if found:
            with open("city.json", "w", encoding = "utf-8") as file:
                json.dump(text, file, indent = 5)
            print("Запись удалена")
        else:
            print("Запись не найдена")

    elif num == 5:
        print(f"{count} выполненных операций")
        break
    else:
        print("Нет такого пункта")