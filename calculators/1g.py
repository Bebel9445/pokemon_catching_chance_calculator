import math

balls = ("Poke ball", "Great ball", "Ultra ball", "Safari ball", "Master ball")
status = ("asleep", "frozen", "paralyzed", "burned", "poisoned")

def calculation(ball:str, status:str, hp_percentage:float, catch_rate:int):
        
    if ball != "Master ball":
        bonus_ball = 12
        match ball:
            case "Poke ball":
                chances = 255
            case "Great ball":
                chances = 200
                bonus_ball = 8
            case "Ultra ball" | "Safari ball":
                chances = 150
            case _:
                chances = 255
        
        match status:
            case "asleep" | "frozen":
                bonus_status = 25
            case "paralyzed" | "burned" | "poisoned":
                bonus_status = 12
            case _:
                bonus_status = 0
        
        x = (bonus_status - 1)/chances

        y = (1 - catch_rate / (chances - bonus_status))

        z = (math.floor((hp_percentage ** -1) * (255*4)/(bonus_ball)) / 255)

        result = x + (1 - x) * (1 - y) * z
    
        return min(result, 1)
    else:
        return 1

print(calculation("Poke ball", "", 0.5, 255))
