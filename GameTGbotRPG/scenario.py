

from data import player,save_players
from config import bot
from bestiari import *
import telepot
from battle_commands import *
def load(chat_id,message_id,data):
    player[chat_id].stamina = 145
    player[chat_id].max_mana = 100
    player[chat_id].mana = 100
    player[chat_id].sila = 20
    player[chat_id].agila = 112
    player[chat_id].luck = 20
    player[chat_id].intelect = 100
    #player[chat_id].invetary.append('Большое зелье здоровья')
    #player[chat_id].invetary.extend(['Героическое зелье здоровья','Героическое зелье здоровья'])

    player[chat_id].use_hand.append('Звездный лук')
    player[chat_id].abillity.extend(['Выстрел навскидку','Двойной выстрел','Магический выстрел'])
    player[chat_id].quest.extend(['Меч орка','Кровь дракона','Чешуйка черного дракона','Язык дракона','Когти дракона'])
    restore(chat_id)
    save_players()
    keyboard = {
        'inline_keyboard':[
        [{'text':'Загрузка','callback_data':'final_army_go_c'}]
        ]
    }
    bot.sendMessage(chat_id,'Загружаемся',reply_markup=keyboard)
def start_game_1 (chat_id,message_id):
    bot.deleteMessage((chat_id, message_id))
    text = ('Вы открыли глаза, перед вами сидела красивая женщина. <b>Я богиня</b> -, произнесла она. Тебе не повезло\n'
            'Какой бы ты выбор не сделал, ты бы все равно погиб. Я же позволю тебе переродиться в новом мире,'
            'где каждый твой выбор важен. В моем мире завелся владыка тьмы и уничтожает мой мир. <b>Я расколола свой мир на множество частей</b>'
            'Даже если ты погибнешь, ты сможешь возродится в одном из осколков и снова можешь попытаться спасти мир.\n'
            'А теперь я даю тебе первый выбор, <b>выбери свои способности</b>:')
    keyboard = {'inline_keyboard': [
        [{'text': 'Удача', 'callback_data': 'luck'}, {'text': 'Воин', 'callback_data': 'melee'}],
        [{'text': 'Магия', 'callback_data': 'magic'}, {'text': 'Стрелок', 'callback_data': 'range'}]
    ]
    }
    bot.sendMessage(chat_id,text , reply_markup=keyboard,parse_mode='HTML')  # Отправляем клавиатуру пользователю

def choise_data (chat_id,message_id, data):

    bot.deleteMessage((chat_id, message_id))
    if chat_id in player:
        if data == 'luck':
            player[chat_id].luck +=5
            player[chat_id].player_class.append('Везунчик')
            restore(chat_id)
            save_players()
            player_class = 'Везунчик'
            stats.update_class_stats(player_class, 'created')
            stats.created += 1
            stats.update_alive()  # Обновляем количество живых игроков
            save_players()  # Сохраняем состояние в модули
            save_stats(stats)
            forest_star(chat_id, message_id)
        elif data == 'melee':
            player[chat_id].sila += 5
            player[chat_id].player_class.append('Воин')
            restore(chat_id)
            save_players()
            player_class = 'Воин'
            stats.update_class_stats(player_class, 'created')
            stats.created += 1
            stats.update_alive()  # Обновляем количество живых игроков
            save_players()  # Сохраняем состояние в модули
            save_stats(stats)
            forest_star(chat_id, message_id)
        elif data == 'range':
            player[chat_id].agila += 5
            restore(chat_id)
            player[chat_id].player_class.append('Стрелок')
            save_players()
            player_class = 'Стрелок'
            stats.update_class_stats(player_class, 'created')
            stats.created += 1
            stats.update_alive()  # Обновляем количество живых игроков
            save_players()  # Сохраняем состояние в модули
            save_stats(stats)
            forest_star(chat_id, message_id)
        elif data == 'magic':
            player[chat_id].intelect += 5
            restore(chat_id)
            player[chat_id].player_class.append('Маг')
            save_players()
            player_class = 'Маг'
            stats.update_class_stats(player_class, 'created')
            stats.created += 1
            stats.update_alive()  # Обновляем количество живых игроков
            save_players()  # Сохраняем состояние в модули
            save_stats(stats)
            forest_star(chat_id, message_id)

def forest_star(chat_id, message_id):
    print(f'\n{player[chat_id].name}:{player[chat_id].player_class} Появился в этом мире')
    if 'Маг' in player[chat_id].player_class:
        text = 'Применить магию'
        callback = 'use_magic'
    elif 'Стрелок' in  player[chat_id].player_class:
        text = 'Сделать оружие'
        callback = 'craft_weapon'
    elif 'Воин' in player[chat_id].player_class:
        text ='Поискать оружие'
        callback = 'find_weapon'
    elif 'Везунчик' in player[chat_id].player_class:
        text = 'Внимательно осмотреться'
        callback = 'find_amul'

    keyboard = {
        'inline_keyboard': [
            [{'text': 'Идти прямо', 'callback_data': 'go_forward'}, {'text': 'Осмотреться', 'callback_data': 'osmotr'}],
            [ {'text': 'крикнуть СТАТУС!', 'callback_data': 'status'}],
            [{'text': text, 'callback_data': callback}]

        ]
    }
    bot.sendMessage(chat_id, 'Вы оказались на лесной опушке, ваши действия? Потом сделать описание и картинку',
                    reply_markup=keyboard)  # Отправляем клавиатуру пользователю
def status_rofl(chat_id,message_id,data):
    if 'Везунчик' in player[chat_id].player_class:
        stat = player[chat_id].show_stat()
        text ='Неожиданно, перед вами всплыло окно характеристик, интересный результат'
        buttons = [['СТАТУС', "/start"], ['Развитие', 'Отзыв'],
                   ['Пожертвование']
                   ]  # Настраиваем нужные кнопки
        keyboard = {'keyboard': buttons,
                    'resize_keyboard': True}  # Создаем Реплуклавиатуру , ставит размер пользователя
        bot.sendMessage(chat_id,f'{stat}')
        bot.sendMessage(chat_id,text,reply_markup =keyboard)
    else:
        bot.sendMessage(chat_id,'После того как вы заорали <b>"СТАТУС"</b>, ничего не произошло\n'
                                'Из-за этого вы начали чувствовать себя крайне глупо',parse_mode='HTML')
def find_weapon(chat_id,message_id,data):

    bot.deleteMessage((chat_id, message_id))
    if data == 'use_magic':
        player[chat_id].abillity.append('Стрела огня')
        save_players()
        bot.sendMessage(chat_id, 'Вы представили словно кидаете огненное копье, неожиданно в вашей руке материализовалась огненная стрела.\n'
                                 'Бросив ее, она разлетелась об дерево и подожгла местность вокруг удара ')
    elif data == 'find_amul':
        player[chat_id].quest_invetary.append('Странный амулет')
        player[chat_id].abillity.append('Быстрый удар')
        player[chat_id].use_hand.append('Стальной кинжал')
        save_players()
        bot.sendMessage(chat_id, 'Внимательно осмотрев поляну, в траве вы заметили что то блестящее\n'
                                 'это был странной формы амулет и какой то кинжал')
    elif data == 'find_weapon':
        player[chat_id].use_hand.append('Меч-палка')
        player[chat_id].abillity.append('Выпад')
        save_players()
        bot.sendMessage(chat_id, 'Осмотрев поляну и ближайший куст, вы отломали ветку\n'
                                 'которая более менее была похоже на меч, лучше уж так, чем совсем без оружия')
    elif data == 'craft_weapon':
        player[chat_id].use_hand.append('Самодельный лук')
        player[chat_id].abillity.append('Выстрел навскидку')
        save_players()
        bot.sendMessage(chat_id, 'Изучив местность и ближайший куст обтянутый лозами и лианами, вы смастерили себе лук.\n'
                                 'Осмотрев его, вы задумались, что в детстве делали куда лучше')

    if 'Стрела огня' in player[chat_id].abillity:
        text = 'По практиковаться в магии'
        callback = 'magic_practical'
    if 'Странный амулет' in player[chat_id].quest_invetary:
        text ='Рассмотреть амулет'
        callback = 'inspect_amulet'
    elif 'Самодельный лук'in player[chat_id].use_hand:
        text = 'По практиковаться в стрельбе'
        callback ='shot_bow'
    elif 'Меч-палка'in player[chat_id].use_hand:
        text = 'Сделать взмах мечом'
        callback = 'shot_sword'
    keyboard = {'inline_keyboard': [
        [{'text': 'Идти прямо', 'callback_data': 'go_forward'}],
        [ {'text': text, 'callback_data': callback}]
    ]
    }
    bot.sendMessage(chat_id, 'Вас удовлетворил результат',
                    reply_markup=keyboard)  # Отправляем клавиатуру пользователю



