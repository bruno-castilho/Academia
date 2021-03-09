from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from professores import Professores
from aluno import Aluno
from tkinter.scrolledtext import ScrolledText
from treino import Treino


class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)

class InterfaceProfessor:
    def __init__(self, sessao):
        self.sessao = sessao
        self.treino  = Treino()

        self.aluno = Aluno()
        self.professor = Professores()

        self.window = self.main()
        self.layout()
        self.frame = self.alunos(self.professor.alunos(self.sessao["id"]))

        



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

        Button(buttons, text='Alunos', width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.alunos, self.professor.alunos(self.sessao["id"]))).grid(row=0,column=1, padx= 2, pady=20)
        Button(buttons, text='Perfil',  width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.perfilProfessor, self.sessao["id"])).grid(row=0,column=2, padx= 2, pady=20)

    def alunos(self, alunos):
        
        container = Frame(self.window, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        #self.find(container)

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
            Button(tabela, text='VER', width= 4, bg=self.rgb((0, 255, 155)), bd=3, command=Callback(self.reload, self.perfilAluno, aluno["id"])).grid(row=i,column=5, padx= 3, pady=3)


        
        canvas.create_window((0, 0), window=tabela, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        return container

    
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
            Button(tabela, text='VER', width= 4, bg=self.rgb((0, 255, 155)), bd=3).grid(row=i,column=4, padx= 3, pady=3)



        
        canvas.create_window((0, 0), window=tabela, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)                                

        return container
     
    def find(self, frame, func1 , func2):
        container = Frame(frame, bg=self.rgb((90, 90, 90)))
        container.pack(side="top")

        inputFiltro = Entry(container,  width=101)
        inputFiltro.grid(row=0,column=0, padx= 1, pady=5)

        filtrar = Button(container, text="BUSCAR", bg=self.rgb((100, 0, 255)), width=5, command=lambda: self.reload(func1, func2(inputFiltro.get())))
        filtrar.grid(row=0, column=1, padx=5, pady=5)

    def reload(self, funct, data=None):
        self.frame.destroy()
        if data != None:
            self.frame = funct(data)
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
 
    def perfilAluno(self, id):
        aluno = self.aluno.alunoId(id)

        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Aluno", font=('bold'))
        titulo.pack(side="top", pady=20)

        perfil = Frame(container)
        perfil.pack(side="top")

        nome = Label(perfil)
        nome.grid(row=0 ,column=0, padx= 50, pady=20)
        Label(nome, text="Nome:").pack()
        Label(nome, text=aluno["nome"]).pack()

        email = Label(perfil)
        email.grid(row=0 ,column=1, padx= 50, pady=20)
        Label(email, text="Email:").pack()
        Label(email, text=aluno["email"]).pack()


        altura = Label(perfil)
        altura.grid(row=0 ,column=2, padx= 50, pady=20)
        Label(altura, text="Altura:").pack()
        Label(altura, text=str(aluno["altura"]) + " m").pack()

        peso = Label(perfil)
        peso.grid(row=1 ,column=0, padx= 50, pady=20)
        Label(peso, text="Peso:").pack()
        Label(peso, text=str(aluno["peso"]) + " kg").pack()

        nascimento = Label(perfil)
        nascimento.grid(row=1 ,column=1, padx= 50, pady=20)
        Label(nascimento, text="Nascimento:").pack()
        Label(nascimento, text=f'{aluno["nascimento"]["dia"]}/{aluno["nascimento"]["mes"]}/{aluno["nascimento"]["ano"]}').pack()
        
        idade = Label(perfil)
        idade.grid(row=1 ,column=2, padx= 50, pady=20)
        Label(idade, text="Idade:").pack()
        Label(idade, text=23).pack()



        Button(container, text="Treino", bg=self.rgb((0, 255, 155)), command = lambda: self.abrirTreino(id)).pack(pady=50)

        return container

    def perfilProfessor(self, id):
        professor = self.professor.professorId(id)

        container = Frame(self.window)
        container.pack(side="top")

        titulo = Label(container, text="Professor", font=('bold'))
        titulo.pack(side="top", pady=20)

        perfil = Frame(container)
        perfil.pack(side="top")

        nome = Label(perfil)
        nome.grid(row=0 ,column=0, padx= 50, pady=20)
        Label(nome, text="Nome:").pack()
        Label(nome, text=professor["nome"]).pack()

        email = Label(perfil)
        email.grid(row=0 ,column=1, padx= 50, pady=20)
        Label(email, text="Email:").pack()
        Label(email, text=professor["email"]).pack()


        altura = Label(perfil)
        altura.grid(row=0 ,column=2, padx= 50, pady=20)
        Label(altura, text="Usuário:").pack()
        Label(altura, text=professor["usuario"]).pack()

        nascimento = Label(perfil)
        nascimento.grid(row=1 ,column=0, padx= 50, pady=20)
        Label(nascimento, text="Nascimento:").pack()
        Label(nascimento, text=f'{professor["nascimento"]["dia"]}/{professor["nascimento"]["mes"]}/{professor["nascimento"]["ano"]}').pack()
        
        idade = Label(perfil)
        idade.grid(row=1 ,column=1, padx= 50, pady=20)
        Label(idade, text="Idade:").pack()
        Label(idade, text=professor["idade"]).pack()



        Button(container, text="Editar", bg=self.rgb((0, 255, 155)), command= lambda: self.reload(self.editarProfessor, self.sessao["id"])).pack(pady=50)

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


        #botoes
        botoes = Frame(container)
        botoes.pack(side="top", pady=50)

        cancelar = Button(botoes, text="Cancelar", font=('bold'), width= 15, bg=self.rgb((0, 144, 255)), command= lambda: self.reload(self.perfilProfessor, self.sessao["id"]))
        cancelar.grid(row=0,column=0, padx=5)

        enviar = Button(botoes, text='Enviar', font=('bold'), width= 15,  bg=self.rgb((0, 255, 155)), command = lambda: self.janelaMensagem(self.professor.editar(id,{
                                                                                                                        "nome": inputNome.get(),
                                                                                                                        "email": inputEmail.get(),
                                                                                                                        "usuario": inputUsuario.get(), 
                                                                                                                        "senha": inputSenha.get(), 
                                                                                                                        "repetirsenha": inputRepetirSenha.get(),
                                                                                                                        "nascimento": cal.get(),
                                                                                                                        "atuacoes":{"Natação": professor["atuacoes"]["Natação"],
                                                                                                                                   "Dança": professor["atuacoes"]["Dança"],
                                                                                                                                   "Yoga": professor["atuacoes"]["Yoga"],
                                                                                                                                   "Musculação": professor["atuacoes"]["Musculação"],
                                                                                                                                   "Crossfit": professor["atuacoes"]["Crossfit"],
                                                                                                                                   "Muay Thai": professor["atuacoes"]["Muay Thai"],
                                                                                                                                   "Jiu Jitsu": professor["atuacoes"]["Jiu Jitsu"],
                                                                                                                                   "Boxe": professor["atuacoes"]["Boxe"]
                                                                                                                                }
                                                                                                                        })))    
        enviar.grid(row=0,column=1, padx=5)
        

        return container

    def abrirTreino(self, alunoId):
        treino = self.treino.procurar({"alunoId": alunoId, "professorId": self.sessao["id"]})
        root = Tk()
        root.geometry("500x500")

        texto = ScrolledText(root)
        texto.pack()

        

        if treino == None:
            Button(root, text="Salvar", command= lambda: [self.treino.cadastrar({
                                                                                "texto": texto.get(1.0, END),
                                                                                "alunoId": alunoId,
                                                                                "professorId": self.sessao["id"]                                                                        
                                                                                }), root.destroy()]).pack(pady=25)
        else:
            texto.insert(INSERT, treino["texto"])

            Button(root, text="Salvar", command= lambda: [self.treino.atualizar({
                                                                    "texto": texto.get(1.0, END),
                                                                    "treinoId": treino["id"]                                                      
                                                                    }), root.destroy()]).pack(pady=25)



        root.mainloop()
        
