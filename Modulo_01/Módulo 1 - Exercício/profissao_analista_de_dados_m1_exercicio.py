"""Profissao Analista de dados M1 Exercicio.ipynb

# **Exercícios**

## 1\. Google Colab

Crie uma célula de código que escreva o texto "Olá mundo!", utilize o comando `print`.
"""

print('Olá, Mundo!')

"""Crie uma célua de texto e adicione uma imagem.


---

## 2\. Números

Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de ticket médio abaixo:

<br>

| Dia   | Valor Total Vendas | Qtd Total Vendas | Ticket Medio |
|-------|--------------------|------------------|--------------|
| 19/01 | (A)                | 3                | 320.52       |
| 20/01 | 834.47             | (B)              | 119.21       |
| 23/01 | 15378.12           | 5                | (C)          |
"""

# (A) = 961,56

Qtv_19 = 3
Tmd_19 = 320.52

A = Qtv_19 * Tmd_19
print(A)

# (B) = 7

Vtv_20 = 834.47
Tmd_20 = 119.21

B = Vtv_20 / Tmd_20
print(B)

# (C) = 3075,624

Vtv_23 = 15378.12
Qtv_23 = 5

C = Vtv_23 / Qtv_23
print(C)

"""---

## 3\. Strings

Aplique três métodos distintos na *string* abaixo, você pode conferir alguns métodos neste [link](https://www.w3schools.com/python/python_ref_string.asp):
"""

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao.upper())
posicao = cancao.find('moinho')
print(posicao)
print(cancao.isalpha())

"""Extraia da string abaixo o valor da taxa **selic** na variável `selic` e o valor do **ano** na variavel `ano`. Imprima os valores na tela."""

noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'
selic = noticia[12:17]
print(selic)

ano = noticia.find('6')
print(ano)

"""---

## 4\. Booleanos

Utilize a tabela da verdade para responder: qual o valor da variável x?
"""

a = False
b = True

x = not a & b
print(x)