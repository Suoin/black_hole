from scenario_3 import *

#АКТ 3 ЗОЛОТОЙ ДРАКОН + ТРЕТИЙ ГЕНЕРАЛ ХЕНИУС
def two_general_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('После сообщения о смерти генерала. Армия монстров  начала сдаваться, теже кто отказался от сдачи. Были убиты.\n'
            'Спустившись во двор, часть солдат охраняли монстров, часть искала ценности. Остаться и участвовать в казне или поискать ценности?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Казнь монстров','callback_data':'exucute'},{'text':'Грабеж цитадели','callback_data':'maroder'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def two_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'exucute':
        # Текст для сценария казни
        text = (
            'Вы лично отправили на тот свет около пятидесяти монстров, прежде чем последние из них пали. Тела врагов собрали в огромный костер и подожгли. '
            'К вечеру прозвучал приказ о сборе армии — впереди предстоял марш к следующему замку.'
        )
    else:
        # Текст для сценария осмотра замка
        text = ('Вы обыскали замок и прилегающие здания. '
                'Ваши поиски увенчались успехом: удалось найти несколько зелий и оружие, способное заменить изношенное снаряжение.'
                'К вечеру прозвучал приказ о сборе — армия готовилась к маршу к следующему замку врага.' )

        # Добавление зелий в инвентарь
        player[chat_id].invetary.extend(
            ['Усиленное зелье здоровья', 'Усиленное зелье маны'])
        # Карта классов и оружия
        weapon_mapping = {
            'Маг': 'Посох утренней звезды',
            'Воин': 'Меч генерала',
            'Стрелок': 'Звездный лук',
            'Везунчик': 'Обсидиановый кинжал'
        }

        # Назначение оружия в зависимости от класса игрока
        for class_name, weapon in weapon_mapping.items():
            if class_name in player[chat_id].player_class:
                player[chat_id].use_hand.clear()
                player[chat_id].use_hand.append(weapon)
                break
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'Сбор','callback_data':'tri_go_army'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_go_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text =('После сбора армии, выстроившейся в походные ряды, командир объявил, что город, где планировалось пополнить запасы, захвачен монстрами.'
           ' Армии предстояло выступить немедленно, чтобы отбить его.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Марш','callback_data':'tri_town'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Несколько дней армия продвигалась к городу, и вот наконец за горизонтом показались его стены. '
            'На них были вывешены тела людей, а на пиках, возвышающихся над воротами, торчали отрубленные головы. '
            'Постройка осадного лагеря заняла почти целый день. '
            'Командир отдал приказ: сформировать разведывательный отряд для проникновения в город, а основные силы подготовить к штурму.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Основные силы','callback_data':'town_siege'},{'text':'Развед отряд','callback_data':'sso'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def sso(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы присоединились к разведывательному отряду. Перед рассветом, в тишине, группа спустилась в канализационные туннели, ведущие вглубь города. '
            'Запах сырости и тлена сопровождал вас на каждом шагу, пока вы пробирались вперед, надеясь остаться незамеченными.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Идти вперед', 'callback_data': 'tunnel_go'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tunnel_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Продвигаясь по зловонным туннелям, ваш отряд внезапно столкнулся с группой крысолюдей. '
            'Эти твари, вооружённые ржавыми клинками и покрытые грязью, бдительно патрулировали местность, издавая шипящие звуки.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'tunnel_fight'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tunnel_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Rat_man()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        tunnel_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def tunnel_fight_win(chat_id):
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
            [{'text': 'Ожидать своих', 'callback_data': 'tunnel_fight_final'} ]
        ]}
        bot.sendMessage(chat_id, 'Разделавшись с отрядом крысолюдей, вы выбрались на поверхность и начали наносить удары по врагу. '
                                 'Ваш отряд ловко расправлялся с подкреплениями, спешащими к городским стенам. '
                                 'Нападая с разных сторон, вы сеяли хаос, отвлекая силы противника, в ожидании момента, когда основные войска прорвутся внутрь города.',
                        reply_markup=keyboard)
def town_siege(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('С первыми лучами солнца прозвучал приказ к штурму. Катапульты начали громить стены, одна за другой создавая проломы. '
            'Осадные башни медленно двинулись вперед, укрывая солдат от стрел врага. '
            'Штурмовые лестницы взметнулись к стенам, а бойцы ринулись в атаку, невзирая на град стрел и камней, обрушивающихся сверху. ')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В брешь', 'callback_data': 'wall_hole'},{'text':'На лестницы','callback_data':'siege_death'}],
            [{'text':'На башню','callback_data':'siege_tower'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def siege_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Сквозь град стрел вы с штурмовой группой прорвались к стенам, потеряв нескольких бойцов. '
            'Установив лестницу под непрерывным огнем врага, вы приготовились к подъему наверх, чтобы вступить в схватку за стены города. ')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Подниматься по лестнице', 'callback_data': 'siege_death_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def siege_death_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Взбираясь по лестнице, вы вдруг ощутили, как жар начинает становиться невыносимым. '
            'Слышен был грохот, и в следующий момент огромная масса раскаленной смолы обрушилась на вас, обжигая все на своем пути.')
    bot.sendMessage(chat_id, text)
    kill(chat_id)
    save_players()
def wall_hole(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Прорвавшись через брешь в стене, вы оказались лицом к лицу с новой преградой — стеной из монстров. Лица врагов были наполнены яростью и ненавистью. '
           'Вы выбрали свою цель, вцепились в оружие и вступили в бой, не думая о том, что может произойти дальше.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'wall_hole_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def wall_hole_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        wall_hole_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def wall_hole_a_win(chat_id):
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
            [{'text': 'Следующий монстр', 'callback_data': 'wall_hole_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Всюду падали тела ваших союзников и монстров, слышался лязг металла о металл, убив свою цель, вы нашли следующую',
                        reply_markup=keyboard)
def wall_hole_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        wall_hole_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def wall_hole_b_win(chat_id):
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
            [{'text': 'Добить остатки', 'callback_data': 'wall_hole_c'} ]
        ]}
        bot.sendMessage(chat_id, 'Силы монстров значительно поредели. В их рядах остались лишь самые отчаянные, а ваши бойцы чувствуют, что победа уже близка.',
                        reply_markup=keyboard)
def wall_hole_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        wall_hole_c_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def wall_hole_c_win(chat_id):
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
            [{'text': 'Сбор на площади', 'callback_data': 'wall_hole_e'} ]
        ]}
        bot.sendMessage(chat_id, 'Монстры начали отступать вглубь города, оставив последние позиции. '
                                 'Те, кто еще сражались, были уничтожены отрядом и частью армии, что уже захватили стены. '
                                 'Командир отдал приказ собраться на центральной площади ',
                        reply_markup=keyboard)
