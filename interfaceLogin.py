from tkinter import *
from login import Login
from interfaceAdmin import InterfaceAdmin
from interfaceProfessor import InterfaceProfessor


class InterfaceLogin:
    def __init__(self):
        self.login = Login()
        self.window = self.main()
        self.frame = self.formulario()

        self.window.mainloop()

    def main(self):
        main = Tk()
        main.title("Login")
        main.geometry("500x500")

        return main
    
    def formulario(self):
        frame = Frame(self.window)
        frame.pack(side="top", pady=90)

        
        Label(frame, text="LOGIN", font=('bold')).grid(row=0, column=0, pady=20)


        usuario = Frame(frame)
        usuario.grid(row=1, column=0, pady=10)
        Label(usuario, text="Usuário:").pack()
        inputUsuario = Entry(usuario, width=30)
        inputUsuario.pack()

        senha = Frame(frame)
        senha.grid(row=2, column=0, pady=5)
        Label(senha, text="Senha:").pack()
        inputSenha = Entry(senha, width=30)
        inputSenha.pack()

        Button(frame, text='Enviar', font=('bold'), command= lambda: self.janelaMensagem(self.login.login({
                                                                                "usuario": inputUsuario.get(),
                                                                                "senha": inputSenha.get()                            
                                                                                }))).grid(row=3, pady=40)


        return frame

    def janelaMensagem(self, data):
        janela = Tk()
        janela.title("Login")
        janela.geometry("450x100")

        Label(janela, text=data[0], font=('bold')).pack(side="top", pady=20)
        
        if data[1] !=  None:
            if data[1]["admin"]:
                Button(janela, text="OK", width=7, command=lambda:[janela.destroy(), self.window.destroy(), InterfaceAdmin(data[1])]).pack(side="top")
            else:
                Button(janela, text="OK", width=7, command=lambda:[janela.destroy(), self.window.destroy(), InterfaceProfessor(data[1])]).pack(side="top")
        else:
            Button(janela, text="OK", width=7, command=lambda: janela.destroy() ).pack(side="top")


        janela.mainloop()

