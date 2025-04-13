import random

from config import bot
class Player:
    def __init__(self,name):
        self.name = name
        self.money = 0

        # Изначальные характеристики
        self._sila = 5
        self._agila = 5
        self._intelect = 5
        self._luck = 5
        self._stamina = 5

        self.attack = 2 #базовы вернуть 2
        self.shield = 0

        # Зависимые параметры
        self.max_mana = int(20 + 5 * self._intelect)
        self.mana = self.max_mana

        self.max_hp = int(80 + 4 * self._stamina)
        self.hp = self.max_hp

        self.energy_max = 30
        self.energy = self.energy_max
        #Контейнеры
        #Зона активных предметов
        self.invetary =[] #инвентарь сюда добавляем предметы которые можно использовать
        self.abillity = [] #Текущие способности, заклинания, бафы и прочее
        self.use_hand = []  # Помещаем сюда основное оружие (на самом деле бесмыслено, наверно)
        # Технический контейнер для индификации класса игрока
        self.player_class =[] # Воин, Маг, Стрелок, Везунчик, во втором сезоне добавить ранги надо
        # ЗОНА ПРЕДМЕТОВ КВЕСТОВ И ДЛЯ ПРОДАЖи
        self.quest_invetary =[ ] # Контейнер с квестовыми предметами, которые можно продать
        self.quest = [] # помещаем предметы, которые продать нельзя
        self.debuff = []
        # Зона флагов и состояний
        # Квест флаги на линейки квестов
        self.goblin_flag = False #скрытый квест на логово гоблинов
        self.guild_visit= False #флаг посещения гильдии для рынка во втором сезоне надо сделать полноценный, а не костыль из флагов
        self.accept_goblin = False
        self.visit_wolf = False
        self.goblin_wait = 4
        self.wait_town = 3
        self.secret_room = False
        self.slaim = False
        self.slaim_complete = False
        self.help_solider = False
        self.goblin_complete = False
        self.two_quest = False
        self.commander = False




        self.one_boss = False
        self.two_boss = False
        self.tried_boss = False
        self.four_boss = False
        self.big_boss = False

        # Флаги после квеста слайм
        self.class_guild_visit = False # флаг проверяем, был ли игрок в гильдии своего класса
        #Квест на везунчика выяснить просихождения амулета
        self.group_foward = True

        #Флаги скрытых боссов
        # Флаги которые должны быть в True, что бы получить доступ к дракону зеленому
        self.slaim_see = False # меняется в первом квесте под городом
        self.library = False # игрок должен посетить библиотеку и выбрать книгу о драконе
        self.history = False
        self.green_dragon = False



        #Флаги на черного дракона
        self.book_dragon = False
        self.talk_commander = False

        self.black_dragon = False

        #флаги на красного дракона
        self.red_dragon = False
        #Флаги на золотого дракона
        self.gold_dragon = False


        # КОСТЫЛЬ БОЕВОЙ СИСТЕМЫ, ТУТ НУЖЕН СЛОВАРЬ ВСЕХ ВОЗМОЖНЫХ АТТАК ЧТО МОЖЕТ БЫТЬ У ИГРОКА
        # ВАЖНО! ПЕРЕСМОТРЕТЬ ВО ВТОРОМ СЕЗОНЕ
        self.system ={
            'action':{
            'Быстрый удар': self.fast_kick,
            'Выпад':self.charge, #Воин
            'Выстрел навскидку':self.speed_shot,
            'Меч-палка':self.start_sword,
            'Самодельный лук':self.start_bow,
            'Стрела огня': self.arrow_fire,
            'Ледяная стрела': self.ice_arrow,
            'Стальной кинжал': self.steel_knife,

            'Зелье здоровья':self.heal,
            'Большое зелье здоровья':self.big_heal,
            'Зелье маны':self.mana_pot,
            'Большое зелье маны':self.big_mana,
            'Усиленное зелье здоровья':self.great_hp,
            'Усиленное зелье маны':self.great_mana,
            'Героическое зелье здоровья':self.heroic_hp,
            'Героическое зелье маны':self.heroic_mana,

            'Рассечение': self.dissecting,
            'Взрывной удар': self.boom_blow,
            'Концентрация':self.constration,
            'Яростный крик':self.rage_screem,
            'Прицельный выстрел':self.aim_shot,
            'Уклонение':self.dodge,
            'Двойной выстрел':self.duble_shot,
            'Аура концентрации':self.aura_consetration,
            'Проникающий удар':self.penatration_blow,
            'Случайный удар':self.random_blow,
            'Аура':self.aura,
            'Неизвестная способность':self.unknow_abil,
            'Огненный шар':self.fire_ball,
            'Ледянные иглы':self.ice_ig,
            'Щит льда':self.ice_shield,
            'Щит огня':self.fire_shield,

            'Стабилизация':self.stabilizate,
            'Нестабильный удар':self.unstabile,

            'Магический выстрел':self.magic_shot,
            'Быстрая стрельба':self.rapid_fire,

            'Ледяной взрыв':self.ice_exploge,
            'Вытягивание маны':self.mana_drain,

            'Кровавый удар':self.blood_blow,
            'Быстрые удары':self.speed_blow,

            'Кристаллический лук':self.crystall_bow,
            'Магический посох':self.staff,
            'Ртутный кинжал':self.rtut_knife,
            'Меч волка':self.wolf_sword,

            'Метнуть кинжал':self.trhow_knife,

            'Ледяная буря':self.ice_bury,
            'Огненный шторм':self.fire_storm,

            'Вихрь':self.storm,

            'Град стрел':self.valley,
            #Скиллы дракона и драконида
            'Регенерация':self.regeneration,
            'Лечение':self.heal_regen,
            'Меч орка':self.orc_sword,
            'Щит дракона':self.dragon_shield,
            'Огненное дыхание':self.dragon_fire,
            'Удар дракона':self.kick_dragon,
            'Удар когтями':self.swap,

            # Финал блока



            'Меч демона':self.deamon_sword,

            'Лук генерала':self.bow_general,

            'Кинжал убийцы':self.knife_killer,

            'Лазурный посох':self.blue_staff,

            'Духовный выстрел':self.spirit_shot,
            'Духовный удар':self.spirit_blow,
            'Удар духа':self.spirit_kick,
            'Сжигание маны':self.mana_burn,


            'Меч генерала':self.sword_general,
            'Звездный лук':self.star_bow,
            'Посох утренней звезды':self.star_staff,
            'Обсидиановый кинжал':self.final_knife

        }}



        # Системные флаги для боевой системы трогать и модифицировать нельзя ВООБЩЕ НЕЛЬЗЯ ТРОГАТЬ!!!
        self.in_battle = False
        self.target = None
        self.last_battle_message = None
        self.on_battle_end = None  # Добавляем поле для коллбека
        self.messages = []



    def recalculate_stats(self):
        """Пересчёт зависимых параметров"""
        self.max_mana = self.max_mana = 20 + 5 * self._intelect
        self.max_hp = 80 + 4 * self._stamina
        self.energy_max = 30

    @property
    def sila(self):
        return self._sila

    @sila.setter
    def sila(self, value):
        self._sila = value
        self.recalculate_stats()

    @property
    def agila(self):
        return self._agila

    @agila.setter
    def agila(self, value):
        self._agila = value
        self.recalculate_stats()

    @property
    def intelect(self):
        return self._intelect

    @intelect.setter
    def intelect(self, value):
        self._intelect = value
        self.recalculate_stats()

    @property
    def luck(self):
        return self._luck

    @luck.setter
    def luck(self, value):
        self._luck = value
        self.recalculate_stats()

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = value
        self.recalculate_stats()

    # ВЫЗОВ СТАТИСИКИ ПЕРСОНАЖА
    def show_stat(self):
        stat= (f'Имя :{self.name}\n'
               f'Класс {', '.join(self.player_class) if self.player_class else 'Нет'}\n'
               f'Основное оружие: {', '.join(self.use_hand) if self.use_hand else 'Нет'}\n'
               f'Здоровье: {self.hp}|{self.max_hp}\n'
               f'Мана: {self.mana}|{self.max_mana}\n'
               f'Энергия: {self.energy}|{self.energy_max}\n'
               f'Деньги: {self.money}\n'
               '\n'
               f"Способности: {', '.join(self.abillity) if self.abillity else 'Нет'}\n"
               '\n'
               f'Сила: {self.sila}\n'
               f'Ловкость: {self.agila}\n'
               f'Интеллект: {self.intelect}\n'
               f'Удача: {self.luck}\n'
               f'СТАМИНА:{self.stamina}\n'
               '\n'
               f'Рюкзак: {', '.join(self.quest_invetary) if self.quest_invetary else 'Пусто'}\n'
               f"Карманы и сумки: {', '.join(self.invetary) if self.invetary else 'Пусто'}\n"
               f'Пояс: {', '.join(self.quest) if self.quest else 'Пусто'}\n'
               
               
               #f'Макс мана: {self.max_mana} отладочный параметр\n' #Временный отладочный параметр
               #f'Макс хп: {self.max_hp}отладочный праметр\n'
               #f'Макс эенергия: {self.energy_max} Отладочный параметр, не забыть убрать' #Временный отладочный параметр

               )
        return stat
