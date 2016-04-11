from header import *

class Jogador(object):

	
	"""docstring for Jogador"""
	def __init__(self):
		super(Jogador, self).__init__()
		#ARGUMENTOS
		self.bibliotecaSprites = pygame.image.load('sprites\RyuSprites.gif')
		#LIMITES ANIMACAO
		self.limiteIdle = 4
		self.estadoAtual = 0 



	
	#Idle animacao
	def idleAnimation(self,janelaPrincipal,posicaox,posicaoy):
		jogador1 = pygame.image.load('sprites\RyuSprites.gif')
		#Inclui imagem na memoria VGA
		#Verifica se ja passou o limite
		if self.estadoAtual == self.limiteIdle:
			self.estadoAtual = 0
		pass
		#Inclui imagem na memoria VGA
		janelaPrincipal.blit(self.bibliotecaSprites,(posicaox,posicaoy),(0+(self.estadoAtual*50),18,50,80))
		#Vai para proximo sprite
		self.estadoAtual += 1
		pass