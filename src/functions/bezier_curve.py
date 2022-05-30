from functions.bresenham import bresenham

def bezier_point(control_pts, t, n):
    pts = control_pts
    r = 1
    i = 0

    while r <= n:
        while i <= (n-r):
            pts[i] = [round((1-t) * pts[i][0] + t * pts[i+1][0]), round((1-t) * pts[i][1] + t * pts[i+1][1])]
            i += 1
        r += 1

    return [pts[0][0], pts[0][1]] #novo ponto

def bezier(pts):#define a curvatura da linha para dados pontos de controles
    control_pts = pts
    n = len(control_pts) - 1
    pts_curve = []
    p = []
    t = 0
    i = 0
    
    while t <= 15:
        pts_curve.append(bezier_point(control_pts, t / 15, n))
        t += 1

    while i < len(pts_curve) - 1:
        p += bresenham([pts_curve[i], pts_curve[i+1]])
        i += 1

    return p
        