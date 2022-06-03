def sutherland_hodgman(poli_pts, clip_poli):
    def inside(p): #confere se os pontos estão dentro da area do poligono
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
        
    def computeIntersection(): #calcula a interseção de dois segmentos
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
        dp = [ s[0] - e[0], s[1] - e[1] ]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
    output_list = poli_pts
    cp1 = clip_poli[-1]
 
    for clip_pt in clip_poli: #percorre todos os pontos do poligono de corte
        cp2 = clip_pt
        input_list = output_list
        output_list = []
        s = input_list[-1]
 
        for poli_pt in input_list:
            e = poli_pt
            if inside(e):
                if not inside(s):
                    output_list.append(computeIntersection())
                output_list.append(e)
            elif inside(s):
                output_list.append(computeIntersection())
            s = e
        cp1 = cp2
    for i in range(len(output_list)):
        output_list[i][0] = int(output_list[i][0]//1)
        output_list[i][1] = int(output_list[i][1]//1)

    return(output_list)