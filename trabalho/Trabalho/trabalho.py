#  this code is made by Carlos Daniel Alves Mometto
print ('Hello, Carlos Daniel Alves Mometto!')

valorDoPedido= float(input('Digite o valor: ')) #Here we take the total value of the order
quantidadeParcelas= int(input('Digite o número de parcelas: ')) #Here we take the number of installments

if quantidadeParcelas < 4:
    juros = 0.0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16
else:
    juros = 32
valor_parcela = (valorDoPedido * (1 + juros / 100)) / quantidadeParcelas  #Calculating the installment value with interest
print(f'O valor de cada parcela é: R$ {valor_parcela:.2f}')
valorTotalParcelado = valor_parcela * quantidadeParcelas #Calculating the total value to be paid
print(f'O valor total a ser pago é: R$ {valorTotalParcelado:.2f}')


