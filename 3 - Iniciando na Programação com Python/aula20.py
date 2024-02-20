primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_numero_1 = int(primeiro_valor)
int_numero_2 = int(segundo_valor)

if primeiro_valor >= segundo_valor:
  print(f'primeiro_valor={primeiro_valor} é maior ou igual que o segundo_valor={segundo_valor}')
else:
  print(f'segundo_valor={segundo_valor} é maior que o primeiro_valor={primeiro_valor}')
