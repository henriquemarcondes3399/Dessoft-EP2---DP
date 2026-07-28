def transforma_base(questoes):
    base = {}
    for questao in questoes:
        nivel = questao['nivel']
        if nivel not in base:
            base[nivel] = []
        base[nivel].append(questao)
    return base

