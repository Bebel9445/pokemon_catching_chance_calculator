import random
import locale

locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")

def calcul_a(pv:float, taux:int, bonus_ball:float, bonus_status:float):
    return (1 - 2/3 * pv) * taux * bonus_ball * bonus_status

def calcul_b(a:float):
    return (2**16 - 1) * (a / (2 ** 8 - 1)) ** 0.25

def test_capture(proba:float, nombre_essais:int):
    result_total = 0
    for i in range(nombre_essais):
        result = 0
        for j in range(4):
            if random.randint(0, 65535) < proba:
                result += 1
        if result == 4:
            result_total += 1
    return result_total / nombre_essais

def calculateur(pv:float, taux:int, bonus_ball:float, bonus_status:float):
    a = calcul_a(pv, taux, bonus_ball, bonus_status)
    if a < 255:
        b = calcul_b(a)
        print(f"Proba de capture théorique : {(b / 65535) ** 4 * 100} %")
        print(f"Proba de capture (sur {1000} essai(s)) : {test_capture(b, 1000) * 100} %")
    else:
        print(f"Proba de capture : 100 %")

taux = int(input("Taux de capture : "))
pv = eval(input("Taux de PV : "))
bonus_ball = float(input("Bonus de la ball : "))
bonus_status = float(input("Bonus du status : "))
calculateur(pv, taux, bonus_ball, bonus_status)