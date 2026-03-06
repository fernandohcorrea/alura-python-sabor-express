from ast import main
import os

opcao_escolhida = 0
registros_restaurantes = [
    {
        'nome': 'Restaurante A',
        'endereco': 'Rua A, 123',
        'telefone': '(11) 1234-5678',
        'ativo': False
    },
    {
        'nome': 'Restaurante B',
        'endereco': 'Rua B, 456',
        'telefone': '(11) 9876-5432',
        'ativo': False
    }
]

def exibir_nome_app():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def encerrar_programa():
    limpar_tela()
    print('Programa encerrado. Até mais!')
    os._exit(0)


def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair \n')


def opcao_invalida():
    limpar_tela()
    banner("Opção inválida")
    input('Pressione Enter para continuar...')
    main()

def banner(titulo):
    limpar_tela()
    length = len(titulo) + 10
    linha = "=" * length
    print(linha)
    print(f"==> {titulo}")
    print(linha)


def cadastrar_restaurante():
    banner("Cadastrar restaurante")
    nome = input('Digite o nome do restaurante: ')
    endereco = input('Digite o endereço do restaurante: ')
    telefone = input('Digite o telefone do restaurante: ')

    append_restaurante(nome, endereco, telefone)
    print(f'\nRestaurante cadastrado com sucesso!\n\nNome: {nome}\nEndereço: {endereco}\nTelefone: {telefone}')
    input('Pressione Enter para continuar...')
    main()

def append_restaurante(nome, endereco, telefone):
    registros_restaurantes.append({'nome': nome, 'endereco': endereco, 'telefone': telefone, 'ativo': False})

def listar_restaurantes():
    banner("Listar restaurantes")
    if len(registros_restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
        input('Pressione Enter para continuar...')
        main()
    else:
        for idx, restaurante in enumerate(registros_restaurantes):
            status = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f"{idx + 1}. {restaurante['nome']} - {restaurante['endereco']} - {restaurante['telefone']} - Status: {status}")
    input('Pressione Enter para continuar...')
    main()

def ativar_restaurante():
    banner("Ativar restaurante")
    if len(registros_restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
        input('Pressione Enter para continuar...')
        main()
    else:
        for idx, restaurante in enumerate(registros_restaurantes):
            status = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f"{idx + 1}. {restaurante['nome']} - {restaurante['endereco']} - {restaurante['telefone']} - Status: {status}")
        
        try:
            opcao_escolhida = int(input('Digite o número do restaurante que deseja ativar: '))
            if 1 <= opcao_escolhida <= len(registros_restaurantes):
                registros_restaurantes[opcao_escolhida - 1]['ativo'] = True
                print(f'\nRestaurante "{registros_restaurantes[opcao_escolhida - 1]["nome"]}" ativado com sucesso!')
            else:
                print('Número inválido. Por favor, escolha um número válido.')
        except:
            print('Entrada inválida. Por favor, digite um número válido.')

    input('Pressione Enter para continuar...')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            encerrar_programa()   
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_tela()
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()



if __name__ == "__main__":
    main()
