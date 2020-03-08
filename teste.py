print("\nOlá, Seja Bem Vindo a este Programa que responde algumas funções do seu animal")

print("\nSerá preciso fornecer os dados do seu Camaleão\n")

from ac2_lp2 import Camaleao

nome = input("Informe o Nome do seu Cameleão: ")
cor = input("Qual a cor do seu Camaleão: ")
idade = input("Qual a Idade: ")
inseto_f = input("Qual o Inseto Favorito:")
##self, nome, cor, idade, inseto_favorito

c = Camaleao(nome,cor,idade,inseto_f)

print("\nO que gostaria de ver o seu animal fazendo? ")

ativar = int(input("\nInserir 1 para velo comer e 2 trocar de cor: "))

#comer_inseto
#mudar_de_cor

if ativar == 1:
    print(c.comer_inseto(),'(',inseto_f,')')
elif cor == 'azul':
    print(c.mudar_de_cor(),'de',cor,'para VERDE')
else:
    print(c.mudar_de_cor(),'de',cor,'para AZUL')
