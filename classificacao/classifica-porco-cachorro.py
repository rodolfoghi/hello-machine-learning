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
teste = [misterioso1, misterioso2, misterioso3]

# prevê que tipo de animal é cada animal misterioso
print(modelo.predict(teste))
