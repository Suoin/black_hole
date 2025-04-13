

from scenario import *
one_boss = True
def slaim_guild(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    core = player[chat_id].quest

    player[chat_id].quest = [item for item in core if item != 'Ядро слизи']

    player[chat_id].money += 50
    save_players()
    text ='За выполнения этого квеста, я дам вам один свиток способности'
    description = {
        'Быстрые удары' : 'Серия быстрых ударов',
        'Кровавый удар' : 'Удар вызывающий кровотечение у цели',
        'Ледяной взрыв' : 'Ледяной взрыв быстро охлаждающий цель',
        'Вытягивание маны' : 'С помощью него вы можете вытянуть ману у вараг',
        'Магический выстрел': 'Заряжает стрелу вашей маной',
        'Быстрая стрельба': 'Серия быстрых выстрелов',
        'Стабилизация': 'В свитке говорится, что это способность может открыть новый эффект у способности, какой неизвестно',
        'Нестабильный удар' : 'Для успешного удара вам потребуется """"'

    }
    class_award = {
        'Воин': [
            [{'text': 'Быстрые удары', 'callback_data': 'Быстрые удары'}],
            [{'text': 'Кровавый удар', 'callback_data': 'Кровавый удар'}]
        ],
        'Стрелок': [
            [{'text': 'Магический выстрел', 'callback_data': 'Магический выстрел'},
             {'text': 'Быстрая стрельба', 'callback_data': 'Быстрая стрельба'}],
        ],
        'Везунчик': [
            [{'text': 'Нестабильный удар', 'callback_data': 'Нестабильный удар'}],
            [{'text': 'Стабилизация', 'callback_data': 'Стабилизация'}]
        ],
        'Маг': [
            [{'text': 'Ледяной взрыв', 'callback_data': 'Ледяной взрыв'}],
            [{'text': 'Вытягивание маны', 'callback_data': 'Вытягивание маны'}]
        ]
    }
    player_class = player[chat_id].player_class[0]
    actions = class_award.get(player_class, [])
    abilities_text = ""
    for action in actions:
        for ability in action:
            ability_name = ability['text']
            abilities_text += f"{ability_name}: {description.get(ability_name, 'Описание отсутствует.')}\n"

    # Обновленный текст с описанием
    text = f'{text}\n\nДоступные способности:\n{abilities_text}'

    # Отправляем сообщение
    keyboard = {'inline_keyboard': actions}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def off_town_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    player[chat_id].goblin_complete = True
    inventary = player[chat_id].quest_invetary
    goblin_ear = inventary.count('Ухо гоблина')

    # Удаление всех экземпляров "Ухо гоблина"
    player[chat_id].quest_invetary = [item for item in inventary if item != 'Ухо гоблина']

    # Основной текст и подсчет монет
    text = f'Вам удалось собрать {goblin_ear} ушей, хороший результат для новичка. Каждое ухо оплачивается за 10 монет.\nВы можете выбрать 1 свиток способности.'
    if goblin_ear >= 6:
        player[chat_id].money += 100
    else:
        player[chat_id].money += goblin_ear * 10
    save_players()

    # Описание способностей для каждого класса
    abilities_description = {
        'Рассечение': 'Рассекающий выпад усиленный от вашей ловкости, расходуя вашу энергию.',
        'Взрывной удар': 'Сильный удар усиленный вашей силой и расходует энергию.',
        'Концентрация': 'Увеличивает силу следующего удара, расходует ману.',
        'Яростный крик': 'Пугающий крик, заставляющий врага застыть от страха, расходует ману. ',
        'Прицельный выстрел': 'Точный выстрел в уязвимую точку урон зависит от ловкости, расходует энергию.',
        'Уклонение': 'Позволяет уклониться от атаки врага, расходует энергию. Тест.',
        'Двойной выстрел': 'Быстрый двойной выстрел наносит урон от силы оружия, расходует энергию.',
        'Аура концентрации': 'Усиливает, урон от вашего оружия, расходует ману',
        'Проникающий удар': 'Точный удар, позволяет игнорировать броню врага, расходует энергию',
        'Случайный удар': 'Случайны удар, описание в свитке отсутствует, расходует энергию',
        'Аура': 'Все что известно о этой способности, то что она расходует ману',
        'Неизвестная способность': 'описание на свитке содержало только ...мана',
        'Огненный шар': 'Огненный шар , он везде огненный шар',
        'Ледяные иглы': 'При применение создает облако острых льдинок, обрушивая их на врага',
        'Щит льда': 'Создает вокруг заклинателя щит льда, усиливающий ледяную магию, имеется неизвестный эффект',
        'Щит огня': 'Создает вокруг заклинателя щит огня, усливает огненную магию, имеется неизвестный эффект'
    }

    # Классовые действия (для случая, когда ушей меньше 7)
    class_actions_full = {
        'Воин': [
            [{'text': 'Рассечение', 'callback_data': 'Рассечение'}, {'text': 'Взрывной удар', 'callback_data': 'Взрывной удар'}],
            [{'text': 'Концентрация', 'callback_data': 'Концентрация'}, {'text': 'Яростный крик', 'callback_data': 'Яростный крик'}]
        ],
        'Стрелок': [
            [{'text': 'Прицельный выстрел', 'callback_data': 'Прицельный выстрел'}, {'text': 'Уклонение', 'callback_data': 'Уклонение'}],
            [{'text': 'Двойной выстрел', 'callback_data': 'Двойной выстрел'}, {'text': 'Аура концентрации', 'callback_data': 'Аура концентрации'}]
        ],
        'Везунчик': [
            [{'text': 'Проникающий удар', 'callback_data': 'Проникающий удар'}, {'text': 'Случайный удар', 'callback_data': 'Случайный удар'}],
            [{'text': 'Аура', 'callback_data': 'Аура'}, {'text': 'Неизвестная способность', 'callback_data': 'Неизвестная способность'}]
        ],
        'Маг': [
            [{'text': 'Огненный шар', 'callback_data': 'Огненный шар'}, {'text': 'Ледяные иглы', 'callback_data': 'Ледяные иглы'}],
            [{'text': 'Щит льда', 'callback_data': 'Щит льда'}, {'text': 'Щит огня', 'callback_data': 'Щит огня'}]
        ]
    }

    # Классовые действия (если ушей меньше 7)
    class_actions_limited = {
        'Воин': [
            [{'text': 'Рассечение', 'callback_data': 'Рассечение'}],
            [{'text': 'Концентрация', 'callback_data': 'Концентрация'}]
        ],
        'Стрелок': [
            [{'text': 'Прицельный выстрел', 'callback_data': 'Прицельный выстрел'},
             {'text': 'Уклонение', 'callback_data': 'Уклонение'}],
        ],
        'Везунчик': [
            [{'text': 'Проникающий удар', 'callback_data': 'Проникающий удар'}],
            [{'text': 'Аура', 'callback_data': 'Аура'}]
        ],
        'Маг': [
            [{'text': 'Огненный шар', 'callback_data': 'Огненный шар'}],
            [{'text': 'Щит огня', 'callback_data': 'Щит огня'}]
        ]
    }

    # Выбираем клавиатуру в зависимости от количества ушей
    player_class = player[chat_id].player_class[0]  # Извлекаем строку из списка
    if goblin_ear >= 6:
        available_actions = class_actions_full.get(player_class, [])
    else:
        available_actions = class_actions_limited.get(player_class, [])

    # Формируем описание способностей для доступных кнопок
    abilities_text = ""
    for action in available_actions:
        for ability in action:
            ability_name = ability['text']
            abilities_text += f"{ability_name}: {abilities_description.get(ability_name, 'Описание отсутствует.')}\n"

    # Обновленный текст с описанием
    text = f'{text}\n\nДоступные способности:\n{abilities_text}'

    # Отправляем сообщение
    keyboard = {'inline_keyboard': available_actions}
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
    return goblin_ear
def choise_data_3(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    # Обрабатываем выбор способности
    if data in ['Кровавый удар', 'Быстрые удары', 'Магический выстрел', 'Быстрая стрельба', 'Вытягивание маны', 'Ледяной взрыв',
                'Нестабильный удар', 'Стабилизация']:
        # Добавляем способность в список игрока
        player[chat_id].abillity.append(data)
        save_players()

        # Новый текст после выбора способности
        text = f'Вы получили способность: {data}. Хороший выбор, пока вас не было, приходил человек и разыскивал новичков с вашим классом'

        # Обновленная клавиатура для продолжения
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Узнать подробнее', 'callback_data': 'start_know'}]
            ]
        }

        # Отправляем новое сообщение с текстом и клавиатурой
        bot.sendMessage(chat_id, text, reply_markup=keyboard)


