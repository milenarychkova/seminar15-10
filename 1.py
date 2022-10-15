from random import randint

def vyvodchar(d,z,u,v):
    print("длина норки =", d)
    print("здоровье =", z)
    print("уважение =", u)
    print("вес =", v)


def draka(tip):
    global zdorov, uvazhenie
    cifra=tip*10
    if tip==1:
        vp=30
    if tip==2:
        vp=50
    if tip==3:
        vp=70
    iskhod=randint(0,ves+vp)
    if iskhod<=ves: #победа
        print("вы выиграли в сражении")
        uvazhenie+=cifra
    else:
        print("вы проиграли в сражении")
        zdorov-=cifra


def son():
    global zdorov, dlina, ves, uvazhenie

    dlina -= 2
    ves -= 2
    uvazhenie -= 5
    zdorov+=20





dlina,zdorov,uvazhenie,ves=9,100,20,30
vyvodchar(dlina,zdorov,uvazhenie,ves)
while uvazhenie<100:
    if zdorov<=0 or dlina<=0 or ves<=0:
        print("вы проиграли")
        break
    print("--------------------------")
    print ("выберите действие на день:")
    print("1-спать "
          "2-копать норку "
          "3-поесть травку "
          "4-подраться")
    vybor=int(input())
    if vybor==1:
        son()
        vyvodchar(dlina,zdorov,uvazhenie,ves)
    if vybor==2:
        print ("выберите интенсивность копания:")
        print ("1-интенсивно "
               "2-лениво")
        intensiv_vybor=int(input())
        if intensiv_vybor==1:
            dlina+=5
            zdorov-=30
        if intensiv_vybor==2:
            dlina+=2
            zdorov-=10
        vyvodchar(dlina, zdorov, uvazhenie, ves)
    if vybor==3:
        print("выберите свежесть травки:")
        print("1-жухлая "
              "2-зеленая")
        trava_vybor=int(input())
        if trava_vybor==1:
            zdorov+=10
            ves+=15
        if trava_vybor==2:
            if uvazhenie<30:
                zdorov-=30
            if uvazhenie>=30:
                zdorov+=30
                ves+=30
        vyvodchar(dlina, zdorov, uvazhenie, ves)
    if vybor==4:
        print("выберите уровень противника:")
        print("1- драться с слабым "
              "2- драться с средним"
              "3- драться с сильным")
        draka_vybor=int(input())
        draka(draka_vybor)
        vyvodchar(dlina, zdorov, uvazhenie, ves)
        if uvazhenie > 100 and zdorov > 0 and dlina > 0 and ves > 0:
            print(" win")
            break
    if zdorov<=0 or dlina<=0 or ves<=0:
        print("вы проиграли")
        break
    print("--------------------------")
    print("наступила ночь")
    dlina = dlina - 2
    zdorov += 20
    uvazhenie -= 2
    ves -= 5
    vyvodchar(dlina, zdorov, uvazhenie, ves)






