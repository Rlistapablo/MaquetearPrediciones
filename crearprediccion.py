from script import predicts as pr
from os import path, system, listdir
def menu_splits():
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
            comp(splits1)
        except:
            pass

def comp(split):
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
            all(split,league1)
        except:
            pass

def all(split,league):
    mat=[league]
    players=pr.getplayers(league,split)
    pl=[]
    for x in players:
        pl.append(x[0])
    lista=listdir(f'img\\teams\\{league.lower()}')
    teams=[]
    for x in lista:
        teams.append(x[:-4].upper())
    while True:
        system('cls')
        partidos=str(input(('Indica el número de partidos: ')))
        try:
            partidos=int(partidos)
            break
        except:
            pass
    matchs=[]
    for x in range(0,partidos):
        temps=[]
        while True:
            if len(temps)==2:
                matchs.append(temps[0]+'/'+temps[1])
                break
            system('cls')
            print('PARTIDOS')
            for y in matchs:
                print(y, end=' ')
            print()
            print('Escoge dos de estos equipos: ')
            for y in teams:
                print(y, end=' ')
            print()
            while True:
                te=str(input(': '))
                for y in teams:
                    if y==te:
                        temps.append(te)
                break
    mat.append(matchs)
    temp_pl=[]
    while len(pl)!=0:
        system('cls')
        for x in pl:
            print(x,end=' ')
        print()
        pla=str(input('Indica los jugadores que quieres añadir (0 para continuar):'))
        if pla=='0':
            break 
        for x in range(0,len(pl)):
            if pl[x]==pla:
                print(x)
                temp_pl.append([pla])
    if temp_pl==[]:
        input('ERROR, NO PUSISTE NINGUN JUGADOR')
        exit()
    for x in matchs:
        opt=x.split('/')
        for y in range(0,len(temp_pl)):
            system('cls')
            print(f"PARA {temp_pl[y][0]}, ESCOGE ENTRE {opt[0]} y {opt[1]}")
            while True:
                re=str(input(':'))
                if re==opt[0] or re==opt[1]:
                    temp_pl[y].append(re)
                    break 
    for x in temp_pl:
        mat.append(x)
    j=str(input('INDICA EL NOMBRE DE LA JORNADA: '))
    pr.gens(mat,j,split)
    input('DONE')
    
    

menu_splits()
