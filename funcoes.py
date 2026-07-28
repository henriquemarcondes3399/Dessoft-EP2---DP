def transforma_base(questoes):
    base = {}
    for questao in questoes:
        nivel = questao['nivel']
        if nivel not in base:
            base[nivel] = []
        base[nivel].append(questao)
    return base
def valida_questao(questao):
    erros = {}

    for chave in ['titulo', 'nivel', 'opcoes', 'correta']:
        if chave not in questao:
            erros[chave] = 'nao_encontrado'

    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'

    if 'titulo' in questao:
        if questao['titulo'].strip() == '':
            erros['titulo'] = 'vazio'

    if 'nivel' in questao:
        if questao['nivel'] not in ['facil', 'medio', 'dificil']:
            erros['nivel'] = 'valor_errado'

    if 'opcoes' in questao:
        opcoes = questao['opcoes']
        if len(opcoes) != 4:
            erros['opcoes'] = 'tamanho_invalido'
        else:
            todas_existem = True
            for letra in ['A', 'B', 'C', 'D']:
                if letra not in opcoes:
                    todas_existem = False

            if not todas_existem:
                erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                vazias = {}
                for letra in ['A', 'B', 'C', 'D']:
                    if opcoes[letra].strip() == '':
                        vazias[letra] = 'vazia'
                if vazias != {}:
                    erros['opcoes'] = vazias
    if 'correta' in questao:
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            erros['correta'] = 'valor_errado'
    return erros


def valida_questoes(questoes):
    resultado = []
    for questao in questoes:
        resultado.append(valida_questao(questao))
    return resultado


import random


def sorteia_questao(questoes, nivel):
    return random.choice(questoes[nivel])

