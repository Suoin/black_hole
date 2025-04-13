class Monster:
    def __init__(self, name):
        self.name = name
        # Зависиимости от характеристик
        self.attack = 10
        self.hp = 100
        self.max_hp = 100# очки здоровья
        self.mana = 50  # очки маны
        # характеристик
        self.sila = 5  # cила влияет на на хп и урон
        self.agila = 5  # ловкость влияете на урон + крит удар
        self.intelect = 5  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = []
        self.debuff = [ ]# Текущие способности и дебафы
        # Зона флагов и состояний

    def attack_a(self, target):
        damage = self.attack-self.sila

        if 'Уклонение' in target.debuff:
            target.debuff.remove('Уклонение')
            target.hp -= 0
            # Удаляем дебафф
            return f'Вы уклонились'

        if 'Яростный крик' in self.debuff:
            target.hp -= 0
            self.debuff.remove('Яростный крик')  # Убираем "Яростный крик" из дебаффов
            return 'Противник ошеломлен'

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон сначала уменьшается за счет shield
        if target.shield > 0:
            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщения
        if initial_shield > 0:
            attack_message = (f"{self.name} наносит {damage} урона. "
                              f"Щит: {target.shield}. HP: {target.hp}.")
            if target.shield > 0:
                return (f'{self.name} нанес вам {damage} урона. '
                        f'Щит поглотил часть урона.')
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f'{self.name} полностью пробил ваш щит.'
        else:
            attack_message = (f"{self.name} наносит {damage} урона. HP: {target.hp}.")
            return f'{self.name} нанес вам {damage} урона.'

    def attack_b(self,target):
        damage = self.attack + self.sila
        if 'Уклонение' in target.debuff:
            target.debuff.remove('Уклонение')
            target.hp -= 0# Удаляем дебафф
            return f'Вы уклонились'

        if 'Яростный крик' in self.debuff:
            self.debuff.remove('Яростный крик')
            target.hp -=0# Убираем "Яростный крик" из дебаффов
            return 'Противник ошеломлен'

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон сначала уменьшается за счет shield
        if target.shield > 0:
            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщения
        if initial_shield > 0:
            attack_message = (f"{self.name} наносит {damage} урона. "
                              f"Щит: {target.shield}. HP: {target.hp}.")
            if target.shield > 0:
                return (f'{self.name} нанес вам {damage} урона. '
                        f'Щит поглотил часть урона.')
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f'{self.name} полностью пробил ваш щит.'
        else:
            attack_message = (f"{self.name} наносит {damage} урона. HP: {target.hp}.")
            return f'{self.name} нанес вам {damage} урона.'

    def attack_c(self, target):
        damage = self.attack + self.agila+self.sila  # Расчет урона

        if 'Уклонение' in target.debuff:
            target.debuff.remove('Уклонение')
            target.hp -= 0
            # Удаляем дебафф
            return f'Вы уклонились'

        if 'Яростный крик' in self.debuff:
            target.hp -= 0
            self.debuff.remove('Яростный крик')  # Убираем "Яростный крик" из дебаффов
            return 'Противник ошеломлен'

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон сначала уменьшается за счет shield
        if target.shield > 0:
            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщения
        if initial_shield > 0:
            attack_message = (f"{self.name} наносит {damage} урона. "
                              f"Щит: {target.shield}. HP: {target.hp}.")
            if target.shield > 0:
                return (f'{self.name} нанес вам {damage} урона. '
                        f'Щит поглотил часть урона.')
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f'{self.name} полностью пробил ваш щит.'
        else:
            attack_message = (f"{self.name} наносит {damage} урона. HP: {target.hp}.")
            return f'{self.name} нанес вам {damage} урона.'

    def show_stat(self):
        stat = (
                f'Возможный урон :{self.attack+self.sila}\n'
                f'Имя :{self.name}\n'
                f'Здоровье: {self.hp}\n'
                f'Мана: {self.mana}\n'
                f'Сила: {self.sila}\n'
                f'Ловкость: {self.agila}\n'
                f'Интеллект: {self.intelect}\n'
                f"Способности: {', '.join(self.abillity) if self.abillity else 'Нет'}"
                )
        return stat

