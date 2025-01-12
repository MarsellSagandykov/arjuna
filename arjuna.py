#Импорт библиотек
import telebot
from telebot import types

#Базы данных


#Получение модераторов
moderator_ids = "Токен модератора"

#Группа
other_group_chat_id = "токен группы"

#Token
token = 'Токен '
bot = telebot.TeleBot(token)



#Создание Клавиатуры
def create_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(row_width=len(buttons), resize_keyboard=True)
    for text in buttons:
        button = types.KeyboardButton(text)
        keyboard.add(button)
    return keyboard

# Клавиатура пользователя
user_buttons = ["Активное задание", "Расписание", "Список призов", "Информация", "Контакты", "Личный кабинет"]
start_menu_keyboard = create_keyboard(user_buttons)
mod_buttons = ["Рассылка", "Публикация на канале", "Посмотреть ответы", "Настройки бота"]
moderator_keyboard = create_keyboard(mod_buttons)

# Обработчик команды "старт"
@bot.message_handler(commands=['start'])
def handle_start(message):
    with open('/home/marson/WorkIO/botarjuna/pic/1.jpg', 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Дорогие друзья, рады приветствовать вас в этом чате! \n \nЕсли вы здесь, значит, вы готовы включаться в активную студенческую жизнь и саморазвиваться! \nПриветствуем всех в клубе "Среда компетенций" Центра компетенций ТГУ.',
            reply_markup=start_menu_keyboard
        )

# Команда "Активное задание"
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'активное задание')
def handle_calendar(message):
    with open('/home/marson/WorkIO/botarjuna/pic/4.jpg', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Задание: Диагностика \n Пройди диагностику компетенций: \n 4 базовых теста на softskills.rsv. \n '
                    '1. Пройди тесты; \n 2. Дождись результатов; \n 3. Напиши нам. \n '
                    'Результат: прислать мне в личные сообщения id с платформы РСВ \nНаграда: 10 авокадиков \n\n'
                    'Задание: Диагностика+ \n Пройди диагностику компетенций: 4 дополнительных теста на softskills.rsv. \n'
                    '1. Пройди тесты; \n 2. Дождись результатов; \n 3. Напиши нам. \n '
                    'Результат: прислать мне в личные сообщения id с платформы РСВ \n Награда: 10 авокадиков \n\n'
                    'Пост Написать пост про игру, которая помогает развить компетенции: \n'
                    '1. Написать мне о том, что хотите выполнить это задание; \n '
                    '2. Прислать текст готового поста в ЛС; \n '
                    '3. Баллы начислим вам после того, как пост будет готов к публикации. \n'
                    'Награда: 5 авокадиков \n\n'
                    'Эссе \n Напиши рефлексивное эссе про свои компетенции: \n '
                    '1. Напиши текст до 2 страниц; \n 2. Пришли его мне в ЛС.\n Награда: 10 авокадиков',
            reply_markup=keyboard
        )

# Команда "Расписание"
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'расписание')
def handle_calendar(message):
    with open('/home/marson/WorkIO/botarjuna/pic/6.png', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        bot.send_photo(
            message.chat.id,
            photo,
            caption='дайджест событий на НОЯБРЬ \n\n'
                    '1 ноября - Квест “В поисках критмыша”; \n'
                    '6 ноября - Мастер класс по визуализации от Марины Шиловой; \n '
                    '13 ноября - игротека “Формула счастья” - уникальная игра от разработчиков Ядра Бакалавриата; \n'
                    '20 ноября - встреча-обсуждение ваших идей; \n'
                    '27 ноября - тренинг-сюрприз (выбираем, что провести по вашим запросам). \n\n'
                    'Проводи осень продуктивно',
            reply_markup=keyboard
        )

# Команда "Список призов"
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'список призов')
def handle_calendar(message):
    with open('/home/marson/WorkIO/botarjuna/pic/7.jpg', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Значок Центр компетенций ТГУ \n Стоимость: 20 авокадиков; \n\n'
                    'Экскурсия в Музее книги Научной библиотеки ТГУ \n Cтоимость: 50 авокадиков; \n\n'
                    'Посещение Первого музея славянской мифологии \n Стоимость: 75 авокадиков; \n\n'
                    'Книга про компетенции (самые разные) \n Стоимость: 100 авокадиков; \n\n'
                    'Набор авторских карточек-дилемм "Компетенции" \n Стоимость: 150 авокадиков; \n\n'
                    'Участие в мастер-классе по гончарному мастерству \n Стоимость: 175 авокадиков; \n\n '
                    'Завтрак со звездой \n Стоимость: 200 авокадиков; \n\n'
                    'Стажировка в институте образования ТГУ \n Стоимость: 250 авокадиков; \n\n',
            reply_markup=keyboard
        )

