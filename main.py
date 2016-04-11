from header import *
from animacao import *

#Criando a janela principal
(width, height) = (500,500)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()

#Background set
background_colour = (0,0,0)
janelaPrincipal.fill(background_colour)

#configuracoes
pygame.display.set_caption('Lutadores EAD')
jogoRunning = True

#clock do jogo
clock = pygame.time.Clock() # create a clock object for timing

#Instancia
jogador1 = Jogador()

#loop principal final
while jogoRunning:
	#ATUALIZA A JANELA
	pygame.display.flip()

	#Jogador Idle
	jogador1.idleAnimation(janelaPrincipal,20,20)

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogoRunning = False
		pass
	clock.tick(8)
	pass
