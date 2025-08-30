

from scenario_2 import *
#АКТ 2 ЧЕРНЫЙ ДРАКОН и ВТОРОЙ ГЕНЕРАл

def act_two(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы вступили в схватку с монстрами, что прилетели. Вы узнали их — это гарпии. '
            'В какой-то момент, не ожидая, вы получили сильный удар по голове и всё потемнело.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Прийти в себя','callback_data':'act_two_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def act_two_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].use_hand.clear()
    player[chat_id].invetary.clear()
    player[chat_id].quest_invetary.clear()
    text = ('Вы пришли в себя и, осмотревшись, поняли, что оказались в огромном гнезде гарпий. Повсюду были разбросаны яйца и тела мертвых солдат. '
            'Осмотрев себя, вы поняли, что гарпии забрали всё ваше снаряжение. '
            'Однако, оглядевшись, вы заметили у одного солдата верёвку, а у другого — материал для палатки. Возможно, из этого получится сделать парашют.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Использовать\nверевку','callback_data':'two_death'},{'text':'Использовать\nткань','callback_data':'two_act_go'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы взяли веревку у солдата — она уже явно ему не пригодится. Нашли точку крепления в гнезде и, сбросив вниз другой конец веревки, приготовились. '
            'Собравшись с духом, вы начали спускаться по веревке, чувствуя, как напряжение нарастает с каждым метром.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Спуститься', 'callback_data': 'two_death_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_death_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы спускались, спускались, а земли всё не было видно. '
                            'В какой-то момент вы поняли, что длины веревки не хватает. '
                            'Гарпии, летающие вокруг, уже заметили вас. Какая глупая смерть, после всего, что было пройдено.')
    kill(chat_id)
    save_players()
def two_act_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Меч орка' in player[chat_id].quest:
        text = ('Забирая ткань у солдата, вы заметили знакомый меч, который раньше взяли у орка. '
                'Уж лучше с ним, чем совсем без оружия.')
        player[chat_id].use_hand.append('Меч орка')
        save_players()
    else:
        text = ('Вы взяли ткань у солдата и приготовились к прыжку. '
                'С каждым моментом напряжение нарастало — всё зависело от того, удастся ли использовать импровизированный парашют.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Прыгнуть', 'callback_data': 'two_act_go_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_act_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы разбежались и прыгнули вниз, взяв ткань за четыре угла. '
            'Она раздулась, словно парашют, и вы начали медленно спускаться, надеясь, что гарпии вас не заметят. '
            'Всё прошло успешно. Теперь стоит ли подождать армию или отправиться в сторону цитадели?')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Ждать', 'callback_data': 'two_death_c'},{'text': 'Идти', 'callback_data': 'two_act_go_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_death_c(chat_id,message,data):
    bot.deleteMessage((chat_id,message))
    bot.sendMessage(chat_id,'Вы решили подождать, возможно, скоро вы увидите армию. Пока вы сидели в ожидании, гарпии наверху подняли тревогу. '
                            '«Сбежала еда», — пронеслось в их криках. Очень быстро они обнаружили вас. Кажется, сегодня вы будете чьим-то обедом.')
    kill(chat_id)
    save_players()
def two_act_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы выдвинулись в сторону цитадели, откуда вас принесли. '
            'Зайдя в лес, вы обратили внимание, что на скалах гарпии подняли тревогу. '
            'Еще бы — их еда смогла ускользнуть. Пройдя вглубь леса, вы заметили огра. Напасть или затаиться?')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'two_death_e'}, {'text': 'Спрятаться', 'callback_data': 'two_act_go_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_death_e(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы помчались в бой с огром, но в какой-то момент упали бессильно. '
                            'Промелькнула мысль: «Сколько дней я был без сознания в гнезде?» — перед тем, как огр поднял дубину, готовясь нанести последний удар.')
    kill(chat_id)
    save_players()
def two_act_go_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили спрятаться от огра, затаившись в тени, и подождать, пока он уйдет. '
            'Когда угроза миновала, вы осторожно продолжили движение, стараясь не привлекать внимания.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Продолжить', 'callback_data': 'two_act_go_e'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)

