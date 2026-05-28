print('Calculadora de gorjeta \n')

valor_conta = float(input('Digite o valor da conta: '))
porcentagem_gorjeta = float(input('Digite a porcentagem de gorjeta: '))

gorjeta = valor_conta * (porcentagem_gorjeta / 100)
total_a_pagar = valor_conta + gorjeta

print(f'Valor da gorjeta: R$ {gorjeta:.2f} \nTotal a pagar: R$ {total_a_pagar:.2f}')

print('*************************************************')

print('Validador de CPF \n')

def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
    if len(cpf) != 11:
        return 'Erro: O CPF deve conter exatamente 11 dígitos.'
    return 'CPF válido.'

cpf = input('Digite seu CPF: ')
print(validar_cpf(cpf))

print('*************************************************')

print('Contador de vogais \n')

def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    quantidade = 0
    for letra in texto:
        if letra in vogais:
            quantidade += 1
    return quantidade

texto = input('Digite um texto: ')
print(f'A quantidade de vogais no texto é: {contar_vogais(texto)}')

print('*************************************************')

print('Verificador de palavras longas \n')

texto = input('Digite um texto: ')

palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)
if palavras_longas:
    print('Palavras longas encontradas: ')
    for palavra in palavras_longas:
        print(palavra)
else:
    print('Nenhuma palavra longa encontrada no texto.')

print('*************************************************')

print('Gerador de senhas seguras \n')

import random

def gerar_senha():
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = '!@#$%^&*'

    senha = [random.choice(maiusculas),
             random.choice(minusculas),
             random.choice(numeros),
             random.choice(especiais)]
    
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

print(f'Senha gerada: {gerar_senha()}')

print('*************************************************')

# import random

print('Pedra, Papel, Tesoura \n')

def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    escolha_usuario = input('Escolha: pedra, papel ou tesoura? ').lower()
    
    if escolha_usuario not in opcoes:
        return 'Escolha inválida!'
    
    print(f'Computador escolheu: {escolha_computador}')

    if escolha_usuario == escolha_computador:
        return 'Empate!'
    
    elif (
        (escolha_usuario == 'tesoura' and escolha_computador == 'pedra') or
        (escolha_usuario == 'papel' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'pedra' and escolha_computador == 'papel')
    ):
        return 'Você venceu!'
    
    else:
        return 'Você perdeu!'
    
print(pedra_papel_tesoura())