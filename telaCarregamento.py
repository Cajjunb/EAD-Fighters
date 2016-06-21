from header import *

class telaCarregamento(object):
	"""docstring for telaCarregamento"""
	def __init__(self):
		super(telaCarregamento, self).__init__()
	


	def setupTelaCarregamento(self,telaNumero):
		if telaNumero == 1:
			self.telaImagem = pygame.image.load('loadingScreens\\telaRosaAmaralina.png')
		elif telaNumero == 2:
			self.telaImagem = pygame.image.load('loadingScreens\\telaRosaLucioTeles.png')
		pass

	def mostraTelaCarregamento(self,janelaPrincipal):
		janelaPrincipal.blit(self.telaImagem,(0,0),(0,0,500,500))
		pygame.display.update()
		pygame.time.wait(5000)
		pass



	def mostraIntro(self,janelaPrincipal):
		intro = pygame.image.load('loadingScreens\intro.png')
		janelaPrincipal.blit(intro,(0,0),(0,0,500,500))
		pygame.display.update()
		pygame.time.wait(5000)
		pass


	def mostraIntro2(self,janelaPrincipal):
		intro = pygame.image.load('loadingScreens\intro2.png')
		janelaPrincipal.blit(intro,(0,0),(0,0,500,500))
		pygame.display.update()
		pygame.time.wait(5000)
		pass