# ЗОНА РАСЧЕТА И ОБРАБОТКИ ОРУЖИЯ И СПОСОБНОСТЕЙ
#КОСТЫЛЬ для реализации динамического боя
    #Функция заглушка, для закрытия ошибок


    # ОРУЖИЕ ДЛЯ ВОИНА
    def sword_general(self,target):
        if 'Поток' in self.debuff:
            damage = 125 * self.attack + 15  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.50)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч генерала нанёс {damage} урона. Восстановлено {energy}: Энергии'
        else:
            damage = 110 * self.attack   # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.40)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч генерала нанёс {damage} урона. Восстановлено {energy}: Энергии'
    def deamon_sword(self,target):
        if 'Поток' in self.debuff:
            damage = 75 * self.attack + 15  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.30)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч демона нанёс {damage} урона. Восстановлено {energy}: Энергии'
        else:
            damage = 75 * self.attack   # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.30)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч демона нанёс {damage} урона. Восстановлено {energy}: Энергии'
    def orc_sword(self,target):
        damage = 100+self.attack
        energy = int(self.energy_max * 0.20)
        mana = int(self.max_mana*0.20)
        target.hp -= damage
        self.energy = min(self.energy + energy, self.energy_max)
        self.mana = min(self.mana + mana, self.max_mana)
        return f'Вы нанесли удар мечом цель получила {damage} урона. Восстновлено {mana} маны и {energy} энергии'
    def wolf_sword(self,target):
        if 'Поток' in self.debuff:
            damage = 25 * self.attack + 5  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.35)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч волка нанёс {damage} урона. Восстановлено {energy}: Энергии'
        else:
            damage = 25 * self.attack  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.35)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Меч волка нанёс {damage} урона. Восстановлено {energy}: Энергии'
    def spirit_blow(self,target):
        coust = coust = int(self.energy_max * 0.55)
        mana_damge = self.sila
        damage = int(self.sila*0.25)
        if self.energy >= coust:
            target.mana -= mana_damge
            target.hp -= damage
            self.energy-=coust
            return f'Духовный удар нанес, урон мане врага {mana_damge} маны сожжено. {damage} урона получила цель'
        else:
            return f'Не хватило энергии, удар пропущен'
    def storm(self,target):
        damage = self.sila
        coust = int(self.energy_max * 0.55)
        if coust <= self.energy:
            if 'Поток' in self.debuff:
                super_damage = self.sila+self.sila+self.sila
                target.hp -= super_damage
                self.energy-=coust
                self.sila +=2
                return f'Вихрь нанес цели: {self.sila},{self.sila},{self.sila}  урона'
            else:
                target.hp -= damage
                self.energy -=coust
                self.sila += 1
                return f'Вихрь нанес цели: {damage} урона'
        else:
            return f'Вам не хватило энергии, удар пропущен'
    def blood_blow(self, target):
        damage = self.sila + 2
        coust = int(self.energy_max * 0.35)
        if coust <= self.energy:
            if 'Кровотечение' in target.debuff:
                damage_1 = damage + 10
                self.energy -= coust
                target.hp -= damage_1
                self.sila += 1
                return f'Кровавый удар нанес {damage_1} урона'
            else:
                self.energy -= coust
                target.hp -= damage
                self.sila += 1
                target.debuff.append('Кровотечение')
                return f'Кровавый удар, вызвал кровотечение, нанесено {damage} урона'
        else:
            return f'Вам не хватило энергии, удар пропущен'

    def speed_blow(self, target):
        damage_1 = self.sila - 10
        coust = int(self.energy_max * 0.75)
        if 'Поток' in self.debuff:
            damage = damage_1 + 5
            super_damage = damage + damage + damage

        else:
            damage = damage_1
            super_damage = damage + damage + damage

        if coust <= self.energy:
            self.energy -= coust
            target.hp -= super_damage
            self.sila += 1
            return f'Вы на несли {damage},{damage},{damage} урона тремя ударами'
        else:
            return f'Вам не хватило энергии, урон пропущен'

    def start_sword(self, target):
        if 'Поток' in self.debuff:
            damage = self.sila*self.attack+2  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.30)
            self.energy = min(self.energy + energy,self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Вы ударили деревяным мечом и нанесли {damage} урона. Восстановлено {energy}: Энергии'
        else:
            damage = self.sila * self.attack+3  # Урон мечом
            target.hp -= damage
            energy = int(self.energy_max * 0.30)
            self.energy = min(self.energy + energy, self.energy_max)
            print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
            return f'Вы ударили деревяным мечом и нанесли {damage} урона. Восстановлено {energy}: Энергии'

    def charge(self, target):
        base_damage = 20 + self.sila
        ener_coust = int(self.energy_max * (0.40 if 'Поток' in self.debuff else 0.43))

        # Увеличиваем урон, если "Поток" присутствует
        if 'Поток' in self.debuff:
            damage = base_damage + 5
        else:
            damage = base_damage

        if ener_coust <= self.energy:
            self.sila += 1
            target.hp -= damage
            self.energy -= ener_coust
            return (f'Вы сделали мощный выпад и нанесли: {damage} урона цели за: {ener_coust} энергии. '
                    f'Здоровье цели после атаки: {target.hp}')
        else:
            return 'Вам не хватило энергии на выпад, вы промахнулись выпадом и получили ответную атаку'
    def dissecting (self,target):
        base_damage = self.agila + 15+self.luck
        if 'Поток' in self.debuff:
            damage = base_damage+5
        else:
            damage = base_damage
        coust = int(self.energy_max * 0.43)
        if coust <= self.energy:
            self.agila += 1
            self.sila += 1
            target.hp -= damage
            self.energy -= coust
            return f'Нанесено {damage} цели. '
        else:
            return f'Не хватило энергии, пропущен удар'
    def boom_blow (self,target):
        base_damage = self.sila + 35
        coust = int(self.energy_max * 0.60)
        if 'Поток' in self.debuff:
            damage = base_damage + 5
        else:
            damage = base_damage
        if coust <= self.energy:
            self.sila += 2
            target.hp -= damage
            self.energy -= coust
            return f'Нанесено {damage} урона цели'
        else:
            return f'Не хватило энергии, пропущен удар'
    def constration (self,target):
        coust = int(self.energy_max * 0.70)
        if 'Поток' in self.debuff:
            return 'Вы в потоке, удар пропущен'
        if coust <= self.energy:
            self.debuff.append('Поток')
            self.energy -= coust
            return f'Вы вошли в поток'
        else:
            return f'Вы попытались сконцетрироватся, но вам не хватило энергии. Удар пропущенг'
    def rage_screem(self,target):
        coust = int(self.energy_max * 0.25)
        if coust <= self.energy:

            target.debuff.append('Яростный крик')
            self.energy -= coust
            return f'Противник ошеломлен от вашего крика'
        else:
            return f'Вам не хватило энергии на мощный крик'
    # ОРУЖИЕ ДЛЯ ЛУЧНИКА
    def star_bow(self,target):
        base_damage = 100 * self.attack
        if 'Концентрация' in self.debuff:
            damage = base_damage + 15
        else:
            damage = base_damage

        # Урон мечом
        target.hp -= damage
        energy = int(self.energy_max * 0.50)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Вы сделали выстрел и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def bow_general(self,target):
        base_damage = 70 * self.attack
        if 'Концентрация' in self.debuff:
            damage = base_damage + 15
        else:
            damage = base_damage

        # Урон мечом
        target.hp -= damage
        energy = int(self.energy_max * 0.35)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Вы сделали выстрел и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def crystall_bow(self,target):
        base_damage = 23 * self.attack
        if 'Концентрация' in self.debuff:
            damage = base_damage + 10
        else:
            damage = base_damage

        # Урон мечом
        target.hp -= damage
        energy = int(self.energy_max * 0.40)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Вы сделали выстрел и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def start_bow(self,target):
        base_damage = self.agila * self.attack
        if 'Концентрация' in self.debuff:
            damage = base_damage + 10
        else:
            damage = base_damage

        # Урон мечом
        target.hp -= damage
        energy = int(self.energy_max * 0.35)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Вы сделали выстрел и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def spirit_shot(self,target):
        coust = coust = int(self.energy_max * 0.50)
        mana_damge = self.agila
        damage = int(self.agila * 0.25)
        if self.energy >= coust:
            target.mana -= mana_damge
            target.hp -= damage
            self.energy -= coust
            return f'Духовный выстрел нанес, урон мане врага {mana_damge} маны сожжено. {damage} урона получила цель'
        else:
            return f'Не хватило энергии, удар пропущен'
    def speed_shot(self,target):
        base_damage = 25 + self.agila - self.luck
        ener_coust = int(self.energy_max * 0.33)
        if 'Концентрация' in self.debuff:
            damage = base_damage + 10
        else:
            damage = base_damage

        if ener_coust <= self.energy:
            self.agila += 1
            self.energy -=ener_coust
            target.hp -= damage
            return (
                f'Вы применили выстрел на вскидку и нанесли: {damage} урона цели за: {ener_coust} энергии. Здоровье цели после атаки: {target.hp}')
        else:
            return f'Вам не хватило энергии на выстрел на вскидку, вы промахнулись и получили ответную атаку'
    def aim_shot (self,target):
        base_damage = self.agila*2 +15
        coust = int(self.energy_max * 0.55)
        if 'Концентрация' in self.debuff:
            damage = base_damage+10
        else:
            damage = base_damage

        if coust <= self.energy:
            self.agila += 2
            self.energy -= coust
            target.hp -=damage
            return f'Прицельный выстрел нанес цели: {damage} урона. Потрачено: {coust} энергии. Здоровье цели: {target.hp}'
        else:
            return f'Вам не хватило энергии на прицельный выстрел, вы промахнулись и получили ответную атаку'
    def dodge (self,target):
        coust = int(self.energy_max * 0.35)
        if coust <= self.energy:

            self.debuff.append('Уклонение')
            self.energy -= coust
            return f'Вы попытались уклониться. Потрачено: {coust} энергии'
        else:
            return f'Вам не хватило энергии для уклонения, противник по вам попал'
    def duble_shot(self,target):
        coust = int(self.energy_max * 1)
        base_damage = (self.agila * 2)+(2*self.agila)+2
        if 'Концентрация' in self.debuff:
            damage = base_damage + 15
        else:
            damage = base_damage

        if coust <= self.energy:

            self.energy -= coust
            target.hp -= damage
            self.agila +=1
            return f'Вы нанесли двойным выстрелом: {damage} урона. Затрачено {coust} энергии'
        else:
            return f'Вам не хватило энергии на двойной выстрел, урон пропустили удар'

    def magic_shot (self,target):
        coust = int(self.max_mana*0.20)
        base_damage = self.mana
        if 'Концентрация' in self.debuff:
            damage = base_damage + 10
        else:
            damage = base_damage
        if coust <= self.mana:
            self.intelect +=1
            target.hp -= damage
            self.mana -= coust
            return f'Вы нанесли {damage} урона магической стрелой'
        else:
            return f'Вам не хватило энергии, удар пропущен'


    def rapid_fire(self,target):
        coust = int(self.energy_max*0.50)
        base_damage = self.agila-15
        if 'Концентрация' in self.debuff:
            damage = base_damage+5
            combo = damage+damage+damage+damage
        else:
            damage = base_damage
            combo = damage + damage + damage + damage
        if coust <= self.energy:
            target.hp -= combo
            self.energy -= coust
            self.agila +=2
            return f'Вы нанесли 4 выстрела, нанесено {damage}, {damage}, {damage}, {damage} урона'
        else:
            return f'Вам не хватило энергии на выстрел, удар пропущен'
    def aura_consetration (self,target):
        coust = int(self.energy_max * 0.70)
        if 'Концентрация' in self.debuff:
            return 'Аура действует, вы получили урон от врага'
        if coust <= self.energy:
            self.debuff.append('Концентрация')
            self.energy -= coust
            return f'Вы наложили на себя ауру Концентрации, потрачено {coust} энергии'
        else:
            return f'Вам не хватило энергии. Удар от противника пропущен'
    def valley(self,target):
        coust = int(self.energy_max * 0.85)
        base_damage = self.agila
        if 'Концентрация' in self.debuff:
            damage = base_damage + 15
            combo = damage + damage + damage + damage
        else:
            damage = base_damage
            combo = damage + damage + damage + damage
        if coust <= self.energy:
            target.hp -= combo
            self.energy -= coust
            self.agila += 2
            return f'Град стрел обрушился на врага, нанесено {damage}, {damage}, {damage}, {damage} урона'
        else:
            return f'Вам не хватило энергии на выстрел, удар пропущен'
    # ОРУЖИЕ И ЗАКЛИНАНИЯ ДЛЯ МАГА
    def star_staff(self,target):
        base_damage = self.intelect * 2 + 20
        damage = base_damage

        # Урон посохом
        target.hp -= damage
        mana = int(self.max_mana * 0.35)
        self.mana = min(self.mana + mana, self.max_mana)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Применив посох вы нанесли {damage} урона. Восстановлено {mana}: Маны'
    def blue_staff(self,target):
        base_damage = self.intelect*2+self.attack
        damage = base_damage

        # Урон посохом
        target.hp -= damage
        mana = int(self.max_mana * 0.20)
        self.mana = min(self.mana + mana, self.max_mana)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Применив посох вы нанесли {damage} урона. Восстановлено {mana}: Маны'
    def staff(self,target):
        base_damage = self.intelect+self.attack
        damage = base_damage

        # Урон посохом
        target.hp -= damage
        mana = int(self.max_mana * 0.25)
        self.mana = min(self.mana + mana, self.max_mana)
        print(f"{self.name} наносит {damage} урона. Здоровье цели после атаки: {target.hp}")
        return f'Применив посох вы нанесли {damage} урона. Восстановлено {mana}: Маны'
    def mana_burn(self,target):
        coust = coust = int(self.max_mana * 0.50)
        mana_damge = self.intelect
        damage = int(self.intelect * 0.25)
        if self.mana >= coust:
            target.mana -= mana_damge
            target.hp -= damage
            self.mana -= coust
            return f'Сжигание маны нанесло, урон мане врага {mana_damge} маны сожжено. {damage} урона получила цель'
        else:
            return f'Не хватило энергии, удар пропущен'
    def arrow_fire(self,target):
        damage = int(self.intelect*1)+15  # Урон стрелой
        mana_coust = int(self.max_mana*0.35)
        if self.mana >= mana_coust:
            if 'Щит огня' in self.debuff:
                super_damage = damage + 5
                target.hp -= super_damage
                self.mana -= mana_coust
                return f'Вы нанесли {super_damage} урона цели'
            else:
                target.hp -= damage
                self.intelect +=1
                self.mana -= mana_coust

                return f'Вы нанесли огненной стрелой {damage} урона, потратив {mana_coust} маны'
        else:

            mana_amount = int(self.max_mana*0.75)
            self.mana = min(self.mana + mana_amount, self.max_mana)

            return f'Недостаточно маны, удар от монстра пропущен, вы восстановили {mana_amount} маны'
    def fire_storm(self,target):
        damage = self.intelect * 3 + 25 # Урон стрелой
        mana_coust = int(self.max_mana*0.70)
        if self.mana >= mana_coust:
            if 'Щит огня' in self.debuff:
                super_damage = damage + 15
                target.hp -= super_damage
                self.intelect += 2
                self.mana -= mana_coust
                return f'Огненный шторм нанес {super_damage} урона цели'
            elif 'Горение' in target.debuff:
                super_damage = damage + 35
                target.hp -= super_damage
                self.intelect += 1
                self.mana -= mana_coust
                return f'Огненный шторм усилил горение и нанес {super_damage} урона цели'
            else:
                target.hp -= damage
                self.intelect +=1
                self.mana -= mana_coust

                return f'Вы нанесли огненной стрелой {damage} урона, потратив {mana_coust} маны'
        else:

            mana_amount = int(self.max_mana*0.75)
            self.mana = min(self.mana + mana_amount, self.max_mana)

            return f'Недостаточно маны, удар от монстра пропущен, вы восстановили {mana_amount} маны'

    def ice_arrow(self,target):
        damage = int(self.intelect*0.80)+20  # Урон мечом
        mana_coust = int(self.max_mana*0.25)
        if self.mana >= mana_coust:
            if 'Щит льда' in self.debuff:
                super_damage = damage + 5
                target.hp -= super_damage
                self.mana -= mana_coust
                self.intelect += 2
                return f'Вы нанесли {super_damage} урона цели'
            else:
                target.hp -= damage
                self.intelect += 1
                self.mana -= mana_coust

                return f'Вы нанесли ледяной стрелой {damage} урона, потратив {mana_coust} маны'
        else:
            mana_amount = int(self.max_mana*0.75)
            self.mana = min(self.mana + mana_amount, self.max_mana)

            return f'Недостаточно маны, удар от монстра пропущен, вы восстановили {mana_amount} маны'

    def ice_exploge(self,target): #Награда за кв по слизям
        damage = self.intelect+self.luck+15
        coust = int(self.max_mana*0.35)
        if self.mana >= coust:
            if 'Горение' in target.debuff:
                super_damage = damage + 45
                target.hp -= super_damage
                target.debuff.remove('Горение')
                self.mana -= coust
                self.intelect += 1
                return f'Быстрое охлаждение создало парвой взрыв и нанесло {super_damage} урона'
            else:
                target.hp -= damage
                self.mana -= coust
                self.intelect += 1
                return f'Ледяной взрыв нанес цели {damage} урона'
        else:
            mana_amount = int(self.max_mana * 0.35)
            self.mana = min(self.mana + mana_amount, self.max_mana)

            return f'Недостаточно маны, удар от монстра пропущен, вы восстановили {mana_amount} маны'

    def mana_drain(self, target): # награда за кв по слизям
        damage = int(target.mana * 0.25)
        damage_2 = int(self.intelect * 0.10)
        cost = int(self.intelect * 0.15)

        if target.mana > 0:
            # Сохраняем исходное значение маны цели
            original_mana = target.mana

            # Уменьшаем ману цели
            target.mana -= damage
            if target.mana < 0:
                target.mana = 0  # Ограничиваем ману цели до 0

            # Высчитываем реальный урон по мане, если цель имела меньше маны, чем ожидалось
            actual_damage = original_mana - target.mana

            # Обновляем параметры игрока
            self.intelect += 1
            self.mana -= cost
            self.mana += damage
            target.hp -= damage_2

            return f'Вы высосали {actual_damage} маны у цели и нанесли {damage_2} урона'
        else:
            return f'У цели нет маны, удар пропущен'



    def fire_ball(self, target):
        coust = int(self.max_mana * 0.38)  # Расход маны
        base_damage = self.intelect + 30  # Базовый урон

        if coust <= self.mana:  # Хватает ли энергии для атаки
            # Урон увеличивается, если цель уже горит
            additional_damage = 25 if 'Горение' in target.debuff else 0
            damage = base_damage + additional_damage

            target.hp -= damage  # Применяем урон к цели
            self.mana -= coust  # Уменьшаем энергию
            self.intelect += 1  # Увеличиваем интеллект
            if 'Горение' not in target.debuff:
                target.debuff.append('Горение')  # Добавляем дебафф "Горение"

            # Сообщение об успешной атаке
            return (f'Вы нанесли цели {damage} урона. '
                    f'{"10 дополнительного урона за горение." if additional_damage else "Цель горит."}')
        else:
            # Восстановление маны при недостатке энергии
            restored_mana = int(self.max_mana*0.75)
            self.mana += restored_mana
            return f'Вам не хватило маны, удар пропущен. Восстановлено {restored_mana} маны.'

    def ice_ig (self,target):
        coust = int(self.max_mana*0.27)
        damage = self.intelect + 20
        if coust <= self.mana:
            if 'Щит льда' in self.debuff:
                super_damage = damage + 5
                target.hp -= super_damage
                self.mana -= coust
                self.intelect +=2
                return f'Вы нанесли {super_damage} урона цели'
            else:
                target.hp -= damage
                self.mana -= coust
                self.intelect += 1
                return f'Вы нанесли {damage} урона цели'
        else:
            mana_amount = int(self.max_mana*0.75)
            self.mana = min(self.mana + mana_amount, self.max_mana)
            return f'Вам не хватило маны, восстановлено {mana_amount} маны'

    def ice_shield (self,target):
        coust = int(self.max_mana*0.30)
        shield = int(self.intelect*1.5)
        if coust <=self.mana:
            self.debuff.append('Щит льда')
            self.shield += shield
            self.mana -= coust
            return f'Вы наложили на себя щит, поглощающий {shield} урона'
        else:
            mana_amount = coust
            self.mana = min(self.mana + mana_amount, self.max_mana)
            return f'Вам не хватило маны, восстановлено {coust} маны'
    def fire_shield (self,target):
        coust = int(self.max_mana*0.30)
        shield = self.intelect*2
        if coust <= self.mana:
            self.debuff.append('Щит огня')
            self.shield += shield
            self.mana -= coust
            return f'Вы наложили на себя щит, поглощающий {shield} урона'
        else:
            mana_amount = coust
            self.mana = min(self.mana + mana_amount, self.max_mana)
            return f'Вам не хватило маны, восстановлено {coust} маны'
    def ice_bury (self,target):
        coust = int(self.max_mana*0.50)
        damage = self.intelect + 30
        if coust <= self.mana:
            if 'Щит льда' in self.debuff:
                super_damage = damage + 25
                target.hp -= super_damage
                self.mana -= coust
                self.intelect +=2
                return f'Вы нанесли {super_damage} урона цели'
            else:
                target.hp -= damage
                self.mana -= coust
                self.intelect += 1
                return f'Вы нанесли {damage} урона цели'
        else:
            mana_amount = int(self.max_mana*0.75)
            self.mana = min(self.mana + mana_amount, self.max_mana)
            return f'Вам не хватило маны, восстановлено {mana_amount} маны'
    # ОРУЖИЕ ДЛЯ ВЕЗУНЧИКА(полу вор, следопыт, шпион)
    def final_knife(self,target):
        damage = 130 * self.attack + self.luck  # Урон кинжалом
        target.hp -= damage
        energy = int(self.energy_max * 0.40)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. HP цели после атаки: {target.hp}")
        return f'Вы ударили кинжалом и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def knife_killer(self,target):
        damage = 65 * self.attack + self.luck  # Урон кинжалом
        target.hp -= damage
        energy = int(self.energy_max * 0.25)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. HP цели после атаки: {target.hp}")
        return f'Вы ударили кинжалом и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def rtut_knife(self,target):
        damage = 28 * self.attack + self.luck  # Урон кинжалом
        target.hp -= damage
        energy = int(self.energy_max * 0.30)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. HP цели после атаки: {target.hp}")
        return f'Вы ударили кинжалом и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def steel_knife(self,target):
        damage = self.agila * self.attack + self.luck  # Урон кинжалом
        target.hp -= damage
        self.agila+=1
        energy = int(self.energy_max * 0.25)
        self.energy = min(self.energy + energy, self.energy_max)
        print(f"{self.name} наносит {damage} урона. HP цели после атаки: {target.hp}")
        return f'Вы ударили кинжалом и нанесли {damage} урона. Восстановлено {energy}: Энергии'
    def fast_kick(self,target):
        damage = 13 + self.agila+self.luck
        ener_coust = int(self.energy_max*0.50)
        if ener_coust <= self.energy:
            self.luck += 1
            self.energy -=ener_coust
            target.hp -= damage
            return (
                f'Вы сделали быстрый удар по цели и нанесли: {damage} урона цели за: {ener_coust} энергии. Здоровье цели после атаки: {target.hp}')
        else:
            return f'Вам не хватило энергии на удар, вы промахнулись выпадом и получили ответную атаку'

    def penatration_blow (self, target):
        coust = int(self.energy_max*0.50)
        damage = self.luck+self.agila
        if coust <= self.energy:
            self.luck +=1
            self.agila +=1
            target.hp -= damage
            self.energy -= coust
            return f'Вы нанесли цели {damage} урона. Потрачено {coust} энергии'
        else:
            return f'Вам не хватило энергии, удар пропущен'

    def random_blow(self, target):
        coust = int(self.energy_max*0.50)
        base_damage = self.luck + 35  # Базовый урон
        variation = random.randint(-int(base_damage * 0.1), int(base_damage * 0.1))  # Разброс ±10%
        damage = base_damage + variation  # Итоговый урон с учетом разброса

        if coust <= self.energy:
            self.luck += 1
            self.agila += 1  # Увеличиваем удачу
            target.hp -= damage
            self.energy -= coust
            return (f'Вы нанесли цели {damage} урона (разброс: {variation:+}). '
                    f'Потрачено {coust} энергии')
        else:
            return f'Вам не хватило энергии. Удар пропущен'
    def aura(self,target):
        coust = int(self.energy_max*0.50)
        if coust <= self.energy:
            self.energy -= coust
            self.debuff.append('Аура')
            return f'Вы наложили на себя ауру'
        else:
            return f'Не хватило энергии на ауру'
    def unknow_abil (self,target):
        coust = int(self.energy_max*0.50)
        damage = self.luck+self.agila + 20
        if coust <=self.energy:
            if 'Неизвестность' in self.debuff:
                self.energy -= coust
                target.hp -= damage
                self.agila += 2
                self.luck +=1
                return f'Вы нанесли {damage} урона цели'
            else:
                self.energy -= coust
                return f'Ничего не произошло. Потрачено {coust} энергии'
        else:
            return f'Вам не хватило энергии'
    def stabilizate(self,target):
        coust = int(self.energy_max*0.25)
        if coust <= self.energy:
            self.debuff.append('Неизвестность')
            self.energy -= coust
            return f'Вы наложили на себя ауру неизвестности'
        else:
            return f'Вам не хватило энергии, удар пропущен'
    def unstabile(self,target):
        damage = self.luck+self.agila+25
        coust = int(self.energy_max*0.25)
        if coust <= self.energy:
            if "Аура" in self.debuff:
                target.hp -= damage
                self.agila +=2
                self.luck +=2
                self.energy -= coust
                return f'Нанесен нестабильный удар, стабилизированный аурой, нанесено {damage} урона'
            else:
                min_damage = int(damage*0.55)
                self.luck +=1
                target.hp -= min_damage
                self.energy -=coust
                return f'Нанесен нестабильный удар. Нанесено {min_damage} урона'
        else:
            return f'Нехватило энергии, удар пропущен'
    def spirit_kick(self,target):
        coust = coust = int(self.energy_max * 0.45)
        mana_damge = self.luck
        damage = int(self.luck * 0.25)
        if self.energy >= coust:
            target.mana -= mana_damge
            target.hp -= damage
            self.energy -= coust
            return f'Удар духа нанес, урон мане врага {mana_damge} маны сожжено. {damage} урона получила цель'
        else:
            return f'Не хватило энергии, удар пропущен'
    def trhow_knife(self,target):
        damage = self.luck+25+self.sila
        coust = int(self.max_mana*50)
        if coust <= self.energy:
            if "Аура" in self.debuff:
                super_damage = damage + 10
                target.hp -= super_damage
                self.agila +=2
                self.luck +=2
                self.mana -= coust
                return f'Вы метнули кинжал нанесено: {super_damage} урона. Затрачено маны: {coust}'
            else:

                target -= damage
                self.energy -=coust
                return f'Вы метнули кинжал нанесено: {damage} урона. Затрачена маны {coust}'
        else:
            return f'Нехватило энергии, удар пропущен'

    # Применение ЗЕЛЕЙ И АРТЕФАКТОВ
    def great_hp(self, target):
        if self.hp >= self.max_hp:
            return "Ваше здоровье полное, ход пропущен"
        else:
            heal_amount = 450
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.invetary.remove('Усиленное зелье здоровья')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.hp}/{self.max_hp}."
    def heal(self,target):
        if self.hp >= self.max_hp:
            return "Ваше здоровье полное, ход пропущен"
        else:
            heal_amount = 75
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.invetary.remove('Зелье здоровья')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.hp}/{self.max_hp}."
    def big_heal(self,target):
        if self.hp >= self.max_hp:
            return "Ваше здоровье полное, ход пропущен"
        else:
            heal_amount = 145
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.invetary.remove('Большое зелье здоровья')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.hp}/{self.max_hp}."
    def great_mana(self,target):
        if self.mana >= self.max_mana:
            return 'Мана полная, ход пропущен'
        else:
            mana_amount = 400
            self.mana = min(self.mana + mana_amount, self.max_mana)
            self.invetary.remove('Усиленное зелье маны')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.mana}/{self.max_mana}."

    def mana_pot(self,target):
        if self.mana >= self.max_mana:
            return 'Мана полная, ход пропущен'
        else:
            mana_amount = 70
            self.mana = min(self.mana + mana_amount, self.max_mana)
            self.invetary.remove('Зелье маны')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.mana}/{self.max_mana}."
    def big_mana(self,target):
        if self.mana >= self.max_mana:
            return 'Мана полная, ход пропущен'
        else:
            mana_amount = 140
            self.mana = min(self.mana + mana_amount, self.max_mana)
            self.invetary.remove('Большое зелье маны')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.mana}/{self.max_mana}."

    def heroic_hp(self, target):
        if self.hp >= self.max_hp:
            return "Ваше здоровье полное, ход пропущен"
        else:
            heal_amount = 500
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.invetary.remove('Героическое зелье здоровья')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.hp}/{self.max_hp}."

    def heroic_mana(self, target):
        if self.mana >= self.max_mana:
            return 'Мана полная, ход пропущен'
        else:
            mana_amount = 500
            self.mana = min(self.mana + mana_amount, self.max_mana)
            self.invetary.remove('Героическое зелье маны')
            return f"Вы выпили зелье и восстановили здоровье. Ваше текущее HP: {self.mana}/{self.max_mana}."
