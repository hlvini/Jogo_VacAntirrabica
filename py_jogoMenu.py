#Importando Libraries 
import pygame
import sys

# Inicializando Pygame
pygame.init()

# Dimensões de Tela
largura = 800
altura = 600

# Cores do Menu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Fontes
pygame.font.init()
font = pygame.font.Font(None, 74)

# Superfície do Display
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Título")

# Menu
opcoes = ["[JOGAR]", "[OPÇÕES]", "[SAIR]"]

# 'def' é uma keyword usada para definir (ou criar) uma função
# função é um bloco de código que somente roda quando chamado
# E.X: def myFunction()
#           print("Hello Function")
# myFunction()

# Essa função sera utilizadas para mostrar as opções da var. 
#'opcoes', centralizar as opçoes, atualizar o display 
#e destacar a opção selecionada em azul
def draw_menu(opcao_selec):
    tela.fill(BLACK)

    for i, opcao in enumerate(opcoes):
        if i == opcao_selec:
            color = BLUE
        else:
            color = WHITE

        text = font.render(opcao, True, color)
        text_rect = text.get_rect(center=(largura // 2, 150 + i * 100))
        tela.blit(text, text_rect)

    pygame.display.flip()

#A função main() ficara responsável para rastrear a opção selecionada
#e receber os inputs do usuário e dar os outpus apropriados para cadas opção selecionada
def main():
    opcao_selec = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    opcao_selec = (opcao_selec + 1) % len(opcoes)
                elif event.key == pygame.K_UP:
                    opcao_selec = (opcao_selec - 1) % len(opcoes)
                elif event.key == pygame.K_RETURN:

                    if opcao_selec == 0:
                        print("JOGAR")
                        # Jogo
                    elif opcao_selec == 1:
                        print("OPÇÕES")
                        # Opções
                    elif opcao_selec == 2:
                        pygame.quit()
                        sys.exit()

        draw_menu(opcao_selec)


if __name__ == "__main__":
    main()
