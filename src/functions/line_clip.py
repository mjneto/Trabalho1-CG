from functions.bresenham import bresenham

def mkcode(x, y, x_min, y_min, x_max, y_max):

    # Calcula os bit para cada ponto

    code = 0
    if x < x_min:
        code |= 1
    elif x > x_max:
        code |= 2
    if y < y_min:
        code |= 4
    elif y > y_max:
        code |= 8
    return code

def cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max):

    # Calcula os bit para cada ponto
    code1 = mkcode(x1, y1, x_min, y_min, x_max, y_max)
    code2 = mkcode(x2, y2, x_min, y_min, x_max, y_max)
    accept = False

    while True: # Enquanto houver pontos para desenhar
        if not (code1 | code2): # Se os pontos estão dentro da área
            accept = True
            break
        elif code1 & code2: # Se os pontos estão fora da área
            break
        else: 
            if code1:
                code_out = code1
            else:
                code_out = code2 
            
            #intersecções
            if code_out & 8:
                y = y_max
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            elif code_out & 4:
                y = y_min
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            elif code_out & 2:
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code_out & 1:
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = mkcode(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2 = x
                y2 = y
                code2 = mkcode(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        return bresenham([[round(x1), round(y1)], [round(x2), round(y2)]]) #em caso de corte
    else:
        return bresenham([[round(x1), round(y1)], [round(x2), round(y2)]]) #retorna a linha original