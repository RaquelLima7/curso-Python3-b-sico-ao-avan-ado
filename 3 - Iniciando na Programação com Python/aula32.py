"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try:
  num_int = int(num)
  if num_int % 2 == 0:
    print('Este número é par.')
  else:
    print('Este número é ímpar.')
except:
  print('Este número não é inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hour = input("Qual é a hora?: ")

try:
  int_hour = int(hour)
  if int_hour >= 0 and int_hour <= 11:
    print("Bom dia")
  elif int_hour >= 12 and int_hour <= 17:
    print("Boa tarde")
  elif int_hour >= 18 and int_hour <= 23:
    print("Boa noite")
  else:
    print("Digite um número de 0 a 23.")
except:
  print("O caracter mencionado não é válido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Informe o seu primeiro nome: ')

if len(name) <= 4:
  print("Seu nome é curto")
elif len(name) == 5 or len(name) == 6:
  print("Seu nome é normal")
elif len(name) > 6:
  print("Seu nome é muito grande")


# Solução do professor

# exercício 1
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

# exercício 2
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
    
# exercício 3

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
    
