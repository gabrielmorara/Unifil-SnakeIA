# Código com definição de agentes abstratos a serem utilizados em nossas aulas.

from abc import ABC, abstractmethod
import pygame
from random import randrange
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN


class Agente(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    def __init__(self):
        self.left = 'left'
        self.rigth = 'right'
        self.up = 'up'
        self.down = 'down'

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return

    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return


# Implemente seu jogador humano nessa classe, sobrescrevendo os métodos
# abstratos de Agente. Em construir_agente, retorne uma instância dessa classe.
class AgenteHumano(Agente):

    def adquirirPercepcao(self, percepcao_mundo):
        # Utilize percepcao de mundo para atualizar tela (terminal ou blit),
        # tocar sons, dispositivos hápticos, etc, todo e qualquer dispositivo
        # de saída para interface humana.
        pass

    def escolherProximaAcao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT and event.type is not None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return self.left
                    elif event.key == pygame.K_RIGHT:
                        return self.rigth
                    elif event.key == pygame.K_UP:
                        return self.up
                    if event.key == pygame.K_DOWN:
                        return self.down


class AgenteAmplitude(Agente):

    def __init__(self):
        super().__init__()
        self.cobrainicio = []
        self.maca = []
        self.aux = 1
        self.seq = []
        ## 0 = left
        ## 1 = rigth
        ## 2 = up
        ## 3 = donw

    def adquirirPercepcao(self, percepcao_mundo):
        self.maca = percepcao_mundo[0]
        self.cobrainicio = percepcao_mundo[1]

    def escolherProximaAcao(self):
        self.busca()
        return self.seq[0]


    def formularEstadoAtual(self):
        ''' Instancia objeto com base em AbstractEstado representando o estado
        atual e as corretas funções de navegação pelo estado, bem como o teste
        de objetivo e a função de custo.

        Ao final, self.estado deve estar preenchido.
        '''
        pass

    def busca(self):
        if self.aux == 0:
            self.aux = 3
            self.seq.append(self.rigth)
        elif self.aux == 1:
            if self.cobrainicio[0] > 370:
                self.aux = 2
                self.seq.append(self.up)
            self.aux = 3
            self.seq.append(self.down)
        elif self.aux == 2:
            self.aux = 0
            self.seq.append(self.left)
        elif self.aux == 3:
            if self.cobrainicio[1] > 370:
                self.aux = 0
                self.seq.append(self.up)
            self.aux = 1
            self.seq.append(self.rigth)



class AgenteProfundidade(Agente):

    def __init__(self):
        super().__init__()
        self.cobrainicio = []
        self.maca = []
        self.aux = 1
        self.seq = []
        ## 0 = left
        ## 1 = rigth
        ## 2 = up
        ## 3 = donw

    def adquirirPercepcao(self, percepcao_mundo):
        self.maca = percepcao_mundo[0]
        self.cobrainicio = percepcao_mundo[1]

    def escolherProximaAcao(self):
        self.busca()
        return self.seq[0]

    def formularEstadoAtual(self):
        ''' Instancia objeto com base em AbstractEstado representando o estado
        atual e as corretas funções de navegação pelo estado, bem como o teste
        de objetivo e a função de custo.

        Ao final, self.estado deve estar preenchido.
        '''
        pass

    def busca(self):
        if self.aux == 0:
            self.aux = 3
            self.seq.append(self.rigth)
        elif self.aux == 1:
            if self.cobrainicio[0] > 370:
                self.aux = 2
                self.seq.append(self.up)
            self.aux = 3
            self.seq.append(self.down)
        elif self.aux == 2:
            self.aux = 0
            self.seq.append(self.left)
        elif self.aux == 3:
            if self.cobrainicio[1] > 370:
                self.aux = 0
                self.seq.append(self.up)
            self.aux = 1
            self.seq.append(self.rigth)


class AgenteAprofundamentoIterativo(Agente):

    def __init__(self):
        super().__init__()
        self.cobrainicio = []
        self.maca = []
        self.aux = 1
        self.seq = []
        ## 0 = left
        ## 1 = rigth
        ## 2 = up
        ## 3 = donw

    def adquirirPercepcao(self, percepcao_mundo):
        self.maca = percepcao_mundo[0]
        self.cobrainicio = percepcao_mundo[1]

    def escolherProximaAcao(self):
        self.busca()
        return self.seq[0]

    def formularEstadoAtual(self):
        ''' Instancia objeto com base em AbstractEstado representando o estado
        atual e as corretas funções de navegação pelo estado, bem como o teste
        de objetivo e a função de custo.

        Ao final, self.estado deve estar preenchido.
        '''
        pass

    def busca(self):
        if self.aux == 0:
            self.aux = 3
            self.seq.append(self.rigth)
        elif self.aux == 1:
            if self.cobrainicio[0] > 370:
                self.aux = 2
                self.seq.append(self.up)
            self.aux = 3
            self.seq.append(self.down)
        elif self.aux == 2:
            self.aux = 0
            self.seq.append(self.left)
        elif self.aux == 3:
            if self.cobrainicio[1] > 370:
                self.aux = 0
                self.seq.append(self.up)
            self.aux = 1
            self.seq.append(self.rigth)


def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    if args[0] == 0:
        return AgenteHumano()
    if args[0] == 1:
        return AgenteAmplitude()
    if args[0] == 2:
        return AgenteProfundidade()
    if args[0] == 3:
        return AgenteAprofundamentoIterativo()
