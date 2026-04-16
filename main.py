class Usuario():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.tentativas = 0
        self.block = False

    def login(self):
        while True:
            senha_digitada = input("Digite a senha: ")

            if self.block:
                print("Usuário bloqueado!")
                return

            if self.senha == senha_digitada:
                print("Login bem sucedido!")
                print(f"Tentativas feitas {self.tentativas}")
                self.tentativas = 0  
                return

            else:
                print("Senha incorreta!")
                self.tentativas += 1
                print(f"Tentativas feitas {self.tentativas}")

            if self.tentativas >= 3:
                self.block = True
                print("Usuário bloqueado!")
                return

    def status(self):
        if self.block:
            print("Você está bloqueado")
        else:
            print("Você não está bloqueado")

        print(f"Número de tentativas feitas {self.tentativas}")


p1 = Usuario(nome="Daniel", senha="Daniel0202")
p1.login()
p1.status()
