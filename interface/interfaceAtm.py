import tkinter as tk               
from tkinter import *
from tkinter import font as tkfont
from interfaceGerente import *



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.fonte = ("Calisto MT", 45, 'bold')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    
        self.frames = {}
        for F in (StartPage, MenuPage, ManagerPage, GerenciaPage):
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

        meuNome = tk.StringVar()
        caixa_entrada_nome = tk.Entry(self, 
                                       textvariable= meuNome,
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
            if minhaSenha.get() == '1234':     
               #criar funcao que relaciona senha e id do cliente
               minhaSenha.set('')
               senhaErrada_label['text']=''
               controller.show_frame('MenuPage')
            else:
               senhaErrada_label['text']= 'Senha Errada'

        enter_button = tk.Button(self,
                                 font = ('Calisto MT', 10),
                                 bg = "#cbc5ea",
                                 text= 'Enter',
                                 command = checaSenha,
                                 relief='raised',
                                 borderwidth= 3,
                                 width = 22,
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
                                 font=('Calisto MT',10),
                                 bg = "#cbc5ea",
                                 relief='raised',
                                 command = Gerenciar,
                                 borderwidth= 3,
                                 width = 22,
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

        #button_frame = tk.Frame(self,bg='#33334d')
        #button_frame.pack(fill='both',expand=True)

       

        depositar_button= tk.Button(self,
                                        text='Depositar',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        depositar_button.pack(pady=5)

        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()

        sacar_button= tk.Button(self,
                                        text='Sacar',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        sacar_button.pack(pady=5)
        
        space_label = tk.Label(self, height =1, bg='#183642')
        space_label.pack()

        pagProg_button= tk.Button(self,
                                        text='Pagamento programado',
                                        command=sair,
                                        relief='raised',
                                        borderwidth=3,
                                        width=40,
                                        height=3
                                        )
        pagProg_button.pack(pady=5)
        
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