def siege_tower(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы присоединились к отряду с осадными башнями. Под шквалом огненных стрел и заклинаний вам удалось сохранить свою башню и дотащить её к стенам. '
            'Будучи в числе первых, вы ринулись на стену, как только открылся помост. ')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data':'siege_tower_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def siege_tower_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Rat_man()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        siege_tower_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def siege_tower_a_win(chat_id):
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
            [{'text': 'Еще одна тварь', 'callback_data': 'siege_tower_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы убили первого крысюка лучника, как заметили тварь с арбалетом и поспешили ее убить',
                        reply_markup=keyboard)
def siege_tower_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Rat_man()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        siege_tower_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def siege_tower_b_win(chat_id):
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
            [{'text': 'Стены почти наши', 'callback_data': 'siege_tower_c'} ]
        ]}
        bot.sendMessage(chat_id, 'К стенам приближались ещё башни, из которых выбегали союзники. '
                                 'Силы монстров начали таять, их ряды редели, и вот уже почти, стены будут наши. '
                                 'Оставалось лишь нанести последний удар, чтобы окончательно сломить сопротивление врага.',
                        reply_markup=keyboard)
def siege_tower_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Rat_man()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        siege_tower_c_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def siege_tower_c_win(chat_id):
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
            [{'text': 'Добить отступающих', 'callback_data': 'wall_hole_e'} ]
        ]}
        bot.sendMessage(chat_id, 'Стены были захвачены, отдан приказ добить отступающих монстров с верху, после чего следовать к центральной площади',
                        reply_markup=keyboard)




