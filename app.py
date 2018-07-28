# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome_antigo = raw_input()

    if(nome_antigo in nomes):
        print 'Digite o nome nome'
        novo_nome = raw_input()
        index = nomes.index(nome_antigo)
        nomes[index] = novo_nome

def procurar_regex(nomes):
    print('Digite a expressão regular:')
    regex = raw_input()
    nomes_concat = ' '.join(nomes)
    resultado = re.findall(regex, nomes_concat)
    print resultado

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome_a_procurar = raw_input()

    if(nome_a_procurar in nomes):
        print 'Nome %s está cadastrado!' % (nome_a_procurar)
    else:
        print 'Nome %s não encontrado!' % (nome_a_procurar)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 6 procurar com regex, 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar(nomes)
        if(escolha == '6'):
            procurar_regex(nomes)
menu()