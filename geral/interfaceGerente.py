import tkinter as tk                
from tkinter import font as tkfont
from tkinter import *
from controler import *
from database import *

controle = Controle()

class ManagerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#183642")
        self.controller = controller

        self.controller.title('Banco CHQ')
        self.controller.state('zoomed')

        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45),
                                 fg= 'white',
                                 background= '#183642')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height =4, bg='#183642')
        space_label.pack()

        nome_label = tk.Label(self, 
                                text='Digite seu ID',
                                font=('Calisto MT',13),
                                bg='#183642',
                                fg='white')
            
        nome_label.pack(pady = 10)

        Id = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                        textvariable= Id,
                                        font=('Calisto MT',12),
                                        width=22
                                        )
            
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)

        

        senha_label = tk.Label(self, 
                                text='Digite sua senha',
                                font=('Calisto MT',13),
                                bg='#183642',
                                fg='white')
            
        senha_label.pack(pady = 10)
            
        minhaSenha = tk.StringVar()
        caixa_entrada_senha = tk.Entry(self, 
                                        textvariable= minhaSenha,
                                        font=('Calisto MT',12),
                                        width=22,
                                       
                                        )
            
        caixa_entrada_senha.focus_set()
        caixa_entrada_senha.pack(ipady = 7)
    

        def handle_focus_in(_):
                caixa_entrada_senha.configure(fg='black', show='*')

        caixa_entrada_senha.bind('<FocusIn>', handle_focus_in)

        def checaSenha():
            senha = minhaSenha.get() 
            Idgerente = Id.get()
            
            if "123" == Idgerente and "123" == senha:
          
               senhaErrada_label['text']=''
               controller.show_frame('GerenciaPage')
            else:
               senhaErrada_label['text']= 'Senha Errada'

        enter_button = tk.Button(self,
                                    text= 'Enter',
                                    command = checaSenha,
                                    relief='raised',
                                    borderwidth= 3,
                                    width = 24,
                                    bg = "#cbc5ea",
                                    height = 2)
        enter_button.pack(pady=10)

        senhaErrada_label = tk.Label(self,
                                        text='',
                                        font=('Calisto MT',13),
                                        fg='white',
                                        bg = '#183642',
                                        anchor='n')
            
        senhaErrada_label.pack()
            
        space_label = tk.Label(self, height =15, bg = '#183642')
        space_label.pack()


        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg= '#183642')
            self.controller = controller

            button_frame = tk.Frame(self,bg='#33334d')
            button_frame.pack(fill='both',expand=True)


            def sair():
                controller.show_frame('StartPage')
        
            sair_button= tk.Button(button_frame,
                                            text='Sair',
                                            command=sair,
                                            relief='raised',
                                            borderwidth=3,
                                            width=24,
                                            height=4)
            sair_button.grid(row=40,column=40,pady=5)