class Goblin(Monster):
    def __init__(self, name='Гоблин',attack=15,hp=50,max_hp=50, mana = 10):
        super().__init__(name)  # Вызов конструктора родительского класса
        # Переопределяем только те атрибуты, которые специфичны для гоблина
        self.attack = attack  # Переопределение атаки
        self.hp = hp  # Переопределение здоровья
        self.max_hp = max_hp
        self.mana = mana  # Переопределение маны
        self.abillity = ['Коварный удар']  # Способности, которые есть у гоблина



class Slaim(Monster):
    def __init__(self, name='Слизь', attack=10, hp=50, mana=10):
        super().__init__(name)
        self.max_hp = 50
        self.attack = attack
        self.hp = hp
        self.mana = mana

class Wolf(Monster):
    def __init__(self, name='Волк', attack=15, hp=50, mana=10):
        super().__init__(name)
        self.max_hp = 50
        self.attack=attack
        self.hp=hp
        self.mana = mana
class Orc(Monster):
    def __init__(self,name = 'Орк', attack = 25, hp= 200,max_hp=200,mana =60):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 10  # cила влияет на на хп и урон
        self.agila = 5  # ловкость влияете на урон + крит удар
        self.intelect = 6  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар мечом','Яростный удар','Удар берсерка']

    def attack_a(self, target):
        cost = 20  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 40 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар мечом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар мечом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар мечом нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 10  # Стоимость атаки
        damage = self.attack + (self.sila if 20 < self.mana < 41 else self.agila)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростный удар нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.sila + self.agila + (self.attack if self.mana >= 1 and self.mana <= 20 else self.intelect)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар берсерка нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар берсерка полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар берсерка нанес вам {damage} урона."


class Begemot(Monster):
    def __init__(self,name = 'Бегемот', attack = 170, hp= 17563,max_hp=17563,mana =600):
        super().__init__(name)
        self.max_hp = max_hp
        self.attack = attack
        self.hp = hp
        self.mana = mana


class Green_dragon(Monster):
    def __init__(self,name = 'Зеленый дракон', attack = 30, hp= 1300,max_hp=1300,mana =600):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 70  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 60  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Огненное дыхание', 'Удар лапой', 'Удар хвостом']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 600 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар лапой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар лапой полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар лапой нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect-40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Огненное дыхание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Огненное дыхание полностью пробило ваш щит!"
        else:
            return f"{self.name} Огненное дыхание нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.agila+10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар хвостом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар хвостом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар хвостом нанес вам {damage} урона."


class Black_dragon(Monster):
    def __init__(self,name = 'Черный дракон', attack = 65, hp= 1420,max_hp=1420,mana =900):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 50  # cила влияет на на хп и урон
        self.agila = 20  # ловкость влияете на урон + крит удар
        self.intelect = 40  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Огненное дыхание', 'Удар лапой', 'Удар хвостом']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 600 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар лапой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар лапой полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар лапой нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect - 40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Огненное дыхание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Огненное дыхание полностью пробило ваш щит!"
        else:
            return f"{self.name} Огненное дыхание нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.agila + 10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар хвостом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар хвостом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар хвостом нанес вам {damage} урона."


class Gold_dragon(Monster):
    def __init__(self,name = 'Золотой дракон', attack = 100, hp= 3200,max_hp=3200,mana =1900):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 50  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 40  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Огненное дыхание', 'Удар лапой', 'Удар хвостом']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 600 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар лапой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар лапой полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар лапой нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect - 40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Огненное дыхание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Огненное дыхание полностью пробило ваш щит!"
        else:
            return f"{self.name} Огненное дыхание нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.agila + 10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар хвостом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар хвостом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар хвостом нанес вам {damage} урона."


class Red_dragon(Monster):
    def __init__(self,name = 'Красный дракон', attack = 107, hp= 3650,max_hp=3650,mana =3000):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 55  # cила влияет на на хп и урон
        self.agila = 22  # ловкость влияете на урон + крит удар
        self.intelect = 47  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Огненное дыхание', 'Удар лапой', 'Удар хвостом']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 600 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар лапой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар лапой полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар лапой нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect - 40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Огненное дыхание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Огненное дыхание полностью пробило ваш щит!"
        else:
            return f"{self.name} Огненное дыхание нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.agila + 10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар хвостом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар хвостом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар хвостом нанес вам {damage} урона."


