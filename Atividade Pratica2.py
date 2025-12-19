# Menu principal
print("Escolha uma atividade no menu abaixo:")
print("1 - Conversor de Moeda Dólar e Euro para Real")
print("2 - Desconto em produtos")
print("3 - Média de alunos")
print("4 - Consumo médio de combustível")
print("5 - Sair")
print("Digite o valor da atividade:\n")

num = int(input())

# Função Conversor Moeda #############
def ConversorMoeda():       #####################
    valDolar = 5.20         #####################
    valEuro = 6.15          #####################
    valorReal = 100         #####################
    totalDolar = valorReal * valDolar
    totalEuro = valorReal * valEuro
    print(f"O valor em Dólar é: {totalDolar:.2f}")
    print(f"O valor em Euro é: {totalEuro:.2f}")
#################################################
#################################################

#  Função Desconto em produtos ###
def DescontoProduto():
    
    produto = 'Camiseta'
    preco = 50.00
    desconto = 0.20  # 20% de desconto  
    # Cálculo do valor com desconto
    valorComDesconto = preco - (preco * desconto)
    descontoValor = preco * desconto
    print(f"O preço da {produto} com desconto é : {valorComDesconto:.2f}, o desconto foi de: {descontoValor:.2f}    ")

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


###########################################
###########################################


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
   ConversorMoeda()

elif num == 2:
    DescontoProduto()
elif num == 3:
    MediaDeNotas()
elif num == 4:
    ConsumoMedio()
elif num == 5:
    print("Saindo...")
else:
    print("Opção inválida")