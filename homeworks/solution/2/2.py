today = list() # today = [] # список можно создать двумя способами: today = list() или today = []
tomorrow = list() # tomorrow = []
other = list() # other = []

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == 'show':
    print('Сегодня')
    print(today)
    print('Завтра')
    print(tomorrow)
    print('Другие')
    print(other)
  elif command == 'add':
    date = input('Введите дату: ')
    task = input('Введите задачу: ')
    if date == 'Сегодня':
      today.append(task)
    elif date == 'Завтра':
      tomorrow.append(task)
    else:
      other.append(task)
    print(f'Задача {task} добавлена')
  elif command == 'exit':
      print('Спасибо за использование! До свидания!')
      run = False
  else:
    print("Неизвестная команда")
    break
