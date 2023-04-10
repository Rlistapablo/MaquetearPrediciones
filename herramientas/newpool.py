from herramientas.script import predicts as pr
mat=['LEC',
     ['VIT/SK','FNC/G2', 'AST/BDS', 'HRT/KOI', 'MAD/XL'],
     ['PABLO','VIT','FNC','AST','KOI','MAD'],
     ['ALVARO','SK','FNC','BDS','TH','MAD'],
     ['JACO','SK','G2','AST','KOI','XL'],
     ['PABLO','VIT','FNC','AST','KOI','MAD'],
     ['ALVARO','SK','FNC','BDS','TH','MAD'],
     ['JACO','SK','G2','AST','KOI','XL'],
     ['PABLO','VIT','FNC','AST','KOI','MAD'],
     ['ALVARO','SK','FNC','BDS','TH','MAD'],
     ['JACO','SK','G2','AST','KOI','XL'],
     ['PABLO','VIT','FNC','AST','KOI','MAD'],
     ['ALVARO','SK','FNC','BDS','TH','MAD'],
     ['JACO','SK','G2','AST','KOI','XL'],
     #['PABLO','VIT','FNC','AST','KOI','MAD'],
     ]
'''
a=pr.gen_mat(mat)
for x in a:
    for c in x:
        print(c, end=', ')
    print()
pr.gen_img(a)'''
pr.gens(mat,'LEC JORNADA 1')