# Команда "Контакты"
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'контакты')
def handle_contacts(message):
    with open('/home/marson/WorkIO/botarjuna/pic/2.jpg', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text='Сообщество Вконтакте:', url="https://vk.com/centr.kompetenci_tsu")
        url_button2 = types.InlineKeyboardButton(text='Официальный телеграм-канал ЦК ТГУ: ', url="https://t.me/centrcomp")
        keyboard.add(url_button1, url_button2)
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Приглашаем подписаться на социальные сети Центра компетенций, чтобы первыми быть в курсе главных событий:',
            reply_markup=keyboard
        )

# Команда "Информация"
@bot.message_handler(content_types=['text'], func=lambda message: message.chat.type == 'private' and message.text.lower() == 'информация')
def handle_information(message):
    with open('/home/marson/WorkIO/botarjuna/pic/3.jpg', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Ссылка на регистрацию в клуб',
                                                url="https://forms.yandex.ru/cloud/66d6dffaf47e73a34c7b7f80")
        keyboard.add(url_button)
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Среда компетенций - это свободное пространство саморазвития, где вы сможете (а мы поможем) выстроить твой собственный маршрут развития \n\n '
                    'Клуб Центра компетенций ТГУ "Среда компетенций" - это сообщество активных студентов про компетенции и саморазвитие! В Клубе вас ждут: '
                    '\n\n - Тренинги по развитию компетенций;'
                    '\n - Игротеки с разбором механиками и образовательного ракурса игр;'
                    '\n - Книжный клуб с разбором персонажей, их компетентностных профилей и путей их развития;'
                    '\n - Участие в подготовке и проведении образовательных событий - в том числе тех, что вы придумываете сами (да, да, мы поможем воплотить ваши идеи и провести мероприятие мечты);'
                    '\n - Марафон заданий с призами про компетенции и саморазвитие.',
            reply_markup=keyboard
        )

# Команда "Личный кабинет"
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'личный кабинет')
def handle_calendar(message):
    with open('/home/marson/WorkIO/botarjuna/pic/7.jpg', 'rb') as photo:
        keyboard = types.InlineKeyboardMarkup()
        bot.send_photo(
            message.chat.id,
            photo,
            caption='Основа под ЛК студента',
            reply_markup=keyboard
        )
##Модератор

#Публикация на канале
@bot.message_handler(func=lambda message: message.chat.type == 'private' and message.text.lower() == 'публикация на канале')
def request_text_for_publication(message):
    user_id = message.from_user.id

    if user_id not in moderator_ids:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")
        return

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_exit = types.KeyboardButton(text='Вернуться Назад')
    markup.add(button_exit)
    bot.send_message(message.chat.id, "Введите текст для публикации или нажмите на кнопку для выхода в меню модератора", reply_markup=markup)

    # Регистрация следующего шага
    bot.register_next_step_handler(message, publish_text_to_group)

def publish_text_to_group(message):
    user_id = message.from_user.id
    text_to_publish = message.text or message.caption

    if text_to_publish and text_to_publish.lower() == 'вернуться назад':
            bot.send_message(message.chat.id, "Выход в меню модератор", reply_markup=moderator_keyboard)
            return

    if user_id in moderator_ids:
        try:
            if message.photo:
                photo_id = message.photo[-1].file_id
                bot.send_photo(other_group_chat_id, photo_id, caption=text_to_publish)
            elif message.video:
                video_id = message.video.file_id
                bot.send_video(other_group_chat_id, video_id, caption=text_to_publish)
            elif text_to_publish:
                bot.send_message(other_group_chat_id, text_to_publish)
        except Exception as e:
            print(f"Error sending message to {other_group_chat_id}: {e}")

        if message.photo:
            bot.send_message(message.chat.id, "Публикация выполнена. Отправлено фото.")
        elif message.video:
            bot.send_message(message.chat.id, "Публикация выполнена. Отправлено видео.")
        elif text_to_publish:
            bot.send_message(message.chat.id, f"Публикация выполнена. Отправлено сообщение:\n{text_to_publish}")
        else:
            bot.send_message(message.chat.id, "Неизвестный тип контента. Публикация не выполнена.")
            bot.register_next_step_handler(message, request_text_for_publication)
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")



if __name__ == '__main__':
    print('Бот успешно запущен')
    bot.infinity_polling()
    print('Бот отключен')
