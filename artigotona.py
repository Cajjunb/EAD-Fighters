from header import *
from Jogador import *

class Artigotona(object):
	"""docstring for artigotona"""
	def __init__(self,char1,char2):
		#clock do jogo
		self.clock = pygame.time.Clock() # create a clock object for timing
		#Jogadores
		self.jogador1 = Jogador(160,190,char1,jogador=1)
		#Jogadores
		self.jogador2 = Jogador(340,190,char2,jogador=2)
		#variavel de estado do jogo
		self.jogoRunning = False
		#Background set
		self.background = pygame.image.load('.\wallpaper\papelartigotona.png')
		#Clock
		self.clock =  pygame.time.Clock() 



		super(Artigotona, self).__init__()


	def jogaArtigotona(self,janelaPrincipal):

		pygame.time.wait(5000)

		#variavel de estado do jogo
		self.jogoRunning = True		
		#loop principal final
		while self.jogoRunning:
			# Se acabou o jogo
			if self.jogador1.chegouMaximoBarraProgresso() or self.jogador2.chegouMaximoBarraProgresso():
				if self.jogador1.chegouMaximoBarraProgresso():
					self.jogoRunning = False
					self.vencedor = "jogador1"
					pass
				else:
					self.jogoRunning = False
					self.vencedor = "jogador2"
					pass
				pass
			#ATUALIZA A JANELA
			janelaPrincipal.blit(self.background,(0,0),(0,0,500,500))
			#Jogador Idle
			self.jogador1.verificaTeclado(janelaPrincipal)
			#atualiza os papeis
			self.jogador1.atualizarBarraProgresso(janelaPrincipal,0,290)
			#Jogador Idle
			self.jogador2.verificaTeclado(janelaPrincipal)
			#atualiza os papeis
			self.jogador2.atualizarBarraProgresso(janelaPrincipal,400,290)


			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					jogoRunning = False
				pass
			self.clock.tick_busy_loop(8)
			pygame.display.update()
			pass	
		pass
		

	def anunciaVencedor(self,janelaPrincipal):
		#Carrega imagens anunciando o vencedor
		if self.vencedor == 'jogador1':
			mensagem = pygame.image.load('.\wallpaper\Vencedor1.png')
			vencedor = 1
			pass
		elif self.vencedor == 'jogador2':
			mensagem = pygame.image.load('.\wallpaper\Vencedor2.png')
			vencedor = 2
			pass
		else:
			#caso seja
			mensagem = pygame.image.load('.\wallpaper\Vencedor1.png')
			pass
		janelaPrincipal.blit(mensagem,(0,0),(0,0,500,500))
		pygame.display.update()
		pygame.time.wait(5000)
		return vencedor
		pass