def osmotr(chat_id,message_id,data):
    bot.sendMessage(chat_id, 'Вы стоите на поляне посреди леса, впереди виднеется тропа, возможно она ведет в город?')
def goblin_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    player[chat_id].goblin_flag = True
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'Уйти', 'callback_data': 'go_forward'},
         {'text': 'Атаковать ', 'callback_data': 'goblin_fight_start'}]
    ]}
    bot.sendMessage(chat_id, 'Вы слышите шум из кустов и заметили как из них задом пятится гоблин',
                    reply_markup=keyboard)


#
# Функция начала битвы с монстром
def goblin_fight_start(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы ...")
    goblin = Goblin(name='Молодой гоблин',attack=15,hp=50)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True
    save_players()
    # Создаем  для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        goblin_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока

def goblin_win(chat_id):
    if player[chat_id].hp <=0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina +=1
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Пойти в город', 'callback_data': 'go_forward'},
             {'text': 'Осмотреть гоблина', 'callback_data': 'goblin_inspect'}]
        ]}
        bot.sendMessage(chat_id, 'Одолев гоблина, вы рассмотрели его труп, возможно это был детеныш гоблина, уж слишком он мелкий',
                        reply_markup=keyboard)
def goblin_inspect(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))

    player[chat_id].quest_invetary.append('Ухо гоблина')
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'Пойти в город', 'callback_data': 'go_forward'}]
    ]}
    bot.sendMessage(chat_id, 'Осмотрев тело гоблина, вы поискали, что можно было бы с него забрать. К вашему разочарованию, у него не было ничего.\n'
                             'В итоге, вы взяли каменный нож гоблина и отрезали с трупа его ухо. Вы слышали, в своем мире, что так делают в фентези мирах',
                    reply_markup=keyboard)



def go_forward(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {'inline_keyboard': [
        [{'text': 'Поискать гильдию', 'callback_data': 'find_guild'}, {'text': 'Осмотреть город', 'callback_data': 'inscpect_town'}],
        [{'text':'Поискать рынок','callback_data':'find_market'}]
    ]
    }
    bot.sendMessage(chat_id, 'Вы решили пойти по тропинке, что вела с лесной поляны. Через некоторое время, вы вышли к небольшому городу.\n'
                             'Стражи на входе не было, хотя по вашим знаниям, что то похожее должно быть. Кое какие знания о фентази мире начали всплывать'
                             'у вас в голове. \n Возможно стоит поискать гильдию авантюристов или сходить на рынок, посмотреть как все тут устроено.',
                    reply_markup=keyboard)  # Отправляем клавиатуру

#СЮЖЕТНАЯ ЛИНИЯ И СЦЕНЫ ГОРОДА, СЕКРЕТНЫЙ КВЕСТ НА ГОБЛИНОВ, КВЕСТ НА СЛАЙМОВ, ОСМОТР ГОРОДА, РЫНОК

# ЗОНА РЕАЛИЗАЦИИ РЫНКА
price = {
    'Ухо гоблина': 30,
    'Странный амулет': 10
}

def find_market(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))  # Удаляем предыдущее сообщение
    if data == 'sell_Ухо гоблина':
        player[chat_id].quest_invetary.remove('Ухо гоблина')
        player[chat_id].money += 30
        save_players()
        bot.sendMessage(chat_id, '<b>Вы продали ухо гоблина за 30 монет</b>',parse_mode='HTML')
    elif data == 'sell_Странный амулет':
        player[chat_id].quest_invetary.remove('Странный амулет')
        player[chat_id].money += 10
        save_players()
        bot.sendMessage(chat_id,'<b>Вы продали странный амулет за 10 монет</b>',parse_mode='HTML')
    # Проверяем значение флага guild_visit у игрока
    if not player[chat_id].guild_visit:
        leave_callback = 'back_off'
    elif player[chat_id].slaim_complete:
        leave_callback = 'on_market'
    elif player[chat_id].slaim:
        leave_callback = 'slaim_go'

    else:
        leave_callback = 'back_on'

    # Формируем клавиатуру
    keyboard = {'inline_keyboard': []}

    # Сообщение о том, что мы можем купить предметы, и их цены
    price_message = "Я могу купить у вас:\n"
    for item in player[chat_id].quest_invetary:
        price_item = price.get(item, 0)  # Получаем цену предмета из словаря price
        price_message += f"{item} по цене {price_item} золотых\n"  # Формируем текст с ценой

        # Добавляем кнопки с названиями предметов
        callback = f"sell_{item}"  # Формируем callback для продажи предмета
        keyboard['inline_keyboard'].append([{'text': item, 'callback_data': callback}])

    # Добавляем кнопку "Купить товары" в конце списка
    keyboard['inline_keyboard'].append([{'text': 'Купить товары', 'callback_data': 'buy_items'}])

    # Добавляем кнопку "Уйти" в любом случае
    keyboard['inline_keyboard'].append([{'text': 'Уйти', 'callback_data': leave_callback}])

    # Отправляем сообщение с описанием цен
    bot.sendMessage(chat_id, price_message, reply_markup=keyboard)


def buy_market(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))  # Удаляем предыдущее сообщение
    if data == 'vial_hp':
        player[chat_id].money -= 10
        player[chat_id].invetary.append ('Зелье здоровья')
        save_players()
        bot.sendMessage(chat_id,'<b>Вы приобрели зелье здоровья</b>',parse_mode='HTML')
    elif data == 'vial_mana':
        player[chat_id].money -= 10
        player[chat_id].invetary.append ('Зелье маны')
        save_players()
        bot.sendMessage(chat_id,'<b>Вы приобрели зелье маны</b>',parse_mode='HTML')
    elif data == 'vial_char':
        if player[chat_id].money < 100:
            bot.sendMessage(chat_id,'У вас не достаточно денег')
        else:
            player[chat_id].money -= 100
            player[chat_id].quest.append ('Зелье характеристик')
            save_players()
            bot.sendMessage(chat_id, '<b>Вы приобрели зелье характеристик</b>',parse_mode='HTML')

    # Проверяем деньги игрока
    if player[chat_id].money >= 10:
        # Сообщение с предложением купить зелья
        text = ("Я могу продать вам зелья:\n"
                "Зелье здоровья за 10 монет, восстанавливает 70 очков здоровья\n"
                "Зелье маны за 10 монет, восстанавливает 70 очков маны\n"
                "Зелье характеристик за 100 монет, на всегда прибавляет 10 очков всех характеристик\n"
                "Выбирай что приобретешь")

        # Формируем инлайн-кнопки для покупки зелий
        keyboard = {
            'inline_keyboard': [
                [{'text': 'Зелье здоровья', 'callback_data': 'vial_hp'}],
                [{'text': 'Зелье маны', 'callback_data': 'vial_mana'}],
                [{'text': 'Зелье характеристик', 'callback_data': 'vial_char'}]
            ]
        }
    else:
        # Сообщение, если у игрока недостаточно денег
        text = "У вас недостаточно денег для покупок."
        keyboard = {'inline_keyboard': []}  # Начинаем с пустой клавиатуры

    # Определяем callback для кнопки "Уйти" в зависимости от флага guild_visit
    if not player[chat_id].guild_visit:
        leave_callback = 'back_off'
    elif player[chat_id].slaim_complete:
        leave_callback = 'on_market'
    elif player[chat_id].slaim:
        leave_callback = 'slaim_go'
    else:
        leave_callback = 'back_on'

    # Добавляем кнопку "Уйти" в любом случае
    keyboard['inline_keyboard'].append([{'text': 'Уйти', 'callback_data': leave_callback}])

    # Отправляем сообщение с клавиатурой
    bot.sendMessage(chat_id, text, reply_markup=keyboard)


