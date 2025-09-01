print ('Hello, Carlos Daniel Alves Mometto!')

print ('-' *3 , '  Tamanho  |  Bife acebolado(BA)  |  Filé de frango(FF)  ', '-' *3)
print ('-'*3 , '     P     |  R$ 16.00            |  R$ 15.00            ', '-' *3)
print ('-'*3 , '     M     |  R$ 18.00            |  R$ 17.00            ', '-' *3)
print ('-'*3 , '     G     |  R$ 22.00            |  R$ 21.00            ', '-' *3)
print ("=" * 45)
acumular = 0.0  # Variable to accumulate the total value of the order
while True:
    sabor = input('Digite o sabor da marmita (BA ou FF): ').upper()  # Taking the flavor of the lunchbox
    if sabor not in ['BA', 'FF']:
        print('Sabor inválido. Por favor, escolha BA ou FF.')
        continue  # If the flavor is invalid, ask again

    Marmita = input('Digite o tamanho da marmita (P, M ou G): ').upper()  # Taking the size of the lunchbox
    if Marmita not in ['P', 'M', 'G']:
        print('Tamanho inválido. Por favor, escolha P, M ou G.')
        continue  # If the size is invalid, ask again
    if Marmita == 'P':
        if sabor == 'BA':
            valor = 16.00  # Price for small size Bife acebolado
        else:
            valor = 15.00  # Price for small size Filé de frango
    elif Marmita == 'M':
        if sabor == 'BA':
            valor = 18.00  
        else:
            valor = 17.00  
    else:  # If the size is G
        if sabor == 'BA':
            valor = 22.00  
        else:
            valor = 21.00  
    acumular += valor  
    print(f'Seu pedido {Marmita} tamanho {sabor} custa R$ {valor:.2f}')  # Displaying the cost of the order
    pedido = input('Deseja algo mais? (S ou N): ').upper()  # Asking if the customer wants something else
    if pedido == 'S':
        continue  # If the customer wants something else, continue to the next iteration
    break
print(f'O valor total do seu pedido é: R$ {acumular:.2f}')
print('Obrigado pela preferência!')
