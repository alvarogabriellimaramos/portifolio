import os
from time import sleep
def texto(txt):
    tam = len(txt)
    print('='*tam)
    print(txt)
    print('='*tam)
def menu(*lista):
    c = 1
    for cont in lista:
        print(f'{c} - {cont}')
        c += 1
texto('SISTEMA DE DIRETORIOS E ARQUIVOS - '.center(80))

while True:
    menu('Criar um novo diretorio','Acessar um diretorio','Criar um novo arquivo em um diretorio','Ver lista de arquivos em um diretorio','Sair do programa')
    try:
         print('-'*30)
         usuario = int(input('Digite sua opção - '))
    except:
        texto('ERRO:Digite um numero valido')
    else:
        if usuario  == 1:
            sleep(0.6)
            texto('Novo Diretorio '.center(60))
            nome = str(input("Nome da sua pasta - "))
            try:
                nova_pasta = os.mkdir(f'{nome}')
            except:
                print()
                sleep(0.6)
                texto('ERRO:Ao criar diretorio')
                print()
            else:
                sleep(0.6)
                texto('Diretorio criado com sucesso'.center(60))
        elif usuario == 2:
            texto('Visualização de diretorio'.center(60))
            nome = str(input('Digite o nome do arquivo ou pasta que deseja vizualizar -  '))
            try:
                start = os.startfile(f'{nome}')
            except:
                print()
                sleep(0.6)
                texto('ERRO:Impossivel acessar o diretorio especificado')
                print()
            else:
                print()
                sleep(0.6)
                texto('Diretorio acessado com sucesso')
                print()
        elif usuario == 3:
            sleep(0.6)
            texto('Crianção de arquivos '.center(60))
            nome_pasta = str(input('Nome da pasta que deseja criar o seu arquivo - '))
            nome_arquivo = str(input('Nome do arquivo - '))
            try:
                
                with open(f'{nome_pasta}/{nome_arquivo}','x') as file:
                    file = file
            except:
                print()
                sleep(0.6)
                texto('ERRO:Ao criar arquivo')
                print()
            else:
                print()
                sleep(0.6)
                texto('Arquivo criado com sucesso'.center(40))
                print()
        elif usuario == 4:
            texto('Lista de arquivos '.center(60))
            pasta_nome = str(input("Digite o nome da pasta que deseja fazer a listagem - "))
            while True:
                sleep(0.6)
                menu('Ver de lista de diretorios','Ver lista de arquivos ','Volta ao menu')
                print()
                try:
                    printa = int(input('Qual lista deseja ver ? - '))
                except:
                    print()
                    texto('ERRO:Ao fazer listagem')
                    print()
                else:
                    if printa == 1:
                        texto(f'Lista de diretorios da pasta {pasta_nome}'.center(40))
                        for pasta,dirs,file in os.walk(f'{pasta_nome}'):
                            print(dirs)
                    elif printa == 2:
                        texto(f'Lista de arquivos da pasta {pasta_nome}'.center(40))
                        for pasta,dirs,file in os.walk(f'{pasta_nome}'):
                            print(file)
                    elif printa == 3:
                        print('Voltando para o menu...')
                        break
                    else:
                        print('Digite uma opção valida')
            
        elif usuario == 5:
            print('Finalizando programa ...')
            sleep(1)
            break
        else:
            texto('Erro:Digite uma opção valida ')