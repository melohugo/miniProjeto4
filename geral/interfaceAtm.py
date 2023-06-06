import tkinter as tk               
from tkinter import *
from tkinter import font as tkfont
from controler import *
from interfaceGerente import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.fonte = ("Calisto MT", 45, 'bold')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    
        self.frames = {}
        for F in (StartPage, MenuPage, ManagerPage, GerenciaPage, AddPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

       
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()




class StartPage(tk.Frame):

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

        space_label = tk.Label(self, height =4, bg='#183642')
        space_label.pack()

        nome_label = tk.Label(self, 
                               text='Digite seu CPF/CNPJ',
                               font=('Calisto MT',13),
                               bg='#183642',
                               fg='white')
        
        nome_label.pack(pady = 10)

        meuCPF = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= meuCPF,
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
                                       width=22
                                       )
        
        caixa_entrada_senha.focus_set()
        caixa_entrada_senha.pack(ipady = 7)
  

        def handle_focus_in(_):
            caixa_entrada_senha.configure(fg='black', show='*')

        caixa_entrada_senha.bind('<FocusIn>', handle_focus_in)


        def checaSenha():
            senha = minhaSenha.get() 
            cpf = meuCPF.get()
            if controle.verifCpf(cpf, senha) == True:     
               
               minhaSenha.set('')
               senhaErrada_label['text']=''
               controller.show_frame('MenuPage')
            else:
               senhaErrada_label['text']= 'Senha Errada'

        enter_button = tk.Button(self,
                                 
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = checaSenha,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 24,
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

        def Gerenciar():
            controller.show_frame('ManagerPage')

        gerente_button = tk.Button(self,
                                 text= 'Gerente',
                                 
                                 bg = "#cbc5ea",
                                 relief='raised',
                                 command = Gerenciar,
                                 borderwidth= 3,
                                 width = 24,
                                 height = 2)
        gerente_button.pack(pady=10, expand = True)


      


        
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#183642")
        self.controller = controller

        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45, 'bold'),
                                 fg= 'white',
                                 background= '#183642')
        heading_label.pack(pady=25)

        selecao_label= tk.Label(self,
                                        text='Selecione uma acao',
                                        font=('Calisto MT',25),
                                        fg='white',
                                        bg='#183642'
                                        )
        selecao_label.pack(fill='x')
        def sair():
            controller.show_frame('StartPage')

       
        def deposito():
            valorDep = tk.StringVar()
            caixa_entrada_valor = tk.Entry(self, 
                                       textvariable= valorDep,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada_valor.focus_set()
            caixa_entrada_valor.pack(ipady = 7)
           
            
            def dep():
                valor = valorDep.get()
                
                controle.depositar(float(valor), cpf)
                top = Toplevel()
                top.geometry("280x75")
                top.title('Deposito')
                Label(top, text= f'Deposito de R${valor},00 reais', font= ("Calisto MT", 15)).place(x=8, y=25)
                
            
            button = tk.Button(self,
                               
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = dep,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 23,
                                 height = 2)
            button.pack(pady=10)
            

        depositar_button= tk.Button(self,
                                        text='Depositar',
                                        command=deposito,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        depositar_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
       
            
        def sacar():
            valorSac = tk.StringVar()
            caixa_entrada_valor = tk.Entry(self, 
                                       textvariable= valorSac,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada_valor.focus_set()
            caixa_entrada_valor.pack(ipady = 7)
           
            
            def saqueValor():
                valor = valorSac.get()
                controle.depositar(float(valor), cpf)
                top = Toplevel()
                top.geometry("275x75")
                top.title('Saque')
                Label(top, text= f'Saque de R${valor},00 reais', font= ("Calisto MT", 15)).place(x=8, y=25)
                
            
            button = tk.Button(self,
                               
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = saqueValor,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 22,
                                 height = 2)
            button.pack(pady=10)
            
            

        sacar_button= tk.Button(self,
                                        text='Sacar',
                                        command=sacar,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        sacar_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()
        
    
        def solCred():
            valorCred = tk.StringVar()
            caixa_entrada_valor = tk.Entry(self, 
                                       textvariable= valorCred,
                                       font=('Calisto MT',12),
                                       width=22
                                       )
        
            caixa_entrada_valor.focus_set()
            caixa_entrada_valor.pack(ipady = 7)
           
            
            def credito():
                valor = valorCred.get()
                controle.solCredito(float(valor), cpf)
                top = Toplevel()
                top.geometry("275x75")
                top.title('Credito')
                Label(top, text= f'Pedido de credito de R${valor},00 reais', font= ("Calisto MT", 15)).place(x=8, y=25)
                
            
            button = tk.Button(self,
                               
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = credito,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 22,
                                 height = 2)
            button.pack(pady=10)
            
            
        

        solCredito_button= tk.Button(self,
                                        text='Solicitar credito',
                                        command=solCred,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        solCredito_button.pack(pady=5)
        
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

    

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()