def two_act_go_e(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы шли через лес до самой ночи. До цитадели оставалось не так уж и много, возможно, за ночь вы сможете добраться до своих. '
            'Или лучше передохнуть и найти укрытие — ночью лес опасен.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Идти', 'callback_data': 'two_death_i'}, {'text': 'Искать укрытие', 'callback_data': 'two_act_go_i'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_death_i(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили продолжить путь, но в темноте не заметили огра. '
            'Он отправил вас в полет одним ударом своей дубины, и сознание померкло, прежде чем вы успели осознать, что произошло.')
    kill(chat_id)
    save_players()
def two_act_go_i(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы нашли небольшое укрытие внутри огромного дерева и провели там ночь, скрываясь от опасностей леса. '
            'К утру, отдохнув и восстановив силы, вы были готовы продолжить свой путь.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Продолжить путь', 'callback_data': 'two_act_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_act_go_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Пройдя полдня, вы наконец вышли навстречу движущейся армии. '
            'Вы доложили командующему о том, что с вами произошло. '
            'Хотели бы вы рассказать подробности или пойти отдохнуть и восстановить силы после утомительного путешествия?')
    if 'Меч орка' in player[chat_id].use_hand:
        button = [[{'text': 'Рассказать', 'callback_data': 'two_quest'}]]
    else:
        button = []
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдых', 'callback_data': 'two_restore'}]
        ]+button
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_quest(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы рассказали командиру все в подробностях: о гнезде гарпий и мертвых солдатах. '
            'После этого командир предложил вам отдохнуть, собрать отряд и уничтожить их гнездо.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отказаться', 'callback_data': 'two_restore'},
             {'text': 'Согласиться', 'callback_data': 'two_quest_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_quest_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Большое зелье здоровья','Большое зелье здоровья','Большое зелье здоровья'])
    restore(chat_id)
    text = ('Вы отдохнули и собрали небольшой отряд. '
            'На рассвете следующего дня вы были готовы вернуться в то гнездо, из которого с таким трудом сбежали.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Выдвигаемся','callback_data':'two_quest_b'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def two_quest_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Ваш отряд шел целый день, и наконец, под самую ночь, вы вернулись в тот лес, из которого когда-то выбирались. '
            'Возможно здесь еще где то бродит огр, что вы видели пару дней назад.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Продолжить путь','callback_data':'two_quest_c'},{'text':'Разбить лагерь','callback_data':'two_death_f'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def two_death_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы разбили лагерь, выставили часового и отправились спать. Утром вы так и не проснулись.'
    bot.sendMessage(chat_id, text)
    kill(chat_id)
    save_players()
def two_quest_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили продолжить путь и вскоре обнаружили огра. Если бы вы разбили лагерь, он мог бы вас всех убить.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'two_fight_ogr'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_fight_ogr(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Ogr(name='Огр', hp = 600)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_fight_ogr_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  two_fight_ogr_win(chat_id):
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
            [{'text': 'Отдых', 'callback_data': 'two_quest_w'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив огра, вы все же решили отдохнуть, зная точно, что угроз рядом больше нет.',
                        reply_markup=keyboard)
def two_quest_w(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    text = ('После отдыха вы продолжили путь, и вот уже перед вами появилось гнездовье гарпий. '
            'Гарпии, сидящие наверху, заметили вас и начали слетаться, чтобы убить вторженцев. ')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'garpia_fight'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def garpia_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Garpia(name='Гарпия страж', hp = 450,max_hp=450)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        garpia_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  garpia_fight_win(chat_id):
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
            [{'text': 'Напасть на нее', 'callback_data': 'two_garpia_fight'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив одну из гарпий, вы увидели, как еще одна пытается напасть со спины на одного из членов вашего отряда.',
                        reply_markup=keyboard)

def two_garpia_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Garpia(name='Гарпия страж', hp = 465,max_hp=466)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_garpia_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  two_garpia_fight_win(chat_id):
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
            [{'text': 'Их командир', 'callback_data': 'two_garpia_fight_a'} ]
        ]}
        bot.sendMessage(chat_id, 'Расправившись с ней, вы увидели гарпию, которая, кажется, была командиром этой стаи.',
                        reply_markup=keyboard)

def two_garpia_fight_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Garpia(name='Гарпия командир', hp = 550,max_hp=550)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_garpia_fight_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  two_garpia_fight_a_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].invetary.append('Большое зелье здоровья')
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        restore(chat_id)
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Разбить яйца', 'callback_data': 'egg_garpia'},{'text':'Собрать вещи','callback_data':'item_solider'} ]
        ]}
        text = ('Расправившись с отрядом гарпий, вы взобрались наверх и оказались в огромном гнезде.'
                'Вы заметили, что стаи гарпий на соседних шпилях горы, где находятся их гнезда, начали суетиться. '
                'Время поджимает.<b>Вы можете сделать что-то одно: разбить яйца или собрать вещи с павших.</b>')
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard,parse_mode='HTML')
def two_final_quest(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'egg_garpia':
        text = ('Вы быстро разбили все яйца, что попались вам на пути, надеясь хоть немного замедлить рост их популяции. '
                'Понимая, что времени в обрез, вы поспешили вернуться в лагерь армии, где вас уже ждали.')
    else:
        text = ('Вы быстро с отрядом обыскали трупы солдат, сняли медальоны, и у одного из них нашли старую книжку о черном драконе. '
                'Загадочная находка не давала покоя, но времени было мало. '
                'Закончив осмотр, вы поспешили вернуться в лагерь армии, где нужно было отчитываться перед командующим.')
        player[chat_id].quest.append('Книги о черном драконе')
        player[chat_id].book_dragon = True
    keyboard = {
        'inline_keyboard':[
            [{'text':'В лагерь','callback_data':'quest_complete_two'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def quest_complete_two(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы вернулись в лагерь и доложили командиру. Теперь настал момент отдыха.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдых', 'callback_data': 'two_restore'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_restore(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Вы отдыхали целые сутки, восстанавливая силы. '
            'На следующий день к вам подошел местный интендант и, узнав о потерянном оружии, предложил взять новое снаряжение со склада.')
    if 'Меч орка' in player[chat_id].use_hand:
        button = [[{'text':'Оставить меч орка','callback_data':'no_switch'}]]
    else:
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Получить оружие','callback_data':'two_weapon'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_weapon(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'no_switch':
        text = 'Вы решили оставить меч орка себе, отказавшись от оружие добытого в цитадели'
        button = [[{'text':'Идти на построение','callback_data':'two_go_army'}]]
    else:
        text = 'Вы решили взять новое оружие, которое было добыто в цитадели врага'
        button = [[{'text': 'Взять оружие', 'callback_data': 'two_go_army_a'}]]
    keyboard = {
        'inline_keyboard':[

        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_go_army(chat_id,message_id,data):
    text = 'Текс базовый, его не должно быть'
    bot.deleteMessage((chat_id,message_id))
    if data == 'two_go_army':
        text = 'Вы оставили меч орка себе и пришли на построение армии, которая в скором времени начнет марш ближайшего города.'
    else:
        if 'Маг' in player[chat_id].player_class:
            player[chat_id].use_hand.clear()
            player[chat_id].use_hand.append('Лазурный посох')
            text = 'Вы взяли лазурный посох и отправились на построение, скоро армия отправиться в ближайший город'
        elif 'Воин' in player[chat_id].player_class:
            player[chat_id].use_hand.clear()
            player[chat_id].use_hand.append('Меч демона')
            text = 'Вы взяли Меч демона и отправились на построение, скоро армия отправиться в ближайший город'
        elif 'Стрелок' in player[chat_id].player_class:
            player[chat_id].use_hand.clear()
            player[chat_id].use_hand.append('Лук генерала')
            text = 'Вы взяли Лук генерала и отправились на построение, скоро армия отправиться в ближайший город'
        elif 'Везунчик' in player[chat_id].player_class:
            player[chat_id].use_hand.clear()
            player[chat_id].use_hand.append('Кинжал убийцы')
            text = 'Вы взяли Кинжал убийцы и отправились на построение, скоро армия отправиться в ближайший город'
    keyboard = {
        'inline_keyboard':[
        [{'text':'Марш армии','callback_data':'two_town'}]
            ]
        }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def death_market_a(chat_id,message_id,data):
    text = 'Рынок, пуст. Торговля не ведется'
    bot.sendMessage(chat_id, text)
def two_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия прибыла в город. Он выглядел заброшенным — почти не было людей, а по разрушениям было видно, что город часто подвергается набегам монстров. '
            'Разбив лагерь у стен города, вашему отряду выдали расходные зелья. '
            'Пару дней армия проведет здесь, пополняя припасы. '
            'Стоит ли отдохнуть или заняться чем-то другим?')
    player[chat_id].invetary.extend(['Большое зелье здоровья','Большое зелье здоровья','Большое зелье маны','Большое зелье маны','Зелье здоровья'])
    keyboard = {
        'inline_keyboard':[
            [{'text':'На рынок','callback_data':'death_market_a'},{'text':'Изучить город','callback_data':'research_town'}],
            [{'text':'Остаться в лагере','callback_data':'two_camp'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def in_market(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили зайти в антикварную лавку и поискать что-то ценное. '
            'Среди множества предметов вам приглянулись несколько вещей: карта, талисман и странные часы. '
            'Кажется, каждая из этих вещей таит в себе какую-то загадку. Стоит ли взять их с собой?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Часы','callback_data':'clock'},{'text':'Карта','callback_data':'map'}],
            [{'text':'Талисман','callback_data':'talisman'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def give_me_item(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'clock':
        text = 'Вы взяли, странные часы, возможно их получиться обменять в лагере или просто знать время'
        player[chat_id].quest.append('Часы')
        save_players()
    elif data == 'map':
        text = ('Вы взяли карту, разверну ее, вы приметили на ней знакомые места и какие то отметки, одна из них была рядом\n'
                'с тем место где будет проходить армия, может стоит проверить это место')
        player[chat_id].quest.append('Старая карта')
        save_players()
    else:
        text = 'Вы взяли странный талисман, возможно ее можно оставить у себя или обменять на что то'
        player[chat_id].quest.append('Странный талисман')
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'В лагерь','callback_data':'in_camp'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def research_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if player[chat_id].book_dragon:
        text = ('Осматривая город, вы замечаете, что его жители покинули. Среди пустых улиц вы находите антикварную лавку. '
                'Стоит ли заняться мародерством и исследовать её? Или вернуться в лагерь и не тратить времени на рискованные действия?')
        button = [[{'text':'В лавку','callback_data':'in_market'}]]
    else:
        text = ('Осматривая город, вы замечаете разрушения от набегов, пустые магазинчики и полуразрушенные дома. '
                'В некоторых всё же можно увидеть оставшихся жителей. После осмотра вы решаете вернуться в лагерь')
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'В лагерь','callback_data':'in_camp'}]
        ]+button
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def in_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='В лагере особо нечем заняться — либо отдыхать, либо подойти к командиру и узнать, есть ли задания'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдыхать','callback_data':'two_restore_f'},{'text':'Узнать о заданиях','callback_data':'quest_two'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_two(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы зашли в шатер к командиру, чтобы узнать насчет задания. '
            'Он сообщил, что нужно провести разведку по трем направлениям, ведущим из города, и доложить '
            'о безопасном маршруте, по которому армия сможет двигаться к цитадели второго генерала.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Взяться','callback_data':'quest_two_invite'},{'text':'Отказаться','callback_data':'two_restore_f'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_two_invite(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Был собран небольшой отряд, и, учитывая ваши прошлые заслуги, вас назначили командиром этого отряда. '
            'Теперь вам предстоит провести разведку и обеспечить безопасность маршрута для армии.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Выдвигаемся','callback_data':'quest_two_go'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_two_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Вы направили отряд к месту, где дорога расходилась на три направления. '
            'Левая тропа вела в лес, и по сообщениям разведчиков там царил странный туман. '
            'Правая шла вдоль реки, и могла оказаться более безопасной. '
            'Центральная дорога вела прямо к цитадели, но ни один разведчик не вернулся с этого пути.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'На лево','callback_data':'quest_left'},{'text':'Центральная','callback_data':'quest_center'}],
            [{'text':'На право','callback_data':'quest_right'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_left(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы с отрядом решили проверить, что скрывает лес. '
            'Дорога до его края была спокойной, но когда вы наконец оказались в тумане, который стелился среди деревьев, всё изменилось. '
            'Остановив отряд, вы начали всматриваться в густую мглу. Тишина, что царила вокруг, была почти непривычной, не слышно было даже пения птиц. '
            'Внутри тумана вам показалось, что мелькнули какие-то фигуры, но что это было, вам не удалось понять.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Войти в лес','callback_data':'quest_two_death'},{'text':'Вернуться','callback_data':'quest_two_return'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_two_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Зайдя в лес, вы почувствовали сильное головокружение. '
            'Один за другим солдаты начали падать. Трудно дышать, мир вокруг быстро вращается. Вы упали и отключились.')
    bot.sendMessage(chat_id, text)
    kill(chat_id)
    save_players()
def quest_two_return(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили вернуться и выбрать другую дорогу'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Центральная', 'callback_data': 'quest_center'}],
            [{'text': 'На право', 'callback_data': 'quest_right_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def quest_right(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Пройдя по правой дороге, вы вышли к обрыву. Заглянув вниз, увидели реку. '
            'Пройдя вдоль неё, вы снова столкнулись с обрывом. Этот путь не подходит')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Центральная', 'callback_data': 'quest_center'}],
            [{'text': 'На лево', 'callback_data': 'quest_left'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def quest_right_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Пройдя по правой дороге, вы вышли к обрыву. Заглянув вниз, увидели реку. '
            'Пройдя вдоль неё, вы снова столкнулись с обрывом. Этот путь не подходит')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Центральная дорога', 'callback_data': 'quest_center'}]

        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def quest_center(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили проверить центральную дорогу и выяснить, почему оттуда не вернулся ни один разведчик. '
            'Пройдя полдня, вы наткнулись на лагерь монстров. Вернуться и доложить или уничтожить лагерь кобольдов?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Напасть','callback_data':'quest_two_attack'},{'text':'Вернуться','callback_data':'one_complete'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def complete(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'one_complete':
        text = ('После возвращения, вы доложили командиру о лагере монстров, где находилось около двадцати существ. '
                'Армии пришлось немного задержаться для зачистки лагеря. '
                'Командир в благодарность выдал вам новые зелья, недавно разработанные алхимиками.')
        player[chat_id].invetary.extend(['Усиленное зелье здоровья','Усиленное зелье здоровья','Усиленное зелье маны','Усиленное зелье маны'])
        save_players()
    else:
        player[chat_id].two_quest = True
        player[chat_id].quest.append('Свиток способности')
        player[chat_id].invetary.extend(
            ['Усиленное зелье здоровья', 'Усиленное зелье здоровья', 'Усиленное зелье маны', 'Усиленное зелье маны'])
        save_players()
        text = ('Вы вернулись к командиру и доложили ему о том, что центральная дорога безопасна и на ней уничтожен лагерь монстров\n'
                'Командир впечтелен вашими успехами и выдал вам четыре зелья, два маны и два здоровья. Намекнув что это новые более мощные зелья\n'
                'Так же он дал вам свиток способностей, который был найден в цитадели')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдыхать','callback_data':'two_restore_f'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def quest_two_attack(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили атаковать, лагерь'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'quest_two_attack_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def quest_two_attack_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Cobold()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        quest_two_attack_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  quest_two_attack_a_win(chat_id):
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
            [{'text': 'Следующий', 'callback_data': 'quest_two_attack_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы справились со своим врагом, как к вам уже подкрадывался второй кобольд',
                        reply_markup=keyboard)
def quest_two_attack_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Cobold()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        quest_two_attack_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  quest_two_attack_b_win(chat_id):
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
            [{'text': 'Еще один', 'callback_data': 'quest_two_attack_c'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив второго кобольда, вы запреметили кобольда, который хотел помочь своим',
                        reply_markup=keyboard)
def quest_two_attack_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Cobold()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        quest_two_attack_c_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  quest_two_attack_c_win(chat_id):
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
            [{'text': 'Осмотреть трупы', 'callback_data': 'quest_two_attack_final'} ]
        ]}
        bot.sendMessage(chat_id, 'Ваш отряд уничтожил лагерь врага и начал стаскивать тела в центр, прежде чем их сжечь'
                                 'Вы решили осмотреть их тела.',
                        reply_markup=keyboard)
def quest_two_attack_final(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Старая карта' in player[chat_id].quest:
        text ='Осматривая тела кобольдов, вы заметили знакомый ключ, точно такой же, как был изображен на карте, найденной вами в городе у антиквара'
        player[chat_id].quest.append('Ключ')
        save_players()
    else:
        text = 'Осмотрев, тела. Вы нашли ключ, от чего он неизвестно. По этому вы его сразу же выкинули.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вернуться','callback_data':'complete'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_restore_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    if 'Свиток способности' in player[chat_id].quest:
        button = [[{'text':'Выучить способность','callback_data':'mana_burn'}]]
        text = 'Вы вернулись к себе в палатку, развернули свиток и решили впитать силу знаний из него'
    else:
        button =[[{'text':'Отдохнуть','callback_data':'restore_two_j'}]]
        text = 'наконец, вы можете отдохнуть перед следующим марш броском армии'
    keyboard ={
        'inline_keyboard':[
            []
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def mana_burn(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Стрелок' in player[chat_id].player_class:
        text ='Вы выучили новую способность, выстрел, что сжигает ману врага'
        player[chat_id].abillity.append('Духовный выстрел')
        player[chat_id].quest.remove('Свиток способности')
        save_players()
    elif 'Воин' in player[chat_id].player_class:
        text = 'Вы выучили новую способность, удар, что сжигает ману врага'
        player[chat_id].abillity.append('Духовный удар')
        player[chat_id].quest.remove('Свиток способности')
        save_players()
    elif 'Везунчик' in player[chat_id].player_class:
        text = 'Вы выучили новую способность, удар, что сжигает ману врага'
        player[chat_id].abillity.append('Удар духа')
        player[chat_id].quest.remove('Свиток способности')
        save_players()
    else:
        text = 'Вы выучили новую способность. Сжигание маны'
        player[chat_id].abillity.append('Сжигание маны')
        player[chat_id].quest.remove('Свиток способности')
        save_players()
    keyboard = {
        'inline_keyboard': [
        [{'text':'Отдохнуть','callback_data':'restore_two_f'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def restore_two_j(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text =('Пару дней вы отдыхали, пока наконец не был объявлен сбор армии. '
           'Вы собрали вещи, заняли свое место среди отряда, и армия двинулась дальше, готовая к новому этапу пути.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Вперед', 'callback_data': 'two_army_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_army_go_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].two_quest:
        text = ('Армия проходила мимо лагеря, который вы уничтожили пару дней назад. '
                'То место, куда вы стащили трупы и подожгли, все еще дымилось. Славный был бой, но впереди новые испытания и задачи.')
    else:
        text = ('Армия достигла лагеря, и небольшой отряд кобольдов, стоявший на пути, не смог сдержать натиск многотысячной армии. '
                'Их сопротивление было коротким и бесполезным — лагерь быстро пал, оставив лишь обгоревшие остатки того, что когда-то было их оплотом')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Следовать дальше','callback_data':'two_army_go_j'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_army_go_j(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].luck >= 15 and 'Ключ' in player[chat_id].quest:
        button = [[{'text':'Разговор с командиром','callback_data':'black_dragon_start'}]]
        text = ('Армия после долгого марша остановилась и разбила лагерь для пополнения припасов. '
                'Два дня отдыха были вам предоставлены, и вы могли воспользоваться этим временем, чтобы восстановить силы и подготовиться к дальнейшему пути.')
    else:
        button = []
        text = 'Армия разбила лагерь, после пополнения и отдыха путь продолжиться'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдых','callback_data':'two_army_go_final'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def black_dragon_start(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили поговорить с командиром, который вскоре сообщил, что армия будет проходить через старые храмовые комплексы. '
            'На карте, которую вы нашли, были сделаны отметки, и командир, к вашему удивлению, дал добро на исследование комплекса с небольшим отрядом. '
            'После завершения разведки вы сможете присоединиться к штурму цитадели.')
    player[chat_id].talk_commander = True
    save_players()
    keyboard = {
        'inline_keyboard': [
                               [{'text': 'Отдых', 'callback_data': 'two_army_go_final'}]
                           ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def black_dragon_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Собрав отряд, вы направились на север. Через пол дня вы вышли к храмовому комплексу, состоящему из нескольких храмов. '
           'На карте был отмечен последний храм, но вы понимаете, что есть шанс найти что-то полезное и в других храмах. '
           'Как поступить? Исследовать все храмы или двигаться сразу к последнему?')
    keyboard ={
        'inline_keyboard':[
            [{'text':'В первый храм','callback_data':'chram_death'},{'text':'Пойти дальше','callback_data':'black_dragon_go_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def chram_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы подошли к храму и попытались открыть дверь. Но как только вы сделали шаг вперед, сверху с грохотом упал камень. Очень глупая смерть...'
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def black_dragon_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы прошли вглубь храмового комплекса. Второй храм, казалось, был заброшен уже много лет, его стены разрушены временем. '
            'Подойдя к третьему храму, вы почувствовали странное ощущение тревоги — от него исходила некая зловещая аура. '
            'Возможно, именно здесь вас поджидает смерть.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Уйти','callback_data':'two_arm_go_final_a'},{'text':'Войти','callback_data':'black_dragon_go_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def black_dragon_go_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest.remove('Ключ')
    save_players()
    text = ('Вы решились войти. Замочная скважина идеально подходила под ключ, который вы нашли ранее. '
            'Вставив его и повернув, вы услышали тихий щелчок — дверь медленно открылась.')
    keyboard= {
        'inline_keyboard':[
            [{'text':'Войти в храм','callback_data':'fight_black_dragon'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def fight_black_dragon(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Усиленное зелье здоровья','Усиленное зелье здоровья'])
    save_players()
    text = ('Войдя в храм и продвигаясь дальше, вы оказались на огромной поляне, усеянной клевером. '
            'В самом центре лежал могучий черный дракон, его глаза сверлили вас взглядом, давая понять, что живым покинуть это место не получится.')

    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'fight_black_dragon_start'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def fight_black_dragon_start(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Black_dragon()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        black_dragon_final(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def black_dragon_final(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 10
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Собрать чешую', 'callback_data': 'loot_black_dragon'},{'text':'Впитать силу','callback_data':'skill_black_dragon'} ]
        ]}
        bot.sendMessage(chat_id, 'Одолев черного дракона, потеряв при этом весь свой отряд, вы стояли перед его мертвым телом. '
                                 'Из старых записей, которые вам удалось найти, вы знали, '
                                 'что особые чешуйки дракона ценятся на вес золота. Но если попытаться впитать их силу,'
                                 ' возможно, вам удастся обрести способность самого дракона.',
                        reply_markup=keyboard)
def black_dragon_final_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Усиленное зелье здоровья', 'Усиленное зелье здоровья'])
    save_players()
    if data == 'loot_black_dragon':
        player[chat_id].quest.append('Чешуйка черного дракона')
        save_players()
        text = 'Вы решили, оставить чешуйку с головы дракона на будущее. Столь ценный предмет, можно продать алхимикам'
    else:
        player[chat_id].abillity.append('Щит дракона')
        save_players()
        text = 'Вы сосредоточились и поглотили силу чешуйки, вы приобрели способность "Щит черного дракона"'
    keyboard = {
        'inline_keyboard':[
            [{'text':'К цитадели','callback_data':'two_army_go_citadel'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_army_go_final(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Базовый'
    if player[chat_id].talk_commander:
        text =('Армия продолжила свой путь, и, наконец, вы достигли храмовых комплексов. '
               'Как и договаривались с командиром, вам было разрешено отправиться исследовать северный храм, отмеченный на карте.')
        button = [[{'text':'На север','callback_data':'black_dragon_go'}]]
    else:
        text = ('Армия продолжила свой путь и, наконец, достигла комплекса древних храмов.'
                ' Командир отдал указание собрать отряд для исследования храма, после чего армия продолжила марш.')
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Исследовать храм','callback_data':'research_chram'},{'text':'Продолжить путь','callback_data':'two_army_go_citadel'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def research_chram(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы вызвались принять участие в отряде, который отправится на исследование храма. '
            'Направившись на юг, вы достигли полуразрушенного храма, чьи двери были разрушены и валялись на земле.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Войти','callback_data':'go_charm'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_charm(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Войдя внутрь, вы заметили странные убранства, характерные для некромантов. '
            'На полу валялись скелеты в доспехах, которые начали подниматься, словно оживая перед вашими глазами.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'fight_skeleton'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def fight_skeleton(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Skelet()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        fight_skeleton_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def fight_skeleton_win(chat_id):
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
            [{'text': 'Следующий', 'callback_data': 'fight_skeleton_a'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив скелета вы переключились на другого',
                        reply_markup=keyboard)
def fight_skeleton_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Skelet()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        fight_skeleton_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  fight_skeleton_a_win(chat_id):
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
            [{'text': 'Осмотреть храм', 'callback_data': 'chram_visual'} ]
        ]}
        bot.sendMessage(chat_id, 'Ваш отряд расправился со скелетами, теперь у вас есть время внимательно осмотреть храм',
                        reply_markup=keyboard)
def chram_visual(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы осмотрели храм. Кверху вели две лестницы: одна была разрушена, а другая, казалось, вот-вот рассыплется. '
            'Под алтарем в полу зияла дыра, и из неё виднелись ступеньки, ведущие вниз')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вверх','callback_data':'chram_death_a'},{'text':'Вниз','callback_data':'go_chram_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def chram_death_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили подняться наверх, но на середине пути ступеньки обрушились, и вы с грохотом полетели вниз. '
            'Приземлившись, вы почувствовали, как спина сильно ударилась о каменные осколки.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def go_chram_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Спустившись вниз, вы оказались в тёмном коридоре, который разветвлялся на два пути, уходящих в неизвестность.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Влево','callback_data':'chram_death_b'},{'text':'Вправо','callback_data':'go_chram_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def chram_death_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы выбрали левый коридор и прошли немного вперёд, как вдруг один из членов отряда задел скрытую ловушку. '
           'Прогремел мощный магический взрыв, и в мгновение ока отряд исчез, не оставив даже следов.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def go_chram_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы подошли к массивной двери и, прежде чем открыть её, дали отряду немного времени на отдых. '
           'После краткого перерыва вы решительно открыли дверь. '
           'Войдя в зал, вы увидели огромного рыцаря-скелета, стоявшего в центре. '
           'Как только дверь закрылась за вами, он мгновенно пришёл в движение и бросился в бой.')
    restore(chat_id)
    save_players()
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'fight_skeleton_knight'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def fight_skeleton_knight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Skelet(name = 'Рыцарь скелет', hp =900,max_hp=900)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        fight_skeleton_knight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  fight_skeleton_knight_win(chat_id):
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
            [{'text': 'Осмотреть зал', 'callback_data': 'chram_final'} ]
        ]}
        bot.sendMessage(chat_id, 'Одолев скелета, ваш отряд перевел дух и осмотрел зал, заметив странные символы на стенах и останки стражей.',
                        reply_markup=keyboard)
def chram_final(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Маг' in player[chat_id].player_class:
        text =('Впереди были две двери, и вам предстояло выбрать ту, что не приведет к гибели. '
               'Также вы ощущали магическую энергию, исходящую из-под пола, что могло означать наличие потайной двери.')
        button = [[{'text':'Поискать дверь','callback_data':'necromance'}]]
    else:
        text = 'Впереди было две двери, осталось понять в какую вам войти, что бы не встретить свой конец.'
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Правая дверь','callback_data':'right_door'},{'text':'Левая дверь','callback_data':'right_door'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def necromance(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы обнаружили тайный ход в полу и спустились вниз. В глубине вас встретил алтарь, явно подготовленный некромантами. '
            'Шепот "переродись" доносился оттуда, будто алтарь звал вас. Ваш отряд предложил разрушить его и вернуться к армии.')
    player[chat_id].invetary.extend(
        ['Усиленное зелье здоровья', 'Усиленное зелье маны'])
    keyboard = {
        'inline_keyboard':[
            [{'text':'Разрушить алтарь, вернуться','callback_data':'two_army_go_citadel'},{'text':'Переродиться','callback_data':'relife'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def relife(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы подошли к алтарю, его голос продолжал звать, настоятельно прося разрешения. '
            'Вы уступили. Мгновение — и члены вашего отряда погибли, а вы почувствовали, как новая сила наполняет вас. Вы переродились в некроманта.')
    player[chat_id].player_class.clear()
    player[chat_id].player_class.append('Некромант')
    player[chat_id].abillity.clear()
    player[chat_id].abillity.extend(['Вытягивание жизни','Поднять нежить','Прикосновение мертвеца','Мерцание','Печать разложения','Стрела негативной энергии'])
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вернуться','callback_data':'citadel_two_necro'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def citadel_two_necro(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Добравшись до лагеря, который возвели перед штурмом цитадели генерала, вы направились к командиру, чтобы доложить о разведке храма. '
           'Но вас остановили армейские священники, почувствовав изменения в вас. Некроманты не просто так скрываются от всех. Ваш путь завершился на костре.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def right_door(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы вошли в дверь и с удивлением обнаружили, что обе двери вели в одну и ту же комнату. '
            'В помещении вы нашли несколько зелий, но ничего особо примечательного. '
            'Пора возвращаться к армии, которая уже скоро должна достичь цитадели врага.')
    player[chat_id].invetary.extend(
        ['Усиленное зелье здоровья', 'Усиленное зелье маны'])
    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'К цитадели','callback_data':'two_army_go_citadel'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_army_go_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия разбила лагерь перед цитаделью генерала, и вот-вот начнется штурм. '
            'Последние приготовления завершены, вам выдали несколько усилиных зелей здоровья, осталось лишь немного отдохнуть. Затем была отдана команда: штурм начинается.')
    player[chat_id].invetary.extend(['Усиленное зелье здоровья', 'Усиленное зелье здоровья'])
    restore(chat_id)
    save_players()
    keyboard = {
        'inline_keyboard': [
            [{'text': 'На штрум!', 'callback_data': 'two_citadel_go'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_citadel_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Армия двинулась в сторону цитадели. Таран с оглушительным ударом выбил ворота, и солдаты, словно река, хлынули во двор крепости.'
           ' Но на встречу им вышли два огромных голема, готовые остановить напор наступающих.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'two_citadel_go_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_citadel_go_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Golem()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_citadel_go_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def  two_citadel_go_a_win(chat_id):
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
            [{'text': 'В замок', 'callback_data': 'two_citadel_go_b'},{'text':'Помочь армии','callback_data':'two_citadel_death'} ]
        ]}
        bot.sendMessage(chat_id, 'Ваш отряд одолел первого голема, и, осмотревшись, вы заметили, что второй также повержен. '
                                 'Основные силы врага были сосредоточены во дворе, сдерживаемые солдатами, которые продолжали отчаянно сопротивляться. '
                                 'В этом моменте открывается шанс — либо воспользоваться этой возможностью и ворваться в замок, либо помочь союзникам, '
                                 'которые сражаются во дворе',
                        reply_markup=keyboard)
def two_citadel_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили остаться и помочь солдатам во дворе, вступив в бой. Вместо того чтобы пробиваться в замок, вы сражались, уничтожая врагов одного за другим. '
            'Но внезапно, в этом хаосе, меч пронзил вас сзади. Мясорубка сражений не прощала ошибок, и вы почувствовали, как силы покидают вас.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def two_citadel_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы ворвались в замок и оказались в комнате генерала. Если верить карте, предыдущей цитадели, то путь наверх ведет к его личным покоям, а вниз — в темницы. '
           'Ожидание встречи с генералом или исследование темниц? Вы стояли перед выбором.')
    keyboard = {'inline_keyboard': [
        [{'text': 'Наверх', 'callback_data': 'two_citadel_go_false'},
         {'text': 'Вниз', 'callback_data': 'two_citadel_true'}]
    ]}
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def two_citadel_go_false(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы поднялись наверх, и все вокруг напоминало то, что вы видели в первой крепости. '
            'Достигнув тронного зала, вас встретил неживой страж, не давая пройти дальше.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'two_citadel_go_false_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_citadel_go_false_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Skelet(name='Нежить страж')
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_citadel_go_false_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def two_citadel_go_false_a_win(chat_id):
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
            [{'text': 'Войти', 'callback_data': 'two_citadel_go_false_a_death'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы довольно легко расправились со стражем, никто не вышел ему на помощь, за дверью своего часа ждет генерал',
                        reply_markup=keyboard)
def two_citadel_go_false_a_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Войдя в тронный зал, вы никого не обнаружили, но увидели как магические круги на стенах и на полу, начали мерцать, вы попытались убежать, \n'
           'огромный магический взрыв снес половину замка')
    kill(chat_id)
    save_players()
def two_citadel_true(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы решили проверить в начале темницу, спустившись вниз, путь вам преградил скелет в тяжелой броне и огромным топором'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'two_citadel_go_true_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def two_citadel_go_true_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Skelet(name='Элитный нежить страж', hp = 1000,max_hp=1000,attack=65,mana= 450)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_citadel_go_true_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def two_citadel_go_true_a_win(chat_id):
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
            [{'text': 'Войти', 'callback_data': 'two_general'} ]
        ]}
        bot.sendMessage(chat_id, 'Разделавшись с нежить, вы подошли к дверям, судя по убранству вокруг, двери вели в ритуальный зал',
                        reply_markup=keyboard)
def two_general(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    player[chat_id].invetary.append('Усиленное зелье здоровья')
    save_players()
    text ='Восстановив силы, вы вошли в огромный ритуальный зал, по середине стоял генерал, повелитель мертвых, худой и высокий. Он не стал ничего вам говорить, а сразу ринулся в бой'
    keyboard = {'inline_keyboard': [
        [{'text': 'Атаковать', 'callback_data': 'two_general_fight'}]
    ]}
    bot.sendMessage(chat_id,text, reply_markup=keyboard)
def two_general_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Two_general()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        two_general_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def two_general_fight_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 10
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Объявить о победе', 'callback_data': 'two_general_death'} ]
        ]}
        bot.sendMessage(chat_id, 'Генерал пал, можно объявить о победе и деморализовать врага, после чего решить, что делать со сдавшимся врагами',
                        reply_markup=keyboard)