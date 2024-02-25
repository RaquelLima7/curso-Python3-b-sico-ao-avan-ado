"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Digite uma letra:
# Digite apenas uma letra. \\ se digitar mais de uma
# Palavra formata: ******* (quantidade de caracteres da palavra)
# Se a pessoa digitar ex por exemplo e tiver na palavra, vai aparecer assim:
# Palavra formata: *e****e (vai ficar salvo na memória)
# Quando terminar:
# VOCÊ GANHOU PARABÉNS!
# A palavra era: perfume
# Tentativas: 24

secret_word = 'python'
new_word = '******'
num_count = 0

while True:
  user_input = input('Digite uma letra: ').lower()
  num_count += 1


  if len(user_input) > 1:
    print('Digite apenas uma letra.')
    continue

  for i, caractere in enumerate(secret_word):
    if caractere == user_input:
      list_word = list(new_word)
      list_word[i] = user_input
      new_word = ''.join(list_word)
      if new_word == secret_word:
        print('VOCÊ GANHOU PARABÉNS!')
        print(f'A palavra era: {secret_word}')
        print(f'Tentativas: {num_count}')
      else:
        print(f'Palavra formata: {new_word}')


# solção do professor

# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0
