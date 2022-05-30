def coord_valid(matriz, x, y):
    return x >= 0 and x < len(matriz)-1 and y >= 0 and y < len(matriz)-1

def recursive_fill(matriz, x, y, pts):
    current = matriz[x][y]

    if(current == 0 and coord_valid(matriz, x, y)):
        matriz[x][y] = 1
        pts.append([x, y])

        recursive_fill(matriz, x+1, y, pts)
        recursive_fill(matriz, x, y+1, pts)
        recursive_fill(matriz, x-1, y, pts)
        recursive_fill(matriz, x, y-1, pts)

    return matriz, pts