import telebot

bot = telebot.TeleBot("6532451699:AAE-3bQn44naCZufh-Fvgozktvth_XYzMHc") # создание бота

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(message, get_nickname)


def get_nickname(message):
    nickname = message.text
    if len(nickname) > 20 or nickname[0].isdigit() or not nickname.endswith("bot"):
        bot.send_message(message.chat.id, "Ошибка ввода")
        bot.register_next_step_handler(message, get_nickname)
        return True
    else:
        bot.send_message(message.chat.id, "Ник одобрен!")
        bot.send_message(message.chat.id, "Вам доступны полезные материалы для изучения программирования")
        return False

@bot.message_handler(commands=["programms"])
def list_of_programms(message):
    bot.send_message(message.chat.id, "[Скачать Python](https://www.python.org/downloads/) [Скачать PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)", parse_mode="Markdown")

@bot.message_handler(commands=["exam"])
def ege(message):
    bot.send_message(message.chat.id, "[Канал преподавателя ЕГЭ по информатике](https://t.me/infa_vikusya)", parse_mode="Markdown")

@bot.message_handler(commands=["course"])
def course(message):
    bot.send_message(message.chat.id, "[Курсы подготовки к ОГЭ и ЕГЭ по всем предметам](https://umschool.net/)", parse_mode="Markdown")



bot.infinity_polling() # бесконечный ввод сообщений