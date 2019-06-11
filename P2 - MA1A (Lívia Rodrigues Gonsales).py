#Lívia Rodrigues Gonsales - P2 MA1A (PROVA A)

#Exercício 1 
def media():
    with open('series.csv', 'r') as series:
        for line in series.readlines():
            coluna = line.split(',')
            imdb = float(coluna[5])
            netflix = float(coluna[6])
            med = (imdb+netflix)/2
            print(med)
    series.close()
media()





#Exercício 2

eps = []
series = open('series.csv', 'r')
for line in series.readlines():
    coluna = line.split(',')
    nomep = coluna[4]
    eps.append(nomep)
seriesnovas = open('series_novas.csv', 'r')
for line in seriesnovas.readlines():
    coluna = line.split(',')
    nomep = coluna[4]
    eps.append(nomep)



#Exercício 3

bm = 0
bb = 0
tbbt = 0
fnds = 0
fl = 0
ds = 0
su = 0
lu = 0
na = 0 #narcos
total = int(len(eps))
series = open ('series.csv', 'r')
seriesnovas = open('series_novas.csv', 'r')
for line in series.readlines() and seriesnovas.readlines():
    coluna = line.split(',')
    nome = coluna[0]
    for i in range(total):
        if nome == 'Black Mirror':
            bm = bm+1
            ser = bm
        elif nome == 'Breaking Bad':
            bb = bb+1
            ser = bb
        elif nome == 'The Big Bang Theory':
            tbbt = tbbt+1
            ser = tbbt
        elif nome == 'Friends':
            fnds = fnds+1
            ser = fnds
        elif nome == 'Fuller House':
            fl = fl+1
            ser = fl
        elif nome == 'Designated Survivor':
            ds = ds+1
            ser = ds
        elif nome == 'Suits':
            su = su+1
            ser = su
        elif nome == 'Lucifer':
            lu = lu+1
            ser = lu
        else:
            na = na+1
            ser = na
aaa = ['Black Mirror', 'Breaking Bad', 'The Big Bang Theory', 'Friends', 'Fuller House', 'Designated Survivor', 'Suits', 'Lucifer', 'Narcos']
bbb = [bm, bb, tbbt, fnds, fl, ds, su, lu, na]
x = 0
while x<10:
    print(aaa[x], ': ', bbb[x])
    x = x+1

#Exercício 4

dicio = {'Black Mirror': med/bm, 'Breaking Bad': med/bb, 'The Big Bang Theory': med/tbbt, 'Friends': med/fnds, 'Fuller House': med/fl, 'Designated Survivor': med/ds, 'Suits': med/su, 'Lucifer': med/lu, 'Narcos': med/na}  
print(dicio)




            
            
            
    






























