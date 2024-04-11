"""
receber nome
receber sobrenome
receber idade
criar funçao para calcular se é maior ou menor de idade
imprimir na tela o nome, sobrenome, idade e se é maior ou menor de idade
receber hora e falar se é dia, tarde ou noite
acima de 18 e menor que 65 pode votar, senao nao pode

"""

nome = input('digite seu nome: ')
sobrenome = input('digite, agora , o seu sbrenome: ')
idade = int(input('muito bem, agora digite a sua idade: '))
horario = float(input('digite que horas são: '))

if idade < 18 or idade > 65:
    mm = 'voce não precisa, e nem pode, votar'
else:
    mm = 'vai la e faz sua obrigação de eleitor'

if horario > 1 and horario < 12:
    hora = 'bom dia'
elif horario >= 12 and horario < 18:
    hora = 'boa tarde'
else:
    hora = 'boa noite'

print ()
print (hora, 'de acordo com os seus dados, seu nome é: ', nome,'' + sobrenome, '\n sua idade é: ', idade, 'e', mm)
