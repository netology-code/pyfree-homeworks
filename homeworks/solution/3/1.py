def counter_letter(worlds, letter):
    """Считает количество слов в списке по заданному символу"""

    count = 0  # создаём счётчик
    for world in worlds:  # проходимся по каждому слову world в списке слов worlds 
        if letter.lower() in world.lower():  # приводим к нижнему регистру
            count += 1  # это то же самое что и count = count + 1
    return count  # возвращаем результат


worlds = ['python', 'c++', 'c', 'scala', 'java'] # пример списка
letter = 'c' # букву, которую ищем

result = counter_letter(worlds, letter) # вызываем функцию
print(result) # выводим результат
