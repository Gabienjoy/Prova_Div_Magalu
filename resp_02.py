# Elabore um programa que leia um número que o usuário digitar. Dependendo do
# número informado, das frases abaixo, o sistema imprimirá somente as que forem
# verdadeiras.
# ○ O número é menor que 10.
# ○ O número é par.
# ○ O número está entre 8 e 16.
# ○ O número é 51 ou 80.
# Por exemplo, se o usuário digitar o número “12”, o programa irá imprimir:
# O número é par.
# O número está entre 8 e 16.
# Se o usuário digitar o número “51”, então será impresso:
# O número é 51 ou 80.
# Ou, se o usuário digitar “101”, então o programa não imprime nada.

numero = int(input('Digite um número: '))
resto= numero % 2

if numero < 10:
    print(f'O número: {numero} é menor que 10.')
if resto == 0:
     print(f'O número: {numero} é par.')
if numero >= 8 and numero <= 16:
    print(f'O número: {numero} está entre 8 e 16.')
if numero == 51 or numero == 80:
    print(f'O número: {numero} é 51 ou 80.')