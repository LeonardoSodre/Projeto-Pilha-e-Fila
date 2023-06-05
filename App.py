
def somar(n1, n2):
     
      return n1 + n2
def subtrair(n1, n2):
     
      return n1 + n2
def multiplicar(n1, n2):
  
      return n1 * n2         
def dividir(n1, n2):
 
      return n1 / n2         

operacoes = {
        1: somar,
        2: subtrair,
        3: multiplicar,
        4: dividir
        }

fila_operacoes =[]        

def menuPrincipal():
     print('************************************************************\n \t \t \t BEM VINDO \n ')   
     print('1 - OPERAÇÕES ')
     print('2 - EXPRESSÕES ')
     print('0 - FINALIZAR PROGRAMA ')
     choice1 = int(input('Digite a opção: '))
     

     if choice1  == 1:
        menu_operacoes()
       
     
     elif choice1  == 2:
        print('\n************************************************************\n  \t \t BEM VINDO AO MENUS DAS EXPRESSÕES ************************************************************\n ')
        switch_frist(choice2)  
     
     elif choice1  == 0:
        quit()
     
     else:
        print('ERRO! Opção invalida \nExecute novamente')   
        

def switch_frist(choice2):
        if choice2 == 1:
                
                print('************************************************************')
                print('\t \tADICIONAR OPERAÇÕES NA FILA\n ')
               
                print('\n 1 - Adição (+)')
                print(' 2 - Subtração (-)')
                print(' 3 - Multiplicação (*)')
                print(' 4 - Divisão (/)')        
                choice3 = int(input('Digite a opção desejada: '))
                fila_operacoes.append(choice3)  
                n1 = float(input('Digite o primeiro numero:'))
                fila_operacoes.append(n1)
                n2 = float(input('Digite o segundo numero: '))
                fila_operacoes.append(n2)
                menu_operacoes()
          

        elif choice2 == 2:
                print('EXECUTAR A PROXIMA OPERAÇÃO NA FILA \n')
                if len(fila_operacoes) > 0:
                       operacao =  fila_operacoes[0]
                       n1 = fila_operacoes[1]
                       n2 = fila_operacoes[2]
                      executa_operacao(operacao, n1, n2) 

                              
        elif choice2 == 0:       
              menuPrincipal()

        else:
                print('ERROR! \n EXECUTE NOVAMENTE')     


def executa_operacao(tipo_operacao, n1 , n2): operacoes[tipo_operacao](n1,n2)      

def menu_operacoes():
        print(' \n \n************************************************************\n  \t \t BEM VINDO AO MENU "OPERAÇÕES" \n  \n 1 - ADICIONAR OPERAÇÃO NA FILA \n 2 - EXECUTAR A PROXIMA OPERAÇÃO NA FILA \n 3 - EXECUTAR TODAS AS OPERAÇÕES DA FILA \n 0 - VOLTAR AO MENU PRINCIPAL ') 
        choice2 = int(input('Digite a operação de deseja: '))
        switch_frist(choice2)          
        
           
                    
          
menuPrincipal()


              