from Grade import *

def reflexao(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)

    if m > 1 or m < -1: #se 0 < m < 1
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        return (0, x1, y1, x2, y2)
    elif x1 > x2:
        x1 = x1 * -1
        x2 = x2 * -1
        return (1, x1, y1, x2, y2)
    elif y1 > y2:
        y1 = -abs(y1)
        y2 = -abs(y2)
        return (2, x1, y1, x2, y2)
    else:
        return(None, x1, y1, x2, y2)

def reflexaoInv(troca, p): #inversão da reflexão
    pl = [] #p' = vetor com pontos trocados

    if troca == 0:
        for i in p:
            pl.append((list(reversed(i)))) #reverso
        return pl
    elif troca == 1:
        for i in p:
            pl.append([i[0] * -1, i[1]]) #negativo x
            #print(pl)
        return pl
    elif troca == 2:
        for i in p:
            pl.append([i[0], i[1] * -1]) #negativo y
        return pl
    else:
        return p #nenhuma das condições

def bresenham(pontos):
    [[x1,y1], [x2, y2]] = pontos #unpack p1, p2
    troca, x1, y1, x2, y2 = reflexao(x1, y1, x2, y2) #verifica reflexão

    x = x1
    y = y1
    m = (y2-y1)/(x2-x1) #Δy/Δx
    e = m - (1/2)
    p = [] #vetor de pontos
    
    desenhaPonto([x,y])

    print('({},{})'.format(x,y)) #desenha ponto inicial
    p.append([x,y]) 

    while x < x2:
        if e >= 0:
            y = y + 1
            e = e - 1
        x = x + 1
        e = e + m

        print('({},{})'.format(x,y)) #desenha pontos subsequentes
        p.append([x,y])

    p = reflexaoInv(troca, p)
    print('Pontos pintados:', p)