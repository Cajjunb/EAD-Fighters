from header import *

class telaCarregamento(object):
	"""docstring for telaCarregamento"""
	def __init__(self):
		super(telaCarregamento, self).__init__()
	


	def setupTelaCarregamento(self,telaNumero):
		if telaNumero == 1:
			self.telaImagem = pygame.image.load('loadingScreens\\randomAzul1.png')
		elif telaNumero == 2:
			self.telaImagem = pygame.image.load('loadingScreens\\randomAzul2.png')
		pass

	def setupTelaCarregamentoRandom(self):
		num = random.randint(1,12)
		string = str(num)
		self.telaImagem = pygame.image.load('loadingScreens\\randomAzul'+string+'.png')



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


	def finalAmaralina(self,janelaPrincipal):
		intro = pygame.image.load('final\\finalAmaralina.png')
		janelaPrincipal.blit(intro,(0,0),(0,0,500,500))
		pygame.display.update()
		pygame.time.wait(5000)
		pass

