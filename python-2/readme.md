# Python 2: Programando com a linguagem

[x] Introdução

[x] Trabalhando com listas

[x] Tuples e dictionary

[ ] Funções

[ ] Cadastrando perfis

[ ] Organizando melhor nosso código

[ ] Expressão regulares

[ ] Orientação a objetos e o conceito de classe

[ ] Encapsulamento

[ ] Reaproveitando código através de Herança

[ ] Escrita e leitura de arquivos

[ ] Métodos estáticos

[ ] Tratamento de exceções

## Introdução

Padrão snake_case

## Trabalhando com listas

O delimitador final é **NÃO INCLUSIVO**

Listas são definidas com **colchetes**

```python
>>> convites.append('A')
>>> convites.remove('B')
>>> convites[1:2]
>>> convites[0:]
```

## Tuples e dictionary

Tuplas -> tipos imutáveis de listas, são listas com **parenteses**

```python
>>> tipos_convites = ('vip', 'normal', 'meia', 'cortesia')
```

Dicionário -> para a associação entre o tipo e um valor, por exemplo. São listas com **chaves** e **dois pontos**

```python
>>> convites_com_valor = {'vip' : 60, 'normal' : 40, 'meia' : 30, 'cortesia' : 0}
>>> convites_com_valor['meia']
30

>>> convites_com_valor.keys()
>>> convites_com_valor.values()

>>> type(convites_com_valor)
```

Como é uma linguagem de tipagem forte, não é possível concatenar dados de tipos diferentes (listas + tuplas, por exemplo). 

Porém, podemos converter explicitamente:

``>>> estados = ('RJ', 'SP') + tuple(['MG', 'ES'])``

### Funções

```python
max([10, 5, 7]) # Retorna o valor máximo

min((10, 3, 9)) # Retorna o valor mínimo

sorted(nomes) # Retorna a lista ordenada

```