def central_squer(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'tunnel_fight_final':
        text =(' Выбравшись из туннеля, вы уничтожили все отряды монстров, что двигались к стенам. '
               'После этого вы изменили дислокацию. Вдруг заметили, как часть стены обрушилась, а на её вершине появились осадные башни, открывающие помосты. '
               'Ваши силы начали давить, и монстры начали отступать. В этот момент ваш отряд наносил удары по врагу, стягиваясь к центру города.')
    else:
        text = 'Вы продвигались к центру города, натыкаясь на остатки сил и раненых монстров, что не добил отряд, который проник ранее, наконец вы достигли центра'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'На площадь', 'callback_data': 'central_squer_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def central_squer_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text =('Собравшись на центральной площади, командиры отрядов отдавали указы. '
           'Вам предложили выбрать: участвовать в зачистке города или отдохнуть перед следующими боями.'
           )
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдых', 'callback_data': 'tri_restore'},{'text':'На зачистку','callback_data':'tri_kill_town'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_kill_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    save_players()
    text =('Не успев отдохнув и с ранениями вы отправились с одной из групп на зачистку. '
           'В узких переулках вам встретился растерянный тролль, который, заметив вас, немедленно рванул в вашу сторону.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'tri_kill_town_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_kill_town_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Troll()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        tri_kill_town_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def tri_kill_town_a_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].quest.append('Записки золотого дракона')
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Отдых', 'callback_data': 'tri_restore'} ]
        ]}
        bot.sendMessage(chat_id, 'Победив тролля, вы заметили, что в его броне скрывался странный свиток с названием "Записки золотого дракона". '
                                 'Это был небольшой свиток, который рассказывал о золотом драконе, упоминая, '
                                 'что они иногда проникают в человеческие или монстрические общества, скрывая свою истинную сущность.',
                        reply_markup=keyboard)
