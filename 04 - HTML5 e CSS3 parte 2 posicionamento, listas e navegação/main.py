produtos = []
while True:
    try:
        opcao = input('Para CADASTRAR produto digite 1 - Para SAIR digite 2: ')
        if opcao not in ('1','2'):# and type(opcao) != int:
            print('opcao invalida.')
        elif opcao == '1':
            
            nome_produto = input('Digite nome do produto: ')
            produtos.append(nome_produto)
        else:
            print('Você saiu do programa.')
            break
    except TypeError as e:
        print(f'Errou {e.args[0]}')

if len(produtos) > 0:
    print(f'produtos cadastrados: {produtos}')
else:
    print('não foram cadastrados produtos.')