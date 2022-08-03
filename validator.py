# Bondoc Ana, Rus Alexandru, Ionescu Radu

stari = []
stare_start = []
stare_reject = []
stare_acceptare = []
in_alfabet = []
banda_alfabet = []
tranzitii = {}
status = 0

def validare(tip, stare, linie): #in loc de stare poate fi input, tranzitie, alfabet
    global status
    # in functie de tip validam: 3(tranzitia), 2(alfabet input), 1(tape input), 0(starile)
    if tip == 3:
        tranzitie = [i[1:-1].split(",") for i in stare.split("to")] # impartim dupa "to", si scapam de paranteze (), astfel filtram continutul

        Q1 = tranzitie[0][0] #starea de curenta
        Q2 = tranzitie[1][0] # starea destinatie
        banda_1 = tranzitie[0][1] #continut banda1
        banda_2 = tranzitie[0][2] #continut banda2
        ptbanda_1 = tranzitie[1][1] #continut pe care il scriem pe banda1
        ptbanda_2 = tranzitie[1][2] #continut pe care il scriem pe banda2
        dir_1 = tranzitie[1][3] 
        dir_2 = tranzitie[1][4]

        if dir_1 != 'L' and dir_1 != 'R': #directie invalida
            status = 1
            print(f"wrong direction")
        if dir_2 != 'L' and dir_2 != 'R': #directie invalida 
            status = 1
            print(f"wrong direction")

        ok = 0
        for i in tranzitii:
            if Q1 == i:
                ok = 1
                break

        if ok == 0: #prima tranzitie a lui q1
            tranzitii[Q1] = []

        tranzitii[Q1].append([banda_1, banda_2, Q2, ptbanda_1, ptbanda_2, dir_1, dir_2])

    elif tip == 2:
        ok = 0
        for i in in_alfabet:
            if stare == i:
                ok = 1
                break
        if ok == 0:
            # verificam sa nu fi fost deja citit caracterul, e dublura astfel
            in_alfabet.append(stare)
        else:
            print(f" {stare} already exists") #eroare, semanlizata si prin status care devine 1
            status = 1

    elif tip == 1:
        ok = 0
        for i in banda_alfabet:
            if stare == i:
                ok = 1
                break
        if ok == 0:
            # verificam sa nu fi fost deja citit caracterul, e dublura astfel
            if stare == "":
                stare = " "
                banda_alfabet.append(stare)
            else:
                banda_alfabet.append(stare)
 
        else:
            print(f"{stare} already exists")
            status = 1

    elif tip == 0:
        if stare[-2:] == " s":
            # daca este start state, ne uitam la ultimele 2 caractere(len(s) + len(' '))
            stare = stare[:2]
            stare_start.append(stare)
        elif stare[-2:] == " a":
            # daca este accept state
            stare = stare[:2]
            stare_acceptare.append(stare)
        elif stare[-2:] == " r": #daca este reject state
            stare = stare[:2]
            stare_reject.append(stare)

        ok = 0
        for i in stari:
            if stare == i:
                print(f"{stare} already exists")
                status = 1
                break
        if ok == 0: 
            stari.append(stare)
        


def citire(nume):
    global status
    g = open(nume)
    ls = []
    for linie in g:
        ls.append(linie.rstrip("\n"))
    k = 0  # contor pentru linia curenta
    while k < len(ls):
        if ls[k] == "States:": # verificam validitatea starilor
            a = 0
        elif ls[k] == "Tape alphabet:": #verificam validitatea alfabetului de tape
            a = 1
        elif ls[k] == "Input alphabet:": # verificam validitatea alfabetului de input
            a = 2
        elif ls[k] == "Transitions:": # verificam validitatea tranzsitiilor
            a = 3
        k = k + 1
        while ls[k] != "END":
            validare(a, ls[k], k)
            k = k + 1
        k = k + 1


def validari():
    global status
    accept = 0
    reject = 0
    start = 0

    stari_aiurea = []

    for stare_curenta in tranzitii:
        for i in range(len(tranzitii[stare_curenta])): 
            tranzitie_curenta = tranzitii[stare_curenta][i] #iteram prin tranzitiile starii curente
            
            #un caracter pe post de tape input nu este in alfabetul tape
            if tranzitie_curenta[0] not in banda_alfabet:
                status = 1
                print(f" one tape character should be in the tape alphabet")

            if stare_curenta not in stari:
                # starea curenta nu se afla printre starile din fisier
                status = 1
                if stare_curenta not in stari_aiurea:
                    stari_aiurea.append(stare_curenta)

            # directia nu este una buna
            if tranzitie_curenta[5] != 'L' and tranzitie_curenta[5] != 'R':
                status = 1
                print(f" wrong direction")
            if tranzitie_curenta[6] != 'L' and tranzitie_curenta[6] != 'R':
                status = 1
                print(f" wrong direction")
            if tranzitie_curenta[2] not in stari:
                # starea destinatie nu se afla printre starile din fisier
                status = 1
                if tranzitie_curenta[2] not in stari_aiurea:
                    stari_aiurea.append(tranzitie_curenta[2])

    for s in stari_aiurea: #afisam starile din tranzitii care nu fac parte din fisier, daca exista
        print(f" {s} is not a proper state", end = "\n")

    for stare_curenta in stari:
        if stare_curenta in stare_acceptare:
            accept = accept + 1
        if stare_curenta in stare_reject:
            reject = reject + 1
        if stare_curenta in stare_start:
            start = start + 1

    if accept != 1:
        # sunt mai multe sau mai putine stari de acceptare
        status = 1
        print(f" accept state should be unique")
    if reject != 1:
        # sunt mai multe sau mai putine stari de refuz
        status = 1
        print(f" reject state should be unique")
    if start != 1:
        # sunt mai multe sau mai putine stari de refuz
        status = 1
        print(f" start state should be unique")



citire("tm_config_file")

for i in in_alfabet:
    # verificam ca alfabetul de input sa fie inclus in cel de tape
    ct = 1
    for j in banda_alfabet:
        if i == j:
            ct = 0
    if ct == 1:
        status = 1
        print(f" {i} is not included in tape alphabet")

validari()
if status == 0:
    print("Good job, VALID")
