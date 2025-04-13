# battle.py
from player_stat import stats, save_stats
from data import save_players
from config import bot
from data import player
from bestiari import Monster
import telepot


# Захватываем цель из функции инициализации боя
def set_current_target(chat_id, target):
    player[chat_id].target = target
    print(f"Цель установлена для {chat_id}: {target}")


# Загружаем цель в боевой модуль
def get_current_target(chat_id):
    if chat_id in player:
        print(f"Текущая цель для {chat_id}: {player[chat_id].target}")
        return player[chat_id].target
    return None


# Функция для расчета процента здоровья монстра
def calculate_hp_percentage(target):
    if target.max_hp <= 0:  # Защита от деления на 0
        return 0
    return (target.hp / target.max_hp) * 100


# Обработчик боя
def battle(chat_id, message_id, target):
    print(f"Состояние коллбека на начале боя: {player[chat_id].on_battle_end}")
    target = get_current_target(chat_id)  # Загружаем цель
    if target is None:  # Если нет цели, отладочная часть
        bot.sendMessage(chat_id, "Ошибка: нет текущей цели.")
        return

    stat = target.show_stat()  # Обращаемся к функции класса цели в bestiari
    keyboard = player_attack(chat_id)  # Подключаем генератор клавиатуры
    last_message = bot.sendMessage(chat_id, f'{stat}', reply_markup=keyboard)  # Переменная для удаления сообщения
    player[chat_id].last_battle_message = last_message['message_id']  # Фиксируем ID сообщения

    print(f"Здоровье цели перед проверкой: {target.hp}")  # Отладка

    # Если здоровье цели <= 0, монстр погибает
    if target.hp <= 0:
        print("Монстр погиб!")
        bot.deleteMessage((chat_id, last_message['message_id']))
        print(f"Состояние коллбека перед завершением битвы: {player[chat_id].on_battle_end}")
        handle_battle_end(chat_id, target)  # Передаем коллбек через объект игрока
        return

    # Если здоровье игрока <= 0
    elif player[chat_id].hp <= 0:
        print("Игрок погиб!")
        bot.deleteMessage((chat_id, last_message['message_id']))
        print(f"Состояние коллбека перед завершением битвы: {player[chat_id].on_battle_end}")
        handle_battle_end(chat_id, player[chat_id])  # Передаем коллбек через объект игрока
        return


# Боевой обработчик каллбэков
def battle_on_callback_query(chat_id, message_id, data, on_battle_end=None):
    try:
        if data in player[chat_id].system['action']:
            target = get_current_target(chat_id)  # Загружаем цель
            action = player[chat_id].system['action'][data]  # Загружаем способность атаки

            # Игрок выполняет действие
            player_result = action(target)
            print(f"Результат действия игрока: {player_result}")
            print(f"Здоровье цели после действия: {target.hp}")

            # Проверяем, погиб ли монстр
            if target.hp <= 0:
                handle_battle_end(chat_id, target)
                return

            # Рассчитываем процент здоровья монстра
            hp_percentage = calculate_hp_percentage(target)
            print(f"HP цели: {target.hp}/{target.max_hp}, Процент HP: {hp_percentage}")

            # Если здоровье цели больше 0, монстр выбирает атаку
            if target.hp > 0:  # Проверяем, что монстр еще жив
                if hp_percentage > 60:
                    print("Используется атака A")
                    monster_result = target.attack_a(player[chat_id])  # Attack A
                elif hp_percentage > 20:
                    print("Используется атака B")
                    monster_result = target.attack_b(player[chat_id])  # Attack B
                else:
                    print("Используется атака C")
                    monster_result = target.attack_c(player[chat_id])  # Attack C
            else:
                print("Монстр погиб, атака не выбрана.")
                return

            print(f"Результат действия монстра: {monster_result}")

            # Проверяем, погиб ли игрок
            if player[chat_id].hp <= 0:
                handle_battle_end(chat_id, target)
                return

            # Обновляем характеристику монстра и отправляем сообщение
            stat = target.show_stat()
            stat_a = player[chat_id].hp
            stat_b = player[chat_id].mana
            stat_c = player[chat_id].energy
            bot.deleteMessage((chat_id, message_id))  # Удаляем старое сообщение

            # Формируем сообщение с результатами обеих атак
            result_message = (f"{stat}\n\n{player_result}\n{monster_result}\n"
                              f"Ваше хп: {stat_a}\nВаша мана: {stat_b}\nВаша энергия: {stat_c}")
            keyboard = player_attack(chat_id)  # Кнопки для следующего действия
            last_message = bot.sendMessage(chat_id, result_message, reply_markup=keyboard)

            # Сохраняем ID последнего сообщения
            player[chat_id].last_battle_message = last_message['message_id']

            # Если передан коллбек, вызываем его
            if callable(on_battle_end):
                on_battle_end(chat_id)

    except telepot.exception.TelegramError as e:
        if "Bad Request: message to delete not found" in str(e):
            pass
        else:
            print(f"Ошибка при удалении сообщения: {e.description}")


def handle_battle_end(chat_id, loser):
    print(f"Начало handle_battle_end для {loser}")
    print(f"Состояние коллбека на момент завершения: {player[chat_id].on_battle_end}")

    # Проверка состояния здоровья монстра и игрока, чтобы точно понять, кто проиграл
    if player[chat_id].hp <= 0:  # Игрок погиб
        print("Игрок погиб!")
        bot.sendMessage(chat_id, f'{player[chat_id].name} получил смертельное ранение')  # Сообщение о поражении
    elif isinstance(loser, Monster):  # Если проиграл монстр
        bot.sendMessage(chat_id, f"Ты убил {loser.name}!")  # Сообщение о победе
    else:  # Это возможно для других случаев, если нужно
        bot.sendMessage(chat_id, "Непредвиденная ошибка в бою.")

    # Попытка удалить старое сообщение, если оно существует
    last_message_id = player[chat_id].last_battle_message
    if last_message_id:
        try:
            bot.deleteMessage((chat_id, last_message_id))  # Удаление старого сообщения
            print(f"Сообщение с ID {last_message_id} удалено.")
        except telepot.exception.TelegramError as e:
            if "Bad Request: message to delete not found" in str(e):
                pass  # Сообщение уже удалено, игнорируем ошибку
            else:
                print(f"Ошибка при удалении сообщения: {e.description}")

    # Обновление состояния игрока
    player[chat_id].in_battle = False
    player[chat_id].target = None
    print(f"Игрок в бою: {player[chat_id].in_battle}, Цель: {player[chat_id].target}")

    # Если передан коллбек, вызываем его
    if callable(player[chat_id].on_battle_end):
        print(f"Вызов коллбека: {player[chat_id].on_battle_end}")
        player[chat_id].on_battle_end(chat_id)


def player_attack(chat_id):
    # Собираем уникальные элементы из списков
    unique_items = {
        item for items in [player[chat_id].abillity, player[chat_id].invetary, player[chat_id].use_hand]
        for item in items
    }

    # Создаём кнопки только для уникальных элементов
    buttons = [{'text': f"И: {item}", 'callback_data': f'{item}'} for item in unique_items]

    # Если кнопок нет, добавляем заглушку
    if not buttons:
        buttons = [{'text': "Нечего использовать", 'callback_data': 'no_action'}]

    # Группируем кнопки по 2 в ряд
    return {'inline_keyboard': [buttons[i:i + 2] for i in range(0, len(buttons), 2)]}

