from header import *
from ken import *



# Initialize all the Pygame Modules
pygame.init()

#Criando a janela principal
(width, height) = (500,500)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()

#Background set
background_colour = (0,0,0)

#configuracoes
pygame.display.set_caption('Lutadores EAD')

#clock do jogo
clock = pygame.time.Clock() # create a clock object for timing

#Instancia
jogador1 = Jogador()

menu = pygame.image.load('sprites\How_to_start_a_business_crop.jpg')
janelaPrincipal.blit(menu,(0,0),(0,0,500,500))

jogoRunning = False
#Verifica todos os eventos 
while jogoRunning == False:
	evento = pygame.event.wait()	
	if evento.type == pygame.KEYDOWN:
		jogoRunning = True
		pass
	pass

# Pinta o background
janelaPrincipal.fill(background_colour)

#loop principal final
while jogoRunning:
	#ATUALIZA A JANELA
	pygame.display.flip()
	janelaPrincipal.fill(background_colour)
	#Jogador Idle
	jogador1.verificaTeclado(janelaPrincipal)

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogoRunning = False
		pass
	clock.tick(15)
	pass
