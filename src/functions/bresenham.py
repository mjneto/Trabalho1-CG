from framebuffer import buffer

def reflex(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    reflex_t = [False, False, False]

    if m > 1 or m < -1: #se 0 < m < 1
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        reflex_t[2] = True
    if x1 > x2:
        x1 *= -1
        x2 *= -1
        reflex_t[0] = True
    if y1 > y2:
        y1 = -abs(y1)
        y2 = -abs(y2)
        reflex_t[1] = True
    
    return(reflex_t, x1, y1, x2, y2)

def reverse_reflex(troca, pts): #inversão da reflexão
    pl = [] #p' = vetor com pontos trocados

    for p in pts:
        if troca[1]: p[1] *= -1
        if troca[0] == True: p[0] *= -1
        if troca[2] == True: p[0], p[1] = p[1], p[0]
        pl.append(p)
    return pl

def bresenham(pontos):
    [[x1,y1], [x2, y2]] = pontos #unpack p1, p2
    troca, x1, y1, x2, y2 = reflex(x1, y1, x2, y2) #verifica reflexão

    x = x1
    y = y1
    m = (y2-y1)/(x2-x1) #Δy/Δx
    e = m - (1/2)
    p = [] #vetor de pontos
    p.append([x,y])

    while x < x2:
        if e >= 0:
            y += 1
            e -= 1
        x += 1
        e += m
        p.append([x,y])

    p = reverse_reflex(troca, p)

    return p