from menuTarefas import tarefas
from menuCompras import compras

def menus():
    
    print('\t'*2,'=-'*38)
    print('\n','\t'*6,' Menu')
    print('\n','\t'*3,'~'*14,'\t'*3,'~'*14)
    print('\t'*3,'[ 1 ] TAREFAS',end=' ')
    print('\t'*4,'[ 2 ] COMPRAS')
    print('\t'*3,'~'*14,'\t'*3,'~'*14)
    print('\n','\t'*6,'~'*10)
    print('\t'*6,'[ 0 ] Sair')
    print('\t'*6,'~'*10)
    print('\n','\t'*2,'=-'*38)





def main():
    
    menus()

    while True :
        
        opcao = input('\n\t\t Selecione o Menu: ').strip()
        if opcao == '0' :
            break
        else:
            
            if opcao == '1' :
                tarefas()
            elif opcao == '2' :
                compras()
            else :
                print('\n','\t'*4,'Selecione [ numero ] da opção: \n\n','\t'*5,'[ 1 ][ Tarefas ]   [ 2 ][ Compras ]   [ 0 ][ Sair ]')
            menus()

main()
