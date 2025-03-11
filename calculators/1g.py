master_ball = False
balls = ("Poke ball", "Great ball", "Ultra ball", "Safari ball")
status = ("asleep", "frozen", "paralyzed", "burned", "poisoned")

def calculation_a(ball:str, status:str):
    result = 1
    if not master_ball:
        match ball:
            case "Poke ball":
                chances = 255
            case "Great ball":
                chances = 200
            case "Ultra ball", "Safari ball":
                chances = 150
        
        match status:
            case "asleep", "frozen":
                result = 25/chances
            case "paralyzed", "burned", "poisoned":
                result = 12/chances
    return result
