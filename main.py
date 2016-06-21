from header import *
from MenuJogo import *
from Artigotona import *
from ticTacToe import *
from telaCarregamento import *

# Initialize all the Pygame Modules
pygame.init()

#Criando a janela principal
(width, height) = (500,350)
janelaPrincipal = pygame.display.set_mode((width,height)) 
pygame.display.flip()

#configuracoes
pygame.display.set_caption('EADana!')

#Instancia o objeto que faz o menu
menuObjeto = MenuJogo() 
#Menu Principal e selecao
menuObjeto.selecionaMenuPrincipal(janelaPrincipal)
#Seleciona qual personagem tal personagem vai jogar
char1 = menuObjeto.selecionaChar(janelaPrincipal,jogador=1)
char2 = menuObjeto.selecionaChar(janelaPrincipal,jogador=2)

#tela Carregamento
telaObjeto = telaCarregamento()
telaObjeto.setupTelaCarregamento(1)
telaObjeto.mostraTelaCarregamento(janelaPrincipal)


telaObjeto.mostraIntro(janelaPrincipal)
telaObjeto.mostraIntro2(janelaPrincipal)


#Instancia o objeto que faz o menu
artigotonaObjeto = Artigotona(char1,char2) 
#Roda o JOGO
artigotonaObjeto.jogaArtigotona(janelaPrincipal)
artigotonaObjeto.anunciaVencedor(janelaPrincipal)

telaObjeto.setupTelaCarregamento(2)
telaObjeto.mostraTelaCarregamento(janelaPrincipal)


ticTacToeObjeto = ticTacToe()
ticTacToeObjeto.jogarJogoVelha(janelaPrincipal)

#Background set
background_colour = (0,0,0)