def choise_data_2(chat_id, message_id, data):
    bot.deleteMessage((chat_id,message_id))
    # Обрабатываем выбор способности
    if data in   ['Рассечение','Взрывной удар','Концентрация','Яростный крик','Прицельный выстрел','Уклонение','Двойной выстрел','Аура концентрации',
     'Проникающий удар','Случайный удар','Аура','Неизвестная способность','Огненный шар','Ледяные иглы','Щит льда','Щит огня']:
        # Добавляем способность в список игрока
        player[chat_id].abillity.append(data)
        save_players()

        # Новый текст после выбора способности
        text = f'Вы получили способность: {data}. Хороший выбор, теперь вы можете отправиться на следующий квест'

        # Обновленная клавиатура для продолжения
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Взять квест', 'callback_data': 'take_quest'}]
            ]
        }

        # Отправляем новое сообщение с текстом и клавиатурой
        bot.sendMessage(chat_id, text, reply_markup=keyboard)

def start_know(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Приходил вербовщик, он собирает армию для штурма цитадели генерала Повелителя Тьмы. Я предложила вашу кандидатуру. '
            'Его можно найти у городских ворот — там сейчас собираются войска.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'К воротам','callback_data':'on_gate'},{'text':'в город','callback_data':'in_town'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def in_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Город выглядит уныло, словно он постепенно умирает. Почти не видно жителей, а в разных уголках стоят солдаты. '
            'За те несколько дней, что вы провели, уничтожая слизней, город сильно изменился.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В библиотеку','callback_data':'in_library'},{'text':'На рынок','callback_data':'find_market'}],
            [{'text':'К воротам','callback_data':'on_gate'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def on_market(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('После посещения торговца, вы заметили, '
           'что рынок очень сильно опустел, а торговец у которого вы были, начал закрывать свою лавку')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В библиотеку', 'callback_data': 'in_library'},{'text': 'К воротам', 'callback_data': 'on_gate'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def in_library(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].slaim_see:
        text =('В подземелье вы слышали, что то о каком то монстре, может стоит поискать книгу о нем\n'
               'осталось только вспомнить, о ком шла речь')
        keyboard ={
            'inline_keyboard':[
                [{'text':'Легенды о герое','callback_data':'legend_hero'},{'text':'Сказка \n о драконе','callback_data':'green_dragon'}],
                [{'text':'Справочник монстров','callback_data':'bestary'}]
            ]
        }
    else:
        text = 'Вы в городской библиотеке, в глаза вам бросилось несколько книг'
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Легенды о герое', 'callback_data': 'legend_hero'},
                 {'text': 'Сказка \n о принцессе', 'callback_data': 'green_prince'}],
                [{'text': 'Справочник монстров', 'callback_data': 'bestary'}]
            ]
        }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def book(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Ничего нет'
    if data == 'legend_hero':
        text = ('Вы нашли книгу под названием <b>Легенды о герое</b>. В ней рассказывается о человеке, который жил триста лет назад и победил злого короля. '
                'Однако, после своей победы, он сам превратился в того, кого когда-то победил. Странная и тревожная легенда.')
        player[chat_id].quest.append('Легенды о герое')
    elif data =='green_prince':
        text = ('Вы взяли книгу <b>Сказка о принцессе</b>. Это история о принцессе, чья жизнь была полна трагедий. После каждой смерти она перерождалась, но не находила покоя. '
                'В своих новых жизнях она искала истинную любовь, которая могла бы освободить её от вечного цикла страданий.')
        player[chat_id].quest.append('Сказка о принцессе')
    elif data == 'bestary':
        text = 'Вы взяли <b>Справочник монстров</b>. Это подробная энциклопедия, в которой описаны различные существа, их поведение, предпочтения и образ жизни. '
        player[chat_id].quest.append('Справочник монстров')
    elif data == 'green_dragon':
        player[chat_id].library = True
        save_players()
        text ='Вы взяли книгу <b>Сказка о драконе</b>. В ней рассказывается о зеленом драконе, который обитает в горах и терзает жителей, что живут у подножья. '
        player[chat_id].quest.append('Сказка о драконе')

    keyboard = {
        'inline_keyboard':[
            [{'text':'К воротам','callback_data':'on_gate'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard,parse_mode='HTML')
def on_gate(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы пришли в лагерь, где собирается армия. Спросив у местных, куда вам следует направиться, вы пошли в сторону шатра командира. '
    keyboard = {
        'inline_keyboard':[
            [{'text':'К командиру','callback_data':'commandr'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def commandr(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('<b>«О, новенький решил присоединиться к армии!»</b> — сказал командующий, внимательно осматривая вас. '
            '«Пройдите к вербовщику, он оформит вас. Если у вас есть редкие материалы, передайте их местному кузнецу — он сможет создать оружие на их основе».')

    if 'Магическое ядро' in player[chat_id].quest:
        button = [[{'text':'Отдать ядро','callback_data':'give_core'}]]

    elif 'Ртутное ядро' in player[chat_id].quest:
        button = [[{'text':'Отдать ядро','callback_data':'give_core_a'}]]
    elif 'Клык волка' in player[chat_id].quest:
        button = [[{'text':'Отдать клык','callback_data':'give_touth'}]]
    elif 'Кристалл' in player[chat_id].quest:
        button =[[{'text':'Отдать кристалл','callback_data':'give_crystal'}]]
    else:
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'К вербовщику','callback_data':'in_army'}]
        ] + button
    }

    bot.sendMessage(chat_id,text,reply_markup=keyboard,parse_mode='HTML')
def smite(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Ошибка в логике кода'
    if data == 'give_crystal':
        text = 'Вы пришли к местному кузнецу и отдали кристалл, помимо этого кузнец затребовал все ваши сбережения'
        player[chat_id].money = 0
        player[chat_id].quest.remove('Кристалл')
        save_players()
    elif data == 'give_touth':
        text = 'Вы пришли к местному кузнецу и отдали клык, помимо этого кузнец затребовал все ваши сбережения'
        player[chat_id].money = 0
        player[chat_id].quest.remove('Клык волка')
        save_players()
    elif data == 'give_core_a':
        text = 'Вы пришли к местному кузнецу и отдали ртутное ядро, помимо этого кузнец затребовал все ваши сбережения'
        player[chat_id].money = 0
        player[chat_id].quest.remove('Ртутное ядро')
        save_players()
    elif data == 'give_core':
        text = 'Вы пришли к местному кузнецу и отдали магическое ядро, помимо этого кузнец затребовал все ваши сбережения'
        player[chat_id].money = 0
        player[chat_id].quest.remove('Магическое ядро')
        player[chat_id].quest.remove('Магический свиток')
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'Забрать оружие','callback_data':'take_weapon'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def take_weapon(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Ошибка логики кода, сообщите в отзыве'
    if 'Маг' in player[chat_id].player_class:
        player[chat_id].use_hand.clear()
        player[chat_id].use_hand.append('Магический посох')
        text = 'Вы получили Магический посох, на основе магического ядра, каждая атака восстанавливает ману'
    elif 'Везунчик' in player[chat_id].player_class:
        player[chat_id].use_hand.clear()
        player[chat_id].use_hand.append('Ртутный кинжал')
        text = 'Вы получили ртутный кинжал, он кажется жидким, но постоянно сохраняет форму'
    elif 'Воин' in player[chat_id].player_class:
        player[chat_id].use_hand.clear()
        player[chat_id].use_hand.append('Меч волка')
        text ='Вы получили меч, кузнец назвал его Меч волка, его лезвие по краям усеяно крошкой из зуба волка'
    elif 'Стрелок' in player[chat_id].player_class:
        player[chat_id].use_hand.clear()
        player[chat_id].use_hand.append('Кристаллический лук')
        text = 'Вы получили лук, сделанный из кристала, что по способен изгибаться под натяжением тетивы'
    keyboard = {
        'inline_keyboard':[
            [{'text':'К вербовщику','callback_data':'in_army'}]
        ]
    }
    save_players()
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def in_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вам предложили присоединиться к армии для похода на крепость Повелителя Тьмы. '
            'Пора решить: стать частью этого похода или идти своим путем.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Присоединиться','callback_data':'start_army'},{'text':'Отказаться','callback_data':'stop_army'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def stop_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы отказались от вступления в армию и вернулись в город. '
            'Теперь предстоит подождать, пока армия отправится в поход, и решить, что делать дальше.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Ждать','callback_data':'wait_army'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def wait_army(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))  # Исправлено: передаем два отдельных аргумента

    text ='Нарушение логики'
    # Инициализация пустой клавиатуры
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Ждать', 'callback_data': 'wait_army'}]
        ]
    }

    # Логика обработки данных
    if data == 'wait_army':
        if player[chat_id].wait_town == 3:
            player[chat_id].wait_town -= 1
            text = 'Вы решили подождать несколько дней, когда армия уйдет, возможно что-то тут изменится'
        elif player[chat_id].wait_town == 2:
            player[chat_id].wait_town -= 1
            text = 'Прождав несколько дней, вы заметили, что армия начала готовиться к походу, возможно она скоро уйдет'
        elif player[chat_id].wait_town == 1:
            player[chat_id].wait_town -= 1
            text = 'Наконец, армия ушла в поход, город совсем опустел, возможно вам следует через пару дней выдвинуться за ней'
        elif player[chat_id].wait_town == 0:
            player[chat_id].wait_town -= 1
            text = 'Прождав какое-то время, после ухода армии, на город обрушилась армия монстров, небольшое ополчение, включая вас, встали на защиту города'
            # Изменение клавиатуры для случая защиты
            keyboard = {
                'inline_keyboard': [
                    [{'text': 'На защиту', 'callback_data': 'defende'}]
                ]
            }

    # Отправка сообщения с клавиатурой
    bot.sendMessage(chat_id, text, reply_markup=keyboard)

    # Обработка ситуации с "defende"
def defende(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    text = ('Обороняя город, вы сражались до последнего, но армия монстров продолжала наступать. В какой-то момент ваши силы иссякли, и вы погибли в жестокой схватке. '
            'После вашей смерти монстры устроили резню среди жителей, разрушив всё, что им попадалось на пути, сея хаос и разрушение.')
    bot.sendMessage(chat_id, text)

    kill(chat_id)
    save_players()
def start_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вербовщик передал вам армейское снаряжение и жетон с номером вашего отряда, кратко объяснив, где его найти. '
            'Напоследок он добавил, что через пару дней армия отправляется в поход, и вам стоит подготовиться.')
    player[chat_id].quest.append('Жетон №13-414')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В палатку','callback_data':'base_base'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def base_base(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = (
        'Вы устроились на своей койке в палатке, оставив сумку рядом. Быстро познакомившись с бойцами своего отряда, вы узнали, кто чем занимается. '
        'В следующие несколько дней вы посвятили себя подготовке к предстоящему походу, оттачивая навыки и приводя снаряжение в порядок.')
    if 'Зелье характеристик' in player[chat_id].quest:

        button = [[{'text':'Выпить зелье','callback_data':'water_char'}]]
    else:
        button = []


    keyboard = {
        'inline_keyboard':[
            [{'text':'Ждать похода','callback_data':'wait_start'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def wait_start(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Ошибка логики'
    if data == 'water_char':
        player[chat_id].sila +=10
        player[chat_id].agila +=10
        player[chat_id].intelect +=10
        player[chat_id].luck +=10
        player[chat_id].stamina +=10
        player[chat_id].quest.remove('Зелье характеристик')
        save_players()
        text = ('Вы приняли зелье характеристик, и по телу разлилась волна силы — ваши характеристики увеличились на 10 единиц. '
                'Ощущая себя более уверенно, вы позволили себе немного расслабиться и провести пару дней безделья, пока не прозвучал приказ о сборе.')
    elif data == 'wait_start':
        text = 'Вы провели несколько дней в безделье, пока внезапно не услышали сигнал, созывающий всех на общий сбор.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Общий сбор','callback_data':'sbor_star'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def sbor_star(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия выстроилась, и командир, воспользовавшись магическим усилением голоса, произнес вдохновляющую речь:'
            '"Мы — последняя надежда человечества! Наши жизни, наши мечи и наши сердца защитят этот мир от надвигающейся тьмы!"'
            'После слов, полных решимости, он начал отдавать четкие распоряжения, формируя авангард и основные силы. '
            'В авангард могли отправиться добровольцы, или же вы могли остаться в составе своего отряда.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Основные силы','callback_data':'main_power'},{'text':'Авангард','callback_data':'avangard'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def avangard(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы приняли решение присоединиться к авангарду армии. Собравшись с другими добровольцами, вы начали подготовку к выступлению. '
            'На рассвете отряд должен был отправиться вперед, чтобы расчистить путь для основных сил.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Спать','callback_data':'sleep'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def sleep(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('На рассвете ваш отряд выдвинулся вперед. '
            'Командир дал четкие указания: следовать по маршруту и оставлять опознавательные знаки, чтобы основные силы могли легко найти путь.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Выступаем','callback_data':'spy_go'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def spy_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Ваш отряд выступил в авангарде, прокладывая безопасный маршрут для армии. '
            'При подготовке к движению было предложено сформировать построение, и вам доверили место в первой линии.')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Согласиться','callback_data':'yes'},{'text':'Отказаться','callback_data':'no'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def spy_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Базовое значение'
    if data == 'yes':
        bot.sendMessage(chat_id,'Вы заняли место в первой линии разведки. Продвигаясь через лес, вы внимательно изучали местность, когда неожиданно попали в засаду. '
                                'Стрела молниеносно пробила вашу голову, и всё погрузилось во тьму.')
        kill(chat_id)
        save_players()
    elif data == 'no':
        text = ('Вы заняли место позади отряда, командир вел разведку впереди. Внезапно на вас напала засада, стрела пробила голову того, кто шел впереди. '
                'Теперь вам предстоит выбор: вступить в бой или перегруппироваться и попытаться избежать дальнейших потерь.')
        keyboard = {
            'inline_keyboard':[
            [{'text':'В бой','callback_data':'orc_fight_a'},{'text':'Перегруппироваться','callback_data':'retreat'}]
            ]
        }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)

def retreat(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Группа разведчиков попала в засаду. Когда вы начали отступать, то поняли, что вас зажали в клещи. '
            'Вражеские стрелы летят со всех сторон, и выхода нет. Этот бой был проигран.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def orc_fight_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_a(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_a(chat_id):
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
        text = ('Победив группу орков, вы остановились, чтобы оценить ситуацию. '
                'Нужно было решить, продолжать ли бой с оставшимися орками или же лучше отступить и перегруппироваться.'
                'И позволят ли они вам это сделать? ')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Перегрупироваться', 'callback_data': 'retreat'},{'text': 'Помочь в бою', 'callback_data': 'orc_fight_b'} ]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def orc_fight_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_b(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_b(chat_id):
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
        text = ('Вы справились с орками, устроившими засаду. Пока вы сражались, ваши товарищи уничтожили тех, кто пытался вас зажать в клещи. '
                'Время не ждет, вам предстоит выбрать — осмотреть тела орков на предмет трофеев или помочь раненым, прежде чем будет слишком поздно.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Осмотреть орков', 'callback_data': 'find_orc'},{'text': 'Помочь раненым', 'callback_data': 'help'} ]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def spy_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Базовое значение, если вы его видете, нарушение логикие, сообщите разработчику'
    if data == 'find_orc':
        player[chat_id].quest.append('Меч орка')
        save_players()
        text = ('Осмотрев тела орков, вы нашли интересный меч, который решили взять. После этого вы отдали команду на перегрупировку и взяли на себя командование. '
                'Однако, из-за того, что вы сосредоточились на трофеях и не успели оказать помощь раненым, двое ваших товарищей погибли от ран.')
        keyboard = {
            'inline_keyboard':[
                [{'text':'Перегруппировка','callback_data':'regroup'}]
            ]
        }

    elif data == 'help':
        player[chat_id].help_solider = True
        text = ('Вы осмотрели поле боя. Два солдата лежали неподалеку. Один был ранен не сильно, второй же получил серьезные повреждения. '
                'Вы сосредоточились на оказании помощи тому, кто пострадал сильнее. Пока вы обрабатывали его раны, он пытался что-то сказать.')
        keyboard = {
            'inline_keyboard':[
                [{'text':'Попросить молчать','callback_data':'mute'},{'text':'Выслушать','callback_data':'unmute'}]
            ]
        }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def regroup(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='база'
    if data == 'regroup':
        text = 'Вы перегруппировали отряд, и он готов выдвигаться.'
    elif data == 'mute':

        text = 'Вы попросили раненого помолчать, он замолк. После оказания помощи вы собрали отряд и подготовились к продолжению пути.'
    elif data == 'unmute':
        player[chat_id].history = True
        save_players()
        text = ('Пока вы обрабатывали раны, один из солдат рассказал интересную историю о зеленом драконе, который живет в горах. '
                'Говорят, что сказки о нем не врут — он действительно существует. Закончив обработку ран, вы перегруппировали отряд и были готовы выдвигаться.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Выдвигаемся','callback_data':'spy_go_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def spy_go_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Пройдя дальше, вы заметили небольшой отряд орков который возглавляет довольно крупный орк, по виду довольно опасный, в какой то момент они заметили вас'
            'из его отрядвы выскочил обычный орк и побежал на вас.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'orc_fight_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def orc_fight_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк',hp = 200,attack=25)
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_c(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_c(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].invetary.append('Большое зелье здоровья')
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        text = ('Победив первого орка, который выскочил из-за более крупного, ваш отряд ожидает дальнейших указаний.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'orc_death'},{'text': 'Отступить', 'callback_data': 'retreat_a'} ]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def orc_death(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк-Чемпион',attack=45, hp=4200,mana =200)
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_death(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_death(chat_id):
    if player[chat_id].hp <= 0:
        bot.send(chat_id,'Падая на землю от ран, нанесённых орком-чемпионом, вы почувствовали, как его дубина стремительно опускается на вашу голову.')
        kill(chat_id)
        save_players()
def retreat_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Вы смогли отступить, чтобы продумать стратегию для борьбы с гигантским орком, который явно был слишком силен для открытого сражения. '
            'Если бы вы вступили в бой, скорее всего, весь отряд был бы уничтожен. '
            'Поэтому вы решили устроить засаду: стрелки должны нанести ранения орку, а воины тем временем займутся мелкими орками, чтобы они не мешали')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Засада','callback_data':'orc_champion'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def orc_champion(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк-Чемпион',attack=30,hp =350,mana=120)
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_champion_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_champion_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].invetary.extend(['Большое зелье здоровья', 'Большое зелье здоровья'])
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        text = ('Вы убили орка-чемпиона и нашли большое зелье здоровья. Дальше предстоит решать, что делать.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Помочь в бою', 'callback_data': 'spy_base'},{'text': 'Помочь раненым', 'callback_data': 'spy_base'} ]
        ]}
        bot.sendMessage(chat_id, text,reply_markup=keyboard)
def spy_base(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Битва окончена, раненым оказана помощь, и отряд двинулся дальше. '
            'День близился к концу, и вам нужно было выбрать место для лагеря. '
            'Основные силы двинутся завтра, а вам предстоит продолжить прокладывать маршрут.'
            'Впереди вы заметили пещеру, её темные очертания заставляют почувствовать напряжение, но она может стать хорошим укрытием на ночь. '
            'Либо вы можете устроить лагерь среди деревьев, где тихо, но не так защищено.')
    keyboarad = {
        'inline_keyboard':[
            [{'text':'В пещеру','callback_data':'grove_b'},{'text':'В лес','callback_data':'forest_b'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboarad)
def grove_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы разместились в пещере, и внутри она оказалась намного просторнее, чем казалось снаружи. '
           'Кажется, здесь хватит места для размещения основных сил. '
           'Но, с другой стороны, ощущение, что что-то не так, не покидает вас. '
           'Стоит ли сразу разбить лагерь и отдохнуть или рискнуть и разведать пещеру вглубь?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Разведка пещеры','callback_data':'fight_begemot'},{'text':'Отдых','callback_data':'restore_death'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def restore_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы ушли в сон, больше вы не проснулись')
    kill(chat_id)
    save_players()


def forest_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if player[chat_id].help_solider:
        text = 'Разбив лагерь, вы отдали указания и думаете встать в патруль или пойти на отдых'
        button = [[{'text':'Отдых','callback_data':'restore_life'}]]
    else:
        text = 'Разбив в лагерь и раздав указания, вы взяли еще одного человека и отправились с ним в патруль'
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'В патруль','callback_data':'death_patrol_a'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def death_patrol_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id,data))
    text = 'Патрулируя лагерь, вы заметили отряд орков. Вы отправили напарника поднять тревогу и готовитесь к бою.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'orc_fight_e'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def orc_fight_e(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_e(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_e(chat_id):
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
        text = ('Одолев первого орка, вы заметили, как из-за кустов появляются еще несколько. '
                'Вы тут же атаковали второго, пока третий не мог понять, что происходит.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'orc_death_a'}]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def orc_death_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_death_a(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_death_a(chat_id):
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
        text = ('Остался последний орк. Вы на пределе сил, но другого выбора, кроме как сражаться, у вас нет.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'orc_death_b'}]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def orc_death_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_death_b(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_death_b(chat_id):
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
        text = ('Вы смогли справится с отрядом орков, скоро должно подойти подкрепление. У вас есть время первести дух.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Перевести дух', 'callback_data': 'death_b'}]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def death_b (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Убив орков и немного переведя дух, вы осознаете, что помощь задерживается. Внезапно появляется еще один отряд орков. Это конец.')
    kill(chat_id)
    save_players()


def restore_life(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Вы отправились на отдых, но ваш сон прервал крик о помощи. Один из патрульных будил отряд. '
            'Вы быстро среагировали, подняли всех и отправились на помощь. '
            'Когда прибыли, увидели трех мертвых орков и вашего товарища, которого орк пронзил своим мечом. Они пожалеют об этом!')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'fight_orc_q'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def fight_orc_q(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_q(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_q(chat_id):
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
        text = ('Убив орка, вы переключились на другого, заметив, что ваш отряд постепенно теснит врага, с каждым ударом сокращая их ряды.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Следующий', 'callback_data': 'orc_fight_w'}]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def orc_fight_w(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc = Orc(name='Орк')
    player[chat_id].target = orc
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_win_w(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_win_w(chat_id):
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
        text = ('Расправившись со вторым орком, вы поспешили на помощь остальным, понимая, что каждый момент важен для победы.')
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Добить их', 'callback_data': 'life_a'}]
        ]}
        bot.sendMessage(chat_id, text,
                        reply_markup=keyboard)
def life_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Расправившись с врагом, вы осмотрели тела орков и нашли интересный меч, а также большое зелье здоровья. '
            'После чего продолжили патрулирование. '
            'Немного отдохнув после смены, на рассвете вы отправились в передовой лагерь, чтобы ожидать основные силы.')
    player[chat_id].quest.append('Меч орка')
    player[chat_id].invetary.append('Большое зелье здоровья')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В лагерь','callback_data':'camp_army'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def main_power(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = ('Вы решили остаться с основными силами, понимая, что авангард может столкнуться с засадой и понести потери, в то время как основная армия справится с ситуацией. '
            'Вернувшись в свой отряд, вы стали ждать начала марша основных сил.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Марш армии','callback_data':'go_army_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_army_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Армия следовала по пути, проложенному авангардом, который оставил метки безопасного маршрута и время от времени отправлял сообщения о своем продвижении.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Продолжить путь','callback_data':'go_army_b'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_army_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Продолжая путь, вы достигли места, где авангард столкнулся с врагом. Здесь лежали две могилы. '
            'Если бы вы присоединились к авангарду, возможно, одна из них могла бы стать вашей')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдать почести','callback_data':'press_f'},{'text':'Продолжить','callback_data':'ignore'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def base_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Ошибка логики'
    if data == 'press_f':
        text = ('Отдав почести погибшим воинам, вы догнали армию, которая продолжала двигаться вперед.'
                'Пройдя до заката, она разбила лагерь. Ваш командир отправил вас в шатер совета, сославшись на недомогание.'
                'Внутри шли дебаты: где лучше расположить лагерь — в лесу или в ближайшей пещере? Голоса были равны.'
                'Увидев вас, участники совета сразу обратились с просьбой высказать ваше мнение, зная, что ваш голос может стать решающим.')
    elif data == 'ignore':
        text = ('Пройдя до заката, армия разбила лагерь.\n'
                'Ваш командир отправил вас в шатер совета, сославшись на недомогание. Придя в шатер, там были дебаты.'
                'Где стоит разбить лагерь — в лесу или в ближайшей пещере? Голоса были равные.'
                'Увидев вас, спросили вашего мнения. Ваш голос перевесит чашу весов в ту или иную сторону.'
)
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пещера','callback_data':'grove'},{'text':'Лес','callback_data':'forest_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def grove(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Было принято решение разбить основной лагерь для отдыха в пещере. '
            'Пещера оказалась достаточно просторной, чтобы разместить армию. '
            'Однако кое-что не давало вам покоя: по мелким деталям вы заподозрили, что у этой пещеры может быть хозяин. Вы отбросили эти мысли и готовились ко сну.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдых','callback_data':'restore_a'}]

        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def restore_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вас вырвали из сна: крики и суматоха, армию поднимали по тревоге. '
            'Более-менее придя в себя, вы начали оценивать происходящее, пока не увидели его.'
            ' Огромное чудовище, похожее на гориллу, с белой шерстью и хвостом скорпиона, убивало людей и разрушало лагерь.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'fight_begemot'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def fight_begemot(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    print("Запуск битвы с коллбеком...")
    begemot = Begemot(name='Бегемот')
    player[chat_id].target = begemot
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        begemot_lose(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def begemot_lose(chat_id):
    if player[chat_id].hp <=0:
        bot.sendMessage(chat_id,'Умирая вы чувствовали сожаления, что выбрали пещеру')
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].debuff.clear()
        player[chat_id].stamina += 1

        save_players()

        bot.sendMessage(chat_id, 'Победа не предусмотрена, требуется правка баланса'
                        )
def forest_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Армия выбрала путь через лес, в поисках места для лагеря. Пройдя через него, вы заметили очередное место битвы авангарда с засадой.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Осмотреть','callback_data':'find_battle'},{'text':'В лагерь','callback_data':'a_base_camp'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def a_base_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Базовое значение'
    if data == 'find_battle':
        player[chat_id].quest.append('Меч орка')
        text = ('Осмотрев тела мертвых монстров, вы заметили ценный меч и забрали его. '
                'После этого направились в лагерь, решив, стоит ли отдохнуть или встать на ночной патруль.')
    elif data == 'a_base_camp':
        text = 'Армия нашла место для лагеря. Вы решаете, стоит ли отдохнуть или встать на ночной патруль.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Отдых','callback_data':'dawm'},{'text':'В патруль','callback_data':'go_patrol'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_patrol(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы вызвались в ночной патруль и взяли на себя охрану лагеря, внимательно осматривая темные просторы леса вокруг'
    keyboard ={
        'inline_keyboard':[
            [{'text':'Патрулирование','callback_data':'go_patrol_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_patrol_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'При патрулировании вы заметили шевеление в кустах и разглядели орка-разведчика, осторожно подкрадывающегося к лагерю.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'orc_spy'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def orc_spy(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    orc_spy = Orc(name='Орк разведчик')
    player[chat_id].target = orc_spy
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        orc_spy_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def orc_spy_win(chat_id):
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
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Смена патруля', 'callback_data': 'dawm'} ]
        ]
        }
        bot.sendMessage(chat_id, 'Убив орка, вы продолжили патрулирование. Вскоре к вам подошла новая смена, и вы могли отправиться на отдых.',
                        reply_markup=keyboard)
def dawm(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('На рассвете армия начала собираться к очередному маршу. '
            'Командир сообщил, что скоро мы соединимся с остальными силами, готовящимися к штурму, чтобы завершить подготовку перед решающим сражением.'
            'За цитадель одного из генералов Повелителя Тьмы')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В путь','callback_data':'camp_army'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def camp_army(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('В передовом лагере, стекаются армии из разных городов, марш завершен, и ваша часть войск соединилась с основными силами. '
            'Несколько дней вы предоставлены сами себе. '
            'Заняться в лагере особо нечем, но возможности для отдыха и подготовки к битве есть, возможно есть какие то задания.')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Отдыхать','callback_data':'restore_life_c'},{'text':'Помощь в лагере','callback_data':'help_camp'}],
            [{'text':'Узнать о заданиях','callback_data':'quest_camp'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def help_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили помочь с делами по лагерю и отправились с отрядом рубить лес для заготовки древесины. '
            'После этого вам сообщили, что кузнецу требуется помощь.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдыхать', 'callback_data': 'restore_life_c'},{'text': 'Помощь кузнецу', 'callback_data': 'help_camp_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def help_camp_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Базовая версия'
    if 'Меч орка' in player[chat_id].quest:
        text = ('Вы помогли кузнецу с заточкой оружия, потратив на это целый день. Уже собираясь идти отдыхать, к вам подошел один из солдат. '
                'Он предложил обмен: в обмен на меч орка, который вы нашли ранее, он научит вас новому навыку. '
                'Стоит ли отдать меч и обучиться, или предпочесть отдых?')
        button = [[{'text':'Отдать меч','callback_data':'learn_skill'}]]
    else:
        text = 'Вы помогли кузнецу в заточке оружия, потратив на это целый день. Пора отдохнуть. Слышно, что вернулись разведчики, и армия скоро продолжит свой путь.'
        button = []
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдыхать', 'callback_data': 'restore_life_c'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def learn_skill(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили отдать меч в обмен на обучение. Солдат поблагодарил вас и сказал, что встреча состоится завтра на тренировочной площадке.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Прийти на\n площадку','callback_data':'go_training'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_training(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].luck >= 15:
        text = ('Придя на площадку, вы начали ждать солдата, думая, что он не придет, и уже собирались уйти. '
                'В этот момент он окликнул вас: "Ну что, готов к обучению? Вот чему я тебя научу!"')
        button = [[{'text':'Обучиться','callback_data':'skill_add'}]]
    else:
        text = ('Вы пришли на площадку и ждали вчерашнего солдата, но его всё не было. Кажется, вас обманули. '
                'Вряд ли вы сможете его найти в такой большой армии.')
        button = [[{'text':'Смириться','callback_data':'restore_life_c'}]]
    keyboard ={
        'inline_keyboard':[

        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def skill_add(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Базовый текст, не должен появляться'
    if 'Маг' in player[chat_id].player_class:
        if 'Ледяная стрела' in player[chat_id].abillity:
            text = 'Я научу тебя ледяной буре. Она усиливается, если ты накладываешь на себя усиления ледяной магии'
            player[chat_id].abillity.append('Ледяная буря')
            save_players()
        else:
            text = 'Я научу тебя огненному шторму. Он усиливается, если ты накладываешь на себя усиления огненной магии.'
            player[chat_id].abillity.append('Огненный шторм')
            save_players()
    elif 'Воин' in player[chat_id].player_class:
        text = 'Я научу тебя Вихрю. Это очень энергозатратная способность, но с правильными усилениями результат тебя удивит.'
        player[chat_id].abillity.append('Вихрь')
        save_players()
    elif 'Стрелок' in player[chat_id].player_class:
        text = 'Я научу тебя Граду Стрел. Если у тебя есть усилитель, ты сможешь значительно повысить эффективность этого навыка'
        player[chat_id].abillity.append('Град стрел')
        save_players()
    elif 'Везунчик' in player[chat_id].player_class:
        text = 'Я научу тебя метать кинжал, покрытый маной. После попадания в цель, он вернется обратно к тебе.'
        player[chat_id].abillity.append('Метнуть кинжал')
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'Обучиться','callback_data':'add_skill'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def add_skill(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы провели весь день на тренировке, освоив новый навык. Наконец, настал момент отдохнуть.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Отдохнуть', 'callback_data': 'restore_life_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)

def quest_camp(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили узнать у командира, есть ли задания. '
            'Вам сообщили, что собирается группа разведчиков, которая исследует путь до цитадели генерала Повелителя Тьмы и сообщит о безопасном маршруте. '
            'Хотите присоединиться?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Принять','callback_data':'invite'},{'text':'Отказаться','callback_data':'restore_life_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def invite(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Отряд собран, вас назначили командиром. Готовьтесь к выступлению.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Выдвигаемся','callback_data':'go_patrol_q'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_patrol_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Пройдя от лагеря вперед, вы оказались на распутье, размышляя, какую дорогу стоит разведать. Какой путь окажется безопасней?'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Через лес','callback_data':'forest_go_q'},{'text':'Через горы','callback_data':'mount_go'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def forest_go_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Вы решили пробираться через лес. Углубившись внутрь, заметили отряд орков, кажется, они вас не заметили. '
           'Среди них шло несколько огромных орков')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Атаковать','callback_data':'death_orc_q'},{'text':'Наблюдать','callback_data':'watch'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def death_orc_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы ринулись в бой, и только приблизившись к отряду орков, заметили несколько Орков чемпионов. Бесславный конец.')
    kill(chat_id)
    save_players()
def watch (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили понаблюдать за движением отряда, проверяя, нет ли засады. Среди них оказались Орки чемпионы, сражаться с которыми будет слишком опасно.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Продолжить следить','callback_data':'watch_go'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def watch_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы проследили за орками до выхода из леса и наблюдали, как они направляются к горам. '
            'Отправив сообщение в основной лагерь о безопасности пути, вы задумались: стоит ли ждать армию или последовать за орками?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Следовать за орками','callback_data':'go_orc_watch'},{'text':'Ждать армию','callback_data':'wait_army_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_orc_watch(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы решили последовать за отрядом орков, постепенно понимая, что это разведчики. Куда же они нас приведут?'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Следовать','callback_data':'go_orc_watch_a'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def go_orc_watch_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы последовали за орками дальше. Два из них отстали от отряда, и кажется, их отсутствие не привлекло внимания остальной группы'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Убить орков','callback_data':'kill_orc'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def kill_orc(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы быстро расправились с отставшими орками и снова нагнали их отряд. '
            'Видя, как они исчезают в ущелье, вы задумываетесь: стоит ли рискнуть и последовать за ними?')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пойти за орками','callback_data':'kill_orc_a'},{'text':'Вернуться в лес','callback_data':'wait_army_c'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def kill_orc_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы зашли в ущелье вслед за орками, и на полпути их внимание переключилось на вас. '
                            'Приготовившись к бою, вы уже готовы были вступить в схватку, когда внезапно сверху обрушилось яростное пламя..'
                            'Дракон вышел на охоту в ущелье...')
    kill(chat_id)
    save_players()

def mount_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы подошли к подножью горы, осматривая окрестности. '
            'Камни под ногами скользкие, но вы продолжаете двигаться вдоль подножья, внимательно ища вход в ущелье, которое могло бы скрывать путь дальше. '
            'Туман легким слоем обвивает скалы, скрывая возможные опасности и указывая на то, что место не так безопасно, как казалось на первый взгляд.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вперед','callback_data':'moung_go_a'}]]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def moung_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Наконец, вы нашли вход в ущелье. Темные стены нависают над вами, и внутри ощущается холодный воздух. '
            'Звуки природы отдаляются, поглощаемые узким коридором. Стоит ли рискнуть и войти в неизвестное, или лучше продолжить поиск другого пути?')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Дальше', 'callback_data': 'moung_go_b'},{'text': 'В ущелье', 'callback_data': 'mount_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def moung_go_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вдалеке виднелся полуразрушенный храм, у входа стояла старая статуя дракона, покрытая мхом и трещинами.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Осмотреть', 'callback_data': 'dragon_kill'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def dragon_kill(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы подошли к храму, который явно был заброшен много лет. Половина крыши обвалилась, а статуя дракона казалась готовой вот-вот рухнуть.'
                            'Притронувшись к статуе, вы услышали треск, и она начала осыпаться. Каменная голова дракона рухнула прямо на вас')
    kill(chat_id)
    save_players()

def mount_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы зашли в ущелье и, пройдя до середины, заметили выход впереди. Ваш взгляд также остановился на узкой тропе, ведущей вверх по склону.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'К выходу', 'callback_data': 'moung_go_death'}, {'text': 'На тропу', 'callback_data': 'mount_b'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def moung_go_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы продолжали движение, приближаясь к выходу из ущелья. Оставалось менее километра до конца пути.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Идти', 'callback_data': 'dragon_kill_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def dragon_kill_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы почти достигли выхода из ущелья, когда заметили отряд орков, движущийся вам навстречу. '
            'Вы уже приготовились к бою, как вдруг сверху обрушилось пламя. Зеленый дракон вышел на охоту.')
    bot.sendMessage(chat_id, text)
    kill(chat_id)
    save_players()
def mount_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if player[chat_id].history and player[chat_id].slaim_see and player[chat_id].library:
        text =('Поднявшись по тропе, вы обнаружили небольшой уступ, окружённый скалами, словно путь никуда не ведёт. Однако что-то показалось вам знакомым. '
               'Вспомнив историю из книги или рассказ солдата, которого вы лечили, вы заметили углубление в скале. '
               'Засунув руку внутрь, вы нащупали кнопку. Нажать её или уйти?')
        button = [[{'text':'Нажать','callback_data':'green_dragon_start'}]]
    else:
        text = ('Поднявшись по тропе, вы оказались на небольшом уступе. '
                'Дальше пути не было, словно тропа вела в никуда. Возможно, стоит вернуться и проверить дорогу через лес.')
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Уйти','callback_data':'forest_go_p'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def forest_go_p(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы решили уйти и вернулись к развилке.'
            'Проведя разведку через лес и убедившись в безопасности пути, вы отправили сообщение основным силам и стали ждать прибытия армии.')
    keyboard = {
        'inline_keyboard': [
                               [{'text': 'Ждать армию', 'callback_data': 'wait_army_c'}]
                           ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def green_dragon_start(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))


    text = ('Вы нажали на кнопку, и стена в скале медленно распахнулась. Пройдя внутрь, вы оказались в кратере остывшего вулкана.'
            'В центре покоился огромный зеленый дракон. Его глаза вспыхнули, заметив вас, и, несмотря на свои размеры, он молниеносно сорвался с места. '
            'В считаные мгновения от вашего отряда остались только вы')
    keyboard = {
            'inline_keyboard':[
                [{'text':'В бой','callback_data':'green_dragon_fight'}]
            ]
        }

    bot.sendMessage(chat_id,text,reply_markup=keyboard)



def green_dragon_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    save_players()
    print("Запуск битвы с коллбеком...")
    dragon = Green_dragon(name='Зеленый дракон')
    player[chat_id].target = dragon
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        green_dragon_fight_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def green_dragon_fight_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 10
        player[chat_id].debuff.clear()
        player[chat_id].green_dragon = True
        print("Переход к следующей сцене")
        restore(chat_id)
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Выпить кровь дракона', 'callback_data': 'blood_dragon'},{'text':'Оставить кровь','callback_data':'blood_dragon_a'} ]
        ]}
        bot.sendMessage(chat_id, 'После тяжелого боя с драконом вы одержали победу. '
                                 'Вам было известно, что кровь зеленого дракона обладает большой ценностью. '
                                 'Говорили, что если ее выпить, то можно обрести силу самого дракона.',
                        reply_markup=keyboard)
def dragon_win(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if data == 'blood_dragon':
        if 'Маг' in player[chat_id].player_class:
            player[chat_id].abillity.append('Лечение')
            text = ('Вы почувствовали , как кровь дракона растеклась по вашим жилам и ощутили новую способность\n'
                    'ЛЕЧЕНИЕ')
            save_players()
        else:
            player[chat_id].abillity.append('Регенерация')
            text = ('Вы почувствовали , как кровь дракона растеклась по вашим жилам и ощутили новую способность\n'
                    'РЕГЕНИРАЦИЯ')
            save_players()
    elif data == 'blood_dragon_a':
        text = ('Собрав немного вытекающей крови дракона, вы решили оставить ее у себя, возможно получиться ее выгодно продать\n'
                'после войны или раньше')
        player[chat_id].quest.append('Кровь дракона')
        save_players()
    else:
        text = 'Вы собрали не много крови с туши мертвого дракона, возможно она еще пригодиться'
        player[chat_id].quest.append('Кровь дракона')
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пойти через лес','callback_data':'army_wait_q'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def army_wait_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].green_dragon:
        text = ('Вы вернулись к распутью. После гибели всего отряда в битве с драконом вы в одиночку разведали безопасный путь. '
                'Отправив сообщение армии, вы остались ждать ее прибытия.')
    else:
        text = ('Вы вернулись к распутью, провели разведку через лес и убедились в безопасности пути. '
                'Отправив сообщение армии, вы остались ждать ее прибытия.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Ждать армию', 'callback_data': 'wait_army_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def restore_life_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    save_players()
    text = 'Через пару дней поступил приказ на построение — армия готовилась к выдвижению.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В путь', 'callback_data': 'army_go_q'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def army_go_q(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Огромная армия выстроилась в походный строй, вам осталось выбрать где занять место'
    keyboard = {
        'inline_keyboard':[
            [{'text':'В начале','callback_data':'army_go_w'},{'text':'В середине','callback_data':'army_go_w'}],
            [{'text':'В конце','callback_data':'army_go_w'}]
        ]
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)

def army_go_w(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы заняли позицию и стали ждать приказа, наконец армия начала свое движение к цитадели врага'
    keyboard = {
        'inline_keyboard': [
            [{'text':'В путь','callback_data':'go_army_enemy'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def go_army_enemy(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Армия начала свой путь по данным разведчиков, пройдя к развилке, был отдан приказ идти дорогой через лес'
    keyboard = {
        'inline_keyboard':[
            [{'text':'В лес','callback_data':'army_go_forest'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def army_go_forest(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия двигалась вперед, рассекая лесную чащу своим маршем. '
            'Взглянув вдаль, вы заметили величественные горы, окутанные легкой дымкой. '
            'На миг вам показалось, что над одной из вершин гор парит огромная фигура, напоминающая дракона.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Дальше','callback_data':'roundew'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def roundew(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'roundew':
        text = ('Выйдя из леса, вы наткнулись на группу разведчиков, терпеливо ожидавших прибытия основных сил. '
                'Они быстро присоединились к армии, и вскоре вы продолжили путь к цитадели.')

    else:
        text = ('Дождавшись прибытия основной армии, вы присоединились к её рядам. '
                'После доклада перед командующим вам вручили награду: два зелья здоровья и одно зелье маны. '
                'Армия, собрав силы, продолжила свой путь вперёд.')
        player[chat_id].invetary.extend(['Большое зелье маны', 'Большое зелье здоровья', 'Большое зелье здоровья','Большое зелье здоровья'])
        save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'К цитадели','callback_data':'citadel'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Армия достигла вражеской цитадели и разбила лагерь неподалёку. '
            'Началась подготовка: авангард собирался выступить первым, прокладывая путь для основных сил, которые последуют за ним. '
            'Но в воздухе витала тревога — казалось, авангарду уготован билет в один конец.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'В авангард','callback_data':'win_path'},{'text':'Основные силы','callback_data':'lose_path'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def lose_path(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Авангард двинулся вперёд, скрываясь за горизонтом. Вы остались с основными силами, ожидая своего часа. '
            'Долгое напряжённое ожидание было, наконец, прервано: раздалась команда в атаку.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В атаку', 'callback_data': 'lose_path_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def lose_path_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Основные силы ринулись к проломленным воротам, у которых громоздилось тело павшего гиганта. Огр? '
            'Возможно. Армия ворвалась в центральный двор и разделилась: одна часть направилась к цитадели, другая — к высокой башне.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'К цитадели', 'callback_data': 'citadel_lose'},
             {'text': 'К башне', 'callback_data': 'tower_lose'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tower_lose(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Часть армии устремилась к башне, и вы оказались среди её рядов. '
            'Когда вы приблизились к величественному сооружению, с его вершины внезапно посыпались горугилии, обрушивая хаос и смерть на наступающих.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Бой', 'callback_data': 'lose_path_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def lose_path_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    gorgula = Gorgula(name='Каменная горгулья')
    player[chat_id].target = gorgula
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        gorgula_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def gorgula_win(chat_id):
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
            [{'text': 'К воротам', 'callback_data': 'door'} ]
        ]}
        bot.sendMessage(chat_id, 'Отряд быстро расправился с горгульями, и, преодолев преграды, уже почти подошел к воротам башни.',
                        reply_markup=keyboard)
def door(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы уже приблизились к двери башни, быстро соорудив таран из подручных средств. '
            'Дверь была выбита, открывая путь внутрь. В этот момент прибыл гонец, сообщивший о необходимости отправить часть сил к цитадели. '
            'Вам предстоит выбрать: отправиться туда или войти в башню, возможно, именно там находится генерал.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'К цитадели', 'callback_data': 'citadel_lose_b_a'},
             {'text': 'В башню', 'callback_data': 'tower_lose_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tower_lose_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы ворвались в башню, стремительно зачистив орков, удерживавших её внизу. '
            'Пройдя через падших врагов, вы заметили лестницу, ведущую наверх, в темные высоты башни.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Наверх', 'callback_data': 'tower_lose_b'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def tower_lose_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы поднимались по лестнице, уже на её середине, когда, выглянув через смотровое окно, увидели снаряд катапульты, стремительно приближающийся к вам. '
            'Погибнуть от дружественного огня… Какое невезение!')
    kill(chat_id)
    save_players()
def citadel_lose(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы направились с частью армии к цитадели, и ваши взгляды упали на тела товарищей из авангарда. Битва была для них тяжёлой. Не легче будет и для вас. '
            'Из мелких зданий начали выходить орки, закованные в тяжёлую броню, готовые сражаться до последнего.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'Помочь в бою','callback_data':'citadel_lose_b'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def citadel_lose_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'citadel_lose_b_a':
        text = 'Вы поспешили на помощь армии которая сражалась с орками рыцарями и тут же ринулись в бой'
    else:
        text = 'Орки рыцари начали окружать вас, пора готовиться к бою'

    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'citadel_lose_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def citadel_lose_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ork = Orc(name='Орк рыцарь',hp =350)
    player[chat_id].target = ork
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        citadel_lose_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def citadel_lose_win(chat_id):
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
            [{'text': 'Следующий', 'callback_data': 'citadel_lose_w'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив орка рыцаря, вы переключили внимание на следующего',
                        reply_markup=keyboard)
def citadel_lose_w(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы сошлись в ожесточённой схватке с очередным орком, когда внезапно поле боя накрыл залп стрел. '
            'С вершины цитадели монстры обрушили смертоносный град. Смерть под градом стрел стала неизбежной.')
    kill(chat_id)
    save_players()
def win_path(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы вызвались в авангард. Возможно, позже вы об этом пожалеете, но шанс сразиться с генералом владыки тьмы и убить его выпадает крайне редко.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'На штрум', 'callback_data': 'win_path_a'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def win_path_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Добравшись до ворот в стене, вы столкнулись с огромным гигантом, окружённым множеством орков. '
            'Огр? Возможно. Но это не имеет значения — он должен пасть, иначе ваш штурм захлебнётся прямо здесь.')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'На штрум', 'callback_data': 'win_path_fight'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def win_path_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Ogr(name='Огр привратник')
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        win_path_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def win_path_win(chat_id):
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
            [{'text': 'Во двор', 'callback_data': 'win_path_c'} ]
        ]}
        bot.sendMessage(chat_id, 'Огромная туша огра, своим падением пробила ворота, путь открыт вперед!',
                        reply_markup=keyboard)
def win_path_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'restart':
        restore(chat_id)
        save_players()
        text = ('Вы снова оказались во дворе, накануне штурма цитадели. '
                'Вы живы, хотя были уверены, что генерал убил вас. Амулет, который был у вас, рассыпался на мелкие осколки. Возможно, это дар судьбы — второй шанс?')
    else:
        text = ('Вы ворвались во двор, и, похоже, обитатели крепости ещё не осознали, что штурм уже начался. '
                'Продвигаясь вперёд, вы заметили движение на верхних этажах — орки-лучники заняли позиции. Кажется, они готовятся открыть обстрел.')
    keyboard = {
            'inline_keyboard': [
                [{'text': 'Прорываться', 'callback_data': 'win_lose'},{'text':'В укрытие','callback_data':'lose_win'}],
                [{'text':'Довериться судьбе','callback_data':'win_luck'}]
            ]
        }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def citadel_room(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'win_lose':
        text = ('Вы рванули вперёд, пытаясь прорваться до того, как смертоносный град стрел накроет вас. '
                'Но пары шагов не хватило — десятки стрел пронзили ваше тело, погружая всё вокруг во мрак.')
        bot.sendMessage(chat_id,text)
        kill(chat_id)
        save_players()
    elif data == 'lose_win':
        text = ('Вы попытались найти укрытие, но вокруг не оказалось ничего подходящего. '
                'Слишком опрометчиво... С ужасом вы наблюдали, как смертоносный град стрел обрушивается на вас,')
        bot.sendMessage(chat_id, text)
        kill(chat_id)
        save_players()
    else:
        text = ('Вы решили довериться судьбе и двинулись вперёд, прямо на врага. '
                'Вокруг ваших товарищей косил смертоносный град стрел, но вам везло — ни одна из них не достигла цели. '
                'Вы продолжали путь, пока не добрались до цитадели. Выживших больше не было — вы остались один.')
        keyboard = {
            'inline_keyboard':[
                [{'text':'В цитадель','callback_data':'win_citadel'}]
            ]
        }
        bot.sendMessage(chat_id,text,reply_markup=keyboard)
def win_citadel(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Вы вошли в цитадель, зная, что лёгкой прогулки не будет. Орки-рыцари, стекающиеся из её глубин, явно не собираются позволить вам пройти без боя.'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В бой', 'callback_data': 'win_citadel_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def win_citadel_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ork = Orc(name='Орк рыцарь',hp= 300)
    player[chat_id].target = ork
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        win_citadel_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def win_citadel_a_win(chat_id):
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
            [{'text': 'Следующий', 'callback_data': 'win_citadel_b'} ]
        ]}
        bot.sendMessage(chat_id, 'Вы убили одного орка рыцаря, как вышел второй, чтож это будет не легко',
                        reply_markup=keyboard)
def win_citadel_b(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ork = Orc(name='Орк рыцарь', hp=300)
    player[chat_id].target = ork
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        win_citadel_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def win_citadel_b_win(chat_id):
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
            [{'text': 'Убить демона!', 'callback_data': 'demon'} ]
        ]}
        bot.sendMessage(chat_id, 'Убив орка и пройдя на второй этаж, ваш путь преградил демон, все же это армии владыки тьмы',
                        reply_markup=keyboard)
def demon(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ork = Deamon(name='Демон-страж')
    player[chat_id].target = ork
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        demon_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def demon_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].invetary.extend(['Большое зелье здоровья','Большое зелье здоровья'])
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Перевести дух', 'callback_data': 'general_a'} ]
        ]}
        bot.sendMessage(chat_id, 'Справившись с демоном, вы решили перевести дух и залечить ранения',
                        reply_markup=keyboard)
def general_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Отдохнув, вы продолжили свой путь. '
            'Подойдя к массивным дверям, заметили меньшую дверь, которая, похоже, вела в тот же зал. Или всё-таки стоит рискнуть и пройти через парадный вход?')
    restore(chat_id)
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'Массивная дверь', 'callback_data': 'general_b'},{'text':'Маленькая дверь','callback_data':'its_trap'}]
    ]}
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def its_trap(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Зайдя в малую дверь, вы оказались в темном коридоре. '
            'Дверь, через которую вы вошли, закрылась, и на её месте опустилась тяжёлая стена. '
            'Стены начали сжиматься, и смерть прямо перед самым финалом битвы.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def general_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Приложив все силы, вы отворили огромные двери, и перед вами открылся огромный зал. '
            'В его центре стояло чудовище, которое вы видели у ворот. Не дождавшись, оно сразу ринулось на вас, готовое к схватке.')
    keyboard = {'inline_keyboard': [
        [{'text': 'В бой', 'callback_data': 'general_c'}]
    ]}
    bot.sendMessage(chat_id, text,
                    reply_markup=keyboard)
def general_c(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    ogr = Ogr(name='Огр', hp = 650,max_hp=650)
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
        bot.sendMessage(chat_id, 'Убив огра, вы осмотрели зал. Впереди виднелась дверь, очевидно ведущая в тронный зал. Генерал скрывается там?',
                        reply_markup=keyboard)
def general_e(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы подготовились к бою, перевязав все раны. Чувствуете, как ваша мана постепенно восполняется, пока вы отдыхаете. Что ж, пора убить генерала владыки тьмы.'
            'Проверили тела, убитых монстров и нашли несколько банок зелья здоровья')
    player[chat_id].invetary.extend(['Большое зелье здоровья','Большое зелье здоровья'])
    restore(chat_id)
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'В тронный зал', 'callback_data': 'general_w'}]
    ]}
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def general_w(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Амулет предвестника' in player[chat_id].quest or 'Странный амулет' in player[chat_id].quest_invetary:
        text = (' О, герой, ты смог пройти так далеко, — голос раздался из темноты. — Я вижу у тебя амулет. '
                'Если ты отдашь его, ты сможешь присоединиться к армии владыки тьмы. Это принесёт тебе власть и богатство.')
        button = [[{'text':'Отдать амулет','callback_data':'lose_trap'}]]
    else:
        text = 'Герой, ты смог пройти так далеко, но тут закончиться твой путь, готовься к смерти!'
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Убить генерала!','callback_data':'death_general'}]
        ]+button
    }
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def lose_trap(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы передали амулет генералу владыки тьмы, но вдруг, неожиданно, почувствовали холодный металл, вонзающийся в ваше сердце.'
            ' — Глупец, зачем ты нужен владыке? — раздался голос. — Бесполезный человек.')
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def death_general(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    if one_boss:
        if 'Кровь дракона' in player[chat_id].quest:

            general = First_general(name='Генерал Марцелиус',hp =1600)
            player[chat_id].target = general
            player[chat_id].in_battle = True
            save_players()
            # Создаем коллбек для завершения битвы
            def on_battle_end(chat_id):
                print(f"Коллбек на завершение битвы вызван для {chat_id}")
                death_general_win(chat_id)

            # Сохраняем коллбек в объекте игрока
            player[chat_id].on_battle_end = on_battle_end

            # Логируем коллбек перед передачей
            print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
            battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока
        else:
            general = First_general(name='Генерал Марцелиус')
            player[chat_id].target = general
            player[chat_id].in_battle = True
            save_players()

            # Создаем коллбек для завершения битвы
            def on_battle_end(chat_id):
                print(f"Коллбек на завершение битвы вызван для {chat_id}")
                death_general_win(chat_id)

            # Сохраняем коллбек в объекте игрока
            player[chat_id].on_battle_end = on_battle_end

            # Логируем коллбек перед передачей
            print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
            battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока
    else:
        text = 'Владыка мертв, его убил один из героев в осколке миров'
        keyboard = {
            'inline_keyboard':[
                [{'text':'К армии','callback_data':'general_win_first'}]
            ]
        }
        bot.sendMessage(chat_id,text,reply_markup=keyboard)
def death_general_win(chat_id):
    if player[chat_id].hp <= 0:
        if 'Амулет предвестника' in player[chat_id].quest or 'Странный амулет' in player[chat_id].quest_invetary:
            text = (
                'Кажется, вы погибли. В темноте раздаётся чей-то голос, будто он пробивает мрак. — Еще один шанс... вернись туда, где ты доверился судьбе.')

            # Удаляем "Амулет предвестника", если он есть
            if 'Амулет предвестника' in player[chat_id].quest:
                player[chat_id].quest.remove('Амулет предвестника')

            # Удаляем "Странный амулет", если он есть
            if 'Странный амулет' in player[chat_id].quest_invetary:
                player[chat_id].quest_invetary.remove('Странный амулет')

            button = [[{'text': 'Вернуться', 'callback_data': 'restart'}]]
            keyboard = {
                'inline_keyboard': [] + button
            }
            bot.sendMessage(chat_id, text, reply_markup=keyboard)
        else:
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
            [{'text': 'Забрать осколок брони', 'callback_data': 'general_win_first'}]
        ]}
        bot.sendMessage(chat_id,
                        'Генерал владыки тьмы повержен, он рассыпался в прах, а его броня раскололась на тысячу осколков',
                        reply_markup=keyboard)


def general_win_first(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].one_boss = True
    save_players()
    text = ('Вы одержали победу над генералом владыки тьмы. Осталось еще трое и сам владыка! '
            'Армия добивала остатки выживших — монстры не должны жить, крепость должна быть очищена. '
            'Пока шла зачистка, вы заметили, как к цитадели летела стая каких-то чудовищ.')
    keyboard = {
        'inline_keyboard':[
            [{'text':'К бою','callback_data':'act_two'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)