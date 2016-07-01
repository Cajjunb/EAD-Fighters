from header import *
from somJogo import *


class MenuJogo(object):
	"""docstring for menuJogo"""
	def __init__(self):
	 	pygame.mixer.init()
	 	self.som = somJogo() 
		super(MenuJogo, self).__init__()
	

	def selecionaMenuPrincipal(self, janelaPrincipal):
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
					#Tocar beep
					self.som.tocarBeep()
					pass
				#Caso pressionar o D
				elif evento.key == pygame.K_RIGHT:
					# Muda a imagem da seta Direita
					menu = pygame.image.load('wallpaper\itltescreenCreditos.png')
					#Tocar beep
					self.som.tocarBeep()
					escolhaMenu = 'creditos'
					pass
				#Caso pressionar o enter
				elif evento.key == pygame.K_RETURN:
					#Tocar beep
					self.som.tocarAccept()
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

	def selecionaChar(self,janelaPrincipal,jogador=1):
		#variavel verifica se o menu de selecao de personagem foi aberto
		selecionarPersonagem 	= False
		#Variavel que indica qual personagem ele funciona
		personagemEscolhido 	= 1
		charY = 0
		charX = 0
		#Selecao personagens imagem
		if jogador == 1:
			menu 	= pygame.image.load('wallpaper\charselect1.png')
			pass
		else:
			menu 	= pygame.image.load('wallpaper\charselect2.png')
			pass
		seta 	= pygame.image.load('sprites\BackgroundMessagem2.png')
		painel 	= pygame.image.load('sprites\PainelGrande.png')

		messagebox = pygame.image.load( 'messageBox\\'+ str(charX + (3*charY)) + '.png')

		janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
		janelaPrincipal.blit(painel,(70,10),(0,0,500,500))
		janelaPrincipal.blit(messagebox,(70,10),(0,0,500,500))	
		janelaPrincipal.blit(seta,(90,210),(0,0,500,500))

		pygame.display.flip()

		#Verifica todos os eventos 
		while selecionarPersonagem == False:
			evento = pygame.event.wait()	
			#Flags de som
			valido_key = False
			if evento.type == pygame.KEYDOWN:
				#Verificando o teclado para selecionar personagens
				if evento.key == pygame.K_RIGHT:
					charX += 1
					valido_key = True
					pass
				elif evento.key == pygame.K_LEFT:
					charX -= 1
					valido_key = True
					pass
				elif evento.key == pygame.K_DOWN:
					charY -= 0
					valido_key = True
					pass
				elif evento.key == pygame.K_UP:
					charY += 0
					valido_key = True
					pass
				elif evento.key == pygame.K_RETURN:
					#Sai do personagem e faz a escolha
					selecionarPersonagem = True
					pass
				pass
				#Se eh um botao valido 
				if valido_key == True:
					#Toca um som
					self.som.tocarBeep()
					pass
				elif selecionarPersonagem == True:
					self.som.tocarAccept()
					pass
				charX = abs(charX % 3)
				charY = abs(charY % 1)

				messagebox = pygame.image.load( 'messageBox\\'+ str(charX + (3*charY)) + '.png')

				janelaPrincipal.blit(menu,(0,0),(0,0,500,500))
				janelaPrincipal.blit(painel,(70,10),(0,0,500,500))	
				janelaPrincipal.blit(messagebox,(70,10),(0,0,500,500))	
				janelaPrincipal.blit(seta,(90+(120*charX),210+(60*charY)),(0,0,500,500))
				pygame.display.flip()
			pass
			#Retorno qual personagem foi escolhido
		return charX + charY*3
		pass