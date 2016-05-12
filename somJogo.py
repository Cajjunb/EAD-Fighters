from header import *

class somJogo(object):
	"""docstring for somJogo"""
	def __init__(self):
		super(somJogo, self).__init__()
		self.beep = pygame.mixer.Sound('sounds\meep.ogg')
		self.accept = pygame.mixer.Sound('sounds\ccept.ogg')

	def tocarBeep(self):
		self.beep.play()
		pass

	def tocarAccept(self):
		self.accept.play()
		pass