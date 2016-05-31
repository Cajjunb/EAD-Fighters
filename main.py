from header import *
from MenuJogo import *
from Artigotona import *



# Initialize all the Pygame Modules
pygame.init()

#Criando a janela principal
(width, height) = (500,350)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()

#Instancia o objeto que faz o menu
menuObjeto = MenuJogo() 
#Menu Principal e selecao
menuObjeto.selecionaMenuPrincipal(janelaPrincipal)
#Seleciona qual personagem tal personagem vai jogar
menuObjeto.selecionaChar(janelaPrincipal)

#Instancia o objeto que faz o menu
artigotonaObjeto = Artigotona() 
#Roda o JOGO
artigotonaObjeto.jogaArtigotona(janelaPrincipal)
artigotonaObjeto.anunciaVencedor(janelaPrincipal)

#Background set
background_colour = (0,0,0)

#configuracoes
pygame.display.set_caption('Lutadores EAD')





