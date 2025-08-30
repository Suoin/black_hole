
from scenario import *
from scenario_2 import *
from scenario_3 import *
from scenario_4 import *
from scenario_5 import *
from scenario_final import *
callback_commands ={
                 'status':status_rofl,
                # обработка каллбэков для чойз_дата
'luck':choise_data,'melee':choise_data ,'range':choise_data ,'magic':choise_data,
                # обработка функции форест_старт
'use_magic': find_weapon, 'craft_weapon':find_weapon, 'find_weapon':find_weapon, 'find_amul': find_weapon,
                # Обработка кнопки осмотрется и идти вперед
'go_forward': go_forward, 'osmotr':osmotr,
                #Линия битвы с гоблином
'magic_practical': goblin_fight , 'inspect_amulet':goblin_fight, 'shot_bow':goblin_fight, 'shot_sword':goblin_fight,
'goblin_fight_start':goblin_fight_start, 'attack':goblin_fight_start,'goblin_inspect':goblin_inspect,
                # КАЛЛБЭКИ ОТВЕЧАЮЩИЕ НА СЦЕНЫ В ГОРОДЕ
#КАЛБЕЭКИ ОСМОТРА И КВЕСТ ВЕЗУНЧИКА
#КАЛБЭКИ РЫНКА
'find_guild': find_guild, 'history':history, 'get_weapon':get_weapon,'guild_quest':guild_quest,
'find_market':find_market, 'back_off': go_forward, 'buy_items':buy_market,
#КАлбэки продаж
'sell_Ухо гоблина':find_market, 'sell_Странный амулет': find_market,
'vial_hp': buy_market, 'vial_mana': buy_market, 'vial_char': buy_market,
#КАЛБЭКИ КВЕСТА ВЕЗУНЧИКА
'foward_death':foward_death,'group_foward':group_foward, 'inscpect_town':inspect_town,'wait_a':wait_a,'go_home':go_home,
'evaesdrop':evaesdrop,
#КАЛБЭКИ КВЕСТЫ ГОБЛИНА ИЛИ ОСНОВНОЙ КВЕСТ НА СЛАЙМОВ
'Показать ухо': show_ear,'slaim':slaim,'say_goblin':say_goblin,'denai':slaim,'accept':accept, 'back_on':back_on, 'off_town':off_town,
'go_left':go_left, 'wolf_attack':wolf_attack, 'wolf_inspect':wolf_inspect,'go_right':go_right, 'take_tought':wolf_inspect,
'find_go':find_go, 'wait_b':find_go,'гнездо': logovo_gob, 'fire_find':fire_find,'go_deep':go_deep,'gob_room':gob_room,
'goblin_inspect_a':goblin_inspect_a, 'foward_death_a':foward_death_a,'secret_room':secret_room, 'Прислушаться':stop_a,'goblin_inspect_f':goblin_inspect_f,
'gob_room_a':gob_room_a, 'run_death': run_death, 'down_foward':down_foward, 'shot':shot,'accuraty':accuraty, 'inspect_gormila':inspect_gormila,
'run_death_b':run_death_b, 'shaman_goblin':shaman_goblin,'inspect_nora':inspect_nora,'slice_ear':slice_ear,'exit':exit,'run_a_death':run_a_death,
'king_goblin':king_goblin,'king_inspect':king_inspect,'off_town_a':off_town_a, 'take_quest':take_quest,'slaim_go':slaim_go, 'slaim_start':slaim_start,
'slaim_osmotr':slaim_osmotr, 'slaim_forward':slaim_forward, 'slaim_go_a':slaim_go_a,'slaim_attack_a':slaim_attack_a,'slaim_route':slaim_route,'slaim_forward_a':slaim_forward_a,
'slaim_attack_b':slaim_attack_b,'slaim_inspect_wall':slaim_inspect_wall,'slaim_push':slaim_push,'slaim_boss_a':slaim_boss_a,'slaim_forward_c':slaim_forward_c,
'slaim_death_a':slaim_death_a,'slaim_forward_e':slaim_forward_e,'slaim_attack_e':slaim_attack_e, 'slaim_forward_i':slaim_forward_i,'slaim_visual':slaim_visual,
'slaim_speed':slaim_visual,'slaim_go_1':slaim_go_1,'slaim_death_i':slaim_death_i,'slaim_attack_i':slaim_attack_i,'slaim_forward_2':slaim_forward_2,
'slaim_forward_3':slaim_forward_3,'slaim_right':slaim_right,'slaim_go_2':slaim_go_2,'slaim_go_wall':slaim_go_wall,'slaim_boss_b':slaim_boss_b,'slaim_forward_4':slaim_forward_4,
'slaim_exit':slaim_exit,'slaim_see_2':slaim_exit,'slaim_guild':slaim_guild, 'open_chest':open_chest,
    'Рассечение': choise_data_2,
    'Взрывной удар': choise_data_2,
    'Концентрация': choise_data_2,
    'Яростный крик': choise_data_2,
    'Прицельный выстрел': choise_data_2,
    'Уклонение': choise_data_2,
    'Двойной выстрел': choise_data_2,
    'Аура концентрации': choise_data_2,
    'Проникающий удар': choise_data_2,
    'Случайный удар': choise_data_2,
    'Аура': choise_data_2,
    'Неизвестная способность': choise_data_2,
    'Огненный шар': choise_data_2,
    'Ледяные иглы': choise_data_2,
    'Щит льда': choise_data_2,
    'Щит огня': choise_data_2,

    'Кровавый удар': choise_data_3,
    'Быстрые удары':choise_data_3,
    'Магический выстрел':choise_data_3,
    'Быстрая стрельба': choise_data_3,
    'Нестабильный удар':choise_data_3,
    'Стабилизация': choise_data_3,
    'Вытягивание маны':choise_data_3,
    'Ледяной взрыв':choise_data_3,
    'start_know':start_know,'in_town':in_town,'on_market':on_market, 'in_library':in_library,'legend_hero':book,'green_dragon':book,'bestary':book,
    'green_prince':book, 'on_gate':on_gate,'give_core':smite,'give_core_a':smite,'give_touth':smite,'give_crystal':smite,'take_weapon': take_weapon,
    'in_army':in_army,'stop_army':stop_army,'wait_army':wait_army,'commandr':commandr,'wait_army_a':wait_army,'defende':defende,'start_army':start_army,
    'base_base':base_base,'wait_start':wait_start,'water_char':wait_start,' sbor_star': sbor_star,'main_power':main_power,'go_army_a':go_army_a,'go_army_b':go_army_b,
    'press_f':base_camp,'ignore':base_camp,'grove':grove,'restore':restore_a,'restore_a':restore_a,'fight_begemot':fight_begemot,'forest_a':forest_a,'a_base_camp':a_base_camp,
    'find_battle':a_base_camp,'go_patrol':go_patrol,'go_patrol_a':go_patrol_a,'orc_spy':orc_spy,'dawm':dawm,'camp_army':camp_army,'avangard':avangard,'sleep':sleep,
    'spy_go':spy_go, 'yes':spy_go_a, 'no':spy_go_a,'retreat':retreat,'orc_fight_a':orc_fight_a,'orc_fight_b':orc_fight_b,'find_orc':spy_go_b,'help':spy_go_b,
    'regroup':regroup,'mute':regroup,'unmute':regroup,'orc_death':orc_death,'retreat_a':retreat_a,'orc_champion':orc_champion,'spy_base':spy_base,'grove_b':grove_b,
    'restore_death':restore_death,'forest_b':forest_b,'death_patrol_a':death_patrol_a,'orc_fight_e':orc_fight_e,'orc_death_a':orc_death_a,'orc_death_b':orc_death_b,
    'death_b':death_b,'restore_life':restore_life,'fight_orc_q':fight_orc_q,'orc_fight_w':orc_fight_w,'life_a':life_a,'restore_life_c':restore_life_c,'help_camp':help_camp,
    'help_camp_a':help_camp_a,'learn_skill':learn_skill,'go_training':go_training,'skill_add':skill_add,'add_skill':add_skill,'quest_camp':quest_camp,
    'invite':invite,'go_patrol_q':go_patrol_q,'forest_go_q':forest_go_q,'death_orc_q':death_orc_q,'watch':watch,'watch_go':watch_go,'wait_army_c':roundew,
    'go_orc_watch':go_orc_watch,'go_orc_watch_a':go_orc_watch_a,'kill_orc':kill_orc,'kill_orc_a':kill_orc_a,'mount_go':mount_go,'moung_go_a':moung_go_a,
    'moung_go_b':moung_go_b,'dragon_kill':dragon_kill,'mount_a':mount_a,'moung_go_death':moung_go_death,'dragon_kill_a':dragon_kill_a,
    'mount_b':mount_b,'forest_go_p':forest_go_p,'green_dragon_start':green_dragon_start,'green_dragon_fight':green_dragon_fight,'blood_dragon':dragon_win,
    'blood_dragon_a':dragon_win,'dragon_win':dragon_win,'army_wait_q':army_wait_q,'army_go_q':army_go_q,'go_army_enemy':go_army_enemy,'army_go_forest':army_go_forest,
    'roundew,':roundew,'citadel':citadel,'lose_path':lose_path, 'win_path':win_path,'lose_path_a':lose_path_a,'tower_lose':tower_lose,'lose_path_b':lose_path_b,
    'door':door,'tower_lose_a':tower_lose_a,'tower_lose_b':tower_lose_b,'citadel_lose_b':citadel_lose_b,'citadel_lose_b_a':citadel_lose_b,'citadel_lose_c':citadel_lose_c,
    'citadel_lose_w':citadel_lose_w,'win_path_a':win_path_a,'win_path_fight':win_path_fight,'win_path_c':win_path_c,'win_lose':citadel_room,'lose_win':citadel_room,
    'win_luck':citadel_room,'win_citadel':win_citadel,'win_citadel_a':win_citadel_a,'win_citadel_b':win_citadel_b,'demon':demon,'general_a':general_a,'its_trap':its_trap,
    'general_b':general_b,'general_c':general_c,'general_e':general_e,'general_w':general_w,'lose_trap':lose_trap,'death_general':death_general,
    'general_win_first':general_win_first,'act_two':act_two, 'restart':win_path_c,'citadel_lose':citadel_lose,'sbor_star':sbor_star,'spy_go_c':spy_go_c,
    'orc_fight_c':orc_fight_c,'army_go_w':army_go_w,'roundew':roundew,
    # Команды второго акта

    'act_two_a':act_two_a,'two_death':two_death,'two_death_a':two_death_a,'two_act_go':two_act_go,'two_act_go_a':two_act_go_a,'two_death_c':two_death_c,
    'two_act_go_b':two_act_go_b,'two_death_e':two_death_e,'two_act_go_c':two_act_go_c,'two_act_go_e':two_act_go_e,'two_death_i':two_death_i,'two_act_go_i':two_act_go_i,
    'two_act_go_f':two_act_go_f,'two_quest':two_quest,'two_quest_a':two_quest_a,'two_quest_b':two_quest_b,'two_death_f':two_death_f,'two_quest_c':two_quest_c,
    'two_fight_ogr':two_fight_ogr,'two_quest_w':two_quest_w,'garpia_fight':garpia_fight,'two_garpia_fight':two_garpia_fight,'two_garpia_fight_a':two_garpia_fight_a,
    'egg_garpia':two_final_quest,'item_solider':two_final_quest,'quest_complete_two':quest_complete_two,'no_switch':two_weapon,'two_weapon':two_weapon,
    'two_go_army':two_go_army,'two_go_army_a':two_go_army,'two_town':two_town,'death_market_a':death_market_a,'research_town':research_town,'in_market':in_market,
    'clock':give_me_item,'map':give_me_item,'talisman':give_me_item,'in_camp':in_camp,'two_restore_f':two_restore_f,'quest_two':quest_two,'quest_two_invite':quest_two_invite,
    'quest_two_go':quest_two_go,'quest_left':quest_left,'quest_two_death':quest_two_death,'quest_two_return':quest_two_return,'quest_right_a':quest_right_a,'quest_right':quest_right,
    'quest_center':quest_center,'quest_two_attack':quest_two_attack,'quest_two_attack_a':quest_two_attack_a,'quest_two_attack_b':quest_two_attack_b,'quest_two_attack_final':quest_two_attack_final,
    'complete':complete,'one_complete':complete,'mana_burn':mana_burn,'restore_two_j':restore_two_j,'two_army_go_f':two_army_go_f,'two_army_go_j':two_army_go_j,
    'black_dragon_start':black_dragon_start,'two_army_go_final':two_army_go_final,'black_dragon_go':black_dragon_go,'chram_death':chram_death,'black_dragon_go_a':black_dragon_go_a,
    'black_dragon_go_c':black_dragon_go_c,'fight_black_dragon':fight_black_dragon,'fight_black_dragon_start':fight_black_dragon_start,'loot_black_dragon':black_dragon_final_a,
    'skill_black_dragon':black_dragon_final_a,'research_chram':research_chram,'go_charm':go_charm,'fight_skeleton':fight_skeleton,'fight_skeleton_a':fight_skeleton_a,
    'chram_visual':chram_visual,'chram_death_a':chram_death_a,'go_chram_a':go_chram_a,'chram_death_b':chram_death_b,'go_chram_c':go_chram_c,'fight_skeleton_knight':fight_skeleton_knight,
    'chram_final':chram_final,'right_door':right_door,'necromance':necromance,'relife':relife,'citadel_two_necro':citadel_two_necro,'two_citadel_go':two_citadel_go,
    'two_citadel_go_a':two_citadel_go_a,'two_citadel_go_b':two_citadel_go_b,'two_citadel_death':two_citadel_death,'two_citadel_go_false':two_citadel_go_false,
    'two_citadel_go_false_a':two_citadel_go_false_a,'two_citadel_go_false_a_death':two_citadel_go_false_a_death,'two_citadel_true':two_citadel_true,'two_citadel_go_true_a':two_citadel_go_true_a,
    'two_general':two_general, 'two_restore':two_restore,'quest_two_attack_c':quest_two_attack_c,'restore_two_f':restore_two_j,'two_army_go_citadel':two_army_go_citadel,
    'two_general_fight':two_general_fight,'two_camp':in_camp,

#КОМАНДЫ АКТА НОМЕР ТРИ
'two_general_death':two_general_death,'exucute':two_citadel,'maroder':two_citadel,'tri_go_army':tri_go_army,'tri_town':tri_town,'tunnel_go':tunnel_go,'tunnel_fight':tunnel_fight,
'town_siege':town_siege,'siege_death':siege_death,'siege_death_a':siege_death_a,'wall_hole':wall_hole,'wall_hole_a':wall_hole_a,'wall_hole_b':wall_hole_b,'wall_hole_c':wall_hole_c,
'wall_hole_e':central_squer,'tunnel_fight_final':central_squer,'siege_tower_a':siege_tower_a,'central_squer_a':central_squer_a,'tri_kill_town':tri_kill_town,'tri_kill_town_a':tri_kill_town_a,
'tri_restore':tri_restore,'tri_research_town':tri_research_town,'tri_restore_c':tri_restore_c,'library_tri':library_tri,'castle_tri':castle_tri,'gold_dragon':gold_dragon,
'monster_burn':monster_burn,'grabe_people':monster_burn,'tri_army_go_b':tri_army_go_b,'tri_army_go_c':tri_army_go_c,'village':village,'village_a':village_a,'village_b':village_b,'peon_life':village_b,
'village_c':village_c,'tri_patrol':tri_patrol,'tri_patrol_a':tri_patrol_a,'tri_army_go_f':tri_army_go_f,'gold_dragon_start':gold_dragon_start,'tri_forest_death':tri_forest_death,
'golden_dragon_a':golden_dragon_a,'tri_forest_death_a':tri_forest_death_a,'golden_dragon_b':golden_dragon_b,'lang':lang,'tri_citadel_siege':tri_citadel_siege,'eat_lang':lang,
'tri_citadel':tri_citadel,'first_enemy':first_enemy,'two_enemy':two_enemy,'tri_enemy':tri_enemy,'tri_general':tri_general,'tri_general_win':tri_general_win,
'siege_tower':siege_tower,'siege_tower_b':siege_tower_b,'siege_tower_c':siege_tower_c,'restore_tri_f':restore_tri_f,'fight_golden_dragon':fight_golden_dragon,
'tri_general_fight':tri_general_fight,'sso':sso,


# КОМАНДЫ АКТА НОМЕР ЧЕТЫРЕ
'yes_commander':commander,'no_commander':commander,'say_commander':four_go_army,'ear_commander':four_go_army,'four_army_go_a':four_army_go_a,'four_army_go_b':four_army_go_b,
'four_army_go_death':four_army_go_death,'four_restore_army':four_restore_army,'four_karaul':four_karaul,'four_karaul_a':four_karaul_a,'four_army_restore_a':four_army_restore_a,
'four_camp':four_camp,'four_camp_a':four_camp_a,'four_restore_c':four_restore_c,'patrol_four_a':patrol_four_a,'patrol_four_b':patrol_four_b,'four_camp_b':four_camp_b,
'four_training':four_training,'four_army_go_f':four_army_go_f,'four_libray':four_libray,'four_inspect':four_inspect,'four_research':four_research,'four_market':four_market,
'four_castle':four_castle,'four_guild':four_guild,'guild_archive':guild_archive,'guild_lord':guild_lord,'guild_lord_a':guild_lord_a,'four_army_go_q':four_army_go_q,
'red_dragon_start':red_dragon_start,'red_dragon':red_dragon,'red_dragon_fight':red_dragon_fight,'red_dragon_a':red_dragon_c,'red_dragon_b':red_dragon_c,
'four_siege_citadel':four_siege_citadel,'four_citadel':four_citadel,'four_citadel_a':four_citadel_a,'four_citadel_b':four_citadel_b,'four_citadel_с':four_citadel_с,
'four_restore_z':four_restore_z,'four_general':four_general,'four_general_a':four_general_a,'four_general_b':four_general_b,
    #ФИНАЛЬНЫЙ АКТ И ЕГО КОМАНДЫ
'final_act':final_act,'king':king,'final_army_go_a':final_army_go_a,'final_death':final_death,'final_training':final_training,
'final_army_go_c':final_army_go_c,'final_fight':final_fight,'final_patrol':final_fight,'final_siege':final_siege,'final_siege_a':final_siege_a,'final_lord':final_lord,
'reborn':reborn,'final_army_go':final_army_go,'drakoning':drakoning,'final':final,


    'load':load


}