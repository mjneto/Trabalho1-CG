
from functions.bresenham import bresenham

def poli(pts): #define um poligno com os 3+ pontos
    init = pts[0]
    pts_poli = []

    for p in range(len(pts)):
        try:
            if pts[p+1]: pts_poli.append(bresenham([pts[p], pts[p+1]]))
        except IndexError:
            pts_poli.append(bresenham([pts[p], init]))
    
    return pts_poli