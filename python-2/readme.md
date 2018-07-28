# Python 2: Programando com a linguagem

[x] Introdução

[x] Trabalhando com listas

[x] Tuples e dictionary

[x] Funções

[x] Cadastrando perfis

[x] Organizando melhor nosso código

[x] Expressão regulares

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

- Funções

```python
max([10, 5, 7]) # Retorna o valor máximo

min((10, 3, 9)) # Retorna o valor mínimo

sorted(nomes) # Retorna a lista ordenada
```

## Funções

As funções devem ser definidas pela palavra reservada **def**, seguindo o seguinte padrão:

```python
def gera_nome_convite(convite):
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[posicao_inicial:posicao_final]
  return parte1 + ' ' + parte2
```

A indentação é extremamente importante no Python.

No interpretador do Python, é preciso importar o biblioteca criada:
``>>> from biblioteca import *``

## Cadastrando perfis

``raw_input()`` para o input do usuário

COnversão com as funções ``int()`` e ``float()``

Para trabalhar com datas, utilizamos o **datetime**:

```python
  from datetime import date
  ano_atual = date.today().year
```

## Organizando melhor nosso código

Para executar o arquivo: ``python app.py``

If: ``if(x > 0):``

Foreach: ``for nome in nomes:``

Para definir o encoding da aplicação: ``# -*- coding: UTF-8 -*-``

Para verificar um valor na lista:

```python
> 3 in numeros
FALSE
```

Para verificar o indice do valor na lista:

```python
> letras.index('c')
2
```

## Expressão regulares

Biblioteca: ``import re``

**Função match():** Só procura a primeira ocorrência

``resultado = re.match('Py','Python')``
``resultado.group()``

**Agrupando caracteres:**

``resultado = re.match('[pP]y','Python')``

``re.match('[A-Za-z]y','Python') # Todos os caracteres de A até Z``

**Função findall():** Procura todas as ocorrências

``resultados = re.findall('([A-Za-z]y)', 'Python ou jython')``

Retorna somente os caracteres exemplificados na expressão, ou seja, somente os dois primeiros caracteres.

**Meta caracteres:**

- **[A-Za-z]** qualquer string com letras
- **+** um ou mais caracteres
- **\w** letras e números (**\w|á|é** para acentos)
- **\d** números
- **\s** espaços
- **?** possui um ou não possui (por exemplo **\d?** significa que possua ou não um número)
- **\*** não possui ou possui vários
- **.** qualquer caractere
- **()** define grupos de expressões
- **{x}** possua pelo menos x caracteres
- **{x,y}** possua entre x e y caracteres
- **^** no início da string
- **$** no final da string


**Raw string:**

Devemos utilizar uma raw string para as expressões regulares, para evitar conflitos

``r'[A-Z]+'``
