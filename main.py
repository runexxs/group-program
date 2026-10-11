students = [
    {"fio": "Искусных Иван Олегович", "group": "ВД-3-25", "grades": [5, 4, 5, 5, 4]},
    {"fio": "Бетмирзаев Тамерлан Асланович", "group": "БД-1-25", "grades": [5, 5, 5, 5, 5]},
    {"fio": "Исмаилов Самир Алимович", "group": "БД-2-25", "grades": [3, 4, 3, 4, 3]},
    {"fio": "Гантемиров Мухаммед Заурович", "group": "ВД-2-24", "grades": [4, 4, 4, 4, 4]},
    {"fio": "Муртазалиев Шамиль Муртазалиевич", "group": "ВД-2-24", "grades": [5, 5, 4, 5, 5]}
]

groups = ["БД-1-25", "БД-2-25", "ВД-3-25", "ВД-2-24"]

while True:
    print()
    print("==============================")
    print("  РАБОТА С УЧЕБНОЙ ГРУППОЙ")
    print("==============================")
    print("1. Добавить студента")
    print("2. Изменить студента")
    print("3. Удалить студента")
    print("4. Добавить оценку")
    print("5. Средний балл")
    print("6. Статистика группы")
    print("7. Удалить группу")
    print("0. Выход")
    print("==============================")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print()
        print("--- Добавление студента ---")
        fio = input("Введите ФИО: ")

        est = False
        for s in students:
            if s["fio"].lower() == fio.lower():
                est = True
        if est:
            print("Такой студент уже есть!")
        else:
            group = input("Введите группу: ")
            students.append({"fio": fio, "group": group, "grades": []})
            if group not in groups:
                groups.append(group)
            print("Студент добавлен.")

    elif choice == "2":
        print()
        print("--- Изменение студента ---")
        fio = input("Введите ФИО студента: ")

        found = None
        for s in students:
            if s["fio"].lower() == fio.lower():
                found = s

        if found == None:
            print("Студент не найден.")
        else:
            new_fio = input("Новое ФИ (Enter - не менять): ")
            new_group = input("Новая группа (Enter - не менять): ")
            if new_fio != "":
                found["fi"] = new_fio
            if new_group != "":
                found["group"] = new_group
                if new_group not in groups:
                    groups.append(new_group)
            print("Данные изменены.")

    elif choice == "3":
        print()
        print("--- Удаление студента ---")
        fio = input("Введите ФИO студента: ")

        found = None
        for s in students:
            if s["fio"].lower() == fio.lower():
                found = s

        if found == None:
            print("Студент не найден.")
        else:
            students.remove(found)
            print("Студент удалён.")

    elif choice == "4":
        print()
        print("--- Добавление оценки ---")
        fio = input("Введите ФИО студента: ")

        found = None
        for s in students:
            if s["fio"].lower() == fio.lower():
                found = s

        if found == None:
            print("Студент не найден.")
        else:
            grade = input("Введите оценку: ")
          
            if grade.isdigit():
                found["grades"].append(int(grade))
                print("Оценка добавлена.")
            else:
                print("Оценка должна быть числом!")

    elif choice == "5":
        print()
        print("--- Средний балл ---")
        fio = input("Введите ФИО студента (Enter - пропустить): ")

        if fio != "":
            found = None
            for s in students:
                if s["fio"].lower() == fio.lower():
                    found = s

            if found == None:
                print("Студент не найден.")
            else:
                if len(found["grades"]) > 0:
                    summa = 0
                    for g in found["grades"]:
                        summa = summa + g
                    sr = summa / len(found["grades"])
                    print("Средний балл:", sr)
                else:
                    print("У студента нет оценок.")

        print()
        print("Средний балл по группам:")
        for gr in groups:
            summa = 0
            kolvo = 0
            for s in students:
                if s["group"] == gr:
                    for g in s["grades"]:
                        summa = summa + g
                        kolvo = kolvo + 1
            if kolvo > 0:
                print(gr, ":", summa / kolvo)
            else:
                print(gr, ": нет оценок")

    elif choice == "6":
        print()
        print("--- Статистика группы ---")
        group = input("Введите группу: ")

        otl = 0
        hor = 0
        troe = 0
        dva = 0

        for s in students:
            if s["group"].lower() == group.lower():
                if len(s["grades"]) > 0:
                    summa = 0
                    for g in s["grades"]:
                        summa = summa + g
                    sr = summa / len(s["grades"])
                    if sr >= 4.5:
                        otl = otl + 1
                    elif sr >= 3.5:
                        hor = hor + 1
                    elif sr >= 2.5:
                        troe = troe + 1
                    else:
                        dva = dva + 1

        print()
        print("Группа", group)
        print("Отличников:", otl)
        print("Хорошистов:", hor)
        print("Троечников:", troe)
        print("Двоечников:", dva)

    elif choice == "7":
        print()
        print("--- Удаление группы ---")
        group = input("Введите группу: ")

        est = False
        for s in students:
            if s["group"].lower() == group.lower():
                est = True

        if est:
            print("В группе есть студенты! Сначала удалите их.")
        else:
            if group in groups:
                groups.remove(group)
                print("Группа удалена.")
            else:
                print("Такой группы нет.")

    elif choice == "0":
        print("Пока!")
        break

    else:
        print("Неверный пункт меню.")