from random import randint, randrange
'''
První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6),
dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu.
Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.
'''
def hody():
    hod = 0
    pocet_kol=0
    while hod < 6:
        hod = randint(1, 6)
        pocet_kol += 1
        if hod < 6:
            #print('Tvuj hod je: ', hod)
            #print('Tve kolo: ', pocet_kol)
            #soucet = soucet + karta
            pass
        elif hod == 6:
            print('Tvuj hod je: ', hod)
            print('Tvuj pocet kol: ', pocet_kol)
            return(pocet_kol)

def hrac():
    nejvyssi_hod=0
    for i in range(1,5):
        cislo_hrace=i
        print('Cislo hrace: ',cislo_hrace)
        pocet_kol=hody()
        if nejvyssi_hod<pocet_kol:
            nejvyssi_hod=pocet_kol
            nejlepsi_hrac=cislo_hrace
    return('Cislo nejlepsiho hrace: ', nejlepsi_hrac, 'Pocet her s kterymi vyhral je: ', nejvyssi_hod)

print(hrac())
