print('*************************************************')
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

import random

print('Pedra, Papel, Tesoura \n')

def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    escolha_usuario = input('Escolha: pedra, papel ou tesoura? ').lower()
    
    if escolha_usuario not in opcoes:
        print('Escolha inválida!')
    
    print(f'Computador escolheu: {escolha_computador}')

    if escolha_usuario == escolha_computador:
        print('Empate!')
    
    elif (
        (escolha_usuario == 'tesoura' and escolha_computador == 'pedra') or
        (escolha_usuario == 'papel' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'pedra' and escolha_computador == 'papel')
    ):
        print('Você ganhou!')
    
    else:
        print('Você perdeu!')
    
pedra_papel_tesoura()

print('*************************************************')

import random

print('Descubra o número secreto \n')

def adivinhar_numero():
    numero_secreto = random.randint(1,100)
    tentativas = 0

    while True:
        try:
            palpite = int(input('Digite um número entre 1 e 100: '))

            if not 1 <= palpite <= 100:
                raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100.')

            tentativas += 1

            if palpite == numero_secreto:
                print(f'Parabéns! Você acertou o número {numero_secreto}.')
                break
            elif palpite < numero_secreto:
                print(f'Muito baixo! Tente novamente: {palpite}')
            else:
                print(f'Muito alto! Tente novamente: {palpite}')

        except ValueError as e:
            print(f'Entrada inválida: {e}')

adivinhar_numero()

print('*************************************************')

print('Calculadora \n')

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

def calculadora():
    try:
        num1 = float(input('Digite o primeiro número: '))
        operacao = input('Escolha a operação (+, -, *, /): ')
        num2 = float(input('Digite o segundo número: '))

        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        else:
            print('Operação inválida!')
            return

        print(f'Resultado: {resultado}')

    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
    
calculadora()

print('*************************************************')

print('Gerenciador de tarefas \n')

def gerenciador_tarefas():
    tarefas = []

    while True:
        print('1: Adicionar uma tarefa')
        print('2: Visualizar a lista detarefas')
        print('3: Remover uma tarefa')
        print('4: Sair do programa')
        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            tarefa = input('\nDigite a tarefa a ser adicionada: ').strip()
            if tarefa:
                tarefas.append(tarefa)
                print('Tarefa adicionada com sucesso!\n')
            else:
                print('Erro: A tarefa não pode estar vazia!\n')

        elif escolha == '2':
            if tarefas:
                print('\nLista de Tarefas:')
                for i, tarefa in enumerate(tarefas, 1):
                    print(f'{i}. {tarefa}')
            else:
                print('Nenhuma tarefa na lista.\n')

        elif escolha == '3':
            if not tarefas:
                print('Nenhuma tarefa para remover.\n')
                continue
            try:
                indice = int(input('\nDigite o número da tarefa a ser removida: ')) - 1
                if 0 <= indice < len(tarefas):
                    tarefa_removida = tarefas.pop(indice)
                    print(f'Tarefa "{tarefa_removida}" removida com sucesso!\n')
                else:
                    print('Erro: Número da tarefa inválido!\n')
            except ValueError:
                print('Erro: Entrada inválida. Digite um número válido!\n')

        elif escolha == '4':
            print('\nSaindo do programa. Até mais!')
            break
        else:
            print('Opção inválida! Por favor, escolha uma opção válida.\n')

gerenciador_tarefas()

print('*************************************************')

print('Caixa eletrônico \n')

def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]
    

    try:
        valor_saque = int(input('Digite o valor a ser sacado: '))

        if valor_saque <= 0:
            print('Erro: O valor deve ser maior que zero!')
            
        elif valor_saque % 2 != 0:
            print('Erro: O valor deve ser múltiplo de 2!')
            
        else:
            print('\nCédulas entregues:')
            for cedula in cedulas:
                quantidade = valor_saque // cedula
                if quantidade > 0:
                    print(f'{quantidade} cédula(s) de R$ {cedula}')
                    valor_saque = valor_saque % cedula

    except ValueError:
        print('Erro: Entrada inválida. Digite um número inteiro válido!')

caixa_eletronico()