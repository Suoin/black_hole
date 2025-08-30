import telepot
from telepot.loop import MessageLoop
from config import bot
from data import player,save_players
from player_stat import stats,save_stats
from commands import start_game, on_callback_query
from player import Player
import globasl
import datetime
 # Владыка

green_dragon = True
black_dragon = True
red_dragon = True
gold_dragon =True

one_boss = True
two_boss = True
tried_boss =True
four_boss = True

feedback_stage = {} # СИСТЕМА ОТЗЫВА
#Захватчик сообщения и преобразование в команды
def main(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text'].strip()
        #БЛОК СИСТЕМЫ ОТЗЫВОВ
        if chat_id in feedback_stage and feedback_stage[chat_id] == 'waiting_feedback':
            # Сохраняем отзыв
            save_feedback(text, chat_id)
            bot.sendMessage(chat_id, "Спасибо за ваш отзыв! Он успешно сохранён.")
            feedback_stage.pop(chat_id)  # Завершаем процесс сбора отзыва
            return
        #БЛОК ОБРАБОТКИ СТАРТА ИГРЫ
        if text in commands:
            commands[text](chat_id)
        else:
            # Если игрок уже в процессе создания персонажа, сохраняем его имя
            if chat_id in player and player[chat_id].name == 'Ты либо гений либо дурочек': #костыль, если игрок еще раз нажмет /start получит такой ник
                player[chat_id] = Player(text)  # Создаём объект класса Player
                 # Увеличиваем счетчик созданных игроков

                bot.sendMessage(chat_id, f'Ваш персонаж, {text}, успешно создан!')
                start_game(chat_id)

            else:
                bot.sendMessage(chat_id, 'Используйте кнопки или команду /start для начала игры.') #защита от любителей не следовать инструкции


#Стратовое меню создания персонажа и запуска сцены игры из файла scenario
def start_menu(chat_id):
 
    if globasl.boss == False:
        bot.sendMessage(chat_id,'Владыка повержен, сезон окончен, ожидайте второй сезон')
    elif chat_id in player:
        bot.sendMessage(chat_id, f'Ваш персонаж {player[chat_id].name} жив, новая игра невозможна.')
    else:
        bot.sendMessage(chat_id, f'{stats}\nВведите имя своего персонажа:')
        player[chat_id] = Player('Ты либо гений либо дурочек')  # Включаем создание персонажа и флаг защита

def test(chat_id): #Это тестовая команда для отладки потом ее надо отключить
    if player:
        # Создаем список строк с chat_id и именами персонажей
        player_info = [f'Chat ID: {chat_id} - Имя персонажа: {player_obj.name}' for chat_id, player_obj in player.items()]
        # Отправляем сообщение с информацией о всех персонажах
        bot.sendMessage(chat_id, '\n'.join(player_info))
    else:
        bot.sendMessage(chat_id, 'В базе нет персонажей!')

def kill(chat_id):  # отладочная команда
    if chat_id in player:
        player_class = player[chat_id].player_class
        stats.update_class_stats(player_class, 'dead')
        stats.dead += 1
        del player[chat_id]  # Удаляем персонажа

        stats.update_alive()  # Обновляем количество живых игроков
        save_players()  # Сохраняем изменения
        save_stats(stats)  # Сохраняем статистику
        bot.sendMessage(chat_id, 'Персонаж удалён.')
    else:
        bot.sendMessage(chat_id, 'У вас нет персонажа, для создания нового используйте команду /start')
def status(chat_id):
    if chat_id in player:
        player_stat = player[chat_id].show_stat() # Ntc
        bot.sendMessage(chat_id,player_stat)
    else:
        bot.sendMessage(chat_id,'Персонажа нет, /start для запуска игры')
def money(chat_id):
    text =('Привет. Проект не коммерческий и сервер я оплачиваю самостоятельно.\n'
           'Если тебе понравилась игра, ждешь второго сезона и хочешь увидеть дальнейшее развитие.\n'
           'То ты можешь помочь разработчику материально, сделав перевод любой суммы\n'
           'КАРТА СБЕРБАНК : <b>4276 5000 1081 8167</b>')
    bot.sendMessage(chat_id,text,parse_mode='HTML')
def dev_com(chat_id):
    text = ('Мой email : Suoin@mail.ru\n'
            'В плане развития бота и при достаточных пожертвованиях для поддержания сервера и дальнейшей разработки.'
            'Я планирую реализовать следующие вещи:\n'
            '1.Полноценное взаимодействие с рынком\n'
            '2.Расширить арсенал оружия и заклинаний\n'
            '3.Систему квестов и не линейного сюжета\n'
            '4.Целостный мир, а не линейный коридор\n'
            '5.Групповые бои\n'
            '6.Арена между игроками\n'
            'Для пожертвования вы можете перевести любую сумму на СБЕРБАНК:\n'
            '<b>4276 5000 1081 8167</b>')
    bot.sendMessage(chat_id,text,parse_mode='HTML')

def save_feedback(feedback, chat_id):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('feedbacks.txt', 'a', encoding='utf-8') as f:
        f.write(f"Дата: {date}, ID чата: {chat_id}, Отзыв: {feedback}\n")
def feed_back(chat_id):
    # Устанавливаем пользователя в стадию ввода отзыва
    feedback_stage[chat_id] = 'waiting_feedback'
    bot.sendMessage(chat_id, "Пожалуйста, напишите ваш отзыв в следующем сообщении.")


#словарь текстовых команд
commands = {'/start': start_menu,
            '/test_dev': test,
            '/kill_me': kill,
            '/stat': status,
            'СТАТУС': status,
            'Пожертвование':money,
            'Развитие':dev_com,
            'Отзыв': feed_back

            }


# Запуск бота с обработчиком сообщений и callback-запросов
MessageLoop(bot,{'chat': main,'callback_query': on_callback_query}).run_as_thread()
print("Игра запущена")
# Обработка событий
input("Нажмите Enter для завершения работы бота...")  # Ожидаем завершения работы