#ЛИНИЯ ОСМОТРА ГОРОДА И КВЕСТ ДЛЯ ВЕЗУНЧИКА
def inspect_town(chat_id, message_id, data): # Для простых случай если надо сделать 1-2 проверки
    bot.deleteMessage((chat_id, message_id))
    keyboard = {'inline_keyboard': []}

    if 'Везунчик' in player[chat_id].player_class and player[chat_id].group_foward :
        text = 'Осматривая город и изучая его, вы выяснили где находится рынок и гильдия и заметили странную группу в балахонах.'
        keyboard['inline_keyboard'].append([{'text': 'Следовать за группой', 'callback_data': 'group_foward'}])
    else:
        text = 'Осматривая город и изучая его, вы не нашли ничего примечательного, вы выяснили где находится гильдия искателей и где рынок.'

    # Добавляем общие кнопки
    keyboard['inline_keyboard'].append(
        [{'text': 'Пойти в гильдию', 'callback_data': 'find_guild'},
         {'text': 'Пойти на рынок', 'callback_data': 'find_market'}]
    )

    bot.sendMessage(chat_id, text, reply_markup=keyboard)

def group_foward(chat_id,message_id,data):  #Для сложных структур, если надо проверять много условий для пременнной
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].group_foward = False
    save_players()
    if 'Странный амулет' in player[chat_id].quest_invetary:
        text =('Вы проследовали за группой в балахонах, они скрылись за поворотом\n'
               'Как только вы решили последовать за ними, как почувствовали что найденный амулет начал вибрировать\n'
               'словно прося вас немного подождать')
        add_button = [[{'text':'Подождать', 'callback_data':'wait_a'}]]
    else:
        text ='Вы проследовали за группой в балахонах, они скрылись за поворотом'
        add_button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Уйти','callback_data':'back_off'},{'text':'Следовать за ними','callback_data':'foward_death'}]
        ]+ add_button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def foward_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы решили проследовать за группой людей дальше, зайдя поворот, вы получили удар ножом в шею.\n'
                            'Последнее что вы услышали, "У нас тут крыса"')

    kill(chat_id)
    save_players()
def wait_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Уйти','callback_data':'back_off'},{'text':'Зайти в здание','callback_data':'go_home'}],
            [{'text':'Подслушать','callback_data':'evaesdrop'}]
        ]
    }

    bot.sendMessage(chat_id,'Выждав некоторое время, пока амулет не перестал вибрировать, вы двинулись вслед за группой\n'
                            'Нагнав их за следующим поворотом, вы заметили как они зашли в небольшое здание.\n'
                            'Стоя у двери, вы снова почувствовали как вибрирует амулет',
                    reply_markup=keyboard)
def go_home(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы решили проследовать за группой и аккуратно открыли дверь, проползли внутрь, закрыли дверь\n'
                            'Обернулись, на вас смотрели удивленные культисты, ваш конец был трагичен')
    kill(chat_id)
    save_players()
def evaesdrop(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest_invetary.remove('Странный амулет')
    player[chat_id].quest.append ('Амулет предвестника')
    save_players()
    keyboard ={
        'inline_keyboard':[
        [{'text':'Уйти','callback_data':'back_off'}]
    ]
    }
    bot.sendMessage(chat_id,'Вы подкрались к окну и начали вслушиваться в разговор из него вы поняли\n'
                            'Что найденный вами амулет, это амулет предвестника, который меняет судьбу\n'
                            'Позволяет избежать решения, которое приводит к смерти',reply_markup=keyboard)

#ЛИНИЯ ГИЛЬДИИ КВЕСТЫ И ПОЛУЧЕНИЯ ОРУЖИЯ ЕСЛИ ПРОПУСТИЛ ГОБЛИНА НА СТАРТЕ

def find_guild(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    if 'Стрела огня' in player[chat_id].abillity or any(
            item in player[chat_id].use_hand for item in ['Меч-палка', 'Самодельный лук', 'Стальной кинжал']
    ):
        # Выполняем действие, если одно из условий выполняется

        text ='Рассказать свою историю'
        callback = 'history'
    else:
        text = 'Узнать о мире'
        callback ='get_weapon'


    keyboard = {'inline_keyboard': [
        [{'text': text, 'callback_data': callback}]

    ]
    }
    bot.sendMessage(chat_id, 'Некоторое время побродив по городу, вы наконец то нашли здание, похожее на фентезийную гильдию\n'
                             'Зайдя внутрь здания, внутри вы увидели суету, люди сидели за столами, стояли у стен, шум голосов\n'
                             'Вы подошли к стойки регистрации за которой стояла девушка, подойдя к ней, она спросила чем она может помочь?',
                    reply_markup=keyboard)  # Отправляем клавиатуру

def get_weapon(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))

    player_class = player[chat_id].player_class
    message = ""

    # Подготовка оружия или способности в зависимости от класса
    if 'Везунчик' in player_class:
        weapon = 'Стальной кинжал'
        description = ('девушка дала вам регистрационную карту и протянула вам стальной кинжал\n'
                       'Со словами: он вам пригодится в ваших странствиях\n'
                       'Толком никто не знает как повышаются у вашего класса характеристики, вам предстоит это узнать самостоятельно')
        player[chat_id].use_hand.append(weapon)
    elif 'Маг' in player_class:
        weapon = 'Ледяная стрела'
        description = ('девушка дала вам регистрационную карту и протянула свиток с заклинанием\n'
                       'Как только вы к нему прикоснулись, вас окутал синий свет, и вы поняли, что выучили заклинание Ледяная стрела\n'
                       'Когда вы применяете заклинания, вы тратите ману, а так же каждое успешное заклинание повышает ваш интелект\n'
                       'Урон заклинаний зависит от вашего интелекта и возможно чего-то еще')
        player[chat_id].abillity.append(weapon)
    elif 'Воин' in player_class:
        weapon = 'Меч-палка'
        description = ('девушка дала вам регистрационную карту и протянула вам деревянный меч\n'
                       'Со словами: он вам пригодится в ваших странствиях\n'
                       'Когда вы наносите успешный удар, ваша сила возрастает, а урон зависит от нее\n'
                       'Удачи в ваших странствиях')
        player[chat_id].use_hand.append(weapon)
    elif 'Стрелок' in player_class:
        weapon = 'Самодельный лук'
        description = ('девушка дала вам регистрационную карту и положила на стойку неказистый лук со стрелами\n'
                       'Вот возьмите, он хоть и сделан начинающими мастерами, но лучше иметь хоть такое оружие, чем ничего\n'
                       'Когда вы успешно поражает цель стрелой, болтом или пулей, ваша ловкость возрастает\n'
                       'От чего возрастает урон ваших атак, вам предстоит разобраться в этом самостоятельно')
        player[chat_id].use_hand.append(weapon)
    else:
        bot.sendMessage(chat_id, "Ваш класс не поддерживается.")
        return

    # Отправка сообщения об оружии/способности
    message = f'Рассказав о мире, правилах, {description}'
    save_players()
    bot.sendMessage(chat_id, message)

    # Клавиатура с дальнейшими действиями
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Поблагодарить', 'callback_data': 'guild_quest'}]
        ]
    }

    stat = player[chat_id].show_stat()

    buttons = [['СТАТУС', "/start"], ['Развитие', 'Отзыв'],
                   ['Пожертвование']
                   ]  # Настраиваем нужные кнопки
    keyboard_1 = {'keyboard': buttons,
                    'resize_keyboard': True}  # Создаем Реплуклавиатуру , ставит размер пользователя

    bot.sendMessage(chat_id, 'Девушка за стойкой объяснила вам, как вызвать ваши характеристики снизу вы увидели иконку СТАТУС', reply_markup=keyboard_1)
    bot.sendMessage(chat_id, f'{stat}')
    bot.sendMessage(chat_id,
                        'Заполнив регистрационную карту и вернув ее девушке администратору, она сообщила, что вы теперь зарегистрированный наемник\n'
                        'и можете получать задания в гильдиях по всему государству.',
                        reply_markup=keyboard)



