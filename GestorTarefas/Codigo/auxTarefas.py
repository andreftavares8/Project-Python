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

#ler ficheiro tarefa
def readFunc():
    
    listaPrincipal = []
    dir = openTxt(r"\tarefas.txt")
    myFile = open(os.path.join(dir),"r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            listaPrincipal +=  [row]
    myFile.close()
    return(listaPrincipal)

#escrever tarefa
def writeFunc(allLists):
    dir = openTxt(r"\tarefas.txt")
    myFile = open(os.path.join(dir), "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in allLists:
        for elem in row.lista:
            writer.writerow(elem)
    myFile.close()

#ler nome das listas
def readNomeListas():
    listaPrincipal = []
    dir = openTxt(r"\listaTarefas.txt")
    myFile = open(os.path.join(dir), "r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            listaPrincipal += [row]
    myFile.close()
    return (listaPrincipal)

#escrever nome das listas
def writeNomeListas(alllists):
    dir = openTxt(r"\listaTarefas.txt")
    myFile = open(os.path.join(dir), "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in alllists:
        s = [row.nome, row.num]
        writer.writerow(s)
    myFile.close()

#buscar listas#
def getListas(tarefas, nomeListas):
    allLists = []
    x = 0
    for row in nomeListas:
        y = x + int(row[1])
        allLists = allLists + [myLists(row[0], row[1], tarefas[x:y])]
        x = x + int(row[1])
    return allLists

#atualiza alguns ficheiros 
def atualiza(allLists, lista):
    
    for i in range(0,len(allLists)):
        if allLists[i].nome == lista.nome:
            allLists[i] = lista
    return allLists

def tarefasATerminar(allList):
    print('\n\n','\t'*3,'< --------------------  Menu Tarefas  -------------------- >')
    print('\n','\t'*2,'-='*38)
    data = datetime.datetime.now()
    dataI = datetime.datetime(data.year,data.month,data.day,0,0,0)
    dataF = datetime.datetime(data.year,data.month,data.day,23,59,59)

    print("\n\t\t Tarefas com prazos que terminam hoje:")
    for lista in allList:
        print("\n\t\t",lista.nome)
        sel = 1
        for elem in lista.lista:
            if elem[2] != "":
                array = elem[2].split(" ")
                data = array[0].split("-")
                tempo = array[1].split(":")
                data = datetime.datetime(int(data[0]),int(data[1]),int(data[2]),int(tempo[0]),int(tempo[1]),int(float(tempo[2])))
                if data.year == dataI.year and data.month == dataI.month and data.day == dataI.day:
                    print("\t\t",sel, ")", elem[0]," -> Prazo:",elem[2])
                    sel += 1
        if sel == 1:
            print("\t\t Não existem tarefas a terminar hoje nesta lista")

#1 adiconar tarefa
def addTarefa(listaPrincipal):
    resp = '1'
    while resp == '1':
        temporaria = []
        nome = input("\n\t\t Nome da Tarefa: ")

        op = int(input("\n\t\t Adicionar observações? [ 1 ] Sim [ 2 ] Nao: "))
        observacao = ""
        if op == 1:
            observacao = input("\n\t\t Escreva as observações: ")

        op = int(input("\n\t\t Adicionar prazo de concretização? [ 1 ] Sim [ 2 ] Nao: "))
        if op == 1:
            print("\n\t\t Escreva a data no seguinte formato: dia mes ano hora min seg")
            data = input("\n\t\t Hora, min e seg são campo facultativos e podem ser prenchidos pelo valor ou [ -1 ]\n")
            data = data.split("-")
            ano = int(data[2])
            mes = int(data[1])
            dia = int(data[0])
            hora = 23
            min = 59
            seg = 59
            if len(data) > 3:
                if int(data[3]) != -1:
                    hora = int(data[3])
                    print(hora)
                if int(data[4]) != -1:
                    min = int(data[4])
                    print(min)
                if int(data[5]) != -1:
                    seg = int(data[5])
            #ano(2) mes(1) dia(0) horas(3) minutos(4) segundos(5)
            prazo = datetime.datetime(ano, mes, dia, hora, min, seg)
        else:
            prazo = ""

        if nome in temporaria:
            print('\n','\t'*5,'-'*27)
            print('\t'*5,'Já existe nome da Tarefa !!')
            print('\t'*5,'-'*27)
            input('\n\t\t\t\t\t\t Prima [enter]  ')

        else:

            print('\n','\t'*5,'-'*26)
            print('\t'*5,'Adicionado com sucesso !!!')
            print('\t'*5,'-'*26)
            temporaria += [nome]
            data = datetime.datetime.now()
            temporaria += [data]
            temporaria += [prazo]
            temporaria += ["Aberta"]
            temporaria += [observacao]
            listaPrincipal.lista += [temporaria]
            listaPrincipal.num = str(int(listaPrincipal.num) + 1)

        resp = input("\n\t\t\t Adicionar uma nova Tarefa?  [ 1 ] Sim [ 2 ] Nao").strip().upper()[0]
        if resp == '2':
            print('\t'*6,'-'*19)
            print('\t'*6,'Fim da Tarefa')
            print('\t'*6,'-'*19)

    return listaPrincipal

#2 editar tarefa
def editTarefa(listaPrincipal):
    sel = 1
    for row in listaPrincipal.lista:
        print("\t\t",sel, ")", row[0])
        sel = sel + 1
    if sel != 1:
        sel = int(input("\n\t\t Selecione a tarefa que pretende editar: ")) -1
        if listaPrincipal.lista[sel][3] == "Fechada":
            resp = input("\t\t A tarefa esta fechada tem a certeza que deseja modificar-la? [ 1 ] Sim [ 2 ] Nao")
            if resp == "2":
                return listaPrincipal
        print("\n\t\t Pretende mudar o nome ou as obeservações?")
        op = int(input("\t\t [ 1 ] Nome [ 2 ] Observações"))
        if op == 1:
            listaPrincipal.lista[sel][0] = input("\n\t\t Novo nome: ")
        if op == 2:
            listaPrincipal[sel][4] = input("\n\t\t Escreva a nova observação: ")
    else:
        print("\n\t\t A lista não tem nenhuma tarefa")
    return listaPrincipal

#3 consultar tarefa
def consultFunc(listaPrincipal,funcao):
    print("\n\t\t Nome da lista:",listaPrincipal.nome,"\n")
    print('\n',"=-"*69)
    print('{:>17} {:>40} {:>29} {:>20} {:>27}'.format('TAREFAS','DATA DE CRIAÇÃO','OBSERVAÇÕES','ESTADO','PRAZO'))
    print('-'*139)
    imprimiu = False
    for row in listaPrincipal.lista:
        if (row[3] == "Fechada" and funcao == "sort") or funcao == "main":
            imprimiu = True
            if row[4] != "":
                print('|{:<35}|{:<27}|{:<35}'.format(row[0],row[1],row[4]),end=' ')
            else:
                print('|{:<35}|{:<27}|{:<35}'.format(row[0],row[1],""),end=' ')
            if row[2] != "": 
                print('|{:8}|{:>27}|'.format(row[3],row[2]))
            else:
                print('|{:8}|'.format(row[3]))
            print("--"*69)
    if imprimiu == False:
        print("\n\t\t A lista não tem nenhuma tarefa")

#4 estado da tarefa
def estadoTarefa(listaPrincipal):
    print("\n\t\tDeseja ver as tarefas:")
    print("\t\t[ 1 ] Abertas [ 2 ] Fechadas")
    op = int(input())
    while op == 1 or op == 2:
        imprimiu = False
        for row in listaPrincipal.lista:
            if (op == 1) and (row[3]== "Aberta"):
                imprimiu = True
                print("\t\t" ,row[0])
                print("\t\t Data de Criação:",row[1])
                if row[2] != "":  # existe um data de prazo
                    print("\t\t Prazo:",row[2])
                print("\t\t Estado:", row[3])
                if row[4] != "":
                    print("\t\t Observações:", row[4])
                print("\t\t ------------------------------------------------------")
            if op == 2 and row[3] == "Fechada":
                imprimiu = True
                print("\t\t" ,row[0])
                print("\t\t Data de Criação:",row[1])
                if row[2] != "":  # existe um data de prazo
                    print("\t\t Prazo:",row[2])
                print("\t\t Estado:", row[3])
                if row[4] != "":
                    print("\t\t Observações:", row[4])
                print("\t\t ------------------------------------------------------")
        if imprimiu == False:
            if op == 1:
                print("\n\t\t Não existem tarefas abertas")
            else:
                print("\n\t\t Não existem tarefas fechadas")
        print("\n\t\t Deseja ver as tarefas:")
        print("\t\t[ 1 ] Abertas [ 2 ] Fechadas [3] Retroceder ")
        op = int(input())

#5 marcar fechado
def closeTarefa(listaPrincipal):
    temp = []
    sel = 1
    for i in range(0,len(listaPrincipal.lista)):
        if listaPrincipal.lista[i][3] == "Aberta":
            print("\t\t",sel,")",listaPrincipal.lista[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("\n\t\t Não existem tarefas abertas")
    else:
        sel = int(input("\n\t\t Escolhe a tarefa que quer fechar:")) - 1
        listaPrincipal.lista[temp[sel]][3] = "Fechada"
        print("\n\t\t Tarefa Fechada")
    return(listaPrincipal)

#6 remover tarefa
def removeFunc(listaPrincipal):
    sel = 1
    for row in listaPrincipal.lista:
        print("\t\t",sel,")",row[0])
        sel = sel + 1

    if sel == 1:
        print("\n\t\t Não existem tarefas")
    else:
        op = int(input("\n\t\t Selecione a tarefa que pretende remover:"))
        op =  op - 1

        listaPrincipal.lista.remove(listaPrincipal.lista[op])
        listaPrincipal.num = str(int(listaPrincipal.num) - 1)
    
    return(listaPrincipal)

#7 procurar tarefa
def searchTarefa(listaPrincipal): #mudar list para list.lista
    
    x = input('Escreva o nome: ')
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
            print("\t\t",sel, ")", listaPrincipal.lista[i][0]," (encontrado nas observações)")
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        op = int(input("\n\t\t Que tarefa deseja selecionar?")) -1
        print(listaPrincipal.lista[temp[op]][0])
        print("\t\t Data de Criação:", listaPrincipal.lista[temp[op]][1])
        if listaPrincipal.lista[temp[op]][3] == "Fechada":
            print("\t\t Estado:", listaPrincipal.lista[temp[op]][3], "-> Data de concretização", listaPrincipal.lista[temp[op]][2])
        else:
            print("\t\t Estado:", listaPrincipal.lista[temp[op]][3])
        print("\t\t Observações:", listaPrincipal.lista[temp[op]][4])
        print("------------------------------------------------------")
    else:
        print("\n\t\t Não há tarefas com esse nome")

#8 ordenar lista de tarefas
def sortTarefa(listaPrincipal):
    campo = 0
    funcao = ""
    op = int(input('\n\t\tDeseja organizar por: \n[ 1 ] Nome [ 2 ] Data de criação [ 3 ] Data de concretização: '))

    if op == 1:
        campo = 0
        funcao = "main"
    elif op == 2:
        campo = 1
        funcao = "main"
    elif op == 3:
        campo = 2
        funcao = "sort"

    while(True):
        i = 0
        changed = False

        while i < len(listaPrincipal.lista)-1:
            if (listaPrincipal.lista[i+1][campo] < listaPrincipal.lista[i][campo]):
                aux = listaPrincipal.lista[i]
                listaPrincipal.lista[i] = listaPrincipal.lista[i+1]
                listaPrincipal.lista[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            break;

    consultFunc(listaPrincipal,funcao)

#9 mudar lista atual
def mudarLista(allLists):
    sel = 1
    for listaPrincipal in allLists:
        print("\t\t",sel, ')', listaPrincipal.nome)
        sel = sel + 1
    op=int(input("\n\t\t Para qual deseja mudar: "))
    op = op - 1
    listaPrincipal = allLists[op]
    return listaPrincipal

#10 mudar nome da lista
def mudarNomeLista(listaPrincipal): #list.nome
    nome = input("\n\t\t Novo nome da lista: ")
    listaPrincipal.nome = nome
    return listaPrincipal

#11 criar nova lista
def criarList(allLists):
    nome = input("\n\t\t Nome da lista nova: ")
    allLists.append(myLists(nome,"0",[]))
    return allLists

def removeList(allLists):
    sel = 1
    for listaPrincipal in allLists:
        print("\t\t",sel, ')', listaPrincipal.nome)
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



