from abc import ABC, abstractmethod
import pygame
from random import randrange
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


class RegrasJogo(ABC):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """

    @abstractmethod
    def registrarAgenteJogador(self):
        """ Cria ou recupera id de um elemento de jogo agente.
        """
        return

    @abstractmethod
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return

    @abstractmethod
    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return

    @abstractmethod
    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        return

    @abstractmethod
    def atualizarEstado(self):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        return


class Snake(RegrasJogo):

    def __init__(self):
        self.macas_xy = [
            (230, 180), (160, 110), (190, 200),
            (80, 200), (90, 190), (130, 80),
            (260, 150), (50, 30), (170, 30),
            (260, 20)
        ]

        self.largura = 400
        self.altura = 400
        self.tamanho = 10
        self.placar = 40
        self.sair = True
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.CobraComp = 1
        self.pontos = 0
        self.CobraXY = []
        self.CobraInicio = []
        self.pos_x = randrange(0, self.largura - self.tamanho, 10)
        self.pos_y = randrange(0, self.altura - self.tamanho - self.placar, 10)
        self.CobraInicio.append(self.pos_x)
        self.CobraInicio.append(self.pos_y)
        self.CobraXY.append(self.CobraInicio)
        self.aux_id_jogador = 0
        pygame.init()
        self.fundo = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Snake")
        plota_texto("Aperte Seta para cima jogar com Humano", (255, 255, 255), 25, 10, 100, self.fundo)
        plota_texto("Seta para baixo jogar com Busca Amplitude", (255, 255, 255), 25, 10, 130, self.fundo)
        plota_texto("Seta esquerda jogar com Busca Profundidade", (255, 255, 255), 25, 10, 160, self.fundo)
        plota_texto("Seta para direita jogar com Busca Iterativa", (255, 255, 255), 25, 10, 190, self.fundo)
        pygame.display.update()
        teste = True
        while teste:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_DOWN:
                        self.aux_id_jogador = 1
                        teste = False
                    elif event.key == pygame.K_UP:
                        self.aux_id_jogador = 0
                        teste = False
                    elif event.key == pygame.K_LEFT:
                        self.aux_id_jogador = 2
                        teste = False
                    elif event.key == pygame.K_RIGHT:
                        self.aux_id_jogador = 3
                        teste = False
        plota_texto("Pontuação:" + str(0), (255, 255, 255), 20, 10, 400 - 30, self.fundo)
        plota_cobra(self.fundo, self.CobraXY, self.tamanho)
        plota_maca(self.fundo, self.macas_xy)
        pygame.display.update()

    def return_posi_maca_atual(self):
        return self.macas_xy[self.pontos]

    def registrarAgenteJogador(self):
        """ Cria ou recupera id de um elemento de jogo agente.
        """
        return 1

    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return self.sair

    def gerarCampoVisao(self, id_agente):
        return self.return_posi_maca_atual(), self.CobraInicio

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        lista_maca = self.macas_xy

        if acao == 'left' and self.velocidade_x != self.tamanho:
            self.velocidade_y = 0
            self.velocidade_x = -self.tamanho
        if acao == ('right') and self.velocidade_x != -self.tamanho:
            self.velocidade_y = 0
            self.velocidade_x = self.tamanho
        if acao == ('up') and self.velocidade_y != self.tamanho:
            self.velocidade_x = 0
            self.velocidade_y = -self.tamanho
        if acao == ('down') and self.velocidade_y != -self.tamanho:
            self.velocidade_x = 0
            self.velocidade_y = self.tamanho

        valida_vencedor(self)

        if self.sair:
            self.fundo.fill(preto)
            self.pos_x += self.velocidade_x
            self.pos_y += self.velocidade_y
            for i in range(len(lista_maca)):
                if self.pos_x == lista_maca[i][0] and self.pos_y == lista_maca[i][1]:
                    self.CobraComp += 1
                    self.pontos += 1
                    self.macas_xy[i] = (999, 999)

        self.sair = valida_se_tocou_na_borda(self, self.pos_x, self.tamanho, self.largura, self.pos_y, self.altura)

        self.CobraInicio = []
        self.CobraInicio.append(self.pos_x)
        self.CobraInicio.append(self.pos_y)
        self.CobraXY.append(self.CobraInicio)

        if len(self.CobraXY) > self.CobraComp:
            del self.CobraXY[0]

        # Encostou a cabeça na cobra
        if any(Bloco == self.CobraInicio for Bloco in self.CobraXY[:-1]):
            self.sair = False

    def atualizarEstado(self):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        # Draw de Pontuação
        pygame.draw.rect(self.fundo, preto, [0, self.altura - self.placar, self.largura, self.placar])
        plota_texto("Pontuação: " + str(self.pontos), branco, 30, 10, self.altura - 30, self.fundo)
        plota_cobra(self.fundo, self.CobraXY, self.tamanho)
        plota_maca(self.fundo, self.macas_xy)
        return pygame.display.update()


def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância Jogavel arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return Snake()


def plota_texto(msg, cor, tam, x, y, fundo):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def plota_maca(fundo, lista_maca):
    for _ in range(len(lista_maca)):
        pygame.draw.rect(fundo, vermelho, [lista_maca[_][0], lista_maca[_][1], 10, 10])


def plota_cobra(_fundo, Cobra, tamanho):
    for XY in Cobra:
        pygame.draw.rect(_fundo, verde, [XY[0], XY[1], tamanho, tamanho])


def valida_se_tocou_na_borda(self, pos_x, tamanho, largura, pos_y, altura):
    # Verifica se tocou na borda
    if pos_x + tamanho > largura or pos_x < 0 or pos_y + tamanho > altura or pos_y < 0:
        plota_texto("GAME OVER!", vermelho, 80, 15, 170, self.fundo)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        return False
    else:
        return True


def valida_vencedor(self):
    #  Valida se é vencedor
    if self.pontos >= len(self.macas_xy):
        self.sair = False
        self.macas_xy = (999, 999)
        plota_vencedor(self.fundo)


def plota_vencedor(fundo):
    fundo.fill(preto)
    plota_texto("VENCEDOR!", vermelho, 80, 35, 170, fundo)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