def history(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))

    # Словарь для хранения информации о каждом классе
    class_info = {
        'Везунчик': (
            'Об вашем классе, почти ничего неизвестно, как повышаются характеристики и от чего зависит урон\n'
            'Вам предстоит это выяснить самостоятельно'
        ),
        'Маг': (
            'Ваш класс Маг, урон ваших заклинаний зависит от вашего интеллекта\n'
            'Известно, что когда вы применяете успешно заклинание, он повышается\n'
            'Отчего зависит объем маны, до сих пор не ясно'
        ),
        'Воин': (
            'Ваш класс Воин, урон зависит от вашей силы, чем вы сильнее, тем сильнее бьете\n'
            'Участвуя в битвах и нанося урон врагам, ваша сила может возрасти'
        ),
        'Стрелок': (
            'Ваш класс Стрелок, известно что урон зависит от вашей ловкости\n'
            'Когда вы успешно поражаете цель стрелой, пулей или болтом, ловкость может возрасти'
        )
    }

    # Проверка, какой класс игрока содержится в списке player_class
    player_class_list = player[chat_id].player_class
    message = 'Ваш класс неизвестен или пока не описан.'
    for class_name, description in class_info.items():
        if class_name in player_class_list:
            message = f'Выслушав ваш рассказ, девушка рассказала про ваш класс\n{description}'
            break

    bot.sendMessage(chat_id, message)

    # Клавиатура с дальнейшими действиями
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Поблагодарить', 'callback_data': 'guild_quest'}]
        ]
    }
    stat = player[chat_id].show_stat()

    buttons = [['/kill', "/start"], ['/stat', 'Suo'],
               ['СТАТУС']
               ]  # Настраиваем нужные кнопки
    keyboard_1 = {'keyboard': buttons,
                  'resize_keyboard': True}  # Создаем Реплуклавиатуру , ставит размер пользователя

    bot.sendMessage(chat_id,
                    'Девушка за стойкой объяснила вам, как вызвать ваши характеристики снизу вы увидели иконку СТАТУС',
                    reply_markup=keyboard_1)
    bot.sendMessage(chat_id, f'{stat}')

    bot.sendMessage(chat_id,
                    'После своего рассказа, она протянула вам регистрационный бланк, который вы заполнили и вернули ей\n'
                    'В ответ вы услышали, что можете теперь брать задания наемников по всему государству',
                    reply_markup=keyboard)

# Выбор квеста
def guild_quest(chat_id, message_id, data): # ОБУЧАЮЩАЯ ФУНКЦИЯ ДЛЯ МЕНЯ, НА ОСНОВЕ НЕЕ БУДЕТ РЕАЛИЗОВАН РЫНОК
    bot.deleteMessage((chat_id, message_id))
    player[chat_id].guild_visit = True # фиксируем посещение гильдии, для того чтоб если игрок уходит с рынка не возвращался на шаг назад
    save_players()
    keyboard = {
        'inline_keyboard': []
    }

    # Создаем список для хранения текущего ряда кнопок
    button_row = []

    # Проверяем наличие 'Ухо гоблина'
    if 'Ухо гоблина' in player[chat_id].quest_invetary:
        text = 'Показать ухо'
        callback = 'Показать ухо'
        button_row.append({'text': text, 'callback_data': callback})
    elif player[chat_id].goblin_flag == True and 'Ухо гоблина'not in player[chat_id].quest_invetary:
        text = 'Рассказть о гоблине'
        callback = 'say_goblin'
        button_row.append({'text': text, 'callback_data': callback})

    # Добавляем кнопку "Спросить про квест"
    button_row.append({'text': 'Спросить \nпро квест', 'callback_data': 'slaim'})

    # Добавляем текущий ряд в клавиатуру, если он заполнен
    if len(button_row) == 2:
        keyboard['inline_keyboard'].append(button_row)
        button_row = []  # очищаем ряд для следующих кнопок

    # Добавляем дополнительные кнопки
    # Пример дополнительных кнопок для обучения
    #button_row.append({'text': 'Кнопка 3', 'callback_data': 'button_3'})
    #button_row.append({'text': 'Кнопка 4', 'callback_data': 'button_4'})

    # Добавляем один ряд кнопок, если он заполнен
    if len(button_row) == 2:
        keyboard['inline_keyboard'].append(button_row)

    # Если осталась одна кнопка в ряду, добавляем её в отдельный ряд
    if button_row and len(button_row) < 2:
        keyboard['inline_keyboard'].append(button_row)

    bot.sendMessage(chat_id,
                    'Вы решили поинтересоваться у девушки насчет заданий',
                    reply_markup=keyboard)


# ЛИНИЯ НА КВЕСТ ПОД ГОРОДОМ
def slaim(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].accept_goblin:
        text =('Понимаю ваши опасения насчет, того что вы не справитесь, тогда могу предложить вам другое задание\n'
               'Зачистка слизи в городской канализации, за каждое ядро слизи что вы принесете, вы получите по 10 монет\n'
               'Так же перед началом задания, рекомендую посетить рынок, если вы смогли заработать деньги')
    else:
        text = ('У меня есть для вас задание на зачистку слизи в городской канализации.\n'
                'За каждое ядро что вы принесете вы получите по 10 монет\n'
                'Так же перед началом задания, рекомендую посетить рынок, если вы смогли заработать деньги')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Взять задание','callback_data':'take_quest'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def take_quest(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].slaim = True
    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'На рынок','callback_data':'find_market'},{'text':'На задание','callback_data':'slaim_go'}]
        ]
    }

    bot.sendMessage(chat_id,'Слизни, что то вроде паразитов живучих в канализациях, но так никто не хочет убирать канализации\n'
                            'Мы предлагаем новичкам такие задания, как тренировка способностей, да вы правы по сути это просто уборка канализации',
                    reply_markup=keyboard)
def slaim_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    restore(chat_id)
    keyboard = {
        'inline_keyboard': [
            [{'text':'Спуститься','callback_data':'slaim_start'}]
        ]
    }
    bot.sendMessage(chat_id,'После отдыха перед заданием. Вы стоите перед входом в канализацию, до вашего носа доносится ужасный запах канализации',reply_markup=keyboard)
def slaim_start(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пойти по коридору','callback_data':'slaim_forward'},{'text':'Осмотреться','callback_data':'slaim_osmotr'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы спустились в канализационные туннели, резкий неприятный запах ударил в нос, по всюду раздавался шум воды'
                            'из зловонной реки. Туннели были тускло освещены редкими магическими лампами',
                    reply_markup=keyboard)
