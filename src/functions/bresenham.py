from framebuffer import buffer

def reflex(x1, y1, x2, y2): #verifica reflexão
    try:
        m = (y2-y1)/(x2-x1) #Δy/Δx
    except ZeroDivisionError:
        m = 0
    reflex_t = [False, False, False]

    if m > 1 or m < -1:
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
    
    return(reflex_t, x1, y1, x2, y2) #reflexao retorna o vetor com tipos de reflexao marcadas

def reverse_reflex(troca, pts): #inversão da reflexão
    pts_reverse = []

    for p in pts:
        if troca[1]: p[1] *= -1
        if troca[0]: p[0] *= -1
        if troca[2]: p[0], p[1] = p[1], p[0]
        pts_reverse.append(p)
    return pts_reverse #p' = vetor com pontos trocados

def bresenham(pts):
    [[x1,y1], [x2, y2]] = pts

    troca, x1, y1, x2, y2 = reflex(x1, y1, x2, y2)
    x = x1
    y = y1
    try:
        m = (y2-y1)/(x2-x1) #Δy/Δx
    except ZeroDivisionError:
        m = 0
    e = m - (1/2)
    p = []

    p.append([x,y]) #vetor de pontos para desenho

    while x < x2:
        if e >= 0:
            y += 1
            e -= 1
        x += 1
        e += m
        p.append([x,y])

    p = reverse_reflex(troca, p) #faz a inversão da reflexão

    return p 