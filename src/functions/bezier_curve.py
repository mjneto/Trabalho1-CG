from functions.bresenham import bresenham

def bezier_point(control_pts, t, n): #interpolações
    pts = control_pts

    for r in range(1, n+1):
        for i in range(0, (n-r)+1):
            pts[i] = [
                int(((1-t) * pts[i][0] + t * pts[i+1][0])//1),
                int(((1-t) * pts[i][1] + t * pts[i+1][1])//1)]

    return [pts[0][0], pts[0][1]] #novo ponto

def bezier(pts):#define a curvatura da linha para dados pontos de controles
    control_pts = pts
    n = len(control_pts) - 1
    pts_curve = []
    p = []
    
    for t in range(0, 16):
        pts_curve.append(bezier_point(control_pts, t / 15, n))

    for i in range(len(pts_curve)-1):
        p += bresenham([pts_curve[i], pts_curve[i+1]])

    return p
        