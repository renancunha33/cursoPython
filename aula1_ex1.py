# -*- coding: utf-8 -*-
'''Exercício 1: Desenvolva um programa que selecione um
número aleatório entre 0 e 100. O usuário deverá tentar
adivinhar esse número. Ao final, o programa exibirá a
sequência de palpites do usuário
e o total de tentativas feitas até acertar o número correto'''
import random

NumeroAleatorio: int = random.randint(0, 101)

#print(NumeroAleatorio)
     

NumeroUsuario: int

ListaChutes = []

while (True):
  NumeroUsuario = int(input("Digite um número: "))

  ListaChutes.append(NumeroUsuario)

  if (NumeroUsuario == NumeroAleatorio):
    print("Paraéns vocẽ acertou!")

    break

  if (NumeroUsuario > NumeroAleatorio):
    print("O número correto é menor que este")

    continue

  print("O número correto é maior que este")

print("Os seus chutes foram: ", end="")

for i in range(len(ListaChutes)):
  print(ListaChutes[i], end=" ")

print("O total de chutes foram: ",len(ListaChutes))
