from header import *
from Jogador import *

class Artigotona(object):
	"""docstring for artigotona"""
	def __init__(self):
		#clock do jogo
		self.clock = pygame.time.Clock() # create a clock object for timing
		#Jogadores
		self.jogador1 = Jogador(100,0,jogador=1)
		#Jogadores
		self.jogador2 = Jogador(300,0,jogador=2)
		#variavel de estado do jogo
		self.jogoRunning = False
		#Background set
		self.background = pygame.image.load('.\wallpaper\papelartigotona.png')
		#Clock
		self.clock =  pygame.time.Clock() 



		super(Artigotona, self).__init__()


	def jogaArtigotona(self,janelaPrincipal):

		#variavel de estado do jogo
		self.jogoRunning = True		
		#loop principal final
		while self.jogoRunning:
			#ATUALIZA A JANELA
			janelaPrincipal.blit(self.background,(0,0),(0,0,500,500))
			#Jogador Idle
			self.jogador1.verificaTeclado(janelaPrincipal)
			#atualiza os papeis
			self.jogador1.atalizarBarraProgresso(janelaPrincipal,0,100)
			#Jogador Idle
			self.jogador2.verificaTeclado(janelaPrincipal)
			#atualiza os papeis
			self.jogador2.atalizarBarraProgresso(janelaPrincipal,400,100)


			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					jogoRunning = False
				pass
			self.clock.tick_busy_loop(8)
			pygame.display.update()
			pass	
		pass
		