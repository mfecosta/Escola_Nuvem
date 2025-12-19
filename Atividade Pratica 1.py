# Menu principal
print("Escolha uma atividade no menu abaixo:")
print("1 - Olá Mundo")
print("2 - Calculadora")
print("3 - Calculadora Volume")
print("4 - Calculadora Preço Total")
print("5 - Sair")
print("Digite o valor da atividade:\n")

num = int(input())

# Função Olá Mundo #############
def OlaMundo():          #######
    print("Olá Mundo")   #######
################################

## Função Calculadora  ###
def Calculadora():
    numero1 = 12
    numero2 = 14
    # Cálculo da soma dos números
    soma = numero1 + numero2

    print(f"Soma dos valores é : {soma} ")

###########################################
###########################################

## Função Calculadora Volume ###
def CalculadoraVolune():
    comprimento = 12
    largura = 14
    altura = 20

    # Cálculo do volume (em cm³)
    volume = comprimento * largura * altura

    print(f"Comprimento: {comprimento} cm")
    print(f"Largura: {largura} cm")
    print(f"Altura: {altura} cm")
    print(f"Volume: {volume} cm³")

###########################################
###########################################


## Função Calculo Produtos ###
def CalculoProdutos():
    produto = "Cadeira Infantil"
    preco = 12.40
    quantidade = 3

    # Cálculo dos produtos
    valor = preco * quantidade

    print(f"O preço total dos produtos é : {valor} ")


###########################################
###########################################


## Função Calculadora  ###
def Calculadora():
    numero1 = 12
    numero2 = 14

    # Cálculo da soma dos números
    soma = numero1 + numero2

    print(f"Soma dos valores é : {soma} ")

###########################################
###########################################

# Verificação da escolha
if num == 1:
    OlaMundo()
elif num == 2:
    Calculadora()
elif num == 3:
    CalculadoraVolune()
elif num == 4:
    CalculoProdutos()
elif num == 5:
    print("Saindo...")
else:
    print("Opção inválida")