class Gorgula(Monster):
    def __init__(self, name='Каменная горгулья', attack=25, hp=225,max_hp=225, mana=100):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 10  # cила влияет на на хп и урон
        self.agila = 10  # ловкость влияете на урон + крит удар
        self.intelect = 60  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Визг', 'Удар когтями', 'Каменный обстрел']

    def attack_a(self, target):
        cost = 20  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 60 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Визг нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Визг полностью пробил ваш щит!"
        else:
            return f"{self.name} Визг нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 10  # Стоимость атаки
        damage = self.attack + (self.sila if 20 < self.mana < 41 else self.agila)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар когтями нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар когтями полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар когтями нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.intelect if 1 <= self.mana <= 20 else self.intelect / 2

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Каменный обстрел нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Каменный обстрел полностью пробил ваш щит!"
        else:
            return f"{self.name} Каменный обстрел нанес вам {damage} урона."


class Ogr(Monster):
    def __init__(self, name='Огр', attack=45, hp=500,max_hp=500, mana=160):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 70  # cила влияет на на хп и урон
        self.agila = 1  # ловкость влияете на урон + крит удар
        self.intelect = 3  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар кулаком', 'Топот', 'Яростные удары']

    def attack_a(self, target):
        cost = 20  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 160 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар кулаком нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар кулаком полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар кулаком нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 20  # Стоимость атаки
        damage = self.sila if 40 < self.mana < 100 else self.sila/2

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Топот полностью пробил ваш щит!"
        else:
            return f"{self.name} Топот нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.attack + self.intelect if 1 <= self.mana <= 40 else self.intelect + 17

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростные удары нанесли вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростные удары полностью пробили ваш щит!"
        else:
            return f"{self.name} Яростные удары нанесли вам {damage} урона."


class Deamon(Monster):
    def __init__(self, name='Демон', attack=35, hp=350,max_hp=350, mana=1000):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 10  # cила влияет на на хп и урон
        self.agila = 5  # ловкость влияете на урон + крит удар
        self.intelect = 25  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Огненный шар', 'Когти демона', 'Испепеление']

    def attack_a(self, target):
        cost = 200  # Стоимость атаки
        if self.mana >= 600:
            damage = self.attack + self.intelect
        else:
            damage =self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Огненный шар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Огненный шар полностью пробил ваш щит!"
        else:
            return f"{self.name} Огненный шар нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=400:
            damage = self.attack + self.agila
        else:
            damage = self.agila
        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Когти демона нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Когти демона полностью пробил ваш щит!"
        else:
            return f"{self.name} Когти демона нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 20  # Стоимость атаки
        if self.mana >=100:
            damage = self.sila + self.intelect
        else:
            damage = self.sila+self.intelect -15

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Испепеление нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Испепеление полностью пробило ваш щит!"
        else:
            return f"{self.name} Испепеление нанесло вам {damage} урона."


class First_general(Monster):
    def __init__(self, name='Генерал Марцелиус', attack=35, hp=1300,max_hp=1300, mana=850):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 90  # cила влияет на на хп и урон
        self.agila = 60  # ловкость влияете на урон + крит удар
        self.intelect = 40  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Пронзание', 'Бросок тотема', 'Рассечение']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = 30 - (self.sila if self.mana > 850 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Пронзание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Пронзание полностью пробило ваш щит!"
        else:
            return f"{self.name} Пронзание нанесло вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect - 40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Бросок тотема нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Бросок тотема полностью пробил ваш щит!"
        else:
            return f"{self.name} Бросок тотема нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 100  # Стоимость атаки
        damage = self.agila + 10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Рассечение нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Рассечение полностью пробило ваш щит!"
        else:
            return f"{self.name} Рассечение нанесло вам {damage} урона."


