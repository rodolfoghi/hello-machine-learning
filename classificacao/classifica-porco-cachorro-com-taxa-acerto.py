# -*- coding: utf-8 -*-

# é gordinho? tem perna curta? faz au-au?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [0, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# "1" - é porco, "-1" - é cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

# treinar
modelo.fit(dados, marcacoes)

# animais misteriosos, para o algoritimo descobrir se é porco ou cachorro
misterioso1 = [1, 1, 0]
misterioso2 = [1, 1, 1]
misterioso3 = [1, 0, 1]
testes = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [1, -1, -1]
print("marcacoes teste", marcacoes_teste)

# prevê que tipo de animal é cada animal misterioso
resultado = modelo.predict(testes)
print("resultado", resultado)

diferencas = resultado - marcacoes_teste
print("diferencas", diferencas)

acertos = [d for d in diferencas if d==0]
print("acertos", acertos)

total_de_acertos = len(acertos)
print("total de acertos", total_de_acertos)

total_de_elementos = len(testes)
print("total de elementos testados", total_de_elementos)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print(taxa_de_acerto)