import livro
import user  
import recomendacao

if __name__ == "__main__":
    livros = livro.livros
    usuario = user.criar_usuario()
    recomendacao.recomendar(usuario, livros)
    recomendacao.feedback()