# Cпособности дракона и драконида
    def regeneration(self,target):
        coust = (self.max_mana*1)
        regen = (self.max_hp*1)
        if self.mana >= coust:
            self.hp = min(self.hp+regen,self.max_hp)
            return f'Вы применили драконью регенрацию здоровье восстановленно полностью, потрачено: {coust} маны'
        else:
            return f'Не хватило маны, ход пропущен'
    def heal_regen(self,target):
        coust = (self.energy_max * 1)
        regen = (self.max_hp * 1)
        if self.energy >= coust:
            self.hp = min(self.hp + regen, self.max_hp)
            return f'Вы применили драконье лечение, здоровье восстановленно полностью, потрачено: {coust} Энергии'
        else:
            return f'Не хватило энергии , ход пропущен'

    def dragon_shield(self, target):
        coust = int(self.max_mana * 0.40)
        en_coust = int(self.energy_max * 0.40)
        shield = 150 + self.stamina

        if self.mana >= coust and self.energy >= en_coust:
            # Проверяем и удаляем щиты, если они есть
            if 'Щит льда' in self.debuff:
                self.debuff.remove('Щит льда')
            if 'Щит огня' in self.debuff:
                self.debuff.remove('Щит огня')

            # Накладываем щит дракона
            self.debuff.append('Щит дракона')
            self.shield += shield
            self.mana -= coust
            self.energy -= en_coust

            return f'Вы наложили на себя щит дракона, поглощающий {shield} урона'
        else:
            return f'Вам не хватило ресурсов, удар пропущен'

    def dragon_fire(self,target):
        coust = int(self.max_mana*0.25)
        damage = self.stamina+120
        if self.mana >= coust:
            target.hp-= damage
            self.mana -=coust
            return f'Огненное дыхание нанесло {damage} урона, потрачено {coust} маны'
        else:
            return 'Вам не хватило маны, удар пропущен'
    def kick_dragon(self,target):
        coust = int(self.energy_max*0.25)
        damage = self.stamina *4
        if self.energy >= coust:
            target.hp -= damage
            self.energy -=coust
            return f'Удар дракона нанес {damage} урона цели, потрачено {coust} энергии'
        else:
            return 'Вам не хватило энергии, удар пропущен'
    def swap (self,target):
        damage = 450
        energy = int(self.energy_max * 0.25)
        mana = int(self.max_mana*0.25)
        target.hp -= damage
        self.energy = min(self.energy + energy, self.energy_max)
        self.mana = min(self.mana + mana, self.max_mana)
        return f'Удар когтями нанес {damage} урона. Восстновлено {mana} маны и {energy} энергии'