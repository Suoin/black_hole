from scenario_5 import *
import globasl
#АКТ ФИНАЛ ЛАСТ БОСС

def final_act(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if player[chat_id].commander:
        text ='Вы построили армию для встречи короля. После чего вышли поприветствовать его. '
    else:
        text =' Командир выстроил армию, вы встали в почетный караул для встречи короля'
    keyboard = {
        'inline_keyboard':[
            [{'text':'Речь короля','callback_data':'king'}]
        ]
    }
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
def king(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='После речи, король возглавил армию. Теперь он поведет нас в финальный бой против владыки'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Сбор армии', 'callback_data': 'final_army_go'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_army_go(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='После сбора армии, король повел отряд вперед на замок владыки'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'К замку', 'callback_data': 'final_army_go_a'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_army_go_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('После изнурительного марша в охране короля и напряжения, отслеживая за всем происходящем вокруг'
           'Армия наконец разбила лагерь, до замка повелителя остался день пути. У вас есть время потренироватся'
           'или все же пойти в караул хоть вы смертельно устали')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Тренеровка', 'callback_data': 'final_training'},{'text':'В патруль','callback_data':'final_death'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_death(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text ='Вы уставшим взялись за патрулирование, из за усталости вы не услышали приближающегося врага'
    bot.sendMessage(chat_id,text)
    kill(chat_id)
    save_players()
def final_training(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].stamina +=15
    save_players()
    text ='Вы занялись упражнениями на выносливость, после чего ушли к себе и проспали до утра, только звук рога о сборе армии разбудил вас'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Построение', 'callback_data': 'final_army_go_c'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_army_go_c(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = 'Армия выдвинулась, к вечеру вокруг замка повелителя возводился осадный лагерь. Остается ждать начало штурма или вызваться в разведку'
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Ждать', 'callback_data': 'final_fight'},
             {'text': 'В патруль', 'callback_data': 'final_patrol'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_fight(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    player[chat_id].invetary.extend(['Героическое зелье здоровья','Героическое зелье здоровья','Героическое зелье здоровья'
    , 'Героическое зелье маны','Героическое зелье здоровья','Героическое зелье здоровья'])
    restore(chat_id)
    save_players()
    if data == 'final_patrol':
        text = ('Вы вышли в разведку, замок где сидит владыка когда то принадлежал цветному лорду дракону, что правил четырям цветами драконов'
                'Сильно проредевшая армия повелителя, не сможет оказать сопротивления. Штурм не продлится долго. Вы затаились ожидая начало штурма, пока не услышали'
                'шум надвигающейся армии и присоединились к штурму')
    else:
        text =('Вы отдохнули, проверили снаряжение, убедились что все готов, когда раздался сигнал о начале штурма, вы поспешили занять свое место в отряде и двинулись к замку'
               'армия повелителя уже была ослабленна, серьезного сопротивления не окажут')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'ШТУРМ!', 'callback_data': 'final_siege'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_siege(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Армия смяла монстров и ворвалась во двор замка, где монстры попытались оказать последнее сопротивление'
           'Вы же услышали шепот, взывающий к вам')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Продолжить штурм', 'callback_data': 'final_siege_a'},
             {'text': 'Пойти на шепот', 'callback_data': 'drakoning'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_siege_a(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text =('Пока шел штрум , на поле боя появился владыка тьмы и одни заклинанием уничтожил штурмующие отряды'
           'и своих союзников. Вы остались один на один с владыкой')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'СМЕРТЬ!ВЛАДЫКЕ!', 'callback_data': 'final_lord'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)
def final_lord(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    save_players()
    print("Запуск битвы с коллбеком...")
    ogr = Lord_deamon()
    player[chat_id].target = ogr
    player[chat_id].in_battle = True
    save_players()
    # Создаем коллбек для завершения битвы
    def on_battle_end(chat_id):
        print(f"Коллбек на завершение битвы вызван для {chat_id}")
        final_lord_win(chat_id)

    # Сохраняем коллбек в объекте игрока
    player[chat_id].on_battle_end = on_battle_end

    # Логируем коллбек перед передачей
    print(f"Передаем коллбек на завершение битвы: {on_battle_end}")
    battle(chat_id, message_id, slaim)  # Не передаем коллбек напрямую, он уже в объекте игрока

def final_lord_win(chat_id):


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
        globasl.boss = False
        save_players()
        keyboard = {'inline_keyboard': [
            [{'text': 'Победа!', 'callback_data': 'final'} ]
        ]}
        bot.sendMessage(chat_id, 'Владыка тьмы повережен, осталось возвестить о своей победе',
                        reply_markup=keyboard)

def drakoning(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    text = ('Вы пошли на шепот, зайдя в какое то святилище, вы увидели статую дракона и место, куда нужно положить руку'
            'И постоянный шепот переродись, переродись')
    keyboard = {
        'inline_keyboard': [
            [{'text': 'Положить руку', 'callback_data': 'reborn'},
             {'text': 'Вернутся в бой', 'callback_data': 'final_lord'}]
        ]
    }
    bot.sendMessage(chat_id, text, reply_markup=keyboard)


def reborn(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    restore(chat_id)
    save_players()
    required_items = ['Кровь дракона', 'Чешуйка черного дракона', 'Язык дракона', 'Когти дракона']
    if all(item in player[chat_id].quest for item in required_items):
        text = ('Положив руку на алтарь. Вы почувствовали изменения в себе, ваше тело начало трансформироватся'
                'Вы стали драконидом. Вы решили присоединится к бою. Выйдя из святилища. В центре двора стоял владыка, а вокруг него'
                'лежали тела ваших союзников и монстров. Он убил всех')
        player[chat_id].player_class.clear()
        player[chat_id].player_class.append('Драконид')

        player[chat_id].use_hand.clear()
        player[chat_id].use_hand.append('Удар когтями')

        player[chat_id].abillity.clear()
        player[chat_id].abillity.extend(['Регенерация','Лечение','Щит дракона','Огненное дыхание','Удар дракона'])

        player[chat_id].invetary.clear()
        player[chat_id].quest.clear()
        player[chat_id].quest_invetary.clear()
        player[chat_id].agila += 100
        player[chat_id].luck += 100
        player[chat_id].sila += 100
        player[chat_id].intelect += 100
        player[chat_id].stamina +=100
        save_players()

        keyboard = {
            'inline_keyboard':[
                [{'text':'В бой!','callback_data':'final_lord'}]
            ]
        }
        bot.sendMessage(chat_id,text,reply_markup=keyboard)
    else:
        text =('Вы положили руку на алтарь, ваше тело начало менятся, но чего то не хватило и вы превратились в бесформенную массу плоти'
               'Ужасный конец')
        kill(chat_id)
        save_players()
        bot.sendMessage(chat_id,text)
def final(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    if 'Драконид' in player[chat_id].player_class:
        text =('С силой дракона вы поняли, что богиня не то добро, что нужно миру. Вы можете присоединится к ее замыслу или спасти мир по настоящему'
               'Вы почувствали как осколки с другими мирами начали разрушаться, убивая жителей этих миров')
        gama_over(chat_id)
        save_players()
        bot.sendMessage(chat_id,text)

    else:
        gama_over(chat_id)
        save_players()
        text ='Поздравляю герой, ты спас этот мир и теперь, все осколки мира, будут соединины в единое целое'
        bot.sendMessage(chat_id,text)