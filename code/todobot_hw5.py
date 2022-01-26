from random import choice

import telebot

token = ''

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()


HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* random - добавить на сегодня случайную задачу
* help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    # TODO: 1
    if len(task) < 3:
        bot.send_message(message.chat.id, 'Задачи должны быть больше 3х символов')
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['print'])
def print_(message):
    # TODO: 2
    dates = message.text.split(maxsplit=1)[1].lower().split()
    response  = ''
    for date in dates:
        tasks = todos.get(date)
        response += f'{date}: \n'
        for task in tasks:
            response += f'[ ] {task}\n'
        response += '\n'
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
