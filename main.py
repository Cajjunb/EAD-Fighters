from header import *
from locke import *



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

#inicializa a posicao da flecha do menu em uma opcao inicial
menu = pygame.image.load('wallpaper\itltescreenJogar.png')
janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
pygame.display.flip()
escolhaMenu = 'jogar'
while escolhaMenu != 'jogarApertado' and escolhaMenu != 'creditosApertado' :
	evento = pygame.event.wait()	
	if evento.type == pygame.KEYDOWN:
		#Caso pressionar o a
		if evento.key == pygame.K_LEFT:
			# Muda a imagem da seta esquerda
			menu = pygame.image.load('wallpaper\itltescreenJogar.png')
			escolhaMenu = 'jogar'
			pass
		#Caso pressionar o D
		elif evento.key == pygame.K_RIGHT:
			# Muda a imagem da seta Direita
			menu = pygame.image.load('wallpaper\itltescreenCreditos.png')
			escolhaMenu = 'creditos'
			pass
		#Caso pressionar o enter
		elif evento.key == pygame.K_RETURN:
			if escolhaMenu == 'jogar':
				escolhaMenu = 'jogarApertado'
			elif escolhaMenu == 'creditos':
				escolhaMenu = 'creditosApertado'
				pass
			pass
		pass
	janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
	pygame.display.flip()
	pass


#variavel verifica se o menu de selecao de personagem foi aberto
selecionarPersonagem 	= False
#Variavel que indica qual personagem ele funciona
personagemEscolhido 	= 1
charY = 1
charX = 1
#Selecao personagens imagem
menu = pygame.image.load('wallpaper\charselect.png')
seta = pygame.image.load('sprites\BackgroundMessagem2.png')
janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
janelaPrincipal.blit(seta,(90,210),(0,0,500,500))

pygame.display.flip()

#Verifica todos os eventos 
while selecionarPersonagem == False:
	
	evento = pygame.event.wait()	
	if evento.type == pygame.KEYDOWN:
		#Verificando o teclado para selecionar personagens
		if evento.key == pygame.K_RIGHT:
			charX += 1
			pass
		elif evento.key == pygame.K_LEFT:
			charX -= 1
			pass
		elif evento.key == pygame.K_DOWN:
			charY -= 1
			pass
		elif evento.key == pygame.K_UP:
			charY += 1
			pass
		elif evento.key == pygame.K_RETURN:
			#Sai do personagem e faz a escolha
			selecionarPersonagem = True
			pass
		pass

		charX = abs(charX % 4)
		charY = abs(charY % 4)

		janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
		janelaPrincipal.blit(seta,(90*charX,210*charY),(0,0,500,500))
		pygame.display.flip()
	pass




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