class GerenciaPage(tk.Frame):
     
      def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#183642")
        self.controller = controller

        self.controller.title('Banco CHQ')
        self.controller.state('zoomed')

        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45),
                                 fg='white',
                                 background= '#183642')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height =4, bg='#183642')
        space_label.pack()

        nome_label = tk.Label(self, 
                                text='Selecione uma ação',
                                font=('Calisto MT',25),
                                bg='#183642',
                                fg='white')
            
        nome_label.pack(pady = 10)
            
            
            
        def add():          
            controller.show_frame('AddPage')
        
            
        
        adicionar_button= tk.Button(self,
                                        text='Adicionar',
                                        command=add,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        adicionar_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
        def remover():
            cpfCliente= tk.StringVar()
            caixa_entrada = tk.Entry(self, 
                                       textvariable=cpfCliente ,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada.focus_set()
            caixa_entrada.pack(ipady = 7)
           
            
            def rem():
                clienteRem = cpfCliente.get()
               
                if controle.rmPessoa(clienteRem):
                
                    top = Toplevel()
                    top.geometry("275x75")
                    top.title('Remover Cliente')
                    Label(top, text= f'O cliente {clienteRem} foi removido', font= ("Calisto MT", 15)).place(x=8, y=25)
                else:
                    top = Toplevel()
                    top.geometry("290x75")
                    top.title('Operacao Invalida')
                    Label(top, text= f'O cliente {clienteRem} nao pode ser removido', font= ("Calisto MT", 15)).place(x=8, y=25)
                    
                
            button = tk.Button(self,
                               
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = rem,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 23,
                                 height = 2)
            button.pack(pady=10)

        remover_button= tk.Button(self,
                                        text='Remover',
                                        command=remover,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        remover_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
        

        def atualizar():
             
            dataAtt= tk.StringVar()
            caixa_entrada = tk.Entry(self, 
                                       textvariable=dataAtt,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada.focus_set()
            caixa_entrada.pack(ipady = 7)
            
            def att():
                data = dataAtt.get()
                controle.atualizarPagamento(data)
                
                top = Toplevel()
                top.geometry("275x75")
                top.title('Atualizar Pagamentos')
                Label(top, text= f'Pagamentos do dia {data} atualizados', font= ("Calisto MT", 15)).place(x=8, y=25)
                
                
            
            button = tk.Button(self,
                                
                                    bg = "#cbc5ea",
                                    text= 'Enter',
                                    command = att,
                                    relief='raised',
                                    borderwidth= 3,
                                    width = 22,
                                    height = 2)
            button.pack(pady=10)
             

        attPag_button= tk.Button(self,
                                        text='Atualizar Pagamentos',
                                        command=atualizar,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        attPag_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
        
        def sair():
            controller.show_frame('StartPage')
            
        def checar():
            pedidos = controle.mostrarPedidos()
                
            top = Toplevel()
            top.geometry("300x500")
            top.title('Atualizar Pagamentos')
            Label(top, text= f'{pedidos}', font= ("Calisto MT", 15)).place(x=8, y=25)
            
            

        checarCred_button= tk.Button(self,
                                        text='Checar pedidos de crédito',
                                        command=checar,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        checarCred_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
        def attSenha():
            
            cpf_label = tk.Label(self, 
                               text='Digite o CPF/CNPJ',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
            cpf_label.pack(pady = 8)
            
            cpfCliente= tk.StringVar()
            caixa_entrada = tk.Entry(self, 
                                       textvariable=cpfCliente ,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada.focus_set()
            caixa_entrada.pack(ipady = 7)
            
            novaSenha_label = tk.Label(self, 
                               text='Nova Senha',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
            novaSenha_label.pack(pady = 8)
            
            novaSenha= tk.StringVar()
            caixa_entrada = tk.Entry(self, 
                                       textvariable= novaSenha,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada.focus_set()
            caixa_entrada.pack(ipady = 7)
            
            def senhaNova():
                
                cpf = cpfCliente.get()
                senha = novaSenha.get()
                
                controle.atualizarSenha(cpf, senha)
                top = Toplevel()
                top.geometry("265x75")
                top.title('Senha Att')
                Label(top, text= 'Senha atualizada', font= ("Calisto MT", 15)).place(x=8, y=25)
                
            button = tk.Button(self,
                                
                                    bg = "#cbc5ea",
                                    text= 'Enter',
                                    command = senhaNova,
                                    relief='raised',
                                    borderwidth= 3,
                                    width = 22,
                                    height = 2)
            button.pack(pady=10)
                    

        atualizarSenha_button= tk.Button(self,
                                        text='Atualizar Senha',
                                        command= attSenha,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        atualizarSenha_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        




        sair_button= tk.Button(self,
                                        text='Sair',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        sair_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
     
class AddPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#183642")
        self.controller = controller

        self.controller.title('Banco CHQ')
        self.controller.state('zoomed')
        
        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45),
                                 fg= '#eaeaea',
                                 background= '#183642')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
        selecao_label= tk.Label(self,
                                        text='Cadastre os dados',
                                        font=('Calisto MT',25),
                                        fg='white',
                                        bg='#183642'
                                        )
        selecao_label.pack(fill='x')
        
        nome_label = tk.Label(self, 
                               text='Nome',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 8)

        nome = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= nome,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)
        
       
        
        
        nome_label = tk.Label(self, 
                               text='Tipo',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 8)

        tipo = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= tipo,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)
        
        
        
        nome_label = tk.Label(self, 
                               text='Digite novo CPF/CNPJ',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 8)

        meuCPF = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= meuCPF,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)
        
      
        
        
        
        
        nome_label = tk.Label(self, 
                               text='Endereco',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 8)

        endereco = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= endereco,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)
        
        
        
        nome_label = tk.Label(self, 
                               text='Telefone',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 8)

        tel = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= tel,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_nome.focus_set()
        caixa_entrada_nome.pack(ipady = 7)
        
       
        
    
        senha_label = tk.Label(self, 
                               text='Digite sua senha',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        senha_label.pack(pady = 8)
        
        
        minhanovaSenha = tk.StringVar()
        caixa_entrada_senha = tk.Entry(self, 
                                       textvariable= minhanovaSenha,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
        caixa_entrada_senha.focus_set()
        caixa_entrada_senha.pack(ipady = 7)
        
        def addCliente():
            novoNome = nome.get()
            novoTipo= tipo.get()
            novaKey= meuCPF.get()
            novoEndereco= endereco.get()
            novaSenha = minhanovaSenha.get()
            novoTelefone= tel.get()
            
            controle.addPessoa(novoNome, novaKey, novoEndereco, novoTelefone, novaSenha, novoTipo)
                  
            controller.show_frame('GerenciaPage')
            top = Toplevel()
            top.geometry("280x75")
            top.title('Credito')
            Label(top, text= f'Cliente {novoNome} foi adicionado', font= ("Calisto MT", 15)).place(x=8, y=25)
        
        
        adicionar_button= tk.Button(self,
                                        text='Adicionar',
                                        command= addCliente,
                                        relief='raised',
                                        borderwidth=3,
                                        width=23,
                                        height=3
                                        )
        adicionar_button.pack(pady=5)
        
     