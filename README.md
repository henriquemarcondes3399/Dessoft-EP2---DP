# Dessoft-EP2---DP
# Fortuna DesSoft

Jogo de perguntas e respostas para terminal, desenvolvido como Exercício
Programa 2 da disciplina de Design de Software — Insper.

O jogador responde perguntas de múltipla escolha e acumula prêmios
progressivos. Um único erro zera tudo. O objetivo é chegar em R$ 1.000.000
— ou parar antes e garantir o que já conquistou.


## Como executar

Com os três arquivos na mesma pasta:

    python main.py

O programa pede seu nome, exibe o manual e inicia a partida.


## Como jogar

Em cada pergunta, o jogador pode digitar:

* `A`, `B`, `C` ou `D` — responde a questão
* `PULA` — troca a pergunta atual por outra
* `AJUDA` — revela uma ou duas alternativas erradas

Após cada acerto, o jogo pergunta se o jogador quer CONTINUAR ou PARAR.
Parar significa sair com o prêmio acumulado.


## Regras

O jogador começa com R$ 0, três pulos e duas ajudas.

Cada acerto avança um degrau na escada de prêmios:

    1º  R$     1.000     nível fácil
    2º  R$     5.000     nível fácil
    3º  R$    10.000     nível fácil
    4º  R$    30.000     nível médio
    5º  R$    50.000     nível médio
    6º  R$   100.000     nível médio
    7º  R$   300.000     nível difícil
    8º  R$   500.000     nível difícil
    9º  R$ 1.000.000     nível difícil

Um erro encerra a partida e zera o prêmio. As perguntas nunca se repetem
dentro da mesma partida, e cada pergunta aceita no máximo uma ajuda.

Antes de iniciar, a base de perguntas é validada. Havendo qualquer
inconsistência, o programa lista os problemas encontrados e não começa
o jogo.


## Arquivos

    funcoes.py        as sete funções obrigatórias do enunciado
    lib_questoes.py   base de perguntas e respostas
    main.py           interface, validação de entrada e lógica do jogo


### funcoes.py

Reúne as sete funções desenvolvidas nos exercícios preparatórios.

`transforma_base` reorganiza a lista de questões em um dicionário agrupado
por nível de dificuldade.

`valida_questao` verifica uma questão e devolve um dicionário com os
problemas encontrados. `valida_questoes` aplica essa verificação a uma
lista inteira.

`sorteia_questao` sorteia aleatoriamente uma questão de um nível, e
`sorteia_questao_inedita` garante que a questão sorteada ainda não tenha
aparecido, registrando-a como usada.

`questao_para_texto` formata a questão para exibição no terminal.

`gera_ajuda` sorteia uma ou duas alternativas incorretas e monta a dica.


### lib_questoes.py

Define a variável `quest`, uma lista de dicionários. Cada questão tem
exatamente quatro chaves:

```python
{
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de Janeiro',
               'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
}
```

O campo `nivel` aceita apenas `facil`, `medio` ou `dificil`. Para ampliar
a base, basta inserir novos dicionários nesse mesmo formato.


### main.py

Organizado em quatro blocos separados por comentários:

1. Impressão em tela e validação de entrada — todos os `print` e `input`
2. Validação da base — aborta o jogo se houver questão inconsistente
3. Lógica do jogo — o laço principal, prêmio, pulos e ajudas
4. Programa principal — a função `main()`, que amarra tudo


## O que foi implementado

**Validação de entrada.** Nenhum comando inválido derruba o programa.
Nome vazio, letra inexistente ou resposta diferente de CONTINUAR/PARAR
geram mensagem de erro e nova solicitação.

**Validação da base de dados.** O programa informa exatamente qual questão
tem qual problema antes de permitir que o jogo comece.

**Estado sempre visível.** Prêmio atual, pulos e ajudas restantes aparecem
acima de cada pergunta.

**Partidas em sequência.** Ao final de cada jogo, o programa pergunta se o
jogador quer jogar novamente, sem precisar reexecutar o `main.py`.

**Cores por importância.** As faixas de prêmio têm cores distintas — ciano
até R$ 10 mil, amarelo até R$ 100 mil, magenta em negrito acima disso. As
mensagens seguem a mesma lógica: verde para acerto, vermelho para erro e
avisos, amarelo para dicas.

**Tolerância a base pequena.** Se um nível esgotar suas perguntas, o jogo
busca em outro nível em vez de travar.


## Requisitos

Python 3.6 ou superior. Nenhuma biblioteca externa — apenas `random` e
`os`, ambos da biblioteca padrão.


## Autor

Desenvolvido individualmente como EP2 de Design de Software. -Henrique Marcondes