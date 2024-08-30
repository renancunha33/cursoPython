#Exercício 2: Você está organizando uma lista de alunos por turmas em uma escola. Cada turma contém vários alunos, e cada aluno é representado por um dicionário com informações sobre seu nome e idade.

#a) Criar as turmas: Crie duas turmas, cada uma contendo uma lista de dicionários representando os alunos. Cada dicionário deve ter as chaves "nome" e "idade".

#b) Adicionar um novo aluno: Adicione um novo aluno em uma das turmas.

#c) Remover um aluno: Remova um aluno de uma das turmas.

#d) Exibir os alunos de uma turma


# a)

turmas = {
    "Turma A": [
      {"nome": "Aluno 1", "idade": 20, "id": 1},
      {"nome": "Aluno 2", "idade": 21, "id": 2}
    ],

    "Turma B": [
        {"nome": "Aluno 3", "idade": 22, "id": 3},
        {"nome": "Aluno 4", "idade": 19, "id": 4}
    ]
}

print(turmas)
     
{'Turma A': [{'nome': 'Aluno 1', 'idade': 20, 'id': 1}, {'nome': 'Aluno 2', 'idade': 21, 'id': 2}], 'Turma B': [{'nome': 'Aluno 3', 'idade': 22, 'id': 3}, {'nome': 'Aluno 4', 'idade': 19, 'id': 4}]}

# b)

NovoAluno = {"nome": "Aluno 5", "idade": 23, "id": 5}

turmas["Turma A"].append(NovoAluno)

print(turmas["Turma A"])
     
[{'nome': 'Aluno 1', 'idade': 20, 'id': 1}, {'nome': 'Aluno 2', 'idade': 21, 'id': 2}, {'nome': 'Aluno 5', 'idade': 23, 'id': 5}]

# c)

id = 3

for turma in turmas.keys():
  for aluno in turmas[turma]:
    if aluno["id"] == id:
      turmas[turma].remove(aluno)
     
#Turma A: [{'nome': 'Aluno 1', 'idade': 20, 'id': 1}, {'nome': 'Aluno 2', 'idade': 21, 'id': 2}, {'nome': 'Aluno 5', 'idade': 23, 'id': 5}]
#Turma B: [{'nome': 'Aluno 4', 'idade': 19, 'id': 4}]

# d)

print("Turma A")

for aluno in turmas["Turma A"]:
  print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}")

print()

print("Turma B")

for aluno in turmas["Turma B"]:
  print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}")
