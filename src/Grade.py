import pygame

class framebuffer:
    #cores
    white = (255, 255, 255)
    blue = (0, 176, 240)
    black = (0, 0, 0)
    
    #margem, largura, altura do "pixel"
    margin = 1
    width = 10
    height = 10

    def __init__(self, size):
        matriz = self.criarMatriz() #chama função para criar matriz responsável pela grade desenhada

        window = pygame.display.set_mode(size) #constroi a tela

        done = False #flag de parada
        coordenadas = [] #vetor de coordenadas clicadas

        while done == False:
            for event in pygame.event.get(): #loop grade
                if event.type == pygame.QUIT: #sair
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN: #clique
                    pos = pygame.mouse.get_pos()
        
                    column = pos[0] // (framebuffer.width + framebuffer.margin)
                    row = pos[1] // (framebuffer.width + framebuffer.margin)

                    matriz[row][column] = 1 #seta ponto clicado com 1
                    coordenadas.append([column, row])

            self.desenhaGrade(window, matriz) 
    
    def desenhaPonto():
        pass

    def desenhaGrade(self, window, matriz): #desenha a grade
        window.fill(framebuffer.blue) #preenche fundo
    
        for row in range(36):
                for column in range(36):
                    color = framebuffer.white
                    if matriz[row][column] == 1:
                        color = framebuffer.black
                    pygame.draw.rect(window, color, [(framebuffer.margin + framebuffer.width) * column + framebuffer.margin,
                    (framebuffer.margin + framebuffer.height) * row + framebuffer.margin, framebuffer.width, framebuffer.height]) #desenha os quadrados

        pygame.display.flip() #atualiza

    def criarMatriz(self): #cria matriz responsável pela grade desenhada
        matriz = []

        for row in range(37):
            matriz.append([])
            for column in range(37):
                matriz[row].append(0) #seta toda matriz com 0

        return matriz

frame = framebuffer([400,400])
pygame.quit ()
