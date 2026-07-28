"""Fortuna DesSoft - jogo de perguntas e respostas para terminal."""

import os

import funcoes
from lib_questoes import quest

os.system('') 

RESET = '\033[0m'
NEGRITO = '\033[1m'
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
CIANO = '\033[96m'
MAGENTA = '\033[95m'

PREMIOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
NIVEIS = ['facil', 'facil', 'facil',
          'medio', 'medio', 'medio',
          'dificil', 'dificil', 'dificil']
PULOS_INICIAIS = 3
AJUDAS_INICIAIS = 2


def cor_do_premio(valor):
    """Premios maiores aparecem em cores mais quentes."""
    if valor >= 300000:
        return NEGRITO + MAGENTA
    if valor >= 30000:
        return AMARELO
    if valor > 0:
        return CIANO
    return RESET


def formata_dinheiro(valor):
    return 'R$ ' + format(valor, ',').replace(',', '.')


def dinheiro_colorido(valor):
    return cor_do_premio(valor) + formata_dinheiro(valor) + RESET


def pede_nome():
    nome = input('Qual e o seu nome? ').strip()
    while nome == '':
        print(VERMELHO + 'Voce precisa informar um nome.' + RESET)
        nome = input('Qual e o seu nome? ').strip()
    return nome


def mostra_manual(nome, premios, pulos, ajudas):
    print()
    print('=' * 50)
    print('BEM-VINDO AO FORTUNA DESSOFT, ' + nome.upper() + '!')
    print('=' * 50)
    print()
    print('COMO JOGAR:')
    print('- Voce respondera perguntas de multipla escolha (A, B, C ou D).')
    print('- Cada acerto aumenta o seu premio.')
    print('- Um erro encerra o jogo e voce sai sem nada!')
    print('- Apos cada acerto voce pode parar e levar o premio.')
    print()
    print('AJUDAS DISPONIVEIS:')
    print('- Digite PULA para trocar de pergunta (' + str(pulos) + ' pulos).')
    print('- Digite AJUDA para eliminar alternativas erradas (' + str(ajudas) + ' ajudas).')
    print('- Cada pergunta aceita no maximo uma ajuda.')
    print()
    print('ESCADA DE PREMIOS:')
    for i in range(len(premios)):
        print('  ' + str(i + 1).rjust(2) + '. ' + dinheiro_colorido(premios[i]))
    print()
    print('Chegando em ' + dinheiro_colorido(premios[-1]) + ' voce vence o jogo!')
    print('=' * 50)
    input('Pressione ENTER para comecar... ')


def mostra_status(premio, pulos, ajudas):
    print()
    print('Premio atual: ' + dinheiro_colorido(premio) +
          ' | Pulos: ' + CIANO + str(pulos) + RESET +
          ' | Ajudas: ' + CIANO + str(ajudas) + RESET)


def pede_escolha():
    opcoes = ['A', 'B', 'C', 'D', 'PULA', 'AJUDA']
    escolha = input('Sua resposta (A/B/C/D, PULA ou AJUDA): ').strip().upper()
    while escolha not in opcoes:
        print(VERMELHO + 'Opcao invalida! Escolha entre A, B, C, D, PULA ou AJUDA.' + RESET)
        escolha = input('Sua resposta (A/B/C/D, PULA ou AJUDA): ').strip().upper()
    return escolha


def pergunta_continuar(premio):
    pergunta = 'Quer CONTINUAR ou PARAR com ' + dinheiro_colorido(premio) + '? '
    resposta = input(pergunta).strip().upper()
    while resposta not in ['CONTINUAR', 'PARAR']:
        print(VERMELHO + 'Opcao invalida! Digite CONTINUAR ou PARAR.' + RESET)
        resposta = input(pergunta).strip().upper()
    return resposta


def pergunta_novo_jogo():
    resposta = input('Quer jogar novamente? (SIM/NAO) ').strip().upper()
    while resposta not in ['SIM', 'NAO']:
        print(VERMELHO + 'Opcao invalida! Digite SIM ou NAO.' + RESET)
        resposta = input('Quer jogar novamente? (SIM/NAO) ').strip().upper()
    return resposta == 'SIM'


def mostra_acerto(premio):
    print()
    print(NEGRITO + VERDE + '*** RESPOSTA CORRETA! ***' + RESET)
    print('Seu premio subiu para ' + dinheiro_colorido(premio) + '!')


def mostra_erro(questao):
    correta = questao['correta']
    print()
    print(NEGRITO + VERMELHO + '*** RESPOSTA ERRADA! ***' + RESET)
    print('A resposta certa era ' + VERDE + correta + ': ' +
          questao['opcoes'][correta] + RESET)


