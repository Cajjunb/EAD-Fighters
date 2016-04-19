from header import *

class Jogador(object):

	
	"""docstring for Jogador"""
	def __init__(self):
		super(Jogador, self).__init__()
		#ARGUMENTOS
		self.bibliotecaSprites = pygame.image.load('sprites\RyuSF2Turbo.png')
		aux = self.bibliotecaSprites
		aux.set_colorkey((183,207,135))
		self.bibliotecaSprites = aux.convert_alpha()
		#Posicoes Do personagem
		self.posicaox = 20
		self.posicaoy = 20
		#LIMITES ANIMACAO
		self.limiteIdle = 4
		self.limiteMovimentar = 4
		self.limiteSocoFraco = 3
		self.limiteSocoMedio = 3
		#Qual animacao esta sendo feita
		self.animacaoAtual = "idle"
		self.estadoAtual = 0 
		#Qual Offset para a animacao
		self.socoMedioYOffset = 458
		self.socoMedioXOffset = 168


		#CODIGO DO REPOSITORIO ONLINE

	def verificaTeclado(self,janelaPrincipal ):
		if self.estadoAtual != 0:
			#Acessa todos os eventos
			eventos = pygame.event.get()
			#Verifica todos os eventos 
			for event in eventos:
				#Testa qual tecla foi apertado 
				if event.type == pygame.KEYDOWN:
					#Soco fraco
					if event.key == pygame.K_i:
						self.movimentar(janelaPrincipal, 2 )
						pass
					#Soco forte
					if event.key == pygame.K_o:
						self.socoFraco(janelaPrincipal )
						pass	
					#Soco Medio
					if event.key == pygame.K_p:
						self.socoMedio(janelaPrincipal )
						pass	
				else:
					self.idleAnimation(janelaPrincipal )
					pass
			pass
		if self.animacaoAtual == "movimentar":	
			self.movimentar(janelaPrincipal,2 )
			pass
		elif self.animacaoAtual == "idle":
			self.idleAnimation(janelaPrincipal )
			pass
		elif self.animacaoAtual == "socoFraco":
			self.socoFraco(janelaPrincipal )
			pass
		elif self.animacaoAtual == "socoMedio":
			self.socoMedio(janelaPrincipal )
			pass
		pass

	
	#Idle animacao
	def idleAnimation(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "idle":
			self.animacaoAtual = "idle"
			pass
		jogador1 = self.bibliotecaSprites
		#Inclui imagem na memoria VGA
		#Verifica se ja passou o limite
		if self.estadoAtual >= self.limiteIdle:
			self.estadoAtual = 0
			self.animacaoAtual = "idle"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),5,48,85))
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass

	def movimentar(self,janelaPrincipal,direcao):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "movimentar":
			self.animacaoAtual = "movimentar"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limiteMovimentar:
			self.estadoAtual = 0
			self.animacaoAtual = "movimentar"
		pass
		#Inclui imagem na memoria VGA
		if self.estadoAtual == 1:
#			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*50),135,65,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),90,48,85))
		elif self.estadoAtual == 2:
			#janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(50+65,135,50,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),90,48,85))
			pass
		else:
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),90,48,85))
			pass
		#Vai para proximo sprite
		self.estadoAtual += 1
		self.posicaox += direcao
		pass

	def socoFraco(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "socoFraco":
			self.animacaoAtual = "socoFraco"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limiteSocoFraco:
			self.estadoAtual = 0
			self.animacaoAtual = "socoFraco"
		pass
		#Inclui imagem na memoria VGA
		if self.estadoAtual == 0:
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),self.socoMedioYOffset,48,85))
			pass
		elif self.estadoAtual == 1:
#			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*50),135,65,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+(self.estadoAtual*48),self.socoMedioYOffset,60,85))
		elif self.estadoAtual == 2:
			#janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(50+65,135,50,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(4+14+(self.estadoAtual*48),self.socoMedioYOffset,48,85))
			pass
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass


	def socoMedio(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "socoMedio":
			self.animacaoAtual = "socoMedio"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limiteSocoMedio:
			self.estadoAtual = 0
			self.animacaoAtual = "socoMedio"
		pass
		#Inclui imagem na memoria VGA
		if self.estadoAtual == 0:
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(self.socoMedioXOffset+2+(self.estadoAtual*48),self.socoMedioYOffset,48,85))
			pass
		elif self.estadoAtual == 1:
#			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*50),135,65,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(self.socoMedioXOffset+2+(self.estadoAtual*48),self.socoMedioYOffset,70,85))
		elif self.estadoAtual == 2:
			#janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(50+65,135,50,80))
			janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(self.socoMedioXOffset+22+(self.estadoAtual*48),self.socoMedioYOffset,48,85))
			pass
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass