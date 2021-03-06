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
		self.limitemovimentarDireita = 4
		self.limitemovimentarEsquerda = 4
		self.limiteSocoFraco = 3
		self.limitechuteFraco = 4
		self.limiteAgachar = 1
		self.limiteespecial1 = 4
		#Qual animacao esta sendo feita
		self.animacaoAtual = "idle"
		self.estadoAtual = 0 
		self.estadoAtualIdle = 0
		#Argumentos
		self.coeficienteMovimentacao  = 5

		#Qual Offset para a animacao
		self.chuteFracoYOffset = 458
		self.chuteFracoXOffset = 168


		#CODIGO DO REPOSITORIO ONLINE

	def verificaTeclado(self,janelaPrincipal ):
		if self.estadoAtual != 0 or self.estadoAtualIdle != 0:
			#Acessa todos os eventos
			eventos = pygame.event.get()
			#Verifica todos os eventos 
			for event in eventos:
				#Testa qual tecla foi apertado 
				if event.type == pygame.KEYDOWN:
					#Movimento esquerda
					if event.key == pygame.K_a:
						self.movimentarEsquerda(janelaPrincipal, - self.coeficienteMovimentacao )
						pass
					#Movimento Direita
					elif event.key == pygame.K_d:
						self.movimentarDireita(janelaPrincipal, self.coeficienteMovimentacao )
						pass
					#Agachar
					elif event.key == pygame.K_s:
						self.agachar(janelaPrincipal)
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
		if self.animacaoAtual == "movimentarEsquerda":	
			self.movimentarEsquerda(janelaPrincipal, - self.coeficienteMovimentacao)
			pass
		elif self.animacaoAtual == "movimentarDireita":
			self.movimentarDireita(janelaPrincipal, self.coeficienteMovimentacao )
			pass
		elif self.animacaoAtual == "agachar":
			self.agachar(janelaPrincipal)
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
		elif self.animacaoAtual == "especial1":
			self.especial1(janelaPrincipal )
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
		if self.estadoAtualIdle  >= self.limiteIdle:
			self.estadoAtualIdle = 0
			self.animacaoAtual = "idle"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtualIdle*70),80,70,80))
		#Vai para proximo sprite
		self.estadoAtualIdle += 1
		#RESETA As animacoes dos outros inputs
		self.estadoAtual = 0	

		pass

	def movimentarDireita(self,janelaPrincipal,direcao):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "movimentarDireita":
			self.animacaoAtual = "movimentarDireita"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limitemovimentarDireita:
			self.estadoAtual = 0
			self.animacaoAtual = "movimentarDireita"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),240,70,80))
		#Vai para proximo sprite
		self.estadoAtual += 1
		self.posicaox += direcao
		pass

	def movimentarEsquerda(self,janelaPrincipal,direcao):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "movimentarEsquerda":
			self.animacaoAtual = "movimentarEsquerda"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limitemovimentarEsquerda:
			self.estadoAtual = 0
			self.animacaoAtual = "movimentarEsquerda"
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

	def agachar(self,janelaPrincipal ):
		#verifica se esta registrado que animacao sendo feita eh a atual
		if self.animacaoAtual != "agachar":
			self.animacaoAtual = "agachar"
			pass
		jogador1 = self.bibliotecaSprites
		if self.estadoAtual >= self.limiteAgachar:
			self.estadoAtual = 0
			self.animacaoAtual = "agachar"
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(self.posicaox,self.posicaoy),(0+(self.estadoAtual*70),720,70,80))
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