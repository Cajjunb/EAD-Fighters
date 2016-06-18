from header import *
from somJogo import *
from pygame.locals import *
from sys import exit

class ticTacToe(object):
	"""docstring for ticTacToe"""
	def __init__(self):
		super(ticTacToe, self).__init__()
		
		pygame.init()

		self.som = somJogo()

		grid_filename = 'wallpaper/grid.png'
		self.grid = pygame.image.load(grid_filename).convert_alpha()

		X_filename = 'sprites/x.png'
		self.X = pygame.image.load(X_filename).convert_alpha()

		O_filename = 'sprites/o.png'
		self.O = pygame.image.load(O_filename).convert_alpha()

		self.contador = 1
		 
		self.posicao_horizontal = 0
		self.posicao_vertical = 0

		self.matriz3x3 = [[0,0,0],
		             [0,0,0],
		             [0,0,0]]

		self.clock = pygame.time.Clock()
		pass

	def verificaMatriz(self):
		#PLAYER 1
		#diagonal 1 X
		if self.matriz3x3[0][0]==1 and self.matriz3x3[1][1]==1 and self.matriz3x3[2][2]==1:
			return True
			pass
		#diagonal 2 X
		elif self.matriz3x3[0][2]==1 and self.matriz3x3[1][1]==1 and self.matriz3x3[2][0]==1:
			#outra coisa
			pass
		#1a linha X
		elif self.matriz3x3[0][0]==1 and self.matriz3x3[0][1]==1 and self.matriz3x3[0][2]==1:
			pass
		#2a linha X
		elif self.matriz3x3[1][0]==1 and self.matriz3x3[1][1]==1 and self.matriz3x3[1][2]==1:
			pass
		#3a linha X
		elif self.matriz3x3[2][0]==1 and self.matriz3x3[2][1]==1 and self.matriz3x3[2][2]==1:
			pass
		#1a coluna X
		elif self.matriz3x3[0][0]==1 and self.matriz3x3[1][0]==1 and self.matriz3x3[2][0]==1:
			pass
		#2a coluna X
		elif self.matriz3x3[0][1]==1 and self.matriz3x3[1][1]==1 and self.matriz3x3[2][1]==1:
			pass
		#3a coluna X
		elif self.matriz3x3[0][2]==1 and self.matriz3x3[1][2]==1 and self.matriz3x3[2][2]==1:
			pass
		#PLAYER 2
		#diagonal 1 O
		elif self.matriz3x3[0][0]==2 and self.matriz3x3[1][1]==2 and self.matriz3x3[2][2]==2:
			pass

		#diagonal 2 O
		elif self.matriz3x3[0][2]==2 and self.matriz3x3[1][1]==2 and self.matriz3x3[2][0]==2:
			pass

		#1a linha O
		elif self.matriz3x3[0][0]==2 and self.matriz3x3[0][1]==2 and self.matriz3x3[0][2]==2:
			pass

		#2a linha O
		elif self.matriz3x3[1][0]==2 and self.matriz3x3[1][1]==2 and self.matriz3x3[1][2]==2:
			pass

		#3a linha O
		elif self.matriz3x3[2][0]==2 and self.matriz3x3[2][1]==2 and self.matriz3x3[2][2]==2:
			pass

		#1a coluna O
		elif self.matriz3x3[0][0]==2 and self.matriz3x3[1][0]==2 and self.matriz3x3[2][0]==2:
			pass

		#2a coluna O
		elif self.matriz3x3[0][1]==2 and self.matriz3x3[1][1]==2 and self.matriz3x3[2][1]==2:
			pass

		#3a coluna O
		elif self.matriz3x3[0][2]==2 and self.matriz3x3[1][2]==2 and self.matriz3x3[2][2]==2:
			pass
		pass

	def jogarJogoVelha(self,screen):

		while self.contador<10:
		    screen.blit(self.grid, (0, 0))
		    #print self.matriz3x3
		    for evento in pygame.event.get():
		        if evento.type == QUIT:
		            exit()
		        if evento.type == pygame.KEYDOWN:
		            if evento.key == pygame.K_RIGHT:
		        		self.posicao_horizontal += 1

		            if evento.key == pygame.K_UP:
		            	self.posicao_vertical -= 1

		            if evento.key == pygame.K_DOWN:
		            	self.posicao_vertical += 1

		            if evento.key == pygame.K_LEFT:
		        		self.posicao_horizontal -= 1

		            if evento.key == pygame.K_RETURN:
		                if self.matriz3x3[self.posicao_vertical][self.posicao_horizontal]<1:
		                	self.matriz3x3[self.posicao_vertical][self.posicao_horizontal] = (self.contador%2)+1
		                	self.contador += 1
		                if self.verificaMatriz() == True:
		                	#tela do ganhador
		                	exit()
		                else:
		                	self.som.tocarAccept()               
		    
		    
		    self.posicao_horizontal = abs(self.posicao_horizontal %3)  #razao da imagem# 
		    self.posicao_vertical = abs(self.posicao_vertical %3)

		    for i in range (0,3):
		    	for j in range (0,3):
		    		if self.matriz3x3[j][i] == 1:
		    			screen.blit(self.X, ((i*200)+30, j*140))
		    		elif self.matriz3x3[j][i] == 2:
		    			screen.blit(self.O, ((i*200)+30, j*140))

		    if self.contador%2 == 0:
		    	screen.blit(self.X, ((self.posicao_horizontal*200)+30, self.posicao_vertical*140))
		    else:
		    	screen.blit(self.O, ((self.posicao_horizontal*200)+30, self.posicao_vertical*140))
		    pygame.display.update()
		    time_passed = self.clock.tick(30)



    
    


