import os
import pickle

# Файл для хранения статистики
STAT_FILE = 'stat_player.pkl'

# Структура для хранения статистики
class PlayerStats:
    def __init__(self):
        self.created = 0  # Сколько игроков создано
        self.dead = 0  # Сколько игроков погибло
        self.alive = 0  # Сколько игроков живых

        # Статистика по классам
        self.class_stats = {
            'Воин': {'created': 0, 'dead': 0, 'alive': 0},
            'Стрелок': {'created': 0, 'dead': 0, 'alive': 0},
            'Маг': {'created': 0, 'dead': 0, 'alive': 0},
            'Везунчик': {'created': 0, 'dead': 0, 'alive': 0},
            'Некромант': {'created': 0, 'dead': 0, 'alive': 0},  # Новый класс
            'Драконид': {'created': 0, 'dead': 0, 'alive': 0}    # Новый класс
        }

    def update_alive(self):
        self.alive = self.created - self.dead
        # Обновляем статистику по каждому классу
        for player_class in self.class_stats:
            self.class_stats[player_class]['alive'] = (
                self.class_stats[player_class]['created']
                - self.class_stats[player_class]['dead']
            )

    def update_class_stats(self, player_class, status):
        """
        Обновление статистики для конкретного класса.
        Обновляем статистику, если передан список классов.
        """
        if isinstance(player_class, list):
            for cls in player_class:
                if cls not in self.class_stats:
                    self.class_stats[cls] = {'created': 0, 'dead': 0, 'alive': 0}
                if status == 'created':
                    self.class_stats[cls]['created'] += 1
                elif status == 'dead':
                    self.class_stats[cls]['dead'] += 1
                elif status == 'alive':
                    self.class_stats[cls]['alive'] += 1
        else:
            if player_class not in self.class_stats:
                self.class_stats[player_class] = {'created': 0, 'dead': 0, 'alive': 0}
            if status == 'created':
                self.class_stats[player_class]['created'] += 1
            elif status == 'dead':
                self.class_stats[player_class]['dead'] += 1
            elif status == 'alive':
                self.class_stats[player_class]['alive'] += 1

    def __str__(self):
        # Исключаем классы "Некромант" и "Драконид" из вывода
        excluded_classes = {'Некромант', 'Драконид'}
        class_stats_str = "\n".join(
            [
                f"- {cls}: Создано: {self.class_stats[cls]['created']} | Погибло: {self.class_stats[cls]['dead']} | Живых: {self.class_stats[cls]['alive']}"
                for cls in self.class_stats if cls not in excluded_classes
            ]
        )
        return (f"Создано игроков: {self.created}\n"
                f"{class_stats_str}\n"
                f"Погибло игроков: {self.dead}\n"
                f"Живых игроков: {self.alive}")


# Функции для загрузки и сохранения статистики
def load_stats():
    if os.path.exists(STAT_FILE):
        with open(STAT_FILE, 'rb') as f:
            return pickle.load(f)
    return PlayerStats()


def save_stats(stats):
    with open(STAT_FILE, 'wb') as f:
        pickle.dump(stats, f)


# Загрузка статистики при старте
stats = load_stats()

print(stats)
