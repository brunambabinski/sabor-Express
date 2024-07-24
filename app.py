import os

#restaurantes = ['Pizzaria', 'Sushi', 'Hamburgueria']
restaurantes = [{'Nome':'BellaDonna','Categoria':'Pizza','Ativo':False},
                {'Nome':'Takeo','Categoria':'Sushi','Ativo':True},
                {'Nome':'Sancros','Categoria':'Hamburguer','Ativo':False}]

def exibir_nome_do_programa():
    print('ｓａｂｏｒ ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    # menu para cadastrar restaurante
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status do  restaurante')
    print('4. Sair\n')

def escolher_opcoes():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}!')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo('Finalizando o programa')

def opcao_invalida():
    print('Opção Inválida!')
    voltar_ao_menu()
    
def voltar_ao_menu():
    print()
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print() #pula uma linha

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'Nome':nome_restaurante, 'Categoria':categoria, 'Ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome'] #chave
        categoria = restaurante['Categoria'] #chave
        ativo = 'Ativo' if restaurante['Ativo'] else 'Desativo' #chave
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()
    
def alternar_status():
    exibir_subtitulo('Alterando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que desejas alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo'] #o not altera o estado
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado: #se ele não for encontrado, é verdadeiro e entra no loop
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def main(): #simplifica a manutencao do programa, pois coloca a ordem do programa
    os.system('cls') #limpar o terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()