def slaim_osmotr(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Пойти по коридору', 'callback_data': 'slaim_forward'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы осмотрелись вокруг и поняли, что оказались в туннелях. '
                            'Ничего примечательного: центральный водосток с неприятным запахом, полутьма, '
                            'создаваемая редко расположенными светящимися камнями',reply_markup=keyboard)

def slaim_forward(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пойти на звук','callback_data':'slaim_go_a'},{'text':'Повернуть','callback_data':'slaim_route'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы стоите у развилки. Впереди слышен странный звук, а из поворота ничего не доносится',reply_markup=keyboard)
def slaim_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Атаковать','callback_data':'slaim_attack_a'},{'text':'Вернуться','callback_data':'slaim_forward'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы увидели небольшое желеобразное существо, похожее на наземную медузу. '
                            'Оно подпрыгивало к стене и отскакивало назад. Кажется, это и есть монстр-слизь. '
                            'Почему то в голове у вас всплыло имя "Римуру" ',
                    reply_markup=keyboard)
def slaim_attack_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Простая слизь',attack=5,hp=40)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_attack_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def slaim_attack_a_win(chat_id):
    if player[chat_id].hp <=0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].quest.append('Ядро слизи')
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'К повороту', 'callback_data': 'slaim_route'},]
        ]}
        bot.sendMessage(chat_id, 'Вы победили простую слизь и забрали ее ядро',
                        reply_markup=keyboard)
def slaim_route(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Маг' in player[chat_id].player_class:
        text = ('Вы прошли вглубь канализации. Впереди слышен звук, который вы уже слышали ранее. '
                'Также вы заметили, что со стеной рядом что-то не так')
        button = [[{'text':'Осмотреть стену','callback_data':'slaim_inspect_wall'}]]
    else:
        text = 'Вы прошли вглубь канализации. Впереди слышен звук, который вы уже слышали ранее'
        button = []
    keyboard ={
        'inline_keyboard':[
            [{'text':'Идти дальше','callback_data':'slaim_forward_a'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_inspect_wall(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Надавить ','callback_data':'slaim_push'},{'text':'Уйти','callback_data':'slaim_forward_a'}]
        ]
    }
    bot.sendMessage(chat_id,'Осматривая стену, вы заметили кирпич, который слегка выступает',reply_markup=keyboard)
def slaim_push(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Зайти','callback_data':'slaim_boss_a'},{'text':'Уйти','callback_data':'slaim_forward_a'}]
        ]
    }
    bot.sendMessage(chat_id,'Надавив на кирпич, вы услышали звук механизма, и перед вами открылась дверь. Стоит ли туда заходить?',reply_markup=keyboard)
def slaim_boss_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Магическая слизь', attack=25, hp=400)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_boss_a_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_boss_a_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Магическое ядро')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Выйти\nиз команты', 'callback_data': 'slaim_forward_c'}, ]
        ]}
        bot.sendMessage(chat_id, 'После победы над огромной слизью вы забрали необычное ядро, источающее ману.',
                        reply_markup=keyboard)
def slaim_forward_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Напасть','callback_data':'slaim_attack_b'}]
        ]
    }
    bot.sendMessage(chat_id,'Пройдя дальше, вы увидели слизь, беззаботно ползающую кругами',reply_markup=keyboard)
def slaim_attack_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Простая слизь',attack=5,hp=50)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_attack_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_attack_b_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Ядро слизи')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Идти дальше', 'callback_data': 'slaim_forward_c'}, ]
        ]}
        bot.sendMessage(chat_id, 'Вы победили простую слизь и забрали ее ядро',
                        reply_markup=keyboard)
def slaim_forward_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Идти дальше','callback_data':'slaim_forward_e'},{'text':'Проползти','callback_data':'slaim_death_a'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы продолжили свой путь по туннелю, и свет вокруг стал тускнеть с каждым шагом. '
                            'Впереди снова раздался знакомый звук, который вы уже слышали раньше. '
                            'Внимание привлек небольшой тоннель, в который, похоже, можно проползти. '
                            'Возможно, это будет лучший путь, чтобы обойти темный участок впереди',reply_markup=keyboard)
def slaim_death_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы проползли дальше вглубь туннеля и вдруг почувствовали, как вас начинают обвивать многочисленные слизни. '
                            'Какая глупая смерть — быть поглощённым этими тварями')
    kill(chat_id)
    save_players()
def slaim_forward_e(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Атаковать','callback_data':'slaim_attack_e'}]
        ]
    }
    bot.sendMessage(chat_id,'Впереди вы заметили слизь, упёршуюся в стену и, похоже, пытающуюся пройти через неё',reply_markup=keyboard)
def slaim_attack_e(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Простая слизь',attack=5,hp=50)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_attack_e_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_attack_e_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Ядро слизи')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Идти дальше', 'callback_data': 'slaim_forward_i'}, ]
        ]}
        bot.sendMessage(chat_id, 'Вы победили простую слизь и забрали ее ядро',
                        reply_markup=keyboard)
def slaim_forward_i(chat_id,message_id,data): # на карте это точка 3*слизь
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Осторожно выглянуть','callback_data':'slaim_visual'},{'text':'Резко выйти','callback_data':'slaim_speed'}]
        ]
    }
    bot.sendMessage(chat_id,'Пройдя дальше, вы наткнулись на полутёмный поворот. Прислушавшись, вы не уловили ни единого звука.',reply_markup=keyboard)
def slaim_visual(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'slaim_speed':
        text = ('Вы внезапно выскочили из-за угла, и в какой-то момент вам показалось, что это было глупо. '
                'Впереди раздался звук, исходящий от слизи, напоминающий её характерное шуршание.')
    else:
        text = 'Осторожно выглянув из-за угла и не обнаружив врагов, вы решили продолжить путь дальше.'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Идти дальше','callback_data':'slaim_go_1'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_go_1(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Амулет предвестника' in player[chat_id].quest or 'Странный амулет' in player[chat_id].quest_invetary:
        text = ('Вы подошли к развилке. Где-то впереди звук, который издаёт слизь, стал отчетливее. Слева вы заметили проём. '
                'Когда вы взглянули в него, амулет на вашем шее начал вибрировать, как будто предупреждая вас не стоит поворачивать')
    else:
        text = 'Вы продолжили путь и остановились у развилки. Слева тянулся тёмный коридор без освещения, и впереди слышно шуршание слизи'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Напасть на слизь','callback_data':'slaim_attack_i'},{'text':'Повернуть на лево','callback_data':'slaim_death_i'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_death_i(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Повернув налево, вы прошли десяток метров, но в темноте не заметили обрыв. Не успев среагировать, '
                            'вы упали в канализационную реку, и смерть от токсинов настигла вас — это была жуткая и противная смерть')
    kill(chat_id)
    save_players()
def slaim_attack_i(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Простая слизь',attack=5,hp=50)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_attack_i_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_attack_i_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Ядро слизи')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Идти дальше', 'callback_data': 'slaim_forward_2'}, ]
        ]}
        bot.sendMessage(chat_id, 'Вы победили простую слизь и забрали ее ядро',
                        reply_markup=keyboard)
