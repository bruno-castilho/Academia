from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from admin import Admin
from professores import Professores
from aluno import Aluno


class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)

class InterfaceAdmin:
    def __init__(self, sessao):
        self.sessao = sessao
        self.admin = Admin()
        self.professor = Professores()
        self.aluno = Aluno()

        self.window = self.main()
        self.layout()
        self.frame = self.professores(self.professor.listaProfessores())



        self.window.mainloop()
         
    def rgb(self, rgb):
        return "#%02x%02x%02x" % rgb 

    def main(self):
        main = Tk()
        main.title("Academia fica forte")
        main.geometry("1000x1000")

        return main

    def layout(self):
        buttons = Frame(self.window)
        buttons.pack(side="top")

        Button(buttons, text='Professores', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.professores, self.professor.listaProfessores())).grid(row=0,column=0, padx= 2, pady=20)
        Button(buttons, text='Alunos', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.alunos, self.aluno.listaAlunos())).grid(row=0,column=1, padx= 2, pady=20)
        Button(buttons, text='Admins',  width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.admins, self.admin.listaAdmins())).grid(row=0,column=2, padx= 2, pady=20)
        Button(buttons, text='Cadastrar Aluno', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.cadastrarAluno)).grid(row=0,column=3, padx=2, pady=20)
        Button(buttons, text='Cadastrar Professor', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.cadastrarProfessor)).grid(row=0,column=4, padx= 2, pady=20)
        Button(buttons, text='Cadastrar Admin', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.cadastrarAdmin)).grid(row=0,column=5, padx=2, pady=20)

    def alunos(self, alunos):
        
        container = Frame(self.window, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        self.find(container, self.alunos, self.aluno.filtrar)

        #cabeçalho

        cabecalho = Frame(container, bg=self.rgb((90, 90, 90)))
        cabecalho.pack(side="top")

        Label(cabecalho, text="Nome", width=34, bd=5).grid(row=0 ,column=0, padx= 3, pady=3)
        Label(cabecalho, text="Email", width=34, bd=5).grid(row=0, column=1, padx=3, pady=3)
        Label(cabecalho, text="Idade", width=8, bd=5).grid(row=0, column=2, padx= 3, pady=3)
        Label(cabecalho, text="Altura", width=8, bd=5).grid(row=0, column=3, padx= 3, pady=3)
        Label(cabecalho, text="Peso", width=8, bd=5).grid(row=0 , column=4, padx= 3, pady=3)
        Label(cabecalho, text="", width=8, bd=5, bg=self.rgb((90, 90, 90))).grid(row=0, column=5, padx=3, pady=3)

        #lista
        canvas = Canvas(container, height=1000)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y") 


        tabela = Frame(canvas, bg=self.rgb((90, 90, 90)))


        tabela.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
   

        
        for i, aluno in enumerate(alunos):
            Label(tabela, text=aluno["nome"], width=34, bd=5).grid(row=i,column=0, padx= 3, pady=3)
            Label(tabela, text=aluno["email"], width=34, bd=5).grid(row=i,column=1, padx=3, pady=3)
            Label(tabela, text=aluno["idade"], width=8, bd=5).grid(row=i,column=2, padx= 3, pady=3)
            Label(tabela, text=str(aluno["altura"])+"m", width=8, bd=5).grid(row=i,column=3, padx= 3, pady=3)
            Label(tabela, text=str(aluno["peso"])+"kg", width=8, bd=5).grid(row=i,column=4, padx= 3, pady=3)
            Button(tabela, text='EDITAR', width= 4, bg=self.rgb((0, 255, 155)), bd=3, command=Callback(self.reload, self.editarAluno, aluno["id"])).grid(row=i,column=5, padx= 3, pady=3)


        
        canvas.create_window((0, 0), window=tabela, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        return container

    def professores(self, professores): 
        container = Frame(self.window, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        self.find(container, self.professores, self.professor.filtrar)

        #cabeçalho
        cabecalho = Frame(container, bg=self.rgb((90, 90, 90)))
        cabecalho.pack(side="top")

        Label(cabecalho, text="Nome", width=34, bd=5).grid(row=0 ,column=0, padx= 3, pady=3)
        Label(cabecalho, text="E-mail", width=34, bd=5).grid(row=0, column=1, padx=3, pady=3)
        Label(cabecalho, text="Usuário", width=18, bd=5).grid(row=0, column=2, padx= 3, pady=3)
        Label(cabecalho, text="Idade", width=8, bd=5).grid(row=0, column=3, padx= 3, pady=3)
        Label(cabecalho, text="", width=8, bd=5, bg=self.rgb((90, 90, 90))).grid(row=0, column=4, padx=3, pady=3)


        #lista
        canvas = Canvas(container, height=1000)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y") 


        tabela = Frame(canvas, bg=self.rgb((90, 90, 90)))


        tabela.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        
        for i, professor in enumerate(professores):
            Label(tabela, text=professor["nome"], width=34, bd=5).grid(row=i,column=0, padx= 3, pady=3)
            Label(tabela, text=professor["email"], width=34, bd=5).grid(row=i,column=1, padx=3, pady=3)
            Label(tabela, text=professor["usuario"], width=18, bd=5).grid(row=i,column=2, padx= 3, pady=3)
            Label(tabela, text=professor["idade"], width=8, bd=5).grid(row=i,column=3, padx= 3, pady=3)
            Button(tabela, text='EDITAR', width= 4, bg=self.rgb((0, 255, 155)), bd=3, command=Callback(self.reload, self.editarProfessor , professor["id"])).grid(row=i,column=4, padx= 3, pady=3)



        
        canvas.create_window((0, 0), window=tabela, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        

        return container

    def admins(self, admins):
        container = Frame(self.window, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        self.find(container, self.admins, self.admin.filtrar)

        #cabeçalho
        cabecalho = Frame(container, bg=self.rgb((90, 90, 90)))
        cabecalho.pack(side="top")

        Label(cabecalho, text="Nome", width=32, bd=5).grid(row=0 ,column=0, padx= 3, pady=3)
        Label(cabecalho, text="E-mail", width=32, bd=5).grid(row=0, column=1, padx= 3, pady=3)
        Label(cabecalho, text="Usuário", width=32, bd=5).grid(row=0, column=2, padx= 3, pady=3)
        Label(cabecalho, text="", width=8, bd=5, bg=self.rgb((90, 90, 90))).grid(row=0, column=4, padx=3, pady=3)


        #lista
        canvas = Canvas(container, height=1000)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y") 


        tabela = Frame(canvas, bg=self.rgb((90, 90, 90)))


        tabela.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        for i, admin in enumerate(admins):
            Label(tabela, text=admin["nome"], width=32, bd=5).grid(row=i,column=0, padx= 3, pady=3)
            Label(tabela, text=admin["email"], width=32, bd=5).grid(row=i,column=1, padx= 3, pady=3)
            Label(tabela, text=admin["usuario"], width=32, bd=5).grid(row=i,column=2, padx= 3, pady=3)
            Button(tabela, text='EDITAR', width= 4, bg=self.rgb((0, 255, 155)), bd=3, command=Callback(self.reload, self.editarAdmin, admin["id"])).grid(row=i,column=4, padx= 3, pady=3)



        
        canvas.create_window((0, 0), window=tabela, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)                                

        return container

    def cadastrarAluno(self):
        atuacoes = self.aluno.professoresAtuacoes()

        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Cadastrar Aluno", font=('bold'))
        titulo.pack(side="top", pady=20)

        form = Frame(container)
        form.pack(side="top")

        #entradas
        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        inputNome = Entry(form, width=50)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="Email:").grid(row=0 ,column=1, padx= 50, pady=3)
        inputEmail = Entry(form, width=50)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)

     
        Label(form, text="Altura:").grid(row=2 ,column=0, padx= 50, pady=3)  
        inputAltura = Entry(form, width=50)
        inputAltura.grid(row=3,column=0, padx= 50, pady=5)


        Label(form, text="Peso:").grid(row=2,column=1, padx= 50, pady=3)
        inputPeso= Entry(form, width=50)
        inputPeso.grid(row=3,column=1, padx= 50, pady=5)
        
        
        #calendario
        Label(form, text="Data de nascimento:").grid(row=4 ,column=0, padx= 50, pady=3)

        today = date.today()
        year = today.strftime("%Y")
        day = today.strftime("%d")
        month = today.strftime("%m")
        
        cal = DateEntry(form,width=49,bg="darkblue",fg="white",year=int(year), month=int(month), day=int(day))
        cal.grid(row=5, column=0, padx= 50, pady=5)

        #Matricula
        
        natacao = IntVar()
        Checkbutton(form, text="Natação", variable=natacao).grid(row=4, column=1, sticky=W, padx= 50, pady=3)
        professorNatacao = ttk.Combobox(form, values=atuacoes["Natação"], width=49)
        professorNatacao.grid(row=5, column=1, sticky=W, padx= 50, pady=3)


        danca = IntVar()
        Checkbutton(form, text="Dança", variable=danca).grid(row=6, column=0, sticky=W, padx= 50, pady=3)
        professorDanca = ttk.Combobox(form, values=atuacoes["Dança"], width=49)
        professorDanca.grid(row=7, column=0, sticky=W, padx= 50, pady=3)


        yoga = IntVar()
        Checkbutton(form, text="Yoga", variable=yoga).grid(row=6, column=1, sticky=W, padx= 50, pady=3)
        professorYoga = ttk.Combobox(form, values=atuacoes["Yoga"], width=49)
        professorYoga.grid(row=7, column=1, sticky=W, padx= 50, pady=3)


        musculacao = IntVar()
        Checkbutton(form, text="Musculação", variable=musculacao).grid(row=8, column=0, sticky=W, padx= 50, pady=3)
        professorMusculacao = ttk.Combobox(form, values=atuacoes["Musculação"], width=49)
        professorMusculacao.grid(row=9, column=0, sticky=W, padx= 50, pady=3)

        crossfit = IntVar()
        Checkbutton(form, text="Crossfit", variable=crossfit).grid(row=8, column=1, sticky=W, padx= 50, pady=3)
        professorCrossfit = ttk.Combobox(form, values=atuacoes["Crossfit"], width=49)
        professorCrossfit.grid(row=9, column=1, sticky=W, padx= 50, pady=3)


        muay_thai = IntVar()
        Checkbutton(form, text="Muay Thai", variable=muay_thai).grid(row=10, column=0, sticky=W, padx= 50, pady=3)   
        professorMuayThai = ttk.Combobox(form, values=atuacoes["Muay Thai"], width=49)
        professorMuayThai.grid(row=11, column=0, sticky=W, padx= 50, pady=3)

        jiu_jitsu = IntVar()
        Checkbutton(form, text="Jiu Jitsu", variable=jiu_jitsu).grid(row=10, column=1, sticky=W, padx= 50, pady=3)
        professorJiuJitsu = ttk.Combobox(form, values=atuacoes["Jiu Jitsu"], width=49)
        professorJiuJitsu.grid(row=11, column=1, sticky=W, padx= 50, pady=3)


        boxe = IntVar()
        Checkbutton(form, text="Boxe", variable=boxe).grid(row=12, column=0, sticky=W, padx= 50, pady=3)
        professorBoxe = ttk.Combobox(form, values=atuacoes["Boxe"], width=49)
        professorBoxe.grid(row=13, column=0, sticky=W, padx= 50, pady=3)

        #enviar
        enviar = Button(container, text='Enviar', bg=self.rgb((0, 255, 155)), font=('bold'), width= 15, command= lambda: self.janelaMensagem(self.aluno.cadastrar({
                                                                                                                        "inputs":{
                                                                                                                                "nome": inputNome.get(),
                                                                                                                                "email": inputEmail.get(),
                                                                                                                                "altura": inputAltura.get(), 
                                                                                                                                "peso": inputPeso.get(), 
                                                                                                                                "nascimento": cal.get()
                                                                                                                                },
                                                                                                                        "matriculas":{
                                                                                                                                   "Natação": natacao.get(),
                                                                                                                                   "Dança": danca.get(),
                                                                                                                                   "Yoga": yoga.get(),
                                                                                                                                   "Musculação": musculacao.get(),
                                                                                                                                   "Crossfit": crossfit.get(),
                                                                                                                                   "Muay Thai": muay_thai.get(),
                                                                                                                                   "Jiu Jitsu": jiu_jitsu.get(),
                                                                                                                                   "Boxe": boxe.get()
                                                                                                                                },
                                                                                                                        "professores":{
                                                                                                                                   "Natação": professorNatacao.get(),
                                                                                                                                   "Dança": professorDanca.get(),
                                                                                                                                   "Yoga": professorYoga.get(),
                                                                                                                                   "Musculação": professorMusculacao.get(),
                                                                                                                                   "Crossfit": professorCrossfit.get(),
                                                                                                                                   "Muay Thai": professorMuayThai.get(),
                                                                                                                                   "Jiu Jitsu": professorJiuJitsu.get(),
                                                                                                                                   "Boxe": professorBoxe.get()
                                                                                                                                },
                                                                                                                        "idsProfessores": atuacoes["ids"]
                                                                                                                        })))    
        enviar.pack(side="top", pady=50)



        return container
    
    def cadastrarProfessor(self):
        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Cadastrar Professor",font=('bold'))
        titulo.pack(side="top", pady=20)


        form = Frame(container)
        form.pack(side="top")

        #entradas
        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        inputNome = Entry(form, width=50)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="Email:").grid(row=0 ,column=1, padx= 50, pady=3)
        inputEmail = Entry(form, width=50)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)
       
        Label(form, text="Usuário:").grid(row=2 ,column=0, padx= 50, pady=3)
        inputUsuario = Entry(form, width=50)
        inputUsuario.grid(row=3,column=0, padx= 50, pady=5)

        Label(form, text="Senha:").grid(row=2,column=1, padx= 50, pady=3)
        inputSenha = Entry(form, width=50)
        inputSenha.grid(row=3,column=1, padx= 50, pady=5)

        Label(form, text="Repita senha:").grid(row=4 ,column=0, padx= 50, pady=3)
        inputRepetirSenha = Entry(form, width=50)
        inputRepetirSenha.grid(row=5,column=0, padx= 50, pady=5)

        #calendario
        Label(form, text="Data de nascimeto:").grid(row=4,column=1, padx= 50, pady=3)

        today = date.today()
        year = today.strftime("%Y")
        day = today.strftime("%d")
        month = today.strftime("%m")
        
        cal = DateEntry(form,width=49,bg="darkblue",fg="white",year=int(year), month=int(month), day=int(day))
        cal.grid(row=5, column=1, padx= 50, pady=5)


        #Especialidades
        Label(form, text="Area de atuação:").grid(row=6,column=0, padx= 50, pady=3)
        
        checkbox = Frame(form)
        checkbox.grid(row=7,column=0, padx= 50, pady=5)

        natacao = IntVar()
        Checkbutton(checkbox, text="Natação", variable=natacao).grid(row=0, column=0, sticky=W)

        danca = IntVar()
        Checkbutton(checkbox, text="Dança", variable=danca).grid(row=0, column=1, sticky=W)

        yoga = IntVar()
        Checkbutton(checkbox, text="Yoga", variable=yoga).grid(row=0, column=2, sticky=W)

        musculacao = IntVar()
        Checkbutton(checkbox, text="Musculação", variable=musculacao).grid(row=0, column=3, sticky=W)

        crossfit = IntVar()
        Checkbutton(checkbox, text="Crossfit", variable=crossfit).grid(row=1, column=0, sticky=W)

        muay_thai = IntVar()
        Checkbutton(checkbox, text="Muay Thai", variable=muay_thai).grid(row=1, column=1, sticky=W)

        jiu_jitsu = IntVar()
        Checkbutton(checkbox, text="Jiu Jitsu", variable=jiu_jitsu).grid(row=1, column=2, sticky=W)

        boxe = IntVar()
        Checkbutton(checkbox, text="Boxe", variable=boxe).grid(row=1, column=3, sticky=W)


        #enviar
        enviar = Button(container, text='Enviar', bg=self.rgb((0, 255, 155)), font=('bold'), width= 15, command= lambda: self.janelaMensagem(self.professor.cadastrar({
                                                                                                                        "nome": inputNome.get(),
                                                                                                                        "email": inputEmail.get(),
                                                                                                                        "usuario": inputUsuario.get(), 
                                                                                                                        "senha": inputSenha.get(), 
                                                                                                                        "repetirsenha": inputRepetirSenha.get(),
                                                                                                                        "nascimento": cal.get(),
                                                                                                                        "atuacoes":{"Natação": natacao.get(),
                                                                                                                                   "Dança": danca.get(),
                                                                                                                                   "Yoga": yoga.get(),
                                                                                                                                   "Musculação": musculacao.get(),
                                                                                                                                   "Crossfit": crossfit.get(),
                                                                                                                                   "Muay Thai": muay_thai.get(),
                                                                                                                                   "Jiu Jitsu": jiu_jitsu.get(),
                                                                                                                                   "Boxe": boxe.get()
                                                                                                                                }
                                                                                                                        })))    
        enviar.pack(side="top", pady=50)

        

        return container

    def cadastrarAdmin(self):
        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Cadastrar Admin", font=('bold'))
        titulo.pack(side="top", pady=20)
 
        form = Frame(container)
        form.pack(side="top")

        #entradas
        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        inputNome = Entry(form, width=50)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="E-mail:").grid(row=0 ,column=1, padx= 50, pady=3)
        inputEmail = Entry(form, width=50)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)

        Label(form, text="Usuário:").grid(row=2 ,column=0, padx= 50, pady=3)
        inputUsuario = Entry(form, width=50)
        inputUsuario.grid(row=3,column=0, padx= 50, pady=5)
        
        Label(form, text="Senha:").grid(row=2 ,column=1, padx= 50, pady=3) 
        inputSenha = Entry(form, width=50)
        inputSenha.grid(row=3,column=1, padx= 50, pady=5)

        Label(form, text="Repita a senha:").grid(row=4,column=0, padx= 50, pady=3)
        inputRepetirSenha= Entry(form, width=50)
        inputRepetirSenha.grid(row=5,column=0, padx= 50, pady=5)

        #enviar
        enviar = Button(container, text='Enviar', bg=self.rgb((0, 255, 155)), font=('bold'), width= 15, command= lambda: self.janelaMensagem(self.admin.cadastrar({
                                                                                                                        "nome": inputNome.get(),
                                                                                                                        "email": inputEmail.get(),
                                                                                                                        "usuario": inputUsuario.get(), 
                                                                                                                        "senha": inputSenha.get(), 
                                                                                                                        "repetirsenha": inputRepetirSenha.get(),
                                                                                                                        })))    
        enviar.pack(side="top", pady=50)
        
        return container
   
    def editarAdmin(self, id):
        usuario = self.admin.adminId(id)
        
        container = Frame(self.window)
        container.pack(side="top")

        #titulo
        titulo = Label(container, text="Editar Admin", font=('bold'))
        titulo.pack(side="top", pady=20)
 
        #entradas
        form = Frame(container)
        form.pack(side="top")

        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        stringNome = StringVar(value=usuario["nome"])
        inputNome = Entry(form, width=50, textvariable=stringNome)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="E-mail:").grid(row=0 ,column=1, padx= 50, pady=3)
        stringEmail = StringVar(value=usuario["email"])
        inputEmail = Entry(form, width=50, textvariable=stringEmail)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)

        Label(form, text="Usuário:").grid(row=2 ,column=0, padx= 50, pady=3)
        stringUsuario = StringVar(value=usuario["usuario"])
        inputUsuario = Entry(form, width=50, textvariable=stringUsuario)
        inputUsuario.grid(row=3,column=0, padx= 50, pady=5)
        
        Label(form, text="Senha:").grid(row=2 ,column=1, padx= 50, pady=3) 
        stringSenha = StringVar(value=usuario["senha"])
        inputSenha = Entry(form, width=50, textvariable=stringSenha)
        inputSenha.grid(row=3,column=1, padx= 50, pady=5)

        Label(form, text="Repita a senha:").grid(row=4,column=0, padx= 50, pady=3)
        stringRepetirSenha = StringVar(value=usuario["senha"])
        inputRepetirSenha = Entry(form, width=50, textvariable=stringRepetirSenha)
        inputRepetirSenha.grid(row=5,column=0, padx= 50, pady=5)

        #botoes
        botoes = Frame(container)
        botoes.pack(side="top", pady=50)

        cancelar = Button(botoes, text="Cancelar", font=('bold'), width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.admins, self.admin.listaAdmins()))
        cancelar.grid(row=0,column=0, padx=5)


        deletar = Button(botoes, text="Deletar", font=('bold'), width= 15, bg=self.rgb((255, 55, 55)), command= lambda: self.janelaDeletar(id, self.admin.deletar, self.admins, self.admin.listaAdmins))
        deletar.grid(row=0,column=1, padx=5)

        enviar = Button(botoes, text='Enviar', font=('bold'), width= 15,  bg=self.rgb((0, 255, 155)),command= lambda: self.janelaMensagem(self.admin.editar(id,
                                                                                                                        {
                                                                                                                        "nome": inputNome.get(),
                                                                                                                        "email": inputEmail.get(),
                                                                                                                        "usuario": inputUsuario.get(), 
                                                                                                                        "senha": inputSenha.get(), 
                                                                                                                        "repetirsenha": inputRepetirSenha.get(),
                                                                                                                        })))    
        enviar.grid(row=0,column=2, padx=5)
        


        
        return container

    def editarProfessor(self, id):
        professor = self.professor.professorId(id)

        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Editar Professor",font=('bold'))
        titulo.pack(side="top", pady=20)


        form = Frame(container)
        form.pack(side="top")

        #entradas
        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        stringNome = StringVar(value=professor["nome"])
        inputNome = Entry(form, width=50, textvariable=stringNome)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="Email:").grid(row=0 ,column=1, padx= 50, pady=3)
        stringEmail = StringVar(value=professor["email"])
        inputEmail = Entry(form, width=50, textvariable=stringEmail)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)
       
        Label(form, text="Usuário:").grid(row=2 ,column=0, padx= 50, pady=3)
        stringUsuario = StringVar(value=professor["usuario"])
        inputUsuario = Entry(form, width=50, textvariable=stringUsuario)
        inputUsuario.grid(row=3,column=0, padx= 50, pady=5)

        Label(form, text="Senha:").grid(row=2,column=1, padx= 50, pady=3)
        stringSenha = StringVar(value=professor["senha"])
        inputSenha = Entry(form, width=50, textvariable=stringSenha)
        inputSenha.grid(row=3,column=1, padx= 50, pady=5)

        Label(form, text="Repita senha:").grid(row=4 ,column=0, padx= 50, pady=3)
        stringRepetirSenha = StringVar(value=professor["senha"])
        inputRepetirSenha = Entry(form, width=50, textvariable=stringRepetirSenha)
        inputRepetirSenha.grid(row=5,column=0, padx= 50, pady=5)

        #calendario
        Label(form, text="Data de nascimeto:").grid(row=4,column=1, padx= 50, pady=3)
        
        cal = DateEntry(form,width=49,bg="darkblue",fg="white",year=professor["nascimento"]["ano"], month=professor["nascimento"]["mes"], day=professor["nascimento"]["dia"])
        cal.grid(row=5, column=1, padx= 50, pady=5)


        #Especialidades
        Label(form, text="Area de atuação:").grid(row=6,column=0, padx= 50, pady=3)
        
        checkbox = Frame(form)
        checkbox.grid(row=7,column=0, padx= 50, pady=5)

        natacao = IntVar(value=professor["atuacoes"]["Natação"])
        Checkbutton(checkbox, text="Natação", variable=natacao).grid(row=0, column=0, sticky=W)

        danca = IntVar(value=professor["atuacoes"]["Dança"])
        Checkbutton(checkbox, text="Dança", variable=danca).grid(row=0, column=1, sticky=W)

        yoga = IntVar(value=professor["atuacoes"]["Yoga"])
        Checkbutton(checkbox, text="Yoga", variable=yoga).grid(row=0, column=2, sticky=W)

        musculacao = IntVar(value=professor["atuacoes"]["Musculação"])
        Checkbutton(checkbox, text="Musculação", variable=musculacao).grid(row=0, column=3, sticky=W)

        crossfit = IntVar(value=professor["atuacoes"]["Crossfit"])
        Checkbutton(checkbox, text="Crossfit", variable=crossfit).grid(row=1, column=0, sticky=W)

        muay_thai = IntVar(value=professor["atuacoes"]["Muay Thai"])
        Checkbutton(checkbox, text="Muay Thai", variable=muay_thai).grid(row=1, column=1, sticky=W)

        jiu_jitsu = IntVar(value=professor["atuacoes"]["Jiu Jitsu"])
        Checkbutton(checkbox, text="Jiu Jitsu", variable=jiu_jitsu).grid(row=1, column=2, sticky=W)

        boxe = IntVar(value=professor["atuacoes"]["Boxe"])
        Checkbutton(checkbox, text="Boxe", variable=boxe).grid(row=1, column=3, sticky=W)
        


        #botoes
        botoes = Frame(container)
        botoes.pack(side="top", pady=50)

        cancelar = Button(botoes, text="Cancelar", font=('bold'), width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.professores, self.professor.listaProfessores()))
        cancelar.grid(row=0,column=0, padx=5)


        deletar = Button(botoes, text="Deletar", font=('bold'), width= 15, bg=self.rgb((255, 55, 55)), command= lambda: self.janelaDeletar(id, self.professor.deletar, self.professores,self.professor.listaProfessores))
        deletar.grid(row=0,column=1, padx=5)

        enviar = Button(botoes, text='Enviar', font=('bold'), width= 15,  bg=self.rgb((0, 255, 155)),command= lambda: self.janelaMensagem(self.professor.editar(id,{
                                                                                                                        "nome": inputNome.get(),
                                                                                                                        "email": inputEmail.get(),
                                                                                                                        "usuario": inputUsuario.get(), 
                                                                                                                        "senha": inputSenha.get(), 
                                                                                                                        "repetirsenha": inputRepetirSenha.get(),
                                                                                                                        "nascimento": cal.get(),
                                                                                                                        "atuacoes":{"Natação": natacao.get(),
                                                                                                                                   "Dança": danca.get(),
                                                                                                                                   "Yoga": yoga.get(),
                                                                                                                                   "Musculação": musculacao.get(),
                                                                                                                                   "Crossfit": crossfit.get(),
                                                                                                                                   "Muay Thai": muay_thai.get(),
                                                                                                                                   "Jiu Jitsu": jiu_jitsu.get(),
                                                                                                                                   "Boxe": boxe.get()
                                                                                                                                }
                                                                                                                        })))    
        enviar.grid(row=0,column=2, padx=5)
        

        return container
   
    def editarAluno(self, id):
        aluno = self.aluno.alunoId(id)
        atuacoes = self.aluno.professoresAtuacoes()


        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Editar Aluno", font=('bold'))
        titulo.pack(side="top", pady=20)

        form = Frame(container)
        form.pack(side="top")

        #entradas
        Label(form, text="Nome:").grid(row=0 ,column=0, padx= 50, pady=3)
        stringNome = StringVar(value=aluno["nome"])
        inputNome = Entry(form, width=50, textvariable=stringNome)
        inputNome.grid(row=1,column=0, padx= 50, pady=5)

        Label(form, text="Email:").grid(row=0 ,column=1, padx= 50, pady=3)
        stringEmail = StringVar(value=aluno["email"])
        inputEmail = Entry(form, width=50, textvariable=stringEmail)
        inputEmail.grid(row=1,column=1, padx= 50, pady=5)

     
        Label(form, text="Altura:").grid(row=2 ,column=0, padx= 50, pady=3)  
        stringAltura = StringVar(value=aluno["altura"])
        inputAltura = Entry(form, width=50, textvariable=stringAltura)
        inputAltura.grid(row=3,column=0, padx= 50, pady=5)


        Label(form, text="Peso:").grid(row=2,column=1, padx= 50, pady=3)
        stringPeso = StringVar(value=aluno["peso"])
        inputPeso= Entry(form, width=50, textvariable=stringPeso)
        inputPeso.grid(row=3,column=1, padx= 50, pady=5)
        
        
        #calendario
        Label(form, text="Data de nascimento:").grid(row=4 ,column=0, padx= 50, pady=3)
        
        cal = DateEntry(form,width=49,bg="darkblue",fg="white",year=int(aluno["nascimento"]["ano"]), month=int(aluno["nascimento"]["mes"]), day=int(aluno["nascimento"]["dia"]))
        cal.grid(row=5, column=0, padx= 50, pady=5)

        #Matricula
        
        natacao = IntVar(value=aluno["matriculas"]["Natação"])
        Checkbutton(form, text="Natação", variable=natacao).grid(row=4, column=1, sticky=W, padx= 50, pady=3)
        professorNatacao = ttk.Combobox(form, values=atuacoes["Natação"], width=49)
        professorNatacao.grid(row=5, column=1, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Natação"] != "":
            professorNatacao.current(atuacoes["Natação"].index(aluno["professores"]["Natação"]))

        danca = IntVar(value=aluno["matriculas"]["Dança"])
        Checkbutton(form, text="Dança", variable=danca).grid(row=6, column=0, sticky=W, padx= 50, pady=3)
        professorDanca = ttk.Combobox(form, values=atuacoes["Dança"], width=49)
        professorDanca.grid(row=7, column=0, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Dança"] != "":
            professorDanca.current(atuacoes["Dança"].index(aluno["professores"]["Dança"]))



        yoga = IntVar(value=aluno["matriculas"]["Yoga"])
        Checkbutton(form, text="Yoga", variable=yoga).grid(row=6, column=1, sticky=W, padx= 50, pady=3)
        professorYoga = ttk.Combobox(form, values=atuacoes["Yoga"], width=49)
        professorYoga.grid(row=7, column=1, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Yoga"] != "":
            professorYoga.current(atuacoes["Yoga"].index(aluno["professores"]["Yoga"]))



        musculacao = IntVar(value=aluno["matriculas"]["Musculação"])
        Checkbutton(form, text="Musculação", variable=musculacao).grid(row=8, column=0, sticky=W, padx= 50, pady=3)
        professorMusculacao = ttk.Combobox(form, values=atuacoes["Musculação"], width=49)
        professorMusculacao.grid(row=9, column=0, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Musculação"] != "":
            professorMusculacao.current(atuacoes["Musculação"].index(aluno["professores"]["Musculação"]))

        

        crossfit = IntVar(value=aluno["matriculas"]["Crossfit"])
        Checkbutton(form, text="Crossfit", variable=crossfit).grid(row=8, column=1, sticky=W, padx= 50, pady=3)
        professorCrossfit = ttk.Combobox(form, values=atuacoes["Crossfit"], width=49)
        professorCrossfit.grid(row=9, column=1, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Crossfit"] != "":
            professorCrossfit.current(atuacoes["Crossfit"].index(aluno["professores"]["Crossfit"]))



        muay_thai = IntVar(value=aluno["matriculas"]["Muay Thai"])
        Checkbutton(form, text="Muay Thai", variable=muay_thai).grid(row=10, column=0, sticky=W, padx= 50, pady=3)   
        professorMuayThai = ttk.Combobox(form, values=atuacoes["Muay Thai"], width=49)
        professorMuayThai.grid(row=11, column=0, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Muay Thai"] != "":       
            professorMuayThai.current(atuacoes["Muay Thai"].index(aluno["professores"]["Muay Thai"]))


        jiu_jitsu = IntVar(value=aluno["matriculas"]["Jiu Jitsu"])
        Checkbutton(form, text="Jiu Jitsu", variable=jiu_jitsu).grid(row=10, column=1, sticky=W, padx= 50, pady=3)
        professorJiuJitsu = ttk.Combobox(form, values=atuacoes["Jiu Jitsu"], width=49)
        professorJiuJitsu.grid(row=11, column=1, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Jiu Jitsu"] != "":
            professorJiuJitsu.current(atuacoes["Jiu Jitsu"].index(aluno["professores"]["Jiu Jitsu"]))



        boxe = IntVar(value=aluno["matriculas"]["Boxe"])
        Checkbutton(form, text="Boxe", variable=boxe).grid(row=12, column=0, sticky=W, padx= 50, pady=3)
        professorBoxe = ttk.Combobox(form, values=atuacoes["Boxe"], width=49)
        professorBoxe.grid(row=13, column=0, sticky=W, padx= 50, pady=3)
        if aluno["professores"]["Boxe"] != "":
            professorBoxe.current(atuacoes["Boxe"].index(aluno["professores"]["Boxe"]))


        
        #botoes
        botoes = Frame(container)
        botoes.pack(side="top", pady=50)

        cancelar = Button(botoes, text="Cancelar", font=('bold'), width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.alunos, self.aluno.listaAlunos()))
        cancelar.grid(row=0,column=0, padx=5)


        deletar = Button(botoes, text="Deletar", font=('bold'), width= 15, bg=self.rgb((255, 55, 55)), command= lambda: self.janelaDeletar(id, self.aluno.deletar, self.alunos,self.aluno.listaAlunos))
        deletar.grid(row=0,column=1, padx=5)

        enviar = Button(botoes, text='Enviar', font=('bold'), width= 15,  bg=self.rgb((0, 255, 155)),command= lambda: self.janelaMensagem(self.aluno.editar(id,{
                                                                                                                        "inputs":{
                                                                                                                                "nome": inputNome.get(),
                                                                                                                                "email": inputEmail.get(),
                                                                                                                                "altura": inputAltura.get(), 
                                                                                                                                "peso": inputPeso.get(), 
                                                                                                                                "nascimento": cal.get()
                                                                                                                                },
                                                                                                                        "matriculas":{
                                                                                                                                   "Natação": natacao.get(),
                                                                                                                                   "Dança": danca.get(),
                                                                                                                                   "Yoga": yoga.get(),
                                                                                                                                   "Musculação": musculacao.get(),
                                                                                                                                   "Crossfit": crossfit.get(),
                                                                                                                                   "Muay Thai": muay_thai.get(),
                                                                                                                                   "Jiu Jitsu": jiu_jitsu.get(),
                                                                                                                                   "Boxe": boxe.get()
                                                                                                                                },
                                                                                                                        "professores":{
                                                                                                                                   "Natação": professorNatacao.get(),
                                                                                                                                   "Dança": professorDanca.get(),
                                                                                                                                   "Yoga": professorYoga.get(),
                                                                                                                                   "Musculação": professorMusculacao.get(),
                                                                                                                                   "Crossfit": professorCrossfit.get(),
                                                                                                                                   "Muay Thai": professorMuayThai.get(),
                                                                                                                                   "Boxe": professorBoxe.get(),
                                                                                                                                   "Jiu Jitsu": professorJiuJitsu.get(),
                                                                                                                               },
                                                                                                                       "idsProfessores": atuacoes["ids"]
                                                                                                                        })))    
        enviar.grid(row=0,column=2, padx=5)
       
        return container
    
    def find(self, frame, func1 , func2):
        container = Frame(frame, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        inputFiltro = Entry(container,  width=101)
        inputFiltro.grid(row=0,column=0, padx= 1, pady=5)

        filtrar = Button(container, text="BUSCAR", bg=self.rgb((100, 0, 255)), width=5, command=lambda: self.reload(func1, func2(inputFiltro.get())))
        filtrar.grid(row=0, column=1, padx=5, pady=5)

    def reload(self, funct, id=None):
        self.frame.destroy()
        if id != None:
            self.frame = funct(id)
        else:
            self.frame = funct()
    
    def janelaMensagem(self, mensagem):
        janela = Tk()
        janela.title("Academia fica forte")
        janela.geometry("450x100")

        Label(janela, text=mensagem, font=('bold')).pack(side="top", pady=20)
        
        Button(janela, text="OK", width=7, command=lambda: janela.destroy()).pack(side="top")


        janela.mainloop()

    def janelaDeletar(self, id, func1, func2, func3):
        janela = Tk()
        janela.title("Academia fica forte")
        janela.geometry("450x100")

        Label(janela, text="Deseja mesmo deletar!", font=('bold')).pack(side="top", pady=20)

        botoes = Frame(janela)
        botoes.pack(side="top")
        
        sim = Button(botoes, text="SIM", width=7, command=lambda:[
                                                        func1(id),
                                                        janela.destroy(), 
                                                        self.reload(func2, func3())])
        sim.grid(row=0,column=0, padx=5)

        nao = Button(botoes, text="NÃO", width=7, command=lambda:[janela.destroy()])
        nao.grid(row=0,column=1, padx=5)


        janela.mainloop()



