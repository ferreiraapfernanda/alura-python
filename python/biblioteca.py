# python/biblioteca.py

def gera_nome_convite(convite):
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[posicao_inicial:posicao_final]
  return parte1 + ' ' + parte2

def envia_convite(nome):
  print "Enviando convite para %s" % (nome)

def processa_convite(convite)
  nome = gera_nome_convite(convite)
  envia_convite(nome)