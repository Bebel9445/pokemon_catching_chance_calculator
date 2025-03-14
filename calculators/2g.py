import math

a = (0, 2, 3, 4, 5, 6, 8, 11, 16, 21, 31, 41, 51, 61, 81, 101, 121, 141, 161, 181, 201, 221, 241, 255)
b = (63, 75, 84, 90, 95, 103, 113, 126, 134, 149, 160, 169, 177, 191, 201, 211, 220, 227, 234, 240, 246, 251, 253, 255)

def find_b(num:int):
    global a, b
    i = 0
    while a[i] <= num:
        i += 1
    return b[i-1]

def calculate_a(hp_max:int, hp_current:int, rate:int, ball:str, bonus_status:str, player_level:int, enemy_level:int, enemy_speed:int, fishing:bool, weight:int, player_species:str, player_gender:str, enemy_species:str, enemy_gender:str, uses_moon_stone:bool):
    match bonus_status:
        case "asleep" | "frozen":
            bonus_status = 10
        case _:
            bonus_status = 0
    
    match ball:
        case "Great ball":
            bonus_ball = 1.5
        case "Ultra ball":
            bonus_ball = 2
        case "Master ball":
            bonus_ball = 255
        case "Fast ball":
            bonus_ball = 4 if enemy_speed >= 100 else 1
        case "Level ball":
            if player_level > 4 * enemy_level:
                bonus_ball = 8
            elif player_level > 2 * enemy_level:
                bonus_ball = 4
            elif player_level > enemy_level:
                bonus_ball = 2
            else:
                bonus_ball = 1
        case "Lure ball":
            bonus_ball = 4 if fishing else 1
        case "Heavy ball":
            if weight < 100:
                bonus_ball = (rate - 20) / rate
            elif weight < 200:
                bonus_ball = 1
            elif weight < 300:
                bonus_ball = (rate + 20) / rate
            else:
                bonus_ball = (rate + 30) / rate
        case "Love ball":
            bonus_ball = 8 if player_species == enemy_species and player_gender != enemy_gender else 1
        case "Moon ball":
            bonus_ball = 4 if uses_moon_stone else 1
        case _ :
            bonus_ball = 1

    if 3 * hp_max > 255:
        hp_max = math.floor(hp_max / 2)
        hp_current = math.floor(hp_current / 2)

    result = math.floor(((3 * hp_max - 2 * hp_current) * rate * bonus_ball) / (3 * hp_max))
    result = max(result, 1)
    return min(result, 255)

