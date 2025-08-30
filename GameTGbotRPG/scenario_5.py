from scenario_4 import *
#АКТ 4 ЧЕТВЕРТЫЙ ГЕНЕРАЛ И КРАСНЫЙ ДРАКОН
def commander(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    if data == 'yes_commander':
        player[chat_id].commander = True
        save_players()
        text = 'Вы согласились стать командиром. Первое что вы решили сделать зачитать речь перед армией'
        keyboard = {
            'inline_keyboard':[
                [{'text':'Речь','callback_data':'say_commander'}]
            ]
        }
        bot.sendMessage(chat_id,text,reply_markup=keyboard)
    else:
        text = ('Вы отказались занять пост командующего и был выбран другой. Вы вернулись в свой отряд'
                'новый командир собрал армию для произношения речи')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Слушать', 'callback_data': 'ear_commander'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_go_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text =('После произнесенной речи вы двинулись осматривать собранные трофеи. Оружие и артефакты были распределены между отрядами, а себе вы оставили два зелья. '
               'Закончив осмотр, вы отдали команду на построение армии, готовясь к следующему шагу.')
        player[chat_id].invetary.extend(['Героическое зелье здоровья','Героическое зелье маны'])
        save_players()
        keyboard = {
            'inline_keyboard':[
                [{'text':'Построение','callback_data':'four_army_go_a'}]
            ]
        }
        bot.sendMessage(chat_id,text,reply_markup=keyboard)
    else:
        text ='Ваш отряд получил припасы и оружие. Через какое то время был отдан приказ об общем сборе, армия скоро двинется дальше'
        player[chat_id].invetary.extend(['Героическое зелье здоровья', 'Героическое зелье маны'])
        save_players()
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Построение', 'callback_data': 'four_army_go_a'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_army_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Армия была построена, отдан приказ на движение'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Вперед', 'callback_data': 'four_army_go_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_army_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text =('Весь день армия продвигалась через земли, разрушенные монстрами, сталкиваясь с сожженными деревнями. '
               'К вечеру армия сделала большой марш. Стоит ли продолжить путь или лучше разбить лагерь для отдыха?')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Двигаться вперед', 'callback_data': 'four_army_go_death'},{'text':'Разбить лагерь','callback_data':'four_restore_army'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        text =('В течение дня армия двигалась по опустошенным землям, минуя сожженные деревни и выжженные поля. '
               'К вечеру командир отдал приказ разбить лагерь для ночного отдыха.')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Разбить лагерь', 'callback_data': 'four_restore_army'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_army_go_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы решили продолжить марш, несмотря на усталость войска. К середине ночи ваш отряд попал в засаду отступающей армии монстров, стремившихся к цитадели генерала. '
           'Измученные солдаты не смогли дать отпор, и битва обернулась трагедией. Вы пали как командир, а ваша голова станет трофеем в замке врага.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def four_restore_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text ='Армия разбила лагерь, вы отдали приказы командирам батальонов, что бы они выставили караульных'
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Выставить караул', 'callback_data': 'four_army_restore_a'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        text ='Армия разбила лагерь, ваш командир отряда определил вас в караул'
        keyboard = {
            'inline_keyboard':[
                [{'text': 'В караул', 'callback_data': 'four_karaul'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_karaul(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Патрулируя окрестности лагеря, вы заметили тролля, вышедшего из ближайшего леса и направлявшегося к лагерю.'
            ' Не теряя времени, вы двинулись ему наперерез.')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'В бой', 'callback_data': 'four_karaul_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_karaul_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Troll()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        four_karaul_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def four_karaul_a_win(chat_id):
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
            [{'text': 'На отдых', 'callback_data': 'four_army_restore_a'} ]
        ]}
        bot.sendMessage(chat_id, 'Одолев тролля, вы продолжили патрулирование до следующей смены. После чего вы отправились отдыхать',
                        reply_markup=keyboard)
def four_army_restore_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text =('На рассвете армия продолжила путь через выжженные земли. '
           'Впереди должен был находиться пограничный город, но надежд на его сохранность почти не оставалось. '
           'Под вечер вы добрались до места, где он стоял: от города остались лишь руины. '
           'В них армия разбила лагерь, решив задержаться на несколько дней. До цитадели генерала оставалось два дня пути.')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Лагерь', 'callback_data': 'four_camp'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text = ('Армия разбила лагерь, а вы, как командующий, раздали указания командирам. '
                'Затем вы объявили собрание, чтобы обсудить дальнейший план действий.')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Собрание', 'callback_data': 'four_camp_a'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        text =('Армия разбила лагерь для пополнения припасов, планируя остаться здесь на несколько дней. '
               'Вы можете присоединиться к патрульным командам или позволить себе немного отдохнуть.')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'В патруль', 'callback_data': 'four_camp_a'},{'text':'Отдыхать','callback_data':'four_restore_c'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_camp_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    if player[chat_id].commander:
        text = ('После того как командиры вернулись к своим отрядам, вы завершили обсуждение плана штурма цитадели. '
                'Написав письмо королю о предстоящем наступлении, вы сообщили ему о ключевом моменте — открытии пути к замку владыки тьмы.')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Отправить письмо', 'callback_data': 'four_camp_b'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        text = 'Вы записались в патрульные команды, несколько дней вы будете патрулировать окрестности, охраняя лагерь'
        keyboard = {
            'inline_keyboard':[
                [{'text': 'В патруль', 'callback_data': 'patrol_four_a'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def patrol_four_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Первую ночь, вы спокойно провели в патруле. На вторую же ночь, вы заметили отряд монстров'
           'Собрав отряд, вы вышли чтоб его уничтожить')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'В бой', 'callback_data': 'patrol_four_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def patrol_four_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Dog_head()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        patrol_four_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def patrol_four_b_win(chat_id):
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
            [{'text': 'Отдыхать', 'callback_data': 'four_camp_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Разобравшись с отрядом псоглавцев, вы наконец сменились и отправились на отдых',
                        reply_markup=keyboard)
def four_camp_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    if player[chat_id].commander:
        text =('Отправив письма, вы несколько дней занимались рутинными делами командующего'
               'После пополнения запасов и отдыха, вы отдали приказ о сборе армии. Скоро будет решающий штурм')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Сбор армии', 'callback_data': 'four_army_go_f'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        text ='Отдохнув, у вас еще осталось несколько дней в запасе, чтоб себя чем то занять. Можно потренироваться'
        keyboard = {
            'inline_keyboard':[
                [{'text': 'Тренировка', 'callback_data': 'four_training'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_training(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Пока вы занимались тренировкой, к вам подошел один из солдат и предложил исследовать интересное здание в руинах города.'
           'Согласиться или отказаться и пойти отдыхать до сбора армии?')
    player[chat_id].sila +=5
    player[chat_id].luck +=5
    player[chat_id].agila +=5
    player[chat_id].intelect +=5
    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Пойти', 'callback_data': 'four_libray'},{'text':'Отказаться','callback_data':'four_army_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_libray(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы пошли вместе с ним. Дойдя до здания, вы поняли что это разрушенная библиотека'
           'Возможно там будет что то интересное. Зайдя вы принялись обыскивать, то что хотя бы сохранилось')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Искать', 'callback_data': 'four_inspect'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_inspect(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].luck >= 20:
        player[chat_id].quest.append('Карта местности')
        text =('Среди обугленных книг, вам повезло заметить целую карту, на ней отмечена пещера, возможно там есть что то интересное'
               'После чего вы отправились на отдых')
    else:
        text =('Вы потратили остаток дня роясь в обугленных книгах, так ничего и не найдя полезного'
               'после чего вы отправились на отдых')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Отдохнуть', 'callback_data': 'four_restore_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_restore_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Отдохнув, у вас выдался свободный день. Исследовать руины города или бездельничать до сбора армии?'
            'Есть вероятность, погибнуть, так как многие дома переодически осыпаются')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Ждать сбор армии', 'callback_data': 'four_army_go_f'},{'text':'Исследовать руины','callback_data':'four_research'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def four_research(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы решили на свой страх и риск исследовать руины города. Многие улицы завалины обломками, свободные проходы есть до рынка и гильдии искателей'
    keyboard = {
        'inline_keyboard':[
            [{'text': 'На рынок', 'callback_data': 'four_market'},
             {'text': 'К гильдии', 'callback_data': 'four_guild'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_market(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Прийдя на площадь, что раньше была рынком, перед вами предстало печальное зрелище. Сожженные прилавки, старая запекшиеся кровь, уничтоженные товары'
           'С рынка, виднеется замок, где жил местный лорд. Стоит посмотреть что там или вернуться и отдохнуть')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Вернуться', 'callback_data': 'four_army_go_f'},
             {'text': 'К цитадели', 'callback_data': 'four_castle'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_castle(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Добравшись к замку, вы поняли что зря потратили целый день. Вход в замок был завален. Остаеться только вернуться и ждать сбор армии'
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Вернуться', 'callback_data': 'four_army_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_guild(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы подошли к зданию гильдии искателей, оно к удивлению сохранилось хорошо, хоть и видно, что оно пострадало после атаки'
            'Войдя внутрь, стоит решить что лучше осмотреть')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Архивы', 'callback_data': 'guild_archive'},
             {'text': 'На второй\nэтаж', 'callback_data': 'guild_lord'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def guild_archive(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Целый день вы копались в архивах гильдии, ничего интересного вы найти не смогли'
           'Накладные, задания, листы наград и досье членов гильдии, все это неимеет ценности'
           'После чего вы решили вернуться назад')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Вернуться', 'callback_data': 'four_army_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def guild_lord(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы поднялись на второй этаж, сохранился только кабинет местного главы гильдии, войдя в его кабинет'
           'Вы не увидели ничего примечательного обычный рабочий кабинет. Если тут начать поиски, есть возможность обрушения здания')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Уйти отдыхать', 'callback_data': 'four_army_go_f'},
             {'text': 'Поискать', 'callback_data': 'guild_lord_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def guild_lord_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы все же решились поискать что нибудь ценное. В столе вы обнаружили тайник, а в нем книгу о красном драконе. Больше ничего интересного вы не нашли'
           'День уже шел к концу и вы ушли отдыхать')
    player[chat_id].quest.append('Книга о красном драконе')
    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Вернуться', 'callback_data': 'four_army_go_f'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_army_go_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('После отдыха, когда был объявлен сбор армии. Армия выстроилась и готова идти в путь дальше'
            'Впереди ждет цитадель четвертого генерала')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Марш', 'callback_data': 'four_army_go_q'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_army_go_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text ='Проходя путь, вы отпустили небольшую группу на разведку местности, через какое то время она должна присоединится в осадном лагере'
        keyboard = {
            'inline_keyboard':[
                [{'text': 'В осадный лагерь', 'callback_data': 'four_siege_citadel'}]
            ]
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
    else:
        if 'Карта местности' in player[chat_id].quest and 'Книга о красном драконе' in player[chat_id].quest:
            button = [[{'text':'Отправится на разведку','callback_data':'red_dragon_start'}]]
            text =('Армия продвигалась через перевалы, вы рассматривали карту, которую нашли недавно. История снова повторяется'
                   'Местность похожа что на карте. Стоит попросить командира отправится на разведку')
        else:
            button = []
            text =('Армия продвигалась своим маршрутом и вот уже виднелась издалека крепость генерала, скоро будет возведен осадный лагерь'
                   'и последние приготовления для штурма')
        keyboard = {
            'inline_keyboard':[
                [{'text': 'В осадный лагерь', 'callback_data': 'four_siege_citadel'}]
                ]+button
        }
        bot.sendMessage(chat_id, text, reply_markup=keyboard)
def red_dragon_start(chat_id,message_id,data):
    player[chat_id].invetary.extend(['Героическое зелье здоровья','Героическое зелье здоровья','Героическое зелье здоровья'])
    restore(chat_id)
    save_players()
    bot.deleteMessage((chat_id,message_id))
    text = ('Поговорив с командиром, он согласился снарядить отряд на разведку. Вам дали не больше время и указали точку куда возвращаться.'
            'Пройдя по местности вы подошли к странной пещере с огромным входом, дорога уходила вниз, а по края пещеры были вмятены от огромных когтей. '
            'рядом вы нашли рюкзак в котором были зелья, сейчас они вам важнее, чем их владельцу')
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Войти в пещеру', 'callback_data': 'red_dragon'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def red_dragon(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Пройдя в глубь пещеры, вы увидели святящиеся глаза, а после всполох огня, который сжег ваших спутников'
           'Красный дракон в ярости')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'red_dragon_fight'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def red_dragon_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Red_dragon()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        red_dragon_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def red_dragon_fight_win(chat_id):
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
            [{'text': 'Оставить когти', 'callback_data': 'red_dragon_a'},{'text':'Впитать силу','callback_data':'red_dragon_b'} ]
        ]}
        bot.sendMessage(chat_id, 'После тяжелого боя в узких пещерах, вы нанесли смертельную рану. Из книги вы знаете, что когти дракона таят в себе '
                                 'силу дракона, но и ювелиры купят у вас эти когти дороже чем алмазы',
                        reply_markup=keyboard)
def red_dragon_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data =='red_dragon_a':
        player[chat_id].quest.append('Когти дракона')
        text ='Вы решили оставить, когти дракона себе, скоро закончится война и вы будете очень богаты, если выживите. Нужно вернутся в лагерь'
    else:
        player[chat_id].abillity.append('Удар дракона')
        text = ('Вы выпитали силу котгей, приобретя навык удар дракона, вы делает взмах руков словно бьете лапой и на врага обрушивается матерализованя лапа '
                'красного дракона. Теперь стоит поспешить в лагерь')
    save_players()
    keyboard = {
        'inline_keyboard': [
                               [{'text': 'В осадный лагерь', 'callback_data': 'four_siege_citadel'}]
                           ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_siege_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Героическое зелье здоровья', 'Героическое зелье маны'])
    restore(chat_id)
    save_players()
    text ='Перед штурмам, алхимики выдали зелья. Как убийцу трех генералов владык тьмы, вы поведете армию на штурм'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'four_citadel'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text= ('Вы повели армию вперед, осадные орудия пробили стены, вы устремились туда, ворвавшись во внутрь'
           'вы уничтожили несколько монстров, и ворвались в строй врагов, солдаты последовали за вами')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Бой', 'callback_data': 'four_citadel_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_citadel_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Deamon(hp = 1000,attack=65)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        four_citadel_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def four_citadel_a_win(chat_id):
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
            [{'text': 'Еще один', 'callback_data': 'four_citadel_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы прорубались сквозь ряды демонов, ваши союзники умирали, но продолжали идти за вами, убивая демонов',
                        reply_markup=keyboard)
def four_citadel_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Deamon(hp=1150, attack=75)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        four_citadel_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def four_citadel_b_win(chat_id):
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
            [{'text': 'Прорваться', 'callback_data': 'four_citadel_с'} ]
        ]}
        bot.sendMessage(chat_id, 'Армия врага дрогнула под вашим натиском, хоть вы и потеряли половину солдат, но путь к замку перекрывало не много врагов'
                                 'убив их путь к генералу будет открыт',
                        reply_markup=keyboard)
def four_citadel_с(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Deamon(hp=1350, attack=100)
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        four_citadel_с_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def four_citadel_с_win(chat_id):
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
            [{'text': 'Отдых', 'callback_data': 'four_restore_z'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы смогли наконец прорватся в замок, зачистив первый этаж и заняв позиции, небольшой отдых, сбор трофеев и штурм верхних этажей'
                                 'где прячется генерал',
                        reply_markup=keyboard)
def four_restore_z(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Героическое зелье здоровья','Героическое зелье здоровья',
                                     'Героическое зелье здоровья', 'Героическое зелье маны'])
    restore(chat_id)
    save_players()
    text = 'После отдыха, взяв небольшой отряд, вы принялись штурмовать второй этаж'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'На второй этаж', 'callback_data': 'four_general'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_general(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Прорвашись наверх, вы наконец до брали до тронного зала, войдя в него, вы увидели генерала, сидящего на троне. Чтож'
           'Пора ему умереть!')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Умри!Генерал!', 'callback_data': 'four_general_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def four_general_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Four_general()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        four_general_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def four_general_a_win(chat_id):
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
            [{'text': 'Подготовка', 'callback_data': 'four_general_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Четвертый генерал, наконец пал! Выйдя во двор, вы осмотрели поредевшую армию, этот тяжелый марш'
                                 'по убийство генералов, принес много смертей. Теперь же дорога до замка владыки открыта. Но в нгачале нужно отдохнуть',
                        reply_markup=keyboard)
def four_general_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text ='Вы отдыхали несколько дней, разграбляя цитадель владыки. ПОсле чего вы узнали, что прибыл король с подкреплением, в последний бой поведет он'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Вперед', 'callback_data': 'final_act'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)