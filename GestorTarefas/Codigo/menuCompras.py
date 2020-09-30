from auxCompras import myLists,openTxt,read,write,readCate,writeCate,readInventario,writeInventario,readCateItem,writeCateItem,readNomeListas,writeNomeListas,getListas,addCompras,editarCate,closeElem,remove,visualizar,searchElem,sortLista,editarCate,visualizarCate,visualizarItemCate,mudarLista,mudarNomeLista,criarList,atualiza,editarElem,addCate,printLista,removeList


def printMenu():

    print('\n\n','\t'*3,'< ---------------------  Menu Compras  -------------------- > ')
    print('\n','\t'*2,'-='*36)
    print('''
        \n\t\t\t\t    [  1  ]  Adicionar um elemento à lista de compras. 
        \n\t\t\t\t    [  2  ]  Editar um elemento da lista de compras. 
        \n\t\t\t\t    [  3  ]  Marcar um elemento como fechado. 
        \n\t\t\t\t    [  4  ]  Remover um elemento da lista de compras. 
        \n\t\t\t\t    [  5  ]  Visualizar a lista de compras.  
        \n\t\t\t\t    [  6  ]  Procurar elementos por nome.
        \n\t\t\t\t    [  7  ]  Ordenação da lista de compras. 
        \n\t\t\t\t    [  8  ]  Adicionar uma categoria. 
        \n\t\t\t\t    [  9  ]  Editar uma categoria existente. 
        \n\t\t\t\t    [ 10  ]  Consultar categorias. 
        \n\t\t\t\t    [ 11  ]  Consultar todos os items associados a uma categoria.
        \n\t\t\t\t    [ 12  ]  Mudar lista atual.
        \n\t\t\t\t    [ 13  ]  Mudar nome da lista atual.
        \n\t\t\t\t    [ 14  ]  Criar nova lista.
        \n\t\t\t\t    [ 15  ]  Imprimir lista de Compras.
        \n\t\t\t\t    [ 16  ]  Remover uma lista.
        \n\t\t\t\t    [  0  ]  Encerar o Programa.''')
    print('\n','\t'*2,'-='*36)

def compras():
    
    lista = read() #list de conmpras
    inventario = readInventario() # inventario
    listaCate = readCate() # categorias
    cateItem = readCateItem() #categorias item
    listaCompras = readNomeListas()
    allLists = getListas(lista, listaCompras)
    lista = allLists[0]

    opcao = 1

    while (opcao != 0):

        printMenu()
        opcao = input("\n\t\t Selecione a [ opção ] : ").strip()
        
        if opcao == '0':
            print('\n','\t'*5,'-'*34)
            print('\t'*5,'Saiu do progra1ma. VOLTE SEMPRE !!!')
            print('\t'*5,'-'*34)
            break
        
        if opcao == '1':

            print('\n','\t'*5,'-'*39)
            print('\t'*5,"[ 1 ] Adicionar um elemento à lista !! ")
            print('\t'*5,'-'*39)            
            lista = addCompras(lista, inventario)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '2':

            print('\n','\t'*5,'-'*36)
            print('\t'*5,"[ 2 ] Editar um elemento da lista !!")
            print('\t'*5,'-'*36)
            lista = editarElem(lista)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '3':

            print('\n','\t'*5,'-'*40)
            print('\t'*5,"[ 3 ] Marcar um elemento como fechado !!")
            print('\t'*5,'-'*40)
            lista = closeElem(lista,inventario)
            atualiza(allLists, lista)
            inventario = readInventario()
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '4':
            
            print('\n','\t'*5,'-'*37)
            print('\t'*5,"[ 4 ] Remover um elemento da lista !! ")
            print('\t'*5,'-'*37)
            lista = remove(lista)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")


        elif opcao == '5':

            print('\n','\t'*5,'-'*27)
            print('\t'*5,"[ 5 ] Visualizar a lista !! ")
            print('\t'*5,'-'*27)
            visualizar(lista,"main")
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '6':

            print('\n','\t'*5,'-'*36)
            print('\t'*5,"[ 6 ] Procurar elementos por nome !! ")
            print('\t'*5,'-'*36)
            searchElem(lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '7':

            print('\n','\t'*5,'-'*27)
            print('\t'*5,"[ 7 ] Ordenação da lista !! ")
            print('\t'*5,'-'*27)
            sortLista(lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '8':

            print('\n','\t'*5,'-'*32)
            print('\t'*5,"[ 8 ] Adicionar uma categoria !! ")
            print('\t'*5,'-'*32)
            listaCate = addCate(listaCate)
            input("\n\t\t\t\t\t\t Prima [enter]  ")
            
        elif opcao == '9':

            print('\t'*5,'-'*39)
            print('\t'*5,"[ 9 ] Editar uma categoria existente !! ")
            print('\t'*5,'-'*39)
            listaCate = editarCate(listaCate)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '10':

            print('\n','\t'*5,'-'*30)
            print('\t'*5,"[ 10 ] Consultar categorias !! ")
            print('\t'*5,'-'*30)
            visualizarCate(listaCate)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '11':

            print('\n','\t'*5,'-'*61)
            print('\t'*5,"[ 11 ] Consultar todos os items associados a uma categoria !! ")
            print('\t'*5,'-'*61)
            visualizarItemCate(cateItem,listaCate, inventario)
            input("\n\t\t\t\t\t\t Prima [enter]  ")
            
        elif opcao == '12':

            print('\n','\t'*5,'-'*26)
            print('\t'*5,"[ 12 ]Mudar lista atual !! ")
            print('\t'*5,'-'*26)
            lista = mudarLista(allLists)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '13':

            print('\n','\t'*5,'-'*32)
            print('\t'*5,"[ 13 ] Mudar nome lista atual !! ")
            print('\t'*5,'-'*32)
            lista = mudarNomeLista(lista)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '14':

            print('\n','\t'*5,'-'*26)
            print('\t'*5,"[ 14 ] Criar nova lista !! ")
            print('\t'*5,'-'*26)
            allLists = criarList(allLists)
            atualiza(allLists, lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '15':

            print('\n','\t'*5,'-'*26)
            print('\t'*5,"[ 15 ] Imprimir lista de compras !! ")
            print('\t'*5,'-'*26)
            printLista(lista)
            input("\n\t\t\t\t\t\t Prima [enter]  ")

        elif opcao == '16':

                print('\n','\t'*5,'-'*26)
                print('\t'*5,"[ 16 ] Remover uma lista !! ")
                print('\t'*5,'-'*26)
                allLists = removeList(allLists)
                atualiza(allLists, lista)
                input("\n\t\t\t\t\t\t Prima [enter]  ")

        else:
            
            print('\n','\t'*5,'-'*43)
            print('\t'*5,'Selecione o numero correto do Menu COMPRAS.')
            print('\t'*5,'-'*43)

        printMenu()
        

    writeCateItem(cateItem)
    writeInventario(inventario)
    writeCate(listaCate)
    write(allLists)
    writeNomeListas(allLists)