def mostra_fim(nome, premio, motivo):
    print()
    print('=' * 50)
    if motivo == 'vitoria':
        print(NEGRITO + MAGENTA + 'PARABENS, ' + nome.upper() +
              '! VOCE VENCEU O JOGO!' + RESET)
    elif motivo == 'parou':
        print(NEGRITO + AMARELO + nome.upper() +
              ', voce decidiu parar. Boa escolha!' + RESET)
    elif motivo == 'acabaram':
        print(NEGRITO + AMARELO + 'As perguntas da base acabaram, ' +
              nome.upper() + '!' + RESET)
    else:
        print(NEGRITO + VERMELHO + 'FIM DE JOGO, ' + nome.upper() + '!' + RESET)
    print('Voce leva para casa: ' + dinheiro_colorido(premio))
    print('=' * 50)


def mostra_erros_da_base(problemas):
    print('A base de perguntas esta inconsistente. O jogo nao pode comecar.')
    print('Problemas encontrados:')
    for indice, erros in problemas:
        print('  Questao ' + str(indice) + ': ' + str(erros))



def procura_problemas(questoes):
    """Devolve uma lista de (indice, erros) para as questoes com problema."""
    erros = funcoes.valida_questoes(questoes)
    problemas = []
    for i in range(len(erros)):
        if erros[i] != {}:
            problemas.append((i, erros[i]))
    return problemas


def tem_inedita(base, nivel, sorteadas):
    """Diz se ainda existe alguma questao nao sorteada nesse nivel."""
    if nivel not in base:
        return False
    for questao in base[nivel]:
        if questao not in sorteadas:
            return True
    return False


def escolhe_nivel(base, nivel_desejado, sorteadas):
    """Devolve o nivel desejado, ou outro nivel se ele estiver esgotado."""
    ordem = [nivel_desejado, 'facil', 'medio', 'dificil']
    for nivel in ordem:
        if tem_inedita(base, nivel, sorteadas):
            return nivel
    return None


def jogar(base, nome):
    """Roda o jogo e devolve (premio_final, motivo_do_fim)."""
    premio = 0
    pulos = PULOS_INICIAIS
    ajudas = AJUDAS_INICIAIS
    sorteadas = []
    rodada = 0

    while rodada < len(PREMIOS):
        nivel = escolhe_nivel(base, NIVEIS[rodada], sorteadas)
        if nivel is None:
            return premio, 'acabaram'

        questao = funcoes.sorteia_questao_inedita(base, nivel, sorteadas)
        ajuda_usada = False
        respondeu = False

        while not respondeu:
            mostra_status(premio, pulos, ajudas)
            print(funcoes.questao_para_texto(questao, rodada + 1))
            escolha = pede_escolha()

            if escolha == 'PULA':
                if pulos > 0:
                    nivel = escolhe_nivel(base, NIVEIS[rodada], sorteadas)
                    if nivel is None:
                        print(VERMELHO + 'Nao ha mais perguntas para pular. Responda esta!' + RESET)
                    else:
                        pulos -= 1
                        questao = funcoes.sorteia_questao_inedita(base, nivel, sorteadas)
                        ajuda_usada = False
                        print('Pergunta pulada! Restam ' + str(pulos) + ' pulos.')
                else:
                    print(VERMELHO + 'Voce nao tem mais pulos disponiveis!' + RESET)

            elif escolha == 'AJUDA':
                if ajuda_usada:
                    print(VERMELHO + 'Voce ja pediu ajuda nesta pergunta!' + RESET)
                elif ajudas > 0:
                    ajudas -= 1
                    ajuda_usada = True
                    print()
                    print(AMARELO + funcoes.gera_ajuda(questao) + RESET)
                else:
                    print(VERMELHO + 'Voce nao tem mais ajudas disponiveis!' + RESET)

            else:
                respondeu = True
                if escolha == questao['correta']:
                    premio = PREMIOS[rodada]
                    mostra_acerto(premio)
                    rodada += 1
                    if rodada == len(PREMIOS):
                        return premio, 'vitoria'
                    if pergunta_continuar(premio) == 'PARAR':
                        return premio, 'parou'
                else:
                    mostra_erro(questao)
                    return 0, 'errou'

    return premio, 'vitoria'

def main():
    questoes = quest

    problemas = procura_problemas(questoes)
    if problemas != []:
        mostra_erros_da_base(problemas)
        return

    base = funcoes.transforma_base(questoes)
    nome = pede_nome()
    mostra_manual(nome, PREMIOS, PULOS_INICIAIS, AJUDAS_INICIAIS)

    jogando = True
    while jogando:
        premio, motivo = jogar(base, nome)
        mostra_fim(nome, premio, motivo)
        print()
        jogando = pergunta_novo_jogo()

    print()
    print(NEGRITO + CIANO + 'Obrigado por jogar, ' + nome.upper() + '!' + RESET)


main()