import os

restaurantes = []

def exibir_nome_do_programa():
    nome_programa = '''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░'''
    print(f'{nome_programa}\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal:')
    main()

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * len(texto)
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome = input('Nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')

    dados_restaurante = {
        'nome': nome,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome} foi cadastrado com sucesso.\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print('=' * 25)
        print(f'- Nome: {nome}')
        print(f'    - Categoria: {categoria}')
        print(f'    - Status: {status}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado do restaurante')

    nome = input('Qual o nome do restaurante que deseja alternar o estado? ')

    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()