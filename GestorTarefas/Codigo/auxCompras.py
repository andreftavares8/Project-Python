import csv
import datetime
import os

#extra
class myLists():
    
    def __init__(self, nome, num, lista):
        self.nome = nome
        self.num = num
        self.lista = lista

#diretorio
def openTxt(nameFile):
    dir = os.path.dirname(os.path.abspath(__file__))   # tira o ultimo elemento que é o nome do programa atual
    dir = os.path.dirname(dir) # tira o ultimo elemento que é o nome da pasta dos códigos
    dir = dir +r"\dados"+nameFile # adicionamos a pasta e o nome do ficheiro que queremos abrir (tem de ter o r atrás porque o python interpreta \f como um caracter esepcial)
    return dir

#ler ficheiro compras
def read():
    lista = []
    dir = openTxt(r"\compras.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            lista += [row]
    file.close()
    return (lista)

#escrever ficheiro compras
def write(allLists):
    dir = openTxt(r"\compras.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in allLists:
        for elem in row.lista:
            writer.writerow(elem)
    file.close()

#ler ficheiro categorias
def readCate():
    listaCate = []
    dir = openTxt(r"\categorias.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            listaCate += [row]
    file.close()
    return (listaCate)

# escrever ficheiro categorias
def writeCate(listaCate):
    dir = openTxt(r"\categorias.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in listaCate:
        writer.writerow(row)
    file.close()

# ler inventario
def readInventario():
    inventario = []
    dir = openTxt(r"\inventario.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            inventario += [row]
    file.close()
    return (inventario)

# escrever ficheiro inventario
def writeInventario(inventario):
    dir = openTxt(r"\inventario.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in inventario:
        writer.writerow(row)
    file.close()

# ler categoria por item
def readCateItem():
    cateItem = []
    dir = openTxt(r"\cateItem.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            cateItem += [row]
    file.close()
    return (cateItem)

# escrever categoria por item
def writeCateItem(lista):
    dir = openTxt(r"\cateItem.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in lista:
        writer.writerow(row)
    file.close()

# ler nome de listas
def readNomeListas():
    lista = []
    dir = openTxt(r"\listaCompras.txt")
    myFile = open(os.path.join(dir), "r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            lista = lista + [row]
    myFile.close()
    return (lista)

# escrever nome listas
def writeNomeListas(alllists):
    dir = openTxt(r"\listaCompras.txt")
    myFile = open(os.path.join(dir), "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in alllists:
        s = [row.nome, row.num]
        writer.writerow(s)
    myFile.close()

# buscar listas
def getListas(tarefas, nomeListas):
    allLists = []
    x = 0
    for row in nomeListas:
        y = x + int(row[1])
        allLists = allLists + [myLists(row[0], row[1], tarefas[x:y])]
        x = x + int(row[1])
    return allLists

# atualiza (interage com outras funcões)
def atualiza(allLists, lista):
    for i in range(0,len(allLists)):
        if allLists[i].nome == lista.nome:
            allLists[i] = lista
    return allLists

# 1 adicionar elemento à lista de compras
def addCompras(lista, inventario):
    nome = input("\n\t\t Nome do produto: ")
    sel = 1
    temp = []
    print("\n\t\t Produto          | Preço Por unicade      | Quantidade existente ")
    for i in range(0, len(inventario)):
        testFind = inventario[i][0].find(nome)
        if testFind != -1:
            print("\t\t",sel, ")", inventario[i][0],"\t\t\t\t",inventario[i][2], "\t\t\t\t\t",inventario[i][1])
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        op = (int(input("\n\t\t O que deseja comprar:")))
        op -= 1
        temporaria = []
        temporaria += [inventario[temp[op]][0]]
        quant = int(input("Que quantidade deseja adicionar"))
        while quant > int(inventario[temp[op]][1]):
            print("\t\t bla bla bal")
            quant = int(input("Adicione outra quantia"))
        temporaria += [quant]
        date = datetime.datetime.now()
        temporaria+= [date]
        temporaria += [inventario[temp[op]][2]] + ["Aberta"] + [""]
        resp = int(input("Deseja deixar observações? \n [ 1 ] Sim [ 2 ] Nao"))
        if resp == 1:
            obs = input('Observação: ')
            temporaria += [obs]
        if resp == '2':
            temporaria += [""]
        lista.lista += [temporaria]
        lista.num = str(int(lista.num) + 1)
    else:
        print("\n\t\t Não existem produtos com esse nome")
    return lista

# 2 editar elemento da lista de compras
def editarElem(lista):
    sel = 1
    for row in lista.lista:
        print("\t\t",sel, ')', row[0])
        sel += 1
    sel = int(input("\n\t\t Selecione o que pretende editar: ")) -1

    if lista.lista[sel][3] == 'Fechada':
        resp = input("\n\t\t O elemento esta pago. Tem a certeza que quer modicá-lo: \n [ 1 ] Sim [ 2 ] Nao")
        if resp == '2':
            return
    print('\n\t\t O que pretende modificar?')
    opcao = int(input("\t\t [ 1 ] Nome [ 2 ] Observaçoes"))
    if opcao == 1:
        nome = input('\n\t\t Novo nome: ')
        lista.lista[sel][0] = nome
    elif opcao == 2:
        observacoes = input('\n\t\t Nova observação: ')
        lista.lista[sel][6] = observacoes
    return(lista)


# 3 fechar elemento da lista de compras
def closeElem(listaPrincipal,inventario):
    temp = []
    sel = 1
    for i in range(0,len(listaPrincipal.lista)):
        if listaPrincipal.lista[i][4] == "Aberta":
            print("\t\t",sel,")",listaPrincipal.lista[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("\n\t\t Todos os elementos estão fechados")
    else:
        print("\n\t\t Escolhe o elemento que quer fechar:")
        sel = int(input()) - 1
        for i in range(0,len(inventario)):
            if inventario[i][0] == listaPrincipal.lista[temp[sel]][0]:
                if int(inventario[i][1]) < int(listaPrincipal.lista[temp[sel]][1]):
                    print("\n\t\t Quantidade de produto demasiado grande")
                    print("\n\t\t Por favor diminua a quantidade antes de fechar o elemento")
                    return(listaPrincipal)
                else:
                    inventario[i][1] = int(inventario[i][1])-int(listaPrincipal.lista[temp[sel]][1])
                    writeInventario(inventario)
        listaPrincipal.lista[temp[sel]][5] = datetime.datetime.now()
        listaPrincipal.lista[temp[sel]][4] = "Fechada"

    return(listaPrincipal)

# 4 remover elemento da lista de compras
def remove(listaPrincipal):
    sel = 1
    for row in listaPrincipal.lista:
        print("\t\t",sel,')',row[0])
        sel += 1
    if sel != -1:
        op = int(input("\n\t\tSelecione o elemento que pretende remover"))
        op -= 1
        listaPrincipal.lista.remove(listaPrincipal.lista[op])
        listaPrincipal.num = str(int(listaPrincipal.num) - 1)
    else:
        print("\n\t\t Não existe nenhum elemento para remover")
    return listaPrincipal

# 5 visualizar lista de compras
def visualizar(listaPrincipal,funcao):
    total = 0
    imprimiu = False
    print("\n\t\t Nome da lista:",listaPrincipal.nome,"\n")
    for row in listaPrincipal.lista:
        if (row[4] == "Fechada" and funcao == "sort") or funcao == "main":
            imprimiu = True
            print("\t\t",row[0])
            print("\t\t Quantidade:",row[1]," -> Preço:",row[3])
            print("\t\t Data de Criação:",row[2])
            if row[4] == "Fechada":
                print("\t\t Estado:", row[4], "-> Data de concretização", row[5])
            else:
                print("\t\t Estado:", row[4])
            print("\t\t Observações:", row[6])
            print("\t\t ------------------------------------------------------")
            total = total + float(row[1]) + float(row[3])
    if imprimiu == True:
        print("\n\t\t Total da compra:", total)
    else:
        print("\n\t\t Não existem produtos na lista de compras")

# 6 procurar elemento
def searchElem(listaPrincipal):
    x = input('\n\t\t Escreva o nome: ')
    sel = 1
    temp = []
    for i in range(0, len(listaPrincipal.lista)):
        findNome = listaPrincipal.lista[i][0].find(x)
        if findNome != -1:
            print("\t\t",sel, ")", listaPrincipal.lista[i][0])
            temp = temp + [i]
            sel = sel + 1

        findObser = listaPrincipal.lista[i][4].find(x)
        if findObser != -1 and findNome == -1:
            print(sel, ")", listaPrincipal.lista[i][0]," (encontrado nas observações)")
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        op = int(input("\n\t\t Que elemento deseja selecionar?")) -1
        print("\t\t",listaPrincipal.lista[op][0])
        print("\t\t Quantidade:",listaPrincipal.lista[op][1]," -> Preço:",listaPrincipal.lista[op][3])
        print("\t\t Data de Criação:",listaPrincipal.lista[op][2])
        if listaPrincipal.lista[op][4] == "Fechada":
            print("\t\t Estado:", listaPrincipal.lista[op][4], "-> Data de concretização", listaPrincipal.lista[op][5])
        else:
            print("\t\t Estado:", listaPrincipal.lista[op][4])
        print("\t\t Observações:", listaPrincipal.lista[op][6])

    else:
        print("\n\t\t Não há elementos com esse nome")

# 7 ordenarar a lista
def sortLista(lista):
    campo = 0
    print("\n\t\t Quer organizar por: \n\t\t [ 1 ] nome [ 2 ] data de criação [ 3 ] data de concretisação")
    op = int(input())

    if op == 1:
        campo = 0
    elif op == 2:
        campo = 2
    elif op == 3:
        campo = 3

    while(True):
        i = 0
        changed = False

        while i < len(lista.lista)-1:
            if (lista.lista[i+1][campo] < lista.lista[i][campo]):
                aux = lista.lista[i]
                lista.lista[i] = lista.lista[i+1]
                lista.lista[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            break;

    visualizar(lista, "main")

# 8 adicionar categoria
def addCate(listaCate):
    temp = []
    nome = input("\n\t\t Nome da categoria:")
    temp = temp + [nome]
    op = int(input("\t\t Deseja adicionar categoria superior?  \n [ 1 ] Sim [ 2 ] Não"))
    if op == 1:
        print("\t\t Escreva a categoria superior:")
        cat = input()
    else:
        cat = ""
    temp = temp + [cat]
    data = datetime.datetime.now()
    temp = temp + [data]
    op = int(input("\t\t Deseja adicionar informações?  \n [ 1 ] Sim [ 2 ] Não"))
    if op == 1:
        print("\t\t Escreva as informações:")
        obs = input()
    else:
        obs = ""
    temp = temp + [obs]
    listaCate = listaCate + [temp]
    return listaCate

# 9 editar categorias
def editarCate(lista):
    sel = 1
    for row in lista:
        print("\t\t",sel, ')', row[0])
        sel += 1
    if sel == 1:
        print("\n\t\t Não existem categorias")
        return lista
    else:
        op = int(input('\t\t Selecione a categoria que pretende editar: ')) - 1
        print('\n\t\t O que pretende modificar?')
        opcao = int(input("\t\t [ 1 ] Nome [ 2 ] Categoria Sup [3] Observaçoes"))

        if opcao == 1:
            nome = input("\n\t\t Novo nome: ")
            lista[op][0] = nome
        if opcao == 2:
            cat = input("\n\t\t Nova Categoria: ")
            lista[op][0] = cat
        elif opcao == 3:
            obs = input("\n\t\t Nova observação: ")
            lista[op][4] = obs
        return lista

# 10 consultar categorias
def visualizarCate(listaCate):
    for row in listaCate:
        print("\t\t",row[0])
        if row[1] != "":
            print("\t\t Categoria Superior:",row[1],)
        print("\t\t Data de Criação:",row[2])
        print("\t\t Informações:", row[3])
        print("\t\t ------------------------------------------------------")

# 11 visualizar itens por categoria
def visualizarItemCate(cateItem,listaCate, inventario):
    temp = []
    sel = 1
    for i in range(0,len(listaCate)):
        if listaCate[i][1] == "":
            print("\t\t",sel,")",listaCate[i][0])
            temp += [i]
            sel += 1
        if sel == 1:
            print("\n\t\t Não existem categorias")
            return;
    op = int(input("\n\t\t Escolha a categoria"))
    op = temp[op-1]
    cat = listaCate[op][0]
    if foundCate(listaCate,cat) == False:
        itens = []
        sel = 1
        for row in cateItem:
            if row[0] == cat:
                print("\t\t",sel,")",row[1])
                itens += [row[1]]
                sel += 1
        if sel == 1:
            print("\t\t Não existem produtos nesta categoria")
        else:
            op = int(input("\t\t Escolha o produto")) -1
            printItem(itens[op],inventario)
    else:
        itens = []
        sel = 1
        for row in listaCate:
            if row[1] == cat:
                print("\t\t",sel,")",row[0])
                itens += [row[0]]
                sel += 1
        if sel == 1:
            print("\t\t Não existem subcategorias nesta categoria")
        else:
            for row in cateItem:
                if row[0] == cat:
                    print("\t\t",sel,")",row[0])
                    itens += [row[0]]
                    sel += 1
            op = int(input("\t\t Escolha a categoria")) -1
            printSubCategoria(itens[op],cateItem,inventario);

def foundCate(listCate,cat):
    for elem in listCate:
        if elem[1] == cat:
            return True
    return False

def printSubCategoria(cat,cateItem,inventario):
    itens = []
    sel = 1
    for row in cateItem:
        if row[0] == cat:
            print("\t\t",sel,")",row[1])
            itens += [row[1]]
            sel += 1
    if sel == 1:
        print("\t\t Não existem produtos nesta categoria")
    else:
        op = int(input("\t\t Escolha o produto")) -1
        printItem(itens[op],inventario)

def printItem(produto,inventario):
    for row in inventario:
        if row[0] == produto:
            print("\n\t\t",row[0])
            print("\t\t Quantidade:",row[1]," -> Preço:",row[3])
            if row[4] == "Fechada":
                print("\t\t Estado:", row[3])
            else:
                print("\t\t Estado:", row[3])
            print("\t\t Observações:", row[4])
            break

# 12 mudar de lista
def mudarLista(allLists):
    sel = 1
    for lista in allLists:
        print("\t\t",sel, ')', lista.nome)
        sel = sel + 1
    op=int(input("\n\t\t Qual é que deseja mudar:"))
    op = op - 1
    lista = allLists[op]
    return lista

#13 mudar nome da lista
def mudarNomeLista(lista): #list.nome
    nome = input("\n\t\t Novo nome da lista:")
    lista.nome = nome
    return lista

#14 criar lista nova
def criarList(allLists):
    nome = input("\n\t\t Nome da lista nova:")
    allLists.append(myLists(nome,"0",[]))
    return allLists

# 15 imprimir lista de compras
def printLista(lista):
    nome = r"\"impressaoCompras"+r"\""+lista.nome+".txt"
    nome = nome.replace('"',"")
    dir = openTxt(nome)
    file = open(os.path.join(dir), "w")
    date = datetime.datetime.now()
    st = "Programa Compras          \nData de Impressão: "+str(date.day)+"/"+str(date.month)+"/"+str(date.year)+"\n\n"
    file.write(st)
    st = "                      Lista "+lista.nome+"\n"
    file.write(st)
    file.write("-------------------------------------------------------------\n")
    file.write("          Nome          |     Quantidade     |     Preço    \n")
    for elem in lista.lista:
        st = " [ ] "+elem[0]
        i = 0

        while i < (28-len(elem[0])):
            st += " "
            i += 1
        st += elem[1]
        i = 0
        while i < 16:
            st += " "
            i += 1
        st += elem[3]+"\n"
        file.write(st)
    file.close()

    print("\n\t\t Lista de Compras impressa")

def removeList(allLists):
    sel = 1
    for lista in allLists:
        print("\t\t",sel, ')', lista.nome)
        sel = sel + 1
    op=int(input("\n\t\t Qual deseja remover: "))
    op = op - 1
    if not allLists[op].lista:
        allLists.remove(allLists[op])
    else:
        op = int(input(("\n\t\t A lista que quer não está vazia. Quer mesmo removê-la? [ 1 ] Sim [ 2 ] Nao: ")))
        if op == 1:
            allLists.remove(allLists[op])
    return allLists
