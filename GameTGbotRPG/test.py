import pickle

# Путь к файлу
#PLAYER_FILE = 'players_status.pkl'
PLAYER_FILE = 'stat_player.pkl'
# Рекурсивная функция для вывода всех данных
def recursive_print(obj, indent=0):
    """ Рекурсивно выводит содержимое объекта. """
    spacing = "  " * indent
    if isinstance(obj, dict):
        # Если объект - словарь, выводим его ключи и значения
        for key, value in obj.items():
            print(f"{spacing}Key: {key} ->")
            recursive_print(value, indent + 1)
    elif isinstance(obj, list):
        # Если объект - список, выводим элементы
        for i, item in enumerate(obj):
            print(f"{spacing}Index {i}:")
            recursive_print(item, indent + 1)
    elif isinstance(obj, object):
        # Если объект - экземпляр класса, выводим его атрибуты
        print(f"{spacing}Object of type {type(obj)}:")
        for attr in dir(obj):
            # Выводим только публичные атрибуты (без магических методов)
            if not attr.startswith("__"):
                try:
                    value = getattr(obj, attr)
                    print(f"{spacing}  {attr}: {value}")
                except Exception as e:
                    print(f"{spacing}  {attr}: Error reading attribute ({e})")
    else:
        # Просто выводим другие объекты (строки, числа и т.д.)
        print(f"{spacing}{repr(obj)}")

# Чтение и вывод данных из файла
try:
    with open(PLAYER_FILE, 'rb') as file:
        players_data = pickle.load(file)
        print("Содержимое файла:")
        recursive_print(players_data)  # Рекурсивно выводим все содержимое
except FileNotFoundError:
    print(f"Файл {PLAYER_FILE} не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")


def general_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Ogr(name='Огр', hp = 650)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        general_c_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def general_c_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Подготовка', 'callback_data': 'general_e'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив огра, вы осмотрели зал, впереди была дверь, явна ведущая в тронный зал, генерал скрываеться там?',
                        reply_markup=keyboard)