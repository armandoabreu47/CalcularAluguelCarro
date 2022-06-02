km = float(input('Quantos km foram pecorridos pelo carro alugado: '))
dias = int(input('Quantos dias foi alugado: '))

valor = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é de R${} , referente a R${} dos dias e R${} referente aos km' .format(valor,dias * 60,km * 0.15))

