import tkinter as tk                
from tkinter import font as tkfont
from tkinter import *
from modulos.controler import *

controle = Controle()

class ManagerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#313d5a")
        self.controller = controller

        self.controller.title('Banco CHQ')
        self.controller.state('zoomed')

        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45, 'bold'),
                                 fg= 'white',
                                 background= '#313d5a')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height =4, bg='#313d5a')
        space_label.pack()

        nome_label = tk.Label(self, 
                                text='Digite seu ID',
                                font=('Calisto MT',13),
                                bg='#313d5a',
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
                                bg='#313d5a',
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
            Idgerente = Id.get()
            if controle.verifCpf(Idgerente, senha) == True:     
               
               minhaSenha.set('')
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
                                    height = 2)
        enter_button.pack(pady=10)

        senhaErrada_label = tk.Label(self,
                                        text='',
                                        font=('Calisto MT',13),
                                        fg='white',
                                        bg = '#313d5a',
                                        anchor='n')
            
        senhaErrada_label.pack()
            
        space_label = tk.Label(self, height =15, bg = '#313d5a')
        space_label.pack()


        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg= '#313d5a')
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
        tk.Frame.__init__(self, parent, bg= "#313d5a")
        self.controller = controller

        self.controller.title('Banco CHQ')
        self.controller.state('zoomed')

        heading_label = tk.Label(self,
                                 text= 'Banco HCQ',
                                 font= ('Calisto MT', 45, 'bold'),
                                 fg='white',
                                 background= '#313d5a')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height =4, bg='#313d5a')
        space_label.pack()

        nome_label = tk.Label(self, 
                                text='Selecione uma ação',
                                font=('Calisto MT',25),
                                bg='#313d5a',
                                fg='white')
            
        nome_label.pack(pady = 10)

        def sair():
            controller.show_frame('StartPage')
        
        adicionar_button= tk.Button(self,
                                        text='Adicionar',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        adicionar_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#313d5a')
        space_label.pack()

        remover_button= tk.Button(self,
                                        text='Remover',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        remover_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#313d5a')
        space_label.pack()


        checarCred_button= tk.Button(self,
                                        text='Checar pedidos de crédito',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        checarCred_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#313d5a')
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

        space_label = tk.Label(self, height =1, bg='#313d5a')
        space_label.pack()
     

