a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
#b=BBBBBB a=AAAAA a=AAAAA c=1.10

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)