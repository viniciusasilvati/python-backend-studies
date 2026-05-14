'''
produto1 = int(input('Digite a quantidade de maças vendidas: '))
produto2 = int(input('Digite a quantidade de bananas vendidas: '))

if produto1 == produto2:
    print('Houve um empate de vendas.')

elif produto1 > produto2:
    print('As maçãs tiveram mais vendas.')

else:
    print('As bananas tiveram mais vendas.') 
'''

'''
atividade1 = int(input('Informe os dias para a atividade A: '))
atividade2 = int(input('Informe os dias para a atividade B: '))
atividade3 = int(input('Informe os dias para a atividade C: '))
tempo_total = atividade1 + atividade2 + atividade3

if atividade1 < 1 or atividade2 < 1 or atividade3 <1:
    print('Erro: Os dias não podem ser negativos.')

else:
    print(f'Tempo total do projeto: {tempo_total} dias.')
'''

'''
temperatura = int(input('Digite a temperatura atual: '))

if temperatura > 25:
    print('Alerta! Temperatura acima do limite permitido.')

else:
    print('Temperatura dentro do limite permitido.')
'''

'''
peso = int(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura **2)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso.')

elif 18.5 <= imc < 25:
    print('Peso normal.')

else:
    print('Acima do peso.')
'''

'''
despesas = float(input('Digite o valor total de despesas do mês (R$): '))

if despesas > 3000:
    print('Atenção! Você ultrapassou o limite de orçamento.')

else:
    print('Parabéns! Você está dentro do orçamento.')
    '''

'''
hora_atual = int(input('Digite a hora atual (formato 24 horas): '))

if 8 <= hora_atual < 18:
    print('Acesso permitido.')

else:
    print('Acesso negado.')
    '''

'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f'Média: {media:.2f}')

if media >= 7:
    print('Aprovado.')

elif 5 <= media < 7:
    print('Recuperação.')

else:
    print('Reprovado')
'''

'''
distancia = float(input('Digite a distância percorrida (em km): '))

if distancia <= 100:
    print('Valor do pedágio: R$ 10,00')

elif 100 < distancia <= 200:
    print('Valor do pedágio: R$ 20,00')

else:
    print('Valor do pedágio: R$ 30,00')
'''

'''
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('O número é par.')

else:
    print('O número é ímpar.')
'''

renda = float(input('Digite o valor da sua renda mensal: R$ '))
parcela = float(input('Digite o valor da parcela desejada: R$ '))

if renda > 2000 and parcela <= renda * 0.3:
    print('Empréstimo aprovado.')

else:
    print('Empréstimo negado: Parcela acima de 30% da renda.')
