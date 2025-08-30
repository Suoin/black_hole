import dill
import os


#Здесь мы храним статистику по игрокам
PLAYER_FILE = 'players_status.pkl'


# Объект бота

#Сохранение
#Модуль сохранения состояния игрока

import dill

def save_players():
    with open(PLAYER_FILE, 'wb') as f:
        dill.dump(player, f)

def load_players():
    if os.path.exists(PLAYER_FILE):
        with open(PLAYER_FILE, 'rb') as f:
            try:
                return dill.load(f)
            except EOFError:
                return {}
    return {}

player = load_players()  # Загружаем состояние игроков при запуске