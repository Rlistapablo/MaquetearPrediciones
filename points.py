from script import predicts as pr
from os import path, system, listdir
def mainmenu():
    while True:
        system('cls')
        print("INDICA LO QUE QUIERES HACER:\n1.AÑADIR JUGADOR\n2.ACTUALIZAR PUNTOS")
        a=str(input(': '))
        if a=='1':
            menu_splits('1')
        if a=='2':
            menu_splits('2')
        if a=='':
            exit()

def menu_splits(act):
    splits=pr.getsplit()
    while True:
        system('cls')
        cou=1
        print('SELECCIONA UN SPLIT:')
        for x in splits:
            print(str(cou)+'.',x)
            cou+=1
        r=str(input('VALUE (NULL PARA SALIR): '))
        if r=='':
            break
        try:
            splits1=splits[int(r)-1]
            comp(act,splits1)
        except:
            pass

def comp(act,split):
    lista=listdir('img\\comp')
    league=[]
    for x in lista:
        league.append(x[:-4].upper())
    while True:
        system('cls')
        count=1
        print('SELECCIONA UNA LIGA')
        for x in league:
            print(str(count)+'.',x)
            count+=1
        r=str(input('VALUE (NULL PARA SALIR): '))
        if r=='':
            break
        try:
            league1=league[int(r)-1]
            ot(act,split,league1)
        except:
            pass

def ot(act,split,league):
    if act=='1':
        add(split,league)
    elif act=='2':
        addpont(split,league)

def add(split,league):
    system('cls')
    players=pr.getplayers(league,split)
    pl=[]
    for x in players:
        pl.append(x[0])
    lista=listdir('img\\players')
    pla=[]
    for x in lista:
        pla.append(x[:-4].upper())
    for x in pl:
        for y in pla:
            if x==y:
                pla.remove(x)
    if len(pla)==0:
        input('NO SE PUEDE AÑADIR JUGADOR A LA LIGA, YA QUE LA IMAGEN NO SE HAYA')
        exit()
    while True:
        for x in pla:
            print(x,end=' ')
        print()
        a=str(input('INDICA EL JUGADOR QUE QUIERES AÑADIR: '))
        passa=False 
        for y in pla:
            if a==y:
                passa=True 
        if passa==True:
            break 
    add_player(a,league,split)

def addpont(split,league):
    players=pr.getplayers(league,split)
    pl=[]
    for x in players:
        pl.append(x[0])
    while True:
        for x in pl:
            print(x,end=' ')
        print()
        a=str(input('INDICA EL JUGADOR QUE QUIERES AÑADIR PUNTOS: '))
        passa=False 
        for y in pl:
            if a==y:
                passa=True 
        if passa==True:
            break 
    while True:
        b=str(input('CUANTOS PUNTOS: '))
        try:
            update(a,league,split,int(b))
            break
        except:
            pass


def add_player(name,comp,split):
    pr.add_player(name,comp,split)

def update(name,comp,split,points):
    pr.update_points(name,comp,split,points)

mainmenu()

