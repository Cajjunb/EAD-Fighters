from header import *

class menuJogo(object):
	"""docstring for menuJogo"""
	def __init__(self):
		super(menuJogo, self).__init__()
	

	def selecionaMenuPrincipal(self, janelaPrincipal):
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
		pass

	def selecionaChar(self,janelaPrincipal):
		#variavel verifica se o menu de selecao de personagem foi aberto
		selecionarPersonagem 	= False
		#Variavel que indica qual personagem ele funciona
		personagemEscolhido 	= 1
		charY = 0
		charX = 0
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

				charX = abs(charX % 3)
				charY = abs(charY % 2)

				janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
				janelaPrincipal.blit(seta,(90+(120*charX),210+(60*charY)),(0,0,500,500))
				pygame.display.flip()
			pass
			#Retorno qual personagem foi escolhido
		return (charX,charY)
		pass