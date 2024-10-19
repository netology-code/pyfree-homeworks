today = list() # today = [] # список можно создать двумя способами: today = list() или today = []
tomorrow = list() # tomorrow = []
other = list() # other = []


HELP = '''
Список доступных команд:
* show - напечать все задачи
* todo - добавить задачу
* help - Напечатать help
'''


while True:
    command = input('Введите команду\n')
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date == 'Сегодня': 
          today.append(task)
        elif date == 'Завтра':
          tomorrow.append(task)
        else:
          other.append(task)
        print(f'Задача {task} добавлена')
    elif command == 'show':
        print('Сегодня')
        print(today)      
        print('Завтра')
        print(tomorrow)
        print('Другие')
        print(other)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда!')
        print(HELP)
