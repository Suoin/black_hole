import telepot
from data import player
from navigator import callback_commands
from scenario import battle_on_callback_query,start_game_1
from  config import bot

#  общий обработчик каллбэков
def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    chat_id = msg['message']['chat']['id']
    message_id = msg['message']['message_id']

    # Если игрок находится в бою, передаем запрос в обработчик боевой системы
    if player[chat_id].in_battle:
        # Важно: тут мы просто передаем управление в файл scenario, чтобы не было конфликтов
        battle_on_callback_query(chat_id, message_id, data)
        return  # Завершаем обработку, так как запрос уже передан в другой обработчик

    # Обрабатываем запросы на навигацию
    if data == 'right' or data == 'left':
        start_game_1(chat_id, message_id)
    elif data in callback_commands:
        callback_commands[data](chat_id, message_id, data)
    else:
        bot.sendMessage(chat_id, f'Как ты это сделал? Напиши отзыв об этом. Команда {data}')


def start_game(chat_id):

    buttons = [["/start",'Развитие'],['Пожертвование','Отзыв']] #Настраиваем нужные кнопки
    keyboard = {'keyboard': buttons, 'resize_keyboard': True} # Создаем Реплуклавиатуру , ставит размер пользователя
    keyboard_1 = {'inline_keyboard':[
        [{'text': 'Влево', 'callback_data': 'left'},{'text':'Вправо','callback_data':'right'}]


    ]
    }
    bot.sendMessage(chat_id,'Игра запущена', reply_markup =keyboard) # Отправляем клавиатуру пользователю
    bot.sendMessage(chat_id, 'На вас мчится грузовик, вы думаете куда отпрыгнуть, куда вы отпрыгните?', reply_markup=keyboard_1)


