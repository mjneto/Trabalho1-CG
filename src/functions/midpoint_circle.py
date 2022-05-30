def draw8points(x, y, xc, yc): #guarda os 8 pontos para desenhar
    circle_points = []

    circle_points.append([x + xc, y + yc])
    circle_points.append([y + xc, x + yc])
    circle_points.append([y + xc, -x + yc]) 
    circle_points.append([x + xc, -y + yc]) 
    circle_points.append([-x + xc, -y + yc]) 
    circle_points.append([-y + xc, -x + yc]) 
    circle_points.append([-y + xc, x + yc])
    circle_points.append([-x + xc, y + yc])

    return circle_points

def circle_mid(r, xc, yc): #define o circulo dado centro e raio
    pts = []
    x = 0
    y = r
    e = -r

    pts.append(draw8points(x, y, xc, yc))

    while(x <= y):
        e += 2 * x + 1
        x += 1
        if e >= 0:
            e += 2 - 2 * y
            y -= 1

        pts.append(draw8points(x, y, xc, yc))

    return pts