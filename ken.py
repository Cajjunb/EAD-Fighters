from header import *

class Jogador(object):

	
	"""docstring for Jogador"""
	def __init__(self):
		super(Jogador, self).__init__()
		#ARGUMENTOS
		self.bibliotecaSprites = pygame.image.load('sprites\ken3.png')
		aux = self.bibliotecaSprites
		self.bibliotecaSprites = aux.convert_alpha()
		#Posicoes Do personagem
		self.posicaox = 20
		self.posicaoy = 20
		#LIMITES ANIMACAO
		self.limiteIdle = 3
		self.limiteMovimentar = 4
		self.limiteSocoFraco = 3
		self.limitechuteFraco = 4
		self.limiteespecial1 = 4
		#Qual animacao esta sendo feita
		self.animacaoAtual = "idle"
		self.estadoAtual = 0 
		#Qual Offset para a animacao
		self.chuteFracoYOffset = 458
		self.chuteFracoXOffset = 168


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
						self.movimentar(janelaPrincipal, 10 )
						pass
					#Soco forte
					elif event.key == pygame.K_o:
						self.socoFraco(janelaPrincipal )
						pass	
					#Soco Medio
					elif event.key == pygame.K_p:
						self.chuteFraco(janelaPrincipal )
						pass
					#especial1
					elif event.key == pygame.K_l:
						self.especial1(janelaPrincipal )
						pass		
				else:
					self.idleAnimation(janelaPrincipal)
					pass
			pass
		if self.animacaoAtual == "movimentar":	
			self.movimentar(janelaPrincipal,10 )
			pass
		elif self.animacaoAtual == "idle":
			self.idleAnimation(janelaPrincipal )
			pass
		elif self.animacaoAtual == "socoFraco":
			self.socoFraco(janelaPrincipal )
			pass
		elif self.animacaoAtual == "chuteFraco":
			self.chuteFraco(janelaPrincipal )
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
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),80,70,80))
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
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),240,70,80))
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
		if self.estadoAtual >= self.limiteSocoFraco and self.estadoAtual != "socoFraco":
			self.estadoAtual = 0
			self.animacaoAtual = "socoFraco"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),160,70,80))
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass


	def chuteFraco(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "chuteFraco":
			self.animacaoAtual = "chuteFraco"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limitechuteFraco:
			self.estadoAtual = 0
			self.animacaoAtual = "chuteFraco"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),480,70,80))
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass


	def especial1(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "especial1":
			self.animacaoAtual = "especial1"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limiteespecial1:
			self.estadoAtual = 0
			self.animacaoAtual = "especial1"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),0,70,80))
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass