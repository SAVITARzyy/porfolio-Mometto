print ('Hello, Carlos Daniel Alves Mometto!')

def escolha_modelo():
    # This function allows the user to choose a model of shirt and displays the available options
    print ('-' *3 , '           Modelo            |   Preço    ', '-' *3)
    print ('-' *3 , ' Manga Curta Simples (MCS)   |  R$ 01,80  ', '-' *3)
    print ('-'*3 , ' Manga longa Simples (MLS)   |  R$ 02,10  ', '-' *3)
    print ('-'*3 , ' Manga Curta Estampada (MCE) |  R$ 02,90  ', '-' *3)
    print ('-'*3 , ' Manga Longa Estampada (MLE) |  R$ 03,20  ', '-' *3)
    modelo= input('Digite o modelo da camiseta (MCS, MLS, MCE ou MLE): ').upper()  # Taking the model of the shirt
    if modelo not in ['MCS', 'MLS', 'MCE', 'MLE']:
        print('Modelo inválido. Por favor, escolha MCS, MLS, MCE ou MLE.')
        return escolha_modelo()
    if modelo == 'MCS':
        preco = 1.80  
    elif modelo == 'MLS':
        preco = 2.10 
    elif modelo == 'MCE':
        preco = 2.90 
    else:  
        preco = 3.20
    return preco

def numero_camisas():
    while True:
        numero= int(input('Digite o número de camisas: '))  # Taking the number of shirts
        if numero <= 0:
            print('Número inválido. Por favor, digite um número maior que zero.')
            continue  # If the number is invalid, ask again
        elif numero < 20 :
            desconto = 0.05  # 5% discount for more than 20 shirts
        elif numero < 200:
            desconto = 0.07  # 7% discount for 20 to 199 shirts
        elif numero  < 20000:
            desconto = 0.12
        else:
            print('Não produzimos essa quantidade.')
            continue  # If the number is too high, ask again
        return desconto, numero
    
def frete():
    while True:
        print('1 -Frete trasportadora (R$ 100,00)')
        print('2 -Frete sedex (R$ 200,00)')
        print('0 -Retirada na loja, grátis')
        try:
            frete = float(input('Digite o frete: '))  # Taking the shipping cost
        except ValueError:
            print('Valor inválido. Por favor, digite um número válido.')
            continue
        if frete not in [0, 1, 2]:
            print('Valor inválido. Por favor, digite 0, 1 ou 2.')
            continue  # If the shipping cost is invalid, ask again
        elif frete == '0':
            return 0.00
        elif frete == '1':
            return  100.00 
        else:
            return  200.00
        

preco = escolha_modelo()
desconto, quantidade = numero_camisas()
valor_frete = frete()


total = (preco * quantidade) * (1 - desconto) + valor_frete

print (f'O valor total do seu pedido é: R$ {total} (modelo: {preco}, quantidade: {quantidade}, desconto: {desconto * 100}%, frete: R$ {valor_frete})')


