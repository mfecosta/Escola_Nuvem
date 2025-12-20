# Menu principal
print("Escolha uma atividade no menu abaixo:")
print("1 - Classificação criança, jovem e adulto e idoso")
print("2 - Cálculo de IMC")
print("3 - Conversor Temperatura")
print("4 - Calculo de ano bissexto")
print("5 - Sair")
print("Digite o valor da atividade:\n")

num = int(input())

# Função Classificação Idade      #############
def ClassificacaoIdade():   #####################
    num_idade = int(input("Digite a idade: "))
    if num_idade <= 12:                       #####################
        print("Classificação Criança")        #####################   
    elif num_idade >= 13 and num_idade <= 18: #####################
        print("Classificação Adolescente")    #####################
    elif num_idade >= 18 and num_idade <= 60: #####################
        print("Classificação Adulto")         #####################
    else:                                     #####################
        print("Classificação Idoso")          #####################
###################################################################
###################################################################

#  Função Cálculo de IMC ###
def CalculoImc():
    print("Cálculo de IMC")
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))        
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 24.9:
        print("Peso normal")    
    elif imc >= 25 and imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

    print(f"Seu IMC é: {imc:.2f}")

###########################################
###########################################

## Função Conversor de Temperatura ###
def ConversorTemperatura(valor, origem, destino):
    origem = origem.upper()
    destino = destino.upper()

    if origem == "C" and destino == "F":
        return (valor * 9/5) + 32
    elif origem == "C" and destino == "K":
        return valor + 273.15
    elif origem == "F" and destino == "C":
        return (valor - 32) * 5/9
    elif origem == "F" and destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif origem == "K" and destino == "C":
        return valor - 273.15
    elif origem == "K" and destino == "F":
        return (valor - 273.15) * 9/5 + 32
    else:
        return valor  # mesma unidade

# Uso do método
valor = float(input("Digite a temperatura: "))
origem = input("Origem (C/F/K): ")
destino = input("Destino (C/F/K): ")

resultado = ConversorTemperatura(valor, origem, destino)
print(f"{valor} {origem.upper()} = {resultado:.2f} {destino.upper()}")

###########################################
###########################################

## Função Ano bissexto ###
def calculoAnoBissexto():
    ano = int(input("Digite o ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
###########################################
###########################################

# Verificação da escolha
if num == 1:
   ClassificacaoIdade()
elif num == 2:
    CalculoImc()
elif num == 3:
    ConversorTemperatura()
elif num == 4:
    calculoAnoBissexto()
elif num == 5:
    print("Saindo...")
else:
    print("Opção inválida")