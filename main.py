from header import *
from locke import *
from menu import *



# Initialize all the Pygame Modules
pygame.init()

#Criando a janela principal
(width, height) = (500,350)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()

#Background set
background_colour = (0,0,0)

#configuracoes
pygame.display.set_caption('Lutadores EAD')

#clock do jogo
clock = pygame.time.Clock() # create a clock object for timing

#mixer do pygame
mixer = pygame.mixer.init()

#Instancia
jogador1 = Jogador()

#variavel de estado do jogo
jogoRunning = True

menu = pygame.image.load('wallpaper\itlescreen3.png')
janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
pygame.display.flip()

#variavel verifica se o menu foi aberto
menuAberto = False
#Verifica todos os eventos 
while menuAberto == False:
	evento = pygame.event.wait()	
	if evento.type == pygame.KEYDOWN:
		menuAberto = True
		pass
	pass



menuObjeto = menuJogo() 
#Menu Principal e selecao
menuObjeto.selecionaMenuPrincipal(janelaPrincipal)
#Seleciona qual personagem tal personagem vai jogar
menuObjeto.selecionaChar(janelaPrincipal)




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
	pygame.display.update()
	pass