def tri_restore(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия занялась укреплением города, выставлением патрулей и очисткой улиц от монстров. Найденные тела погибших людей предали земле.'
            'Несколько дней вы были предоставлены сами себе.')
    restore(chat_id)
    save_players()
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Сжигать тела монстров', 'callback_data': 'monster_burn'},
             {'text': 'Изучить город', 'callback_data': 'tri_research_town'}],
            [{'text':'Хоронить людей','callback_data':'grabe_people'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_research_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Пока все были заняты своими делами, вы решили немного отвлечься и осмотреть город. '
           'На горизонте виднелся замок лорда, но по пути ваш взгляд упал на старый указатель с надписью "Библиотека". '
           'Что выбрать: исследовать ее тайны, пойти к замку или позволить себе заслуженный отдых на несколько дней?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В библиотеку','callback_data':'library_tri'},{'text':'Отдыхать','callback_data':'tri_restore_c'}],
            [{'text':'К замку','callback_data':'castle_tri'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def library_tri(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы направились в библиотеку, но внутри вас ждало разочарование: почти все книги были уничтожены или безвозвратно повреждены. '
            'Целый день ушел на изучение обломков знаний прошлого, и лишь когда солнце стало скрываться за горизонтом, вы осознали, как быстро прошло время.'
            'Пора возвращаться в лагерь.')
    keyboard = {'inline_keyboard': [
        [{'text': 'Отдых', 'callback_data': 'tri_restore_c'}]
    ]}
    bot.sendMessage(chat_id,text,reply_markup=keyboard)


def castle_tri(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы вошли в разрушенный замок, следы недавней битвы были повсюду: кровь, обломки и трещины. В тронном зале за троном зияла дыра, пробитая троллем.'
           'Скорее всего там была сокровищница и там теперь пусто')
    keyboard = {'inline_keyboard': [
        [{'text': 'Вернуться в лагерь', 'callback_data': 'tri_restore_c'},{'text':'В дыру','callback_data':'gold_dragon'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def gold_dragon(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Записки золотого дракона' in player[chat_id].quest:
        text =('Вы вошли в дыру и обнаружили королевский архив. '
               'Среди уцелевших книг и свитков вы нашли запись о золотом драконе, жившем в этом городе сотни лет назад. '
               'Забрав находку, вы направились обратно в лагерь.')
        player[chat_id].quest.append('Книга о золотом драконе')
        save_players()
    else:
        text =('Внутри оказались королевские архивы, а не сокровщиница. '
               'Перебрав старые записи, вы не нашли ничего примечательного. День клонился к вечеру, и вы решили вернуться в лагерь.')
    keyboard = {'inline_keyboard': [
        [{'text': 'Отдых', 'callback_data': 'tri_restore_c'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def monster_burn(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'monster_burn':
        text =('Несколько дней вы собирали тела монстров и сжигали их останки. '
               'Над городом поднимались столбы дыма от работы уборочных команд. Наконец, настал долгожданный отдых.')
    else:
        text = ('Несколько дней вы трудились в похоронных командах, осматривая дома, подвалы и улицы, собирая тела погибших. '
                'За городом выросло огромное кладбище. Наконец настал долгожданный отдых.')
    keyboard = {'inline_keyboard': [
        [{'text': 'Отдых', 'callback_data': 'tri_restore_c'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)

def tri_restore_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='После отдыха армии, объявлен сбор за пределами города'
    restore(chat_id)
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'Сбор', 'callback_data': 'tri_army_go_b'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_army_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Армия собралась за городом. Командир произнес речь о предстоящем штурме замка и мести за разрушенный город. '
           'После чего армия двинулась в поход.')
    keyboard = {'inline_keyboard': [
        [{'text': 'Марш армии', 'callback_data': 'tri_army_go_c'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_army_go_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Армия двинулась маршем к цитадели третьего генерала. По пути встречалась небольшая деревушка, и командир распорядился отправить туда отряд на разведку. '
           'Отряд собирался из желающих, так как задача могла обернуться билетом в один конец. Ваша миссия — найти припасы для армии.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Продолжить марш','callback_data':'village_c'},{'text':'В разведку','callback_data':'village'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def village(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы присоединились к разведотряду и отправились к деревне. Прибыв на место, вы обнаружили её полностью разрушенной и покинутой.'
    keyboard = {'inline_keyboard': [
        [{'text': 'Поискать припасы', 'callback_data': 'village_a'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def village_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if 'Зелье здоровья' in player[chat_id].invetary:
        button = [[{'text':'Дать зелье','callback_data':'peon_life'}]]
        text = ('Вы начали обыскивать дома в поисках провизии и инструментов. В одном из зданий вы нашли выжившего крестьянина. '
                'Он был слишком слаб, чтобы его спасти сильным зельем — такое лекарство мгновенно убило бы его. Обычное зелье могло бы помочь'
                'или лучше поискать припасы')
    else:
        text = ('Вы обыскали дома в поисках провизии и инструментов. В одном из зданий вы нашли выжившего крестьянина, но его состояние оказалось безнадежным.'
                ' Из милосердия один из членов отряда безболезненно прекратил его страдания, после чего вы продолжили поиски.')
        button = []
    keyboard = {'inline_keyboard': [
        [{'text': 'Продолжить поиски', 'callback_data': 'village_b'}]
    ]+button}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def village_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'peon_life':
        player[chat_id].invetary.remove('Зелье здоровья')
        player[chat_id].quest.append('Карта дракона')
        save_players()
        text =('Вы дали крестьянину зелье, и, окрепнув, он поблагодарил вас, передав карту, найденную после ухода монстров. '
               'Указав ему безопасный путь, вы продолжили собирать припасы. Закончив, вы направились обратно к армейскому лагерю.')
    else:
        text = 'Собрав необходимые припасы, вы отправились к месту, где армия разбивала лагерь.'
    keyboard = {'inline_keyboard': [
                                       [{'text': 'В лагерь', 'callback_data': 'village_c'}]
                                   ] }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def village_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Армия разбила лагерь для отдыха. Через несколько дней на горизонте покажется крепость третьего генерала.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'В патруль','callback_data':'tri_patrol'},{'text':'Отдых','callback_data':'restore_tri_f'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_patrol(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы вызвались в патруль в первую половину ночи. Пока вы патрулировали лагерь, вы заметили монстра разведчика'
           'Очень быстро вы смогли его догнать')
    keyboard = {'inline_keyboard': [
                                       [{'text': 'В бой', 'callback_data': 'tri_patrol_a'}]
                                   ] }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_patrol_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        tri_patrol_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def tri_patrol_a_win(chat_id):
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
            [{'text': 'Подготовка', 'callback_data': 'restore_tri_f'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив псоглавца, оставшийся патруль прошел в тишине, до смены караула. После чего вы отправились спать',
                        reply_markup=keyboard)
def restore_tri_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = 'С первыми лучами солнца лагерь был свернут, и армия двинулась дальше. До цитадели генерала оставался всего один день пути.'
    keyboard = {'inline_keyboard': [
        [{'text': 'Вперед', 'callback_data': 'tri_army_go_f'}]
    ]}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_army_go_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('После полудня армия вышла на развилку. Одна дорога вела прямо к цитадели, другая же не была отмечена на карте. '
            'Был собран отряд для разведки, в то время как остальная армия продолжила путь.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'К цитадели','callback_data':'tri_citadel_siege'},{'text':'В разведку','callback_data':'gold_dragon_start'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def gold_dragon_start(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    #if all(item in player[chat_id].quest for item in ['Карта дракона', 'Записки золотого дракона']): вариант для опыта
    if 'Карта дракона' in player[chat_id].quest and 'Записки золотого дракона' in player[chat_id].quest:
        button = [[{'text':'Идти по карте','callback_data':'golden_dragon_a'}]]
        text = ('Вы вспомнили, что похожая местность была отмечена на карте, которую дал спасенный крестьянин. '
                'Стоит ли идти по карте, или же исследовать ближайший лес, который может скрывать неожиданные угрозы или находки?')
    else:
        button = []
        text = ('Вы оказались на незнакомой местности и методом проб и ошибок попытались составить карту местности. '
                'Вы начали с изучения леса')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Исследовать лес','callback_data':'tri_forest_death'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_forest_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы зашли в лес, пройдя вглубь вы попали в засаду монстров. Вашему отряду не хватило сил отбиться'
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def golden_dragon_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы вышли к странному лесу, от которого веяло магией. Задача стоит перед вами: '
            'исследовать лес на предмет врагов или артефактов, или продолжить путь, следуя карте, не отвлекаясь на возможные опасности. Что выберете?')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Разведать лес', 'callback_data': 'tri_forest_death_a'}, {'text': 'Следовать по карте', 'callback_data': 'golden_dragon_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_forest_death_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Зайдя в глубины леса, вы приметили небольшую пещеру, направив туда отряд и зайдя в пещеру, вход за вами закрылся, а воздухе почувстовался сладкий аромат яда'
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def golden_dragon_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы последовали по карте и вышли на опушку леса, где увидели золотого дракона, источающего магическую энергию. '
            'Дракон заметил вас и в гневе произнес:Кажется, я запрещал людям посещать этот лес!»'
            'В ярости дракон выпустил в вашу сторону огненный шар, но вам удалось увернуться. Однако, ваш отряд не успел избежать огня и был уничтожен.')
    keyboard ={
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'fight_golden_dragon'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def fight_golden_dragon(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Gold_dragon()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        fight_golden_dragon_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def fight_golden_dragon_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 10
        player[chat_id].quest.append('Язык дракона')
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Оставить язык', 'callback_data': 'lang'},{'text':'Съесть язык','callback_data':'eat_lang'} ]
        ]}
        bot.sendMessage(chat_id, 'После тяжелого боя, вы наконец смогли одолеть эту тварь. Из записей вы знаете, что язык дракона очень ценен'
                                 'а так же что съев его, можно получить способность дракона',
                        reply_markup=keyboard)
def lang(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'eat_lang':
        player[chat_id].abillity.append(' Огненное дыхание')
        save_players()
        text =('Вы съели язык дракона и почувствовали новую способность, теперь вы сами можете дышать огнем'
               'Пора возвращаться в лагерь')
    else:
        save_players()
        text =('Вы решили оставить язык дракона у себя, после битвы с лордом тьмы, если вы выживете вы разбогатеете.'
               'Пора возвращаться в лагерь')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В осадный лагерь','callback_data':'tri_citadel_siege'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_citadel_siege(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.append('Усиленное зелье здоровья')
    restore(chat_id)
    save_players()
    text ='Отдохнув в осадном лагере, утром был объявлен сбор. Армия готовиться к штурму'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Штурм', 'callback_data': 'tri_citadel'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tri_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы ринулись в первых рядах, катапульты быстро пробили стены цитадели и вы устремились внутрь.'
           'Внутри стоял генерал повелителя тьмы, отдавая указы своим солдатам. Прорваться сквозь врагов и он ваш')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Первый враг','callback_data':'first_enemy'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def first_enemy(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        first_enemy_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def first_enemy_win(chat_id):
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
            [{'text': 'Второй', 'callback_data': 'two_enemy'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы пробивались в глубь врагов словно берсерк, солдаты следовали за вами, выбрав вторую цель вы напали на нее',
                        reply_markup=keyboard)
def two_enemy(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Rat_man()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_enemy_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def two_enemy_win(chat_id):
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
            [{'text': 'Третий враг', 'callback_data': 'tri_enemy'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы уже могли разглядеть генерала, который явно понял, что вы прорываетесь к нему, еще один враг встал у вас на пути',
                        reply_markup=keyboard)
def tri_enemy(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Ogr(name='Огр', hp = 650)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        tri_enemy_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def tri_enemy_win(chat_id):
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
            [{'text': 'Подобраться к генералу', 'callback_data': 'tri_general'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы словно сами как монстр, проредили путь до генерала, через толпу врагов, ваш отряд не отставал от вас'
                                 'с такой же яростью убивал всех , до генерала осталось совсем не много',
                        reply_markup=keyboard)
def tri_general(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text =('Вы наконец прочистили дорогу до генерала, жрецы позади вас, восстановили вам здоровье, ману и энергию. Бойцы встали вокруг вас кольцом'
           'Словно создавая арену и не подпускали к вам врагов, один на один, вы против генерала владыки тьмы')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'tri_general_fight'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def tri_general_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Tri_general()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        tri_general_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def tri_general_fight_win(chat_id):
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
            [{'text': 'Победа!', 'callback_data': 'tri_general_win'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы отрезали голову, генералу и возвестили о своей победе, это деморализовала врагов. Армия добила остатки',
                        reply_markup=keyboard)
def tri_general_win(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =' Когда цитадель была захвачена, выяснилось что командир пал в бою. На общем собрании командиров батальонов. Вам предложили занять пост командующего'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Согласиться','callback_data':'yes_commander'},{'text':'Отказаться','callback_data':'no_commander'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)