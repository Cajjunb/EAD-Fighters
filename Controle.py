from header import *

class Controle(object):
	"""docstring for Controle"""
	def __init__(self, jogador=1):
		super(Controle, self).__init__()
		if jogador == 1:
			self.left = pygame.K_a
			self.right = pygame.K_d
			self.up = pygame.K_w
			self.down = pygame.K_s
			self.special = pygame.K_f
			pass
		elif jogador == 2:
			self.left = pygame.K_RIGHT
			self.right = pygame.K_LEFT
			self.up = pygame.K_UP
			self.down = pygame.K_DOWN
			self.special = pygame.K_KP_PLUS 
			pass