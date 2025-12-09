import random
import time
from colorama import init, Fore, Back, Style

init()
postac = [100, 20]
pieniadze = 0
Stalowy_miecz = 20
Ulepszony_Stalowy_miecz = 20
Mithrilowy_miecz = 40
Excalibur = 1500
MAXHP = 200
EXP = 0
LVL = [0, 50]
niga = 10
nig = 10
Ekwipunek = [0, 0]
PA = 1
PF = 1
PK = 1
PL = 1
PKa = 1
print("--- WITAMY W GRZE! ---")
time.sleep(1)

while postac[0] > 0:
    goblin = ["Goblin", random.randint(30, 50), random.randint(10, 20)]
    ultra_goblin = ["Ultra goblin", random.randint(50, 70), random.randint(20, 30)]
    szczur_morski = ["Szczur morski", random.randint(10, 30), random.randint(5, 10)]
    Scylla = ["Scylla", random.randint(200, 300), random.randint(40, 60)]
    los = random.randint(1, 100)

    if los <= 50:
        potwor = szczur_morski
    elif los <= 80:          
        potwor = goblin
    elif los <= 99:          
        potwor = ultra_goblin
    else:                    
        potwor = Scylla
    Siegebreaker_Assault_Beast = ["Siegebreaker_Assault_Beast", random.randint(1000, 8000), 200]
    Diablo = ["Diablo", random.randint(8000, 80000), 400]
    lo = random.randint(1,100)
    if lo <= 99:
        boss = Siegebreaker_Assault_Beast
    else:
        boss = Diablo
    time.sleep(0.5)
    print("\nWalka - a")
    time.sleep(0.5)
    print("Sklep - b")
    time.sleep(0.5)
    print("Walka z BOSSEM(LVL 20) - c")
    time.sleep(0.5)
    print(f"\nTwoje pienieadze = {pieniadze}")
    time.sleep(0.5)
    print(f"Twoj LVL = {LVL[0]}/{LVL[1]}")
    time.sleep(0.5)
    print(f"Twoje HP: {postac[0]}/{MAXHP}")
    inp = input("> ")

    if inp == "a":

        print(f"\nNa twojej drodze stanął {potwor[0]}! Ma {potwor[1]} HP i {potwor[2]} ataku.")
        time.sleep(0.5)
        print("\nWalka! - a")
        time.sleep(0.5)
        print("Ucieczka! - b")
        inp = input("> ")

        if inp == "a":
            print(f"\n--- WALKA Z {potwor[0]} ---")
            while potwor[1] > 0 and postac[0] > 0:
                time.sleep(0.5)
                print(f"Twoje HP: {postac[0]}")
                print(f"HP {potwor[0]}: {potwor[1]}")
                postac[0] -= potwor[2]
                potwor[1] -= postac[1]
                time.sleep(0.5)

            if potwor[1] <= 0 and postac[0] > 0:
                zdobyte = random.randint(10, 100)
                zdobyt = random.randint(2, 10)
                pieniadze += zdobyte
                LVL[0] += zdobyt
                if LVL[0] >= LVL[1]:
                    EXP += 1
                    LVL[0] -= LVL[1]
                    LVL[1] += 5
                print(f"\nPokonałeś {potwor[0]}! Zdobywasz {zdobyte} złotych i {zdobyt} expa")

                if potwor[0] == "Ultra goblin":
                    l = random.randint(1,100)
                    if l <= 10 and PA > 0:
                            print("Zdobyłeś również pierścień Ataku. +20 do Ataku")
                            postac[1] += 20
                            PA -= 1
                            time.sleep(0.5)
                    elif l >=99 and PF > 0:
                                    print("Zdobyłeś również pierścień Antymaga. +100 do Ataku")
                                    postac[1] += 100
                                    PF -= 1
                                    time.sleep(0.5)
                elif potwor[0] == "Scylla":
                    g = random.randint(1,100)
                    if g == 100:
                        if PK > 0:
                            print("Zdobyłeś również Kołczan Prawilności. +100 do MAXHP")
                            MAXHP += 100
                            PK -= 1
                            time.sleep(0.5)

                print(f"Masz teraz {pieniadze} złotych.")
                time.sleep(0.5)
                print(f"LVL:{EXP}")
                time.sleep(0.5)
            elif postac[0] <= 0:
                print("\nZostałeś pokonany...")
                break

        elif inp == "b":
            print("Próbujesz uciec...")
            time.sleep(0.5)
            if random.randint(0, 1) == 1:
                print("Udało ci się uciec!")
                time.sleep(0.5)
            else:
                print(f"Nie udało ci się uciec! {potwor[0]} cię dopada!")
                time.sleep(0.5)
                postac[0] -= potwor[2]
                print(f"{potwor[0]} zadaje ci {potwor[2]} obrażeń!")
                time.sleep(0.5)

    elif inp == "b":
        print("\nWybierz co chcesz kupić")
        time.sleep(0.1)
        print("Stalowy miecz 50 zł - a")
        time.sleep(0.1)
        print("Ulepszony_Stalowy_miecz 100 zł - b")
        time.sleep(0.1)
        print("Mithrilowy_miecz 250 zł - c")
        time.sleep(0.1)
        print("Excalibur 1000 zł - d")
        time.sleep(0.1)
        print("Eliksir życia 30 zł - e")
        time.sleep(0.1)
        print("Ulepszony Eliksir życia 50 zł - f")
        time.sleep(0.1)
        print("Stalowa zbroja 200 zł - g")
        time.sleep(0.1)
        print("Zbroja Zeusa 1500 zł - h ")
        print(f"Twoje pienieadze = {pieniadze}")
        time.sleep(0.1)
        inp = input("> ")

        if inp == "a":
            if Stalowy_miecz ==0:
                print("\nKupiłeś już ten miecz!")
                time.sleep(0.5)
            else:
                if pieniadze >= 50:
                    postac[1] += Stalowy_miecz
                    pieniadze -= 50
                    Stalowy_miecz -= 20
                    print(f"Kupiono Stalowy_miecz Atak +20")
                    time.sleep(0.5)
                else:
                    print("\nNie masz wystarczająco pieniędzy!")
                    time.sleep(0.5)
        elif inp == "b":
            if Ulepszony_Stalowy_miecz ==0:
                print("\nKupiłeś już ten miecz!")
                time.sleep(0.5)
            else:
                if pieniadze >= 100:
                    postac[1] += Stalowy_miecz
                    pieniadze -= 100
                    Ulepszony_Stalowy_miecz -= 20
                    print(f"Kupiono Ulepszony_Stalowy_miecz Atak +20")
                    time.sleep(0.5)
                else:
                    print("\nNie masz wystarczająco pieniędzy!")
                    time.sleep(0.5)
        elif inp == "c":
            if Mithrilowy_miecz ==0:
                print("\nKupiłeś już ten miecz!")
                time.sleep(0.5)
            else:
                if pieniadze >= 250:
                    postac[1] += Mithrilowy_miecz
                    pieniadze -= 250
                    Mithrilowy_miecz -= 40
                    print(f"Kupiono Mithrilowy_miecz Atak +40")
                    time.sleep(0.5)
                else:
                    print("\nNie masz wystarczająco pieniędzy!")
                    time.sleep(0.5)
        elif inp == "d":
            if Excalibur ==0:
                print("\nKupiłeś już ten miecz!")
                time.sleep(0.5)
            else:
                if pieniadze >= 1500:
                    postac[1] += Excalibur
                    pieniadze -= 1500
                    Excalibur -= 1500
                    print(f"Kupiono Excalibur Atak +800")
                    time.sleep(0.5)
                else:
                    print("\nNie masz wystarczająco pieniędzy!")
                    time.sleep(0.5)
        elif inp == "e":
            if pieniadze >= 30:
                pieniadze -= 30
                print("Chcesz go dodać do ekipunku czy użyć ?")
                time.sleep(0.5)
                print("Dodać do ekwipunku - a")
                print("Użyć - b")
                inp = input("> ")
                if inp == "a":
                    Ekwipunek[0] += 1
                    print("Eliksir życia został dodany do Eq")
                elif inp == "b":
                    postac[0] += 40  
                    postac[0] = min(postac[0], MAXHP)
                    print(f"Kupiono eliksir! HP +40. Masz teraz {postac[0]} HP")
                    time.sleep(0.5)
            else:
                print("\nNie masz wystarczająco pieniędzy!")
                time.sleep(0.5)
        elif inp == "f":
            if pieniadze >= 60:
                pieniadze -= 60
                print("Chcesz go dodać do ekipunku czy użyć ?")
                print("Dodać do ekwipunku - a")
                print("Użyć - b")
                inp = input("> ")
                if inp == "a":
                    Ekwipunek[1] += 1
                    print("Ulepszony eliksir życia został dodany do Eq")
                elif inp == "b":
                    postac[0] += 80  
                    postac[0] = min(postac[0], MAXHP)
                    print(f"Kupiono eliksir! HP +80. Masz teraz {postac[0]} HP")
                    time.sleep(0.5)
            else:
                print("\nNie masz wystarczająco pieniędzy!")
                time.sleep(0.5)
        elif inp == "g":
            if niga == 0:
                print("\nKupiłeś już tą zbroję!")
                time.sleep(0.5)
            if pieniadze >= 200:
                MAXHP += 200
                pieniadze -= 200
                niga -= 10
                print(f"Kupiono Stalowa zbroje! MAXHP +100")
                time.sleep(0.5)
            else:
                print("\nNie masz wystarczająco pieniędzy!")
                time.sleep(0.5)
        elif inp == "h":
            if nig == 0:
                print("\nKupiłeś już tą zbroję!")
                time.sleep(0.5)
            if pieniadze >= 1500:
                MAXHP += 800
                pieniadze -= 1500
                nig -= 10
                print(f"Kupiono Zbroje Zeusa! MAXHP +800")
                time.sleep(0.5)
            else:
                print("\nNie masz wystarczająco pieniędzy!")
                time.sleep(0.5)
        else:
            print("\nNieznana opcja!")
            continue
    elif inp == "c":
        if EXP < 20:
            print("Musisz mieć 20 LVL aby odblokować walkę z BOSSEM")
            time.sleep(0.5)
        else:
            while boss[1] > 0 and postac[0] > 0:
                print(f"Twoje HP: {postac[0]}/{MAXHP}  HP Bossa: {boss[1]}")
                print(f"Ekwipunek: Eliksir życia:{Ekwipunek[0]} Ulepszony Eliksir życia{Ekwipunek[1]}")
                print("\nAtak - a")
                print("Ekwipunek - e")
                inp = input("> ")
                
                if inp == "a":
                        print(f"\n--- WALKA Z {boss[0]} ---")
                        while boss[1] > 0 and postac[0] > 0:
                            time.sleep(0.5)
                            print(f"Twoje HP: {postac[0]}")
                            print(f"HP {boss[0]}: {boss[1]}")
                            postac[0] -= boss[2]
                            boss[1] -= postac[1]
                            time.sleep(0.5)
                        if boss[1] <= 0 and postac[0] > 0:
                                zdoby = random.randint(100, 1000)
                                zdob = random.randint(20, 100)
                                pieniadze += zdoby
                                LVL[0] += zdob
                                if LVL[0] >= LVL[1]:
                                    EXP += 1
                                    LVL[0] -= LVL[1]
                                    LVL[1] += 5
                                print(f"\nPokonałeś {boss[0]}! Zdobywasz {zdoby} złotych i {zdob} expa")
                                if boss[0] == "Siegebreaker_Assault_Beast":
                                    k = random.randint(1,100)
                                    if k <= 10 and PL > 0:
                                            print("Zdobyłeś również pierścień Lemurów. +200 do Ataku")
                                            postac[1] += 200
                                            PL -= 1
                                            time.sleep(0.5)
                                    elif k >=99 and PKa > 0:
                                                    print("Zdobyłeś również pierścień Kastiego. +1000 do Ataku")
                                                    postac[1] += 1000
                                                    PKa -= 1
                                                    time.sleep(0.5)
                                elif boss[0] == "Diablo":
                                            print("--- GRATULACJE WYGRAŁEŚ!!! ---")
                                            print("Grę tworzyli:")
                                            print("Kod:Adam")
                                            print("Grafika:Adam")
                                            print("Dzwięk:Adam")
                                            print("Tłumaczenie:Adam")
                                            print("Audiodeskrypcja:Adam")
                                            print("Reżyser:Adam")
                                            print("Redaktor:Adam")
                                            print("Pomysłodawca:Adam")
                                            print("Deco:Adam")
                                            print("Lektor:Adam")
                                            print("Hm:Adam")
                elif inp == "e":
                    print("Eliksir życia - a")
                    print("Ulepszony Eliksir życia - b")
                    inp = input("> ")
                    if inp == "a" and Ekwipunek[0] > 0:
                        Ekwipunek[0] -= 1
                        postac[0] += 40
                        postac[0] = min(postac[0], MAXHP)
                        print("Użyto Eliksir życia! +40 HP")
                    elif inp == "b" and Ekwipunek[1] > 0:
                        Ekwipunek[1] -= 1
                        postac[0] += 80
                        postac[0] = min(postac[0], MAXHP)
                        print("Użyto Ulepszonego Elikiru życia! +80 HP")
                    else:
                        print("Brak potek lub zła opcja!")           
