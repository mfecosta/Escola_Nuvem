# Menu principal
print("Escolha uma atividade no menu abaixo:")
print("1 - Classificação criança, jovem e adulto e idoso")
print("2 - Cálculo de IMC")
print("3 - Média de alunos")
print("4 - Consumo médio de combustível")
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

## Função Calculadora Média de notas ###
def MediaDeNotas():
    nota1 = 7.5
    nota2 = 8.0
    nota3 =6.5
    MediaDeNotas = (nota1 + nota2 + nota3) / 3
    # Cálculo da média das notas
    print(f"A média das notas é : {MediaDeNotas:.2f} ")

###########################################
###########################################


## Função Calculo de Consumo de Combustível ###
def ConsumoMedio():
    produto = "Cadeira Infantil"
    preco = 12.40
    quantidade = 3

    # Cálculo dos produtos
    valor = preco * quantidade

    print(f"O preço total da {produto} é : {valor} ")

##########################################################
##########################################################


## Função Calculadora  ###
def ConsumoMedio():
    distancia = 300  # em km
    combustivelgasto = 25  # em litros
    ConsumoMedio = distancia / combustivelgasto

    # Cálculo do consumo médio
    print(f"O consumo médio de combustível é : {ConsumoMedio:.2f} km/l, percorrendo {distancia} km com {combustivelgasto} litros de combustível ")

###########################################
###########################################

# Verificação da escolha
if num == 1:
   ClassificacaoIdade()

elif num == 2:
    CalculoImc()
elif num == 3:
    MediaDeNotas()
elif num == 4:
    ConsumoMedio()
elif num == 5:
    print("Saindo...")
else:
    print("Opção inválida")