clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for cliente in clientes:
    print(cliente)

print('*************************************************')

contador = 0

while contador < 10:
    print('Processando dados...')
    contador += 1

print('*************************************************')

for i in range(5):
    print('Bem-vindo ao Buscante!')

print('*************************************************')

valores = [10, 20, 30, 40, 50]

soma = 0
for valor in valores:
    soma += valor

print(f'A soma total das receitas é: R$ {soma}')

print('*************************************************')

projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projeto is None:
        print('Projeto ausente')
    else:
        print(projeto)

print('*************************************************')

livros = ['1984', 'Dom Casmurro', 'O Pequeno Príncipe', 'O Hobbit', 'Orgulho e Preconceito']

for livro in livros:
    if livro == 'O Hobbit':
        print(f'Livro encontrado: {livro}')
        break

print('*************************************************')

estoque = 5

while estoque > 0:
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque}')

print('Produto esgotado!')

print('*************************************************')

'''
Início (10): O primeiro número a ser incluído.
Parada (0): O limite exclusivo. Ou seja, o laço para antes de chegar no 0, terminando no 1.
Passo (-1): Indica que a cada volta do laço, o Python deve subtrair 1 do valor atual.
'''

for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {segundos} segundos restantes.')

print('Aproveite a promoção agora!')

print('*************************************************')

livros = [{'Nome': '1984', 'Estoque': 5},
          {'Nome': 'Dom Casmurro', 'Estoque': 0},
          {'Nome': 'O Pequeno Príncipe', 'Estoque': 3},
          {'Nome': 'O Hobbit', 'Estoque': 0},
          {'Nome': 'Orgulho e Preconceito', 'Estoque': 2}]

for livro in livros:
    if livro['Estoque'] == 0:
        continue
    else:
        print(f'Livro disponível: {livro['Nome']}')

print('*************************************************')

while True:
    nome_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if len(nome_usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres')
        continue
    
    if len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres')
        continue

    print('Cadastro realizado com sucesso!')
    break

print('*************************************************')