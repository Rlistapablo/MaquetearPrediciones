from PIL import Image, ImageDraw, ImageFont
import datetime
import sqlite3
class predicts:
    def gens(mats,jornada,splits):
        global split
        split=splits
        global jor
        jor=jornada
        predicts.gen_img(mats)
    
    def getsplit():
        with open("splits.qw","r+") as file:
            sl=file.read().split('\n')
            file.close
        return sl

    def alpha(img):
        img=img.convert('RGBA')
        pixdata = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        return img

    def getcolors(liga):
        with open("colors.qw","r") as file:
            lines=file.read()
            file.close
        new=[]
        for x in lines.split('\n'):
            if x[0]!='#' and x[0]!='' and x[0]!=' ':
                new.append(x)
        for x in new:
            if x.split(':')[0].lower()==liga:
                val=x.split(':')[1]
                tuples=[]
                global background
                global details
                global details2
                for y in val.split('|'):
                    a=y.split(',')
                    f=(int(a[0]),int(a[1]),int(a[2]))
                    tuples.append(f)
                background=tuples[0]
                details=tuples[1]
                details2=tuples[2]

    def gen_mat(mat):
        newmat=[]
        predicts.getcolors(mat[0].lower())
        comp=mat[0].lower()
        ##CABECERA
        temp=[f'img\\comp\\{comp}.jpg']
        for x in range(2,len(mat)):
            temp.append('img\\players\\{}.jpg'.format(mat[x][0].lower()))
        newmat.append(temp)
        ##PUNTOS
        temp=['Points']
        for x in range(2,len(mat)):
            temp.append(predicts.get_points(mat[x][0].upper(),mat[0].upper())[0])
        newmat.append(temp)
        ##PREDICTS
        for x in range(0,len(mat[1])):
            temp=[mat[1][x]]
            for y in range(2,len(mat)):
                temp.append(f'img\\teams\\{comp}\\{mat[y][x+1].lower()}.jpg')
            newmat.append(temp)
        return newmat

    def gen_img(mats):
        mat=predicts.gen_mat(mats)
        plantilla=predicts.make_plant(len(mat),len(mat[0]))
        plantilla=predicts.inserts(plantilla,mat)
        plantilla.save(f"predicts\\{jor.replace(' ','_')}_{datetime.date.today()}.png")

    def make_plant(lens,lens2):
        #VALUES
        white=(255,255,255)
        ancho=(500*lens2+(5*lens2))
        alto=((500*(lens-1))+(5*(lens))+300)
        #PRINTING
        plantilla=Image.new(mode='RGBA',size=(ancho,alto),color=background)
        square1=Image.new(mode='RGBA',size=(500,alto),color=details)
        square2=Image.new(mode='RGBA',size=(ancho,150),color=details)
        square3=Image.new(mode='RGBA',size=(ancho,500),color=details2)
        #PARTIDOS
        plantilla.paste(square1,(0,0))
        #JORNADA
        plantilla.paste(square2,(0,0))
        #PLAYERS
        plantilla.paste(square3,(0,150))
        #SEPARADORES
        vert=Image.new(mode='RGBA',size=(5,alto-150),color=white)
        hor=Image.new(mode='RGBA',size=(ancho,5),color=white)
        #VERTICAL
        count=500
        for x in range(0,lens2):
            plantilla.paste(vert,(count,150))
            count+=505
        #HORIZONTAL
        count=800
        for x in range(0,lens-1):
            plantilla.paste(hor,(0,count))
            count+=505
        #POINTS
        plantilla.paste(square2,(0,650))
        return plantilla
    
    def inserts(plantilla,mat):
        font= ImageFont.truetype("arial.ttf",75)
        #CABECERA
        dr=ImageDraw.Draw(plantilla)
        w,h=dr.textsize(jor+' '+split)
        dr.text(((((plantilla.size[0]/4)-w)/2),(150)/2), jor+' '+split, fill='black', font=font)
        #PLAYERS
        count=0
        for x in mat[0]:
            temp=Image.open(x)
            temp=predicts.alpha(temp)
            plantilla.alpha_composite(temp,(count+50,150+50))
            temp.close()
            count+=505
        #POINTS
        dr.text((100,650+50),mat[1][0],fill='black',font=font)
        count=0
        for x in mat[1]:
            if str(x)!='Points':
                dr.text((count+250,650+50),str(x),fill='black',font=font)
            count+=505
        #PARTIDOS
        county=800
        for x in range(2,len(mat)):
            countx=0
            for y in range(0,len(mat[x])):
                if y==0:
                    dr.text((countx+125,county+225),mat[x][y],fill='black',font=font)
                else:
                    temp=Image.open(mat[x][y])
                    temp=predicts.alpha(temp)
                    plantilla.alpha_composite(temp,(countx+50,county+50))
                    temp.close()
                countx+=505
            county+=505
        return plantilla

    def add_player(name,comp,split):
        cnx=sqlite3.connect('db\\dbpoints.db')
        cursor=cnx.cursor()
        cursor.execute(f"""
            INSERT INTO points (Name,Comp,Split,Points,LastUpdate) VALUES ('{name}','{comp}','{split}',0,'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}');
        """)
        cnx.commit()
        cnx.close()
    
    def get_points(player,comp):
        cnx=sqlite3.connect('db\\dbpoints.db')
        cursor=cnx.cursor()
        cursor.execute(f"""
            SELECT Points FROM points WHERE Name = '{player}' AND Comp = '{comp}' AND Split = '{split}'
        """)
        point=cursor.fetchone()
        cnx.close()
        return point
    
    def update_points(player,comp,split,points):
        cnx=sqlite3.connect('db\\dbpoints.db')
        cursor=cnx.cursor()
        cursor.execute(f"""
            SELECT Points FROM points WHERE Name = '{player}' AND Comp = '{comp}' AND Split = '{split}'
        """)
        point=cursor.fetchone()[0]+points
        cnx.close()
        cnx=sqlite3.connect('db\\dbpoints.db')
        cursor=cnx.cursor()
        cursor.execute(f"""
            UPDATE points
            SET Points = {point}, 
            LastUpdate = '{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
            WHERE Name = '{player}' AND Comp = '{comp}'AND Split = '{split}'
        """)
        cnx.commit()
        cnx.close()
        return point
    
    def getplayers(comp,split):
        cnx=sqlite3.connect('db\\dbpoints.db')
        cursor=cnx.cursor()
        cursor.execute(f"""
            SELECT Name FROM points WHERE Comp = '{comp}' AND Split = '{split}'
        """)
        aaa=cursor.fetchall()
        cnx.close()
        return aaa