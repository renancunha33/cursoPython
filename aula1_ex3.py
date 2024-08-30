#você deve recriar a pirâmide do Mario.

#O tamanho da pirâmide será decidida pelo usuário, por exemplo: uma pirâmide de tamanho 8 será:

altura: int

while True:
    altura = int(input("Digite a altura da pirâmide: "))

    if altura > 0:
        break
     
#modo mais didático

for i in range(altura):
  for _ in range(altura - (i + 1)):
    print(" ", end="")

  for _ in range(i + 1):
    print("#", end="")

  print()

print("",end="\n\n")
    
#########################################################
#modo otimizado

for i in range(1, altura + 1):
    print(" " * (altura - i) + "#" * i)
     
print("",end="\n\n")    
#########################################################
# modo que digita a qtd de espaçoes e #
for i in range(1 , altura + 1):
    print(altura-i,end = " ")
    if i < 10 and altura -i <10:
        print(i,end = "  ")
    elif i >= 10 and altura -i >=10:
        print(i,end = "")
    else:
        print(i,end = " ")
    print(" " * (altura-i) + "#" * i)
