from auxTarefas import myLists,openTxt,readFunc,writeFunc,readNomeListas,writeNomeListas,getListas,addTarefa,editTarefa,consultFunc,estadoTarefa,closeTarefa,removeFunc,searchTarefa,sortTarefa,mudarLista,mudarNomeLista,criarList,atualiza,removeList,tarefasATerminar
import os

def printMenu():

    print('\n\n','\t'*3,'< --------------------  Menu Tarefas  -------------------- >')
    print('\n','\t'*2,'-='*38)
    print('''
        \n\t\t\t\t  [  1  ]  Adicionar uma tarefa.
        \n\t\t\t\t  [  2  ]  Editar uma tarefa. 
        \n\t\t\t\t  [  3  ]  Consultar tarefas. 
        \n\t\t\t\t  [  4  ]  Filtrar tarefas por estado. 
        \n\t\t\t\t  [  5  ]  Marcar uma tarefa como fechada. 
        \n\t\t\t\t  [  6  ]  Remover uma tarefa.
        \n\t\t\t\t  [  7  ]  Procurar tarefas por nome.
        \n\t\t\t\t  [  8  ]  Ordenação da lista de tarefas.
        \n\t\t\t\t  [  9  ]  Mudar lista atual.
        \n\t\t\t\t  [ 10  ]  Mudar nome da lista atual.
        \n\t\t\t\t  [ 11  ]  Criar nova lista.
        \n\t\t\t\t  [ 12  ]  Remover uma lista.
        \n\t\t\t\t  [  0  ]  Encerrar o Programa.''')
    print('\n','\t'*2,'-='*38)

def tarefas():
    
    tarefas = readFunc()
    nomesListas = readNomeListas()
    allLists = getListas(tarefas, nomesListas)
    listaPrincipal = allLists[0]

    opcao = 1

    tarefasATerminar(allLists)
    input("\n\t\t\t\t\t\t Prima [enter]  ")

    while (opcao != 0) :

        printMenu()
        opcao = input("\n\t\t Selecione a [ opção ] : ").strip()
        
        if opcao == '0' :
            print('\n','\t'*5,'-'*34)
            print('\t'*5,'Saiu do programa. VOLTE SEMPRE !!!')
            print('\t'*5,'-'*34)
            break
        
        else:
                        
            if opcao == '1':

                print('\n','\t'*5,'-'*29)
                print('\t'*5,"[ 1 ] Adicionar uma tarefa !! ")
                print('\t'*5,'-'*29)
                listaPrincipal = addTarefa(listaPrincipal)
                writeFunc(allLists)
                writeNomeListas(allLists)
                input("\n\t\t\t\t\t\t Prima [enter]  ")
                    

            elif opcao == '2':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 2 ] Editar uma tarefa !! ")
                print('\t'*5,'-'*26)
                listaPrincipal = editTarefa(listaPrincipal)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '3':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 3 ] Consultar tarefas !! ")
                print('\t'*5,'-'*26)
                consultFunc(listaPrincipal,"main")
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '4':

                print('\n','\t'*5,'-'*35)
                print('\t'*5,"[ 4 ] Filtrar tarefas por estado !! ")
                print('\t'*5,'-'*35)
                estadoTarefa(listaPrincipal)

            elif opcao == '5':

                print('\n','\t'*5,'-'*39) 
                print('\t'*5,"[ 5 ] Marcar uma tarefa como fechada !! ")
                print('\t'*5,'-'*39)
                listaPrincipal = closeTarefa(listaPrincipal)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '6':
                    
                print('\n','\t'*5,'-'*27)
                print('\t'*5,"[ 6 ] Remover uma tarefa !! ")
                print('\t'*5,'-'*27)
                listaPrincipal = removeFunc(listaPrincipal)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '7':

                print('\n','\t'*5,'-'*34)
                print('\t'*5,"[ 7 ] Procurar tarefas por nome !! ")
                print('\t'*5,'-'*34)
                searchTarefa(listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '8':

                print('\n','\t'*5,'-'*38)
                print('\t'*5,"[ 8 ] Ordenação da lista de tarefas !! ")
                print('\t'*5,'-'*38)
                sortTarefa(listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '9':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 9 ] Mudar lista atual !! ")
                print('\t'*5,'-'*26)
                listaPrincipal = mudarLista(allLists)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '10':

                print('\n','\t'*5,'-'*32)
                print('\t'*5,"[ 10 ] Mudar nome lista atual !! ")
                print('\t'*5,'-'*32)
                list = mudarNomeLista(listaPrincipal)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '11':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 11 ] Criar nova lista !! ")
                print('\t'*5,'-'*26)
                allLists = criarList(allLists)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            elif opcao == '12':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 11 ] Remover uma lista !! ")
                print('\t'*5,'-'*26)
                allLists = removeList(allLists)
                atualiza(allLists, listaPrincipal)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

            else:
                    
                print('\n','\t'*5,'-'*43)
                print('\t'*5,'Selecione o numero correto do Menu Tarefas.')
                print('\t'*5,'-'*43)

    writeFunc(allLists)
    writeNomeListas(allLists)
