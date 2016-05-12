from header import *
from locke import *
from menu import *



# Initialize all the Pygame Modules
pygame.init()

#Criando a janela principal
(width, height) = (500,350)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()



#Instancia o objeto que faz o menu
menuObjeto = menuJogo() 
#Menu Principal e selecao
menuObjeto.selecionaMenuPrincipal(janelaPrincipal)
#Seleciona qual personagem tal personagem vai jogar
menuObjeto.selecionaChar(janelaPrincipal)


#Background set
background_colour = (0,0,0)

#configuracoes
pygame.display.set_caption('Lutadores EAD')

#clock do jogo
clock = pygame.time.Clock() # create a clock object for timing

#Instancia
jogador1 = Jogador()

#variavel de estado do jogo
jogoRunning = True

teste 	= pygame.image.load('sprites\paper.png')

#loop principal final
while jogoRunning:
	#ATUALIZA A JANELA
	janelaPrincipal.fill(background_colour)
	#Jogador Idle
	jogador1.verificaTeclado(janelaPrincipal)
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogoRunning = False
		pass
	clock.tick_busy_loop(10)
	janelaPrincipal.blit(teste,(100,100),(0,0,500,500))
	pygame.display.update()
	pass





