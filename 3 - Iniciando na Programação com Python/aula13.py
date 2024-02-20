nome = 'Raquel Lima'
altura = 1.56
peso = 39
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Raquel Lima tem 1.56 de altura,
# pesa 39 quilos e seu imc é
# 16.0
