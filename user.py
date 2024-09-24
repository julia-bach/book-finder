class User:
    def __init__(self, nome, genero_preferido, autor_favorito, idade):
        self.nome = nome
        self.genero_preferido = genero_preferido
        self.autor_favorito = autor_favorito
        self.idade = idade
        

def criar_usuario():
    print(f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print("Bem-vindo ao sistema de recomendação de livros!")
    
    nome = input("\nPara começar, por favor, insira seu nome:\n")
    idade = input("\nQual é sua idade?\n")
    genero_preferido = input("\nQual é o seu gênero literário preferido? (ex: Ficção, Romance, Aventura, etc.):\n")
    autor_favorito = input("\nQual é o seu autor favorito?\n")
    
    usuario = User(nome, genero_preferido, autor_favorito, int(idade))
    return usuario