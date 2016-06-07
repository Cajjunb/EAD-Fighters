from header import *

class somJogo(object):
	"""docstring for somJogo"""
	def __init__(self):
		super(somJogo, self).__init__()
		self.beep = pygame.mixer.Sound('sounds\meep.ogg')
		self.accept = pygame.mixer.Sound('sounds\ccept.ogg')
		self.paperWrite1 = pygame.mixer.Sound('sounds\paperWriting1.ogg')
		self.paperWrite2 = pygame.mixer.Sound('sounds\paperWriting2.ogg')
		self.paperWrite3 = pygame.mixer.Sound('sounds\paperWriting3.ogg')

	def tocarBeep(self):
		self.beep.play()
		pass

	def tocarAccept(self):
		self.accept.play()
		pass

	def tocarPaperWriting(self):
		aleatorio = random.randint(0, 10) %3
		if aleatorio == 0:
			self.paperWrite1.play()
			pass
		elif aleatorio == 1:
			self.paperWrite2.play()
			pass
		else:
			self.paperWrite3.play()
			pass
		pass