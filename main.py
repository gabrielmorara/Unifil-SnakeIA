import time
from regras_jogo import construir_jogo
from agentes import construir_agente
import pygame


# def ler_tempo(em_turnos=False):
#     """ Se o jogo for em turnos, passe 1 (rodada), senão se o jogo for
#     continuo ou estratégico, precisa.
#     """
#     return 1 if em_turnos else time.time()

def iniciar_jogo():
    # Inicializar e configurar jogo
    relogio = pygame.time.Clock()
    jogo = construir_jogo()
    tempo_de_jogo = 0
    aux_id_jogador = jogo.aux_id_jogador
    print(aux_id_jogador)
    id_jogador, jogador = jogo.registrarAgenteJogador(), construir_agente(aux_id_jogador)

    while jogo.isFim():
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(id_jogador)
        print(ambiente_perceptivel)
        jogador.adquirirPercepcao(ambiente_perceptivel)

        # Decidir jogada e apresentar ao jogo
        strx = str(jogador.escolherProximaAcao())
        print(strx)
        jogo.registrarProximaAcao(id_jogador, strx)

        # Atualizar jogo
        # tempo_corrente = ler_tempo()
        jogo.atualizarEstado()
        # tempo_de_jogo += tempo_corrente

        # FPS
        relogio.tick(30)


if __name__ == '__main__':
    iniciar_jogo()
