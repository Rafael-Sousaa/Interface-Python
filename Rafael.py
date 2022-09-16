#Imports
from PySimpleGUI import PySimpleGUI as Py
#Tirando importes nao usados



list = ["mussa", "pal", "pep", "fra", "por", "atum"]
listValores = [14.99, 15.99, 16.99, 19.99, 24.99, 19.99]
def ORDER_Pizza():
    layout_order = [
        [Py.Text("Sabores")],
        [Py.Checkbox("Mussarela            -- R$ 14,99", key = "mussa")],
        [Py.Checkbox("Palmito              -- R$ 15,99", key = "pal")],  
        [Py.Checkbox("Peperoni             -- R$ 16,99", key = "pep")],  
        [Py.Checkbox("Frango com mussarela -- R$ 19,99", key = "fra")],
        [Py.Checkbox("Portuguesa           -- R$ 24,99", key = "por")],     
        [Py.Checkbox("Atum com cebola      -- R$ 19,99", key = "atum")], 
        [Py.Text("Anotações:"), Py.Input(key = "Note", size = (35,3))],
        [Py.Button("Pedir", key = "order")],  
        ]
    
    Window3 = Py.Window("Fast pizza", layout_order)
    events, values = Window3.read()
    if(events == "order"):
        money=0
        for index,element in enumerate(list): 
            if values[element]:
                money = money + listValores[index]

        layout_popup = [
            [Py.Text("Pedido a caminho\n valor:"+str(round (money,2)))],
            ]
        Window4 = Py.Window("Fast pizza", layout_popup)
        Window3.close()
        events, values = Window4.read()

class TelaPython:
    def __init__(self):
        layout_account = [
        [Py.Text("nome de usuário"), Py.Input(key = "user_new", size = (25,1)), Py.Text("Email"), Py.Input(key = "email", size = (30,1))],
        [Py.Text("Senha"), Py.Input(key = "pass_new", size = (25,1)), Py.Text("Endereço"), Py.Input(key = "address", size = (35,1))],
        [Py.Text("CVC"), Py.Input(key = "CVC", size = (3,1)), Py.Text("Data de expiração"), Py.Input(key = "date", size = (6,1)), Py.Button("Confirmar", key = "confirmar")],#mudei o nome ddo botao para confirma
        [Py.Output(size = (60,20),key="output"),Py.Button("Fazer pedido", key = "req" , visible=False)],#criei o botao fazer pedido deixei ele invisel porque ele nao aperece quando começa
        ]

        self.Window2 = Py.Window("Fast Pizza", layout_account)

    def iniciar(self):
        while True:
            self.events, self.values = self.Window2.Read()
            #atribuindo as variaveis
            nome = self.values["user_new"]
            password = self.values["pass_new"]
            email = self.values["email"]
            address = self.values["address"]
            CVC = self.values["CVC"]
            Date = self.values["date"]

            if self.events == Py.WIN_CLOSED:#quando clica no x fecha a janela
                break


            elif(self.events == "confirmar"):#troquei o nome da chave do botao confirmar
                self.Window2['output'].Update('')#limpa o terminal
                self.Window2['req'].Update(visible=False)#coloca o botao para invisivel
                print("Confira seus dados")
                print("")
                list = ["nome", "email","password", "address", "CVC", "Date"]#transformou a lista em string porque com variavel estava dando erro de duplicidade esta duplicando o mesmo valor para todos
                for u in list:
                    if(u == "nome"):
                        if(nome != ""):
                            print(f"Nome:{nome}")
                        else:
                            print("O nome está em branco")
                            break
                    elif(u == "email"):
                        if(email != ""):
                            print(f"Email:{email}")
                        else:
                            print("O email está em branco")
                            break
                    elif(u == "password"):
                        if(password != ""):
                            print(f"Senha:{password}")
                        else:
                            print("A senha está em branco")
                            break
                    elif(u == "address"):
                        if(address != ""):
                            print(f"Endereço:{address}")
                        else:
                            print("O endereço está em branco")
                            break
                    elif(u == "CVC"):
                        if(CVC != ""):
                            print(f"CVC:{CVC}")
                        else:
                            print("O CVC está em branco")
                            break
                    elif(u == "Date"):
                        if(Date != ""):
                            print(f"Data de expiração:{Date}")
                            self.Window2['req'].Update(visible=True)#Deixa o botao visivel 
                        else:
                            print("A data de expiração está em branco")
                            break

            
            elif(self.events == "req"):#funçao do botao pedidos
                with open('User.txt', 'a') as arquivo: # Abre o arquivo User.txt e insere os dados da pessoa registrada
                    # Escreve todos valores no arquivo User.txt
                    arquivo.write(f'{nome} {password}\n')

                    arquivo.close() # Fecha o arquivo User.txt

                self.Window2.close()#fecha a janela cadastro
                ORDER_Pizza()#abre a janela da pizza
                break

        

layout_entry = [
    [Py.Text("Usuário "), Py.Input(key = "user_old", size = (25,1))],
    [Py.Text("Senha   "), Py.Input(key = "pass_old", password_char = "**", size = (25,1))],
    [Py.Button("Entrar", key = "enter")],
    [Py.Button("Criar um conta!", key = "create")],
]

Window = Py.Window("Fast pizza", layout_entry)

while True:
    events, values = Window.read()

    is_user_true = False
    is_pass_true = False

    if events == Py.WIN_CLOSED:#fecha janela quando clica no x
        break

    elif(events == "enter"):
        #fica bugado quando apertar o botao de enter
        user = values["user_old"]
        passw = values["pass_old"]
        if user != "" and passw != "":#verifica se o usario digitou alguma coisa na senha e no nome
            #verificar se o input do usuario for igual á alguma linha dentro do User.txt
            with open('User.txt') as f:#ler o arquivo User.txt
                for line in f:#pega cada linha do arquivo 
                    linhas=line.split(' ')#separa o valores 
                    if linhas[0] == user:#verifica se o nome digitado é igual ao do arquivo
                        is_user_true = True
                        password=str(linhas[1]).split('\n')#separa a senha do espaço vazio
                        
                        if str(password[0]) == str(passw):#verifica se a senha é a mesma do arquivo
                            is_pass_true = True 
                            break
                        
            
            if(is_user_true == True and is_pass_true == True):
                Window.close()
                ORDER_Pizza()
            elif (is_user_true == False):# se o nome  usuario n for encontrado
                Py.popup("Usuario nao encontrado") 
            else:
                Py.popup("Senha invalida")  #senha incorreta 
        else:
            Py.popup("Preencha os dados")  #caso a pessoa nao digitou seus dados

    elif(events == "create"):
        Window.close()
        TelaPython().iniciar()
        #tirei o order pizza e coloquei la em cima porque nao era aqui que chamava 
