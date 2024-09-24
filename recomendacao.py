def recomendar(usuario, livros):
    print(f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print(f"Recomendações de livros para {usuario.nome}:")
    
    recomendacoes = []
    
    for livro in livros:
        escala_pontos = 0
        
        if livro.autor.upper() == usuario.autor_favorito.upper():
            escala_pontos += 2 
        if usuario.genero_preferido.upper() in livro.genero.upper():
            escala_pontos += 2 
        if usuario.idade >= livro.idade_recomendada:
            escala_pontos += 1  
        
        if escala_pontos > 1:
            recomendacoes.append((livro, escala_pontos))

    recomendacoes.sort(key=lambda x: x[1], reverse=True)

    vaiAmar = [livro for livro, pontos in recomendacoes if pontos >= 4]
    vaiGostar = [livro for livro, pontos in recomendacoes if pontos == 3]

    if vaiAmar:
        print("\nVocê vai amar:")
        for livro in vaiAmar:
            print(f"-- {livro.nome} - {livro.autor} ({livro.ano_publicacao}), {livro.genero}")
    
    if vaiGostar:
        print("\nVocê vai gostar:")
        for livro in vaiGostar:
            print(f"-- {livro.nome} - {livro.autor} ({livro.ano_publicacao}), {livro.genero}")
    
    if not recomendacoes:
        print("\nPoxa! Nenhum livro encontrado com base nas suas preferências.")


def feedback():
    print(f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    feedback = int(input("\nEm uma escala de 0 a 10, como você classifica essa recomendação?\n"))

    if feedback >= 0 and feedback <= 4:
        print("\nPoxa! Parece que você não gostou tanto assim...")
        print("\nEspero que possamos lhe agradar futuramente.")
    elif feedback > 4 and feedback <= 7:
        print("\nObrigada pelo feedback!")
        print("\nEstaremos trabalhando para aperfeiçoar cada vez mais nossos serviços.")
    elif feedback > 7 and feedback <= 10:
        print("\nFicamos felizes em saber que gostou das recomendações! :D") 
    else:
        print("\nPor favor, informe um número entre 0 e 10.")
        feedback()

    print(f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def recomendar_livro(usuario, lista_de_livros):
    
    recomendacoes = []
    for livro in lista_de_livros:
        if (livro.genero == usuario.genero_preferido or livro.autor == usuario.autor_favorito) and livro.idade_recomendada <= int(usuario.faixa_etaria.replace("+", "")):
            recomendacoes.append(livro)
    
    if recomendacoes:
        for livro in recomendacoes:
            print(f"Livro: {livro.nome} - Autor: {livro.autor} - Gênero: {livro.genero} - Idade Recomendada: {livro.idade_recomendada}+")
    else:
        print("Nenhum livro encontrado com base nas suas preferências.")