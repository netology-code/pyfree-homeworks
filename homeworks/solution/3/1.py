def counter_letter(worlds, letter):
    """Считает косличество слов с списке по заданному символу"""

    count = 0  # созаём счётчик
    for world in worlds:  # проходимся по каждому слову world в списке слов worlds 
        if letter.lower() in world.lower():  # приводим к нижнему регистру
            count += 1  # это тоже самое что и count = count + 1
    return count  # возвращаем результат


worlds = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'

result = counter_letter(worlds, letter)
print(result)
