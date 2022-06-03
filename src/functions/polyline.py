from functions.bresenham import bresenham

def poli(pts): #define um poligno com os 3+ pontos
    init = pts[0]
    pts_poli = []

    for p in range(len(pts)):
        if p == len(pts)-1: pts_poli.append(bresenham([pts[p], init]))
        else: pts_poli.append(bresenham([pts[p], pts[p+1]]))
    
    return pts_poli