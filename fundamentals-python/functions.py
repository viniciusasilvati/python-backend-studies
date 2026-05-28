def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = calcular_idade(ano_nascimento, ano_atual)
print(f'A idade é {idade} anos.')

print('*************************************************')

def contar_caracteres(palavra):
    return len(palavra)

palavra = input('Digite uma palavra: ')
print(f'Essa palavra tem {contar_caracteres(palavra)} caracteres.')

print('*************************************************')

def saudacao(hora):
    if 0 <= hora < 12:
        return 'Bom dia!'
    elif 12 <= hora < 18:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

hora_atual = int(input('Digite a hora atual (0-23): '))
print(saudacao(hora_atual))

print('*************************************************')

def converter_telefones(telefones):
    return [int(telefone) for telefone in telefones]

def verificar_tipos(telefones):
    for telefone in telefones:
        if not isinstance(telefone, int):
            return 'Erro na conversão.'
        
    return 'Todos os números foram convertidos corretamente!'

telefones = ['11987654321', '21912345678', '31987654321', '11911223344']

telefones_convertidos = converter_telefones(telefones)

print(verificar_tipos(telefones_convertidos))

print('*************************************************')

vendas = input('Digite os valores das vendas: ').split()
total = sum(map(float, vendas))
print(f'O total das vendas foi: {total}')

print('*************************************************')

numeros = input('Digite os números separados por espaço: ').split()
pares = filter(lambda x: int(x) % 2 == 0, numeros)
print('Números pares:', ' '.join(pares))

print('*************************************************')

produtos = input('Digite os produtos separados por vírgula: ').split(', ')
preco = input('Digite os preços separados por vírgula: ').split(', ')

lista_produtos = zip(produtos, preco)

for produto, preco in lista_produtos:
    print(f'{produto}: {preco}')


print('*************************************************')

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero.'

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Escolha a operação (| + | - | * | / |): ')

operacoes = {'+': soma, '-': subtracao, '*': multiplicacao, '/': divisao} 

if operacao in operacoes:  
   resultado = operacoes[operacao](numero1, numero2)  
   print(f"O resultado é: {resultado}")  

else:  
   print("Operação inválida") 

print('*************************************************')

def calcular_desconto(porcentagem):
   def calcular_preco(valor):
      return valor - (valor * porcentagem / 100)
   return calcular_preco

desconto = float(input('Digite a porcentagem de desconto: '))
valor = float(input('Digite o valor da compra: '))

calcular_preco_final = calcular_desconto(desconto)
print(f'Preço final com desconto: {calcular_preco_final(valor)}')

print('*************************************************')

def somar_numeros(numero):
    if numero == 1:
        return 1
    else:
        return numero + somar_numeros(numero - 1)

numero = int(input('Digite um número: '))

print(f'A soma de 1 a {numero} é: {somar_numeros(numero)}')

print('*************************************************')