class Two_general(Monster):
    def __init__(self, name='Генерал Рамениус', attack=60, hp=1350,max_hp=1350, mana=1850):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp=max_hp
        self.mana = mana
        self.sila = 45  # cила влияет на на хп и урон
        self.agila = 20  # ловкость влияете на урон + крит удар
        self.intelect = 30  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар плетью', 'Разрушение', 'Порча']

    def attack_a(self, target):
        cost = 150  # Стоимость атаки
        if self.mana >=1500:
            damage = self.attack + self.agila
        else:
            damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар плетью нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар плетью полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар плетью нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 150  # Стоимость атаки
        if self.mana >=800:
            damage = self.attack + self.intelect
        else:
            damage = self.attack-30+self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Разрушение нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Разрушение полностью пробило ваш щит!"
        else:
            return f"{self.name} Разрушение нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=500:
            damage = self.agila + 10
        else:
            damage = self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Порча нанесла вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Порча полностью пробила ваш щит!"
        else:
            return f"{self.name} Порча нанесла вам {damage} урона."


class Tri_general(Monster):
    def __init__(self, name='Генерал Хенониус', attack=70, hp=3600,max_hp=3600, mana=2850):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 70  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 60  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Пузырьки', 'Удар клешней', 'Сжимание']

    def attack_a(self, target):
        cost = 150  # Стоимость атаки
        if self.mana >= 2000:
            damage = self.attack + self.agila
        else:
            damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Пузырьки нанесли вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Пузырьки полностью пробили ваш щит!"
        else:
            return f"{self.name} Пузырьки нанесли вам {damage} урона."

    def attack_b(self, target):
        cost = 150  # Стоимость атаки
        if self.mana >=1000:
            damage = self.attack + self.intelect
        else:
            damage = self.attack -40 + self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар клешней нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар клешней полностью пробило ваш щит!"
        else:
            return f"{self.name} Удар клешней нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=500:
            damage = self.agila + 10
        else:
            damage = self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Cжимание нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Сжимание полностью пробило ваш щит!"
        else:
            return f"{self.name} Сжимане нанесло вам {damage} урона."


class Four_general(Monster):
    def __init__(self, name='Генерал Неписиус', attack=105, hp=4200,max_hp=4200, mana=5000):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 55  # cила влияет на на хп и урон
        self.agila = 20  # ловкость влияете на урон + крит удар
        self.intelect = 35  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Душение', 'Утомление', 'Вспышка']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >= 4000:
            damage = self.attack + self.agila
        else:
            damage = self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Душение нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Душение полностью пробило ваш щит!"
        else:
            return f"{self.name} Душение нанесло вам {damage} урона."

    def attack_b(self, target):
        cost = 200  # Стоимость атаки
        if self.mana >=3000:
            damage = self.attack + self.intelect
        else:
            damage = self.attack + self.intelect-40

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Утомление нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Утомление полностью пробило ваш щит!"
        else:
            return f"{self.name} Утомление нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=1000:
            damage = self.agila + 10
        else:
            damage = self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Вспышка нанесла вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Вспышка полностью пробила ваш щит!"
        else:
            return f"{self.name} Вспышка нанесла вам {damage} урона."


class Lord_deamon(Monster):
    def __init__(self, name='Повелитель Суоиниус', attack=125, hp=4600,max_hp=4600, mana=10000 ):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 52  # cила влияет на на хп и урон
        self.agila = 33  # ловкость влияете на урон + крит удар
        self.intelect = 45  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Выстрел', 'Разлом', 'Сфера хаоса']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 600 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Выстрел нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Выстрел полностью пробил ваш щит!"
        else:
            return f"{self.name} Выстрел нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else self.intelect - 40)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Разлом нанесло вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Разлом полностью пробило ваш щит!"
        else:
            return f"{self.name} Разлом нанесло вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.agila + 10 if self.mana >= 1 and self.mana <= 200 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Сфера хаоса нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Сфера хаоса полностью пробил ваш щит!"
        else:
            return f"{self.name} Сфера хаоса нанес вам {damage} урона."


class Garpia(Monster):
    def __init__(self, name='Гарипия', attack=30, hp=400,max_hp=400, mana=600):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 15  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 30  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Острые когти', 'Взмах крылом', 'Вихрь']

    def attack_a(self, target):
        cost = 50  # Стоимость атаки
        if self.mana >=400:
            damage = self.attack + self.agila
        else:
            damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Острые когти нанесли вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Острые когти полностью пробили ваш щит!"
        else:
            return f"{self.name} Острые когти нанесли вам {damage} урона."

    def attack_b(self, target):
        cost = 50  # Стоимость атаки
        if self.mana >=200:
            damage = self.attack + self.sila
        else:
            damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name}Взмах крылом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Взмах крылом полностью пробил ваш щит!"
        else:
            return f"{self.name} Взмах крылом нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 25  # Стоимость атаки
        if self.mana >=30:
            damage = self.attack+self.intelect
        else:
            damage = self.intelect-5

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Вихрь нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Вихрь полностью пробил ваш щит!"
        else:
            return f"{self.name} Вихрь нанес вам {damage} урона."


class Cobold(Monster):
    def __init__(self, name='Кобольд', attack=45, hp=520,max_hp=520, mana=700):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 25  # cила влияет на на хп и урон
        self.agila = 15  # ловкость влияете на урон + крит удар
        self.intelect = 30  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Выпад','Земляной шип','Безумный удар']

    def attack_a(self, target):
        cost = 20  # Стоимость атаки
        damage = self.attack + (self.agila if self.mana > 700 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Выпад нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Выпад полностью пробил ваш щит!"
        else:
            return f"{self.name} Выпад нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 10  # Стоимость атаки
        damage = self.attack + (self.intelect if 200 < self.mana < 400 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Земляной шип нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Земляной шип полностью пробил ваш щит!"
        else:
            return f"{self.name} Земляной шип нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 20  # Стоимость атаки
        damage = damage = self.attack + self.agila if 1 <= self.mana <= 150 else self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Безумный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Безумный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Безумный удар нанес вам {damage} урона."


class Skelet(Monster):
    def __init__(self, name='Скелет', attack=45, hp=500,max_hp=500, mana=100):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 38  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 1  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар мечом', 'Яростный удар', 'Удар берсерка']

    def attack_a(self, target):
        cost = 0  # Стоимость атаки
        damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар мечом нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар мечом полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар мечом нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 0  # Стоимость атаки
        damage = self.sila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростный удар нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 0  # Стоимость атаки
        damage = self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар берсерка нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар берсерка полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар берсерка нанес вам {damage} урона."


class Golem(Monster):
    def __init__(self, name='Голем-страж', attack=27, hp=700,max_hp=700, mana=460):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 17  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 33  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Обстрел', 'Размашистый удар', 'Раздавить']

    def attack_a(self, target):
        cost = 20  # Стоимость атаки
        damage = self.attack + (self.intelect if self.mana > 460 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Обстрел нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Обстрел полностью пробил ваш щит!"
        else:
            return f"{self.name} Обстрел нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 10  # Стоимость атаки
        damage = self.attack + (self.sila if 20 < self.mana < 41 else self.agila)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростный удар нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 10  # Стоимость атаки
        damage = self.sila + self.agila + (self.attack if self.mana >= 1 and self.mana <= 20 else self.intelect)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар берсерка нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар берсерка полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар берсерка нанес вам {damage} урона."


class Dog_head(Monster):
    def __init__(self, name='Псоглавец', attack=41, hp=650,max_hp=800, mana=750):
        super().__init__(name)
        self.attack = attack
        self.max_hp = max_hp
        self.hp = hp
        self.mana = mana
        self.sila = 27  # cила влияет на на хп и урон
        self.agila = 19  # ловкость влияете на урон + крит удар
        self.intelect = 15  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар косой', 'Яростный укус', 'Оглушительный вой']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >= 500:
            damage = self.attack + self.agila
        else:
            damage = self.attack

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар косой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар косой полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар косой нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >= 250:
            damage = self.attack + self.sila
        else:
            damage = self.attack + self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный укус нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростный укус полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростный укус нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 25
        if self.mana >= 100:# Стоимость атаки
            damage = self.sila + self.intelect
        else:
            damage = self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Оглушительный вой нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Оглушительный вой полностью пробил ваш щит!"
        else:
            return f"{self.name} Оглушительный вой нанес вам {damage} урона."


class Rat_man(Monster):
    def __init__(self, name='Крысолюд', attack=45, hp=600,max_hp=700, mana=600):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 18  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 30  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Обстрел', 'Удар когтями', 'Яростные укусы']

    def attack_a(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >= 400:
            damage = self.attack + self.agila
        else:
            damage = self.attack


        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Обстрел нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Обстрел полностью пробил ваш щит!"
        else:
            return f"{self.name} Обстрел нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >= 150:
            damage = self.attack + self.sila
        else:
            damage = self.sila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар когтями нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар когтями полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар когтями нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 25  # Стоимость атаки
        if self.mana >= 25:
            damage = self.sila + self.agila
        else:
            damage = self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростные укус нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростные укус полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростные укус нанес вам {damage} урона."


class Troll(Monster):
    def __init__(self, name='Тролль', attack=49, hp=900,max_hp=900, mana=1200):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 58  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 15  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Удар дубиной', 'Пинок', 'Безумный удар']

    def attack_a(self, target):
        cost = 200  # Стоимость атаки
        if self.mana >=800:
            damage = self.attack + self.agila
        else:
            damage = self.agila

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар дубиной нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар дубиной полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар дубиной нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=500:
            damage = self.attack + self.sila
        else:
            damage = self.sila
        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Пинок нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Пинок полностью пробил ваш щит!"
        else:
            return f"{self.name} Пинок нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 100  # Стоимость атаки
        if self.mana >=100:
            damage = self.sila + self.agila
        else:
            damage = self.intelect

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Безумный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Безумный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Безумный удар нанес вам {damage} урона."
class God(Monster):
    def __init__(self, name='Богиня', attack=127, hp=70000,max_hp=70000, mana=46000):
        super().__init__(name)
        self.attack = attack
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.sila = 17  # cила влияет на на хп и урон
        self.agila = 25  # ловкость влияете на урон + крит удар
        self.intelect = 33  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = ['Вспышка', 'Божественный разлом', 'Анигиляция']

    def attack_a(self, target):
        cost = 2000  # Стоимость атаки
        damage = self.attack + (self.intelect if self.mana > 460 else 0)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Обстрел нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Обстрел полностью пробил ваш щит!"
        else:
            return f"{self.name} Обстрел нанес вам {damage} урона."

    def attack_b(self, target):
        cost = 1000  # Стоимость атаки
        damage = self.attack + (self.sila if 20 < self.mana < 41 else self.agila)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Проверка на щит и расчет урона
        initial_shield = target.shield

        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Яростный удар нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Яростный удар полностью пробил ваш щит!"
        else:
            return f"{self.name} Яростный удар нанес вам {damage} урона."

    def attack_c(self, target):
        cost = 800  # Стоимость атаки
        damage = self.sila + self.agila + (self.attack if self.mana >= 1 and self.mana <= 20 else self.intelect)

        # Обработка дебаффа "Уклонение"
        if 'Уклонение' in target.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            target.debuff.remove('Уклонение')  # Удаляем дебафф
            return f"{self.name} попытался атаковать, но вы уклонились!"

        # Обработка дебаффа "Яростный крик"
        if 'Яростный крик' in self.debuff:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            self.debuff.remove('Яростный крик')  # Убираем дебафф
            return f"{self.name} ошеломлен и не может атаковать!"

        # Если выше не сработало, продолжаем выполнение (щит и расчет урона)

        # Изначальное значение щита для формирования сообщения
        initial_shield = target.shield

        # Урон уменьшается за счет щита
        if target.shield > 0:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0

            if damage <= target.shield:
                target.shield -= damage
                remaining_damage = 0
            else:
                remaining_damage = damage - target.shield
                target.shield = 0
        else:
            if self.mana > 0:
                self.mana -= cost
            else:
                self.mana = 0
            remaining_damage = damage

        # Применяем оставшийся урон к HP
        target.hp -= remaining_damage

        # Формирование сообщений
        if initial_shield > 0:
            if target.shield > 0:
                return f"{self.name} Удар берсерка нанес вам {damage} урона. Щит поглотил часть урона."
            else:
                # Удаление дебаффов, связанных с щитами
                for debuff in ['Щит огня', 'Щит льда', 'Щит дракона']:
                    if debuff in target.debuff:
                        target.debuff.remove(debuff)
                return f"{self.name} Удар берсерка полностью пробил ваш щит!"
        else:
            return f"{self.name} Удар берсерка нанес вам {damage} урона."