def slaim_forward_2(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Пройдя вперёд, вы достигли очередной развилки. Справа тянулся полу тёмный коридор, а впереди видели очертания слизня.'
    keyboard ={
        'inline_keyboard':[
            [{'text':'Пройти вперед','callback_data':'slaim_forward_3'},{'text':'Повернуть вправо','callback_data':'slaim_right'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_right(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Повернув в темный коридор и пройдя по нему, вы увидели новый поворот'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вернутся назад','callback_data':'slaim_forward_3'},{'text':'Пойти дальше','callback_data':'slaim_go_2'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_go_2(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Повернув снова, вы увидели очертания стены впереди. Похоже, это тупик, но стоит в этом убедиться.'
    keyboard={
        'inline_keyboard':[
            [{'text':'Подойти к стене','callback_data':'slaim_go_wall'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_go_wall(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Везунчик' in player[chat_id].player_class:
        text = 'Подойдя к стене, вы заметили странность — она казалась хлипкой чем выглядела, и вам стало ясно, что если ударить её с силой, она поддастся'
        button = [[{'text':'Ударить стену','callback_data':'slaim_boss_b'}]]
    else:
        text = 'Подойдя к стене, вы не заметили ничего не обычного, стена как стена'
        button = []
    keyboard = {
        'inline_keyboard':[
            [{'text':'Вернутся к слизи','callback_data':'slaim_forward_3'}]
        ]+button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def slaim_forward_3(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Простая слизь', attack=5, hp=50)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_attack_final_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_attack_final_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Ядро слизи')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Идти дальше', 'callback_data': 'slaim_forward_4'}, ]
        ]}
        bot.sendMessage(chat_id, 'Вы победили простую слизь и забрали ее ядро',
                        reply_markup=keyboard)
def slaim_forward_4(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Пройдя дальше, вы вернулись к выходу. Похоже, ваше задание подошло к концу — пора вернуться в гильдию и отчитаться о выполнении.'
    player[chat_id].slaim_complete = True
    save_players()
    keyboard = {
        'inline_keyboard':[
        [{'text':'К выходу','callback_data':'slaim_exit'}]
    ]}
    bot.sendMessage(chat_id, text,reply_markup=keyboard)
def slaim_exit(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))

    # Инициализация текста и клавиатуры по умолчанию
    text = ''
    keyboard = {
        'inline_keyboard': [
            [{'text': 'В гильдию', 'callback_data': 'slaim_guild'},
             {'text': 'Оглянуться', 'callback_data': 'slaim_see_2'}]
        ]
    }

    # Обработка события "slaim_see_2"
    if data == 'slaim_see_2':
        text = ('Вы оглянулись, чтобы вновь посмотреть на то место, где вы сражались, и услышали чей-то голос, '
                'говорящий о драконе.')
        player[chat_id].slaim_see = True
        save_players()
        keyboard = {
            'inline_keyboard': [
                [{'text': 'В гильдию', 'callback_data': 'slaim_guild'}]
            ]
        }
    # Обработка завершения гоблинского квеста
    elif player[chat_id].goblin_complete:
        text = ('После гнезда гоблинов это казалось почти лёгким испытанием. '
                'Вы чувствуете, как ваша сила возросла. Что же ждёт вас впереди?')
    # Обработка события для новичка
    else:
        text = ('Это было нелегко для новичка, только что оказавшегося в этом мире. '
                'Вы надеетесь, что со временем станете сильнее. Что же приготовил для вас следующий этап?')

    # Отправка сообщения
    bot.sendMessage(chat_id, text, reply_markup=keyboard)

def slaim_boss_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    slaim = Slaim(name='Ртутная слизь', attack=25, hp=400)
    player[chat_id].target = slaim
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        slaim_boss_b_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока


def slaim_boss_b_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].quest.append('Ртутное ядро')
        print("Переход к следующей сцене")
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Вернутся к слизи', 'callback_data': 'slaim_forward_3'}, ]
        ]}
        bot.sendMessage(chat_id, 'После победы над огромной слизью, вы забрали необычное ядро из жидкого металла',
                        reply_markup=keyboard)
# ЛИНИЯ КВЕСТА НА ПЕЩЕРУ ГОБЛИНОВ
def show_ear(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].accept_goblin = True
    player[chat_id].money += 30
    player[chat_id].quest_invetary.remove('Ухо гоблина')
    save_players()
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Принять', 'callback_data': 'accept'}, {'text': 'Отказаться', 'callback_data': 'denai'}]
        ]
    }
    text = ('Девушка забрала у вас ухо гоблина и аккуратно положила его в специальный контейнер. '
            'Затем она отсчитала 30 монет и передала их вам. '
            'Вы говорите, он был совсем маленьким? '
            'Возможно, где-то рядом появилось гнездо гоблинов. '
            'Не хотите ли взять квест на его уничтожение? '
            'Можете не переживать, гоблины — по силам новичкам. А полученные деньги потратьте на подготовку к заданию.')
    bot.sendMessage(chat_id,'Вы получили 30 монет за Ухо гоблина')
    bot.sendMessage(chat_id,text,
                    reply_markup=keyboard)
def say_goblin(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].accept_goblin = True
    player[chat_id].money += 10
    save_players()
    keyboard ={
        'inline_keyboard':[
            [{'text':'Принять','callback_data':'accept'},{'text':'Отказаться','callback_data':'denai'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы рассказываете весьма тревожные вещи. Я'
                            ' бы хотела, чтобы вы взяли своё первое задание на зачистку. '
                            'Хотя зачистка гнезда гоблинов обычно подходит для опытных новичков, я верю, что вы справитесь.'
                            ' Не откажетесь от этого квеста? К тому же я выдам вам награду за предоставленную информацию — 10 монет.',reply_markup=keyboard)

def accept (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'Пойти на рынок','callback_data':'find_market'},{'text':'На задание','callback_data':'back_on'}]
        ]
    }
    bot.sendMessage(chat_id,'Девушка развернула карту и указала на предполагаемое местоположение гнезда гоблинов — место, которое почти не отличалось от того, где вы появились в этом мире. '
                            'Также она рекомендовала посетить рынок перед началом задания — запастись зельями здоровья будет весьма полезно.',
                    reply_markup=keyboard)

def back_on (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id ))
    restore(chat_id)
    save_players()
    keyboard ={
        'inline_keyboard':[
            [{'text':'Выйти из города','callback_data':'off_town'}]
        ]
    }
    bot.sendMessage(chat_id,'После отдыха вы стоите перед городскими воротами. '
                            'Совсем недавно вы попали в этот мир, а теперь уже стали членом гильдии авантюристов. '
                            'Ваше первое задание — зачистить гнездо гоблинов.',
                    reply_markup=keyboard)

def off_town(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if player[chat_id].visit_wolf:
        button = []
    else:
        button =  [[{'text':'Пойти налево','callback_data':'go_left'}]]
    keyboard = {
        'inline_keyboard':[
        [{'text':'Осмотреть место','callback_data':'find_go'},
         {'text':'Пойти направо','callback_data':'go_right'}]
        ]+button

    }


    bot.sendMessage(chat_id,'Вы снова оказались на той опушке, где столкнулись с гоблином. '
                            'На карте, которую вам показали перед заданием, было указано место, где, вероятно, находится гнездо. '
                            'Теперь осталось только с чего то начать.',reply_markup=keyboard)
def find_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].goblin_wait -=1
    if player[chat_id].goblin_wait == 3:
        text = 'Осмотрев кусты, где вы видели гоблина, вы обнаружили нору. Это, похоже, и есть гнездо гоблинов.'
    elif player[chat_id].goblin_wait == 2:
        text = 'Вы прождали некоторое время, ничего не произошло'
    elif 'Странный амулет' in player[chat_id].quest_invetary and player[chat_id].goblin_wait == 1:
        text ='Вы еще прождали, ничего не произошло, амулет начал вибрировать, словно говоря , что ждать еще опасно'
    elif 'Амулет предвестника' in player[chat_id].quest and player[chat_id].goblin_wait == 1:
        text = 'Амулет предвестника вибрирует у вас в кармане, сообщая что ждать еще опасно'
    elif player[chat_id].goblin_wait == 1:
        text = 'Прождав еще некоторое время, снова ничего не произошло'
    elif player[chat_id].goblin_wait == 0:
        goblin_death(chat_id,message_id,data)
        return
    else:
        text ='Текст заглушка'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Ждать','callback_data': 'wait_b'},{'text':'Войти в нору','callback_data':'гнездо'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def goblin_death(chat_id,message_id,data):
    bot.sendMessage(chat_id,'Возможно, ожидание было ошибкой — из норы появился огромный гоблин. По его виду стало понятно, что вам с ним не справиться.')
    print("Запуск битвы с коллбеком...")
    goblin = Goblin(name='Гоблин вождь', attack=70, hp=1200)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        gob_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока


def gob_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
def logovo_gob(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if 'Маг' in player[chat_id].player_class:
        button = [[{'text':'зажечь огонь','callback_data':'fire_find'}]]
    else:
        button =[]
    keyboard = {
        'inline_keyboard':[
            [{'text':'Идти в глубь','callback_data':'go_deep'}]
        ]+ button
    }
    bot.sendMessage(chat_id,'Вы спустились в темную пещеру, где редкие проблески света от странных камней в стенах едва освещают это место.',reply_markup=keyboard)
def fire_find(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    keyboard = {
        'inline_keyboard':[
            [{'text':'В глубь','callback_data':'go_deep'},{'text':'В тунель','callback_data':'gob_room'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы сосредоточились и зажгли огонь на пальце, наполнив пещеру мягким светом. '
                            'В его свете вам стало видно, что от основного коридора уходит еще один туннель.',reply_markup=keyboard)


def go_deep(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    goblin = Goblin(name='Гоблин',attack=10,hp=65)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        goblin_win_b(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока

def goblin_win_b(chat_id):
    if player[chat_id].hp <=0:
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
            [{'text': 'Продолжить движение', 'callback_data': 'gob_room'},
             {'text': 'Осмотреть гоблина', 'callback_data': 'goblin_inspect_a'}]
        ]}
        bot.sendMessage(chat_id, 'Вы победили гоблина, его мертвое тело лежит перед вами',
                        reply_markup=keyboard)
def goblin_inspect_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))

    player[chat_id].quest_invetary.append('Ухо гоблина')
    save_players()
    keyboard = {'inline_keyboard': [
        [{'text': 'Продолжить движение', 'callback_data': 'gob_room'}]
    ]}
    bot.sendMessage(chat_id, 'Вы срезали ухо с гоблина в качестве доказательства убийства, что бы получить награду в гильдии',
                    reply_markup=keyboard)

def gob_room(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Маг' in player[chat_id].player_class:
        button = [[{'text':'Потайной ход','callback_data':'secret_room'}]]
        text = ('Вы прошли через туннель и, прислушавшись, уловили за стеной шорох и странные звуки животных. '
                'Освещая коридор, вы заметили маленький лаз в стене, а из основного туннеля доносятся тяжелые шаги.')
    else:
        button =[]
        text = ('Пройдя дальше, коридор начал расширяться, и тусклый свет кристаллов в стенах едва освещал путь. '
                'Впереди оставалась только тень. Вы слышите звук тяжелых шагов, которые с каждым моментом становятся все ближе.')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Прислушаться','callback_data':'Прислушаться'},{'text':'Двигаться вперед','callback_data':'foward_death_a'}]
        ] + button
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def foward_death_a(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    bot.sendMessage(chat_id,'Пройдя вперед, вы увидели огромного гоблина')
    print("Запуск битвы с коллбеком...")
    goblin = Goblin(name='Гоблин вождь',attack=70,hp=1200)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        goblin_win_c(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока

def goblin_win_c(chat_id):
    if player[chat_id].hp <=0:
        kill(chat_id)
        save_players()
def secret_room(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].secret_room = True
    save_players()
    keyboard ={
        'inline_keyboard':[
            [{'text':'Открыть сундук','callback_data':'open_chest'},{'text':'Выйти из комнаты','callback_data':'Прислушаться'}]
        ]
    }

    bot.sendMessage(chat_id,'Вы оказались в небольшой комнате, в центре которой стоит подозрительный сундук',reply_markup=keyboard)

def open_chest(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest.append('Магический свиток')
    save_players()
    keyboard ={
        'inline_keyboard':[
            [{'text':'Выбраться из комнаты','callback_data':'Прислушаться'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы открыли сундук, в нем вы обнаружили свиток источающий магию',reply_markup=keyboard)

def stop_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].secret_room:
        bot.sendMessage(chat_id,'Выбравшись из комнаты вы натолкнулись на гоблина')
    else:
        bot.sendMessage(chat_id,'Вслушавшись в тишину, вы заметили тяжелые шаги. Вжавшись в стену, вы сдержали дыхание, пока мимо вас не прошел огромный гоблин, не замечая вас в темноте. '
                                'Подождав немного, вы осторожно продолжили свой путь вглубь туннеля и вскоре наткнулись на обычного гоблина, который сразу заметил вас')

    print("Запуск битвы с коллбеком...")
    goblin = Goblin(name='Гоблин', attack=10, hp=65)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True
    save_players()

    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        goblin_win_f(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока


def goblin_win_f(chat_id):
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
            [{'text': 'Продолжить движение', 'callback_data': 'gob_room_a'},
             {'text': 'Осмотреть гоблина', 'callback_data': 'goblin_inspect_f'}]
        ]}
        bot.sendMessage(chat_id, 'Вы победили гоблина, его мертвое тело лежит перед вами',
                        reply_markup=keyboard)
def goblin_inspect_f(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest_invetary.append('Ухо гоблина')
    keyboard ={
        'inline_keyboard':[
            [{'text':'Продолжить движения','callback_data':'gob_room_a'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы срезали ухо гоблина', reply_markup=keyboard)
def gob_room_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Стрелок' in player[chat_id].player_class:
        text =('На повороте вы заметили гоблина, гораздо меньшего, чем тот гигант, с которым вам пришлось столкнуться ранее. '
               'Он несколько раз уходит вглубь пещеры, возможно, если действовать быстро, удастся поразить его с одного выстрела, прежде чем он скроется')
        button = [[{'text':'Сделать выстрел','callback_data':'shot'}]]
    else:
        text = ('На повороте вы заметили гоблина, немного меньше, чем тот, с которым вам пришлось столкнуться ранее. '
                'Понаблюдав за ним, вы заметили, что он периодически уходит дальше по пещере.')
        button =[]

    keyboard = {
        'inline_keyboard':[
            [{'text':'Проползти','callback_data':'down_foward'},{'text':'Пробежать','callback_data':'run_death'}]
        ] + button
    }

    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def run_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы попытались пробежать в проем, как только огромный гоблин отошел. Но едва вы оказались в проеме, как почувствовали сильный удар по голове. '
                            'Земля ускользала из-под ваших ног, и вы упали. Последнее, что вы услышали — хохот гоблина.')
    kill(chat_id)
    save_players()
def down_foward(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))

    if 'Кристалл' in player[chat_id].quest:
        text =('После осмотра гоблина, вы подошли к проему, который он охранял\n'
               'Внутри вы увидели трех обычных гоблинов и гоблина похожего на шамана')
    else:
        text =('Вы дождались когда гоблин ушел и аккуратно подползли вдоль стены к проему\n'
               'Заглянув внутрь вы увидели гоблинов и одного похожего на шамана')
    keyboard = {
    'inline_keyboard':[
        [{'text':'Вороваться','callback_data':'run_death_b'},{'text':'Действовать\nаккуратно','callback_data':'accuraty'}]
    ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)

def shot (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keybord ={
        'inline_keyboard':[
            [{'text':'Подойти к проему','callback_data':'down_foward'},{'text':'Осмотреть громилу','callback_data':'inspect_gormila'}]
        ]
    }
    bot.sendMessage(chat_id,'Дождавшись когда огромный гоблин повернется к вам спиной, вы сделали ставку на выстрел\n'
                            'И она окупилась, пронзив череп гоблина',reply_markup=keybord)
def inspect_gormila(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest.append('Кристалл')

    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'к проему','callback_data':'down_foward'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы осмотрели тело здорового гоблина и нашли у него кристалл, к сожалению, вы заметили, что у гоблина уже были срезаны уши',reply_markup=keyboard)
def accuraty(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {
        'inline_keyboard':[
            [{'text':'В бой','callback_data':'shaman_goblin'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы аккуратно устранили гоблина за гоблином, убивая третьего и вот уже почти подобравшись к шаману, он вас заметил',
                    reply_markup=keyboard)
def shaman_goblin (chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    shaman = Goblin(name='Гоблин-шамана',attack=15,hp=120)
    player[chat_id].target = shaman
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        shaman_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, shaman)  # Не передаем коллбек напрямую, он уже в объекте игрока
def shaman_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        print('Вызываем сцену')
        save_players()
        keyboard ={
            'inline_keyboard':[
                [{'text':'Срезать уши','callback_data':'slice_ear'},
                 {'text':'Проверить лаз','callback_data':'inspect_nora'}],
                [{'text':'Уйти','callback_data':'exit'}]
            ]
        }
        bot.sendMessage(chat_id,'После тяжелой битвы, вы осматриваете поле боя, трупы гоблинов, какой то лаз в стене',reply_markup=keyboard)
def slice_ear(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest_invetary.extend(['Ухо гоблина']*4)

    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text':'Уйти','callback_data':'exit'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы срезали уши гоблинов, вы обратили на посох шамана, его навершие словно раскрошилось',reply_markup=keyboard)
def exit (chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Странный амулет' in player[chat_id].quest_invetary or 'Амулет предвестника' in player[chat_id].quest:
        text = 'Амулет вибрирует, словно говоря, очень плохо пытаться убежать от него, лучше сразиться'
    else:
        text = 'Выйдя наружу, у входа стоял тот огромный гоблин, что вы видели раньше, но теперь в нем было какое то отличие'
    keyboard = {
        'inline_keyboard':[
        [{'text':'Убежать','callback_data':'run_a_death'},{'text':'Вступить в бой','callback_data':'king_goblin'}]
    ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def king_goblin(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    goblin = Goblin(name='Вождь гоблинов',attack=20,hp=175)
    player[chat_id].target = goblin
    player[chat_id].in_battle = True

    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        king_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, goblin)  # Не передаем коллбек напрямую, он уже в объекте игрока
def king_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].on_battle_end = None
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].goblin_compplete = True
        print('Вызываем сцену')
        save_players()
        keyboard ={
            'inline_keyboard':[
                [{'text':'Вернутся в город','callback_data':'off_town_a'},
                 {'text':'Осмотреть гоблина','callback_data':'king_inspect'}]
            ]
        }
        bot.sendMessage(chat_id,'Огромный гоблин был повержен, вы смогли уничтожить гнездо гоблинов, теперь нужно отчитатся'
                                'в гильдии и получить награду за уши гоблинов',reply_markup=keyboard)

def king_inspect(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].quest_invetary.append('Ухо гоблина')
    save_players()
    keyboard ={
        'inline_keyboard':[
            [{'text':'Вернутся в город','callback_data':'off_town_a'}]
        ]
    }
    bot.sendMessage(chat_id,'Вы отрезали ухо гоблина , пора возвращатся в гильдию',reply_markup=keyboard)









def run_a_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы попытались аккуратно проскользнуть мимо огромного гоблина, вы уже думали вам удалось\n'
                            'Как в глазах потемнело и вы почувствовали как падаете. Для своих размеров, этот гоблин оказался очень ловким и быстрым')
    kill(chat_id)
    save_players()
def inspect_nora(chat_id,message_id,data):
    bot.sendMessage(chat_id,'Заглянув в лаз в стене, вы увидели мертвых людей, отвратное зрелище, никто не выжил')
def run_death_b(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    bot.sendMessage(chat_id,'Вы ворвались в помещения, не заметив что в помещение низкие потолки из-за темноты, ударились головой\n'
                            'Рухнув на землю, последнее что вы увидели, окруживших вас гоблинов')
    kill(chat_id)
    save_players()
def go_right(chat_id,message_id,data):
    bot.sendMessage(chat_id,' Вы не обнаружили ничего примечательного.')
def go_left(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].visit_wolf = True
    save_players()
    keyboard = {
        'inline_keyboard':[
            [{'text': 'Напасть','callback_data':'wolf_attack'},{'text':'Уйти','callback_data':'off_town'}]
        ]
    }
    bot.sendMessage(chat_id,'Пробираясь через кусты, вы заметили волка, пока он вас не видит, у вас есть возможность уйти',
                    reply_markup=keyboard)


# Функция начала битвы с монстром cюжетная
def wolf_attack(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    print("Запуск битвы с коллбеком...")
    wolf = Wolf(name='Малый волк',attack=10,hp=60)
    player[chat_id].target = wolf
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        wolf_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, wolf)  # Не передаем коллбек напрямую, он уже в объекте игрока
def wolf_win(chat_id):
    if player[chat_id].hp <= 0:
        kill(chat_id)
        save_players()
    else:
        player[chat_id].target = None
        player[chat_id].in_battle = False
        player[chat_id].stamina += 1
        player[chat_id].debuff.clear()
        player[chat_id].on_battle_end = None
        print('Вызываем сцену')
        save_players()
        keyboard ={
            'inline_keyboard':[
                [{'text':'Вернутся на поляну','callback_data':'off_town'},
                 {'text':'Осмотреть волка','callback_data':'wolf_inspect'}]
            ]
        }
        bot.sendMessage(chat_id,'Одержав победу над волком, его туша лежит перед вами',reply_markup=keyboard)


def wolf_inspect(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if data == 'take_tought':
        player[chat_id].quest.append('Клык волка')
        save_players()

    if 'Воин' in player[chat_id].player_class and not 'Клык волка' in player[chat_id].quest :
        button = [[{'text':'Вырвать зуб','callback_data':'take_tought'}]]
        text = 'Осматривая тело волка, вы заприметили остроту зубов'
    elif 'Клык волка' in player[chat_id].quest:
        button = []
        text ='Вы вырвали несколько клыков с тела волка, больше тут не чего делать'
    else:
        button =[]
        text = 'Осматривая тело волка, вы не нашли ничего , что стоило бы вашего внимания'

    keyboard = {
         'inline_keyboard':[
             [{'text':'Вернутся на поляну','callback_data':'off_town'}]
         ]+button
     }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)








def restore(chat_id):
    player[chat_id].hp = player[chat_id].max_hp
    player[chat_id].mana =  player[chat_id].max_mana
    player[chat_id].energy =  player[chat_id].energy_max





def kill(chat_id):  # Команда убийства игрока, является технической
    if chat_id in player:
        bot.sendMessage(chat_id, f'{player[chat_id].name} погиб .\n'
                                 f'Для начала новой игры введите: /start')
        player_class = player[chat_id].player_class
        stats.update_class_stats(player_class, 'dead')
        stats.dead += 1
        del player[chat_id]  # Удаляем персонажа

        stats.update_alive()  # Обновляем количество живых игроков
        save_players()  # Сохраняем изменения
        save_stats(stats)  # Сохраняем статистику

    else:
        bot.sendMessage(chat_id, 'У вас нет персонажа, для создания нового используйте команду /start')
def gama_over(chat_id):  # Команда убийства игрока, является технической
    if chat_id in player:
        bot.sendMessage(chat_id, f'{player[chat_id].name} Победил владыку .\n'
                                 f'Ожидайте второй сезон!')
        player_class = player[chat_id].player_class
        stats.update_class_stats(player_class, 'dead')
        stats.dead += 1
        del player[chat_id]  # Удаляем персонажа

        stats.update_alive()  # Обновляем количество живых игроков
        save_players()  # Сохраняем изменения
        save_stats(stats)  # Сохраняем статистику
    else:
        bot.sendMessage(chat_id, 'Сезон окончен')