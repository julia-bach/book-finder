
# Sistema de Recomendação de Livros

## Introdução
Este projeto implementa um sistema de recomendação de livros, no qual os usuários podem obter sugestões de livros com base em suas preferências literárias, como autor favorito, gênero preferido e idade. A recomendação é feita com base em uma escala de pontos que considera essas preferências.

## Estrutura do Projeto

### Arquivos principais:
- **livro.py**: define a classe `Livro`, responsável por armazenar informações sobre os livros disponíveis para recomendação.
- **user.py**: define a classe `User` e contém a função `criar_usuario`, que coleta informações do usuário, como nome, idade, gênero literário preferido e autor favorito.
- **recomendacao.py**: contém a lógica de recomendação que processa as informações do usuário e compara com os livros disponíveis para gerar recomendações personalizadas.
- **main.py**: o ponto de entrada do programa, responsável por integrar todos os módulos, criar o usuário, carregar os livros e executar o processo de recomendação.

## Funcionamento do Sistema

1. **Criação de Usuário**:
   - O sistema inicia solicitando informações do usuário: nome, idade, gênero literário preferido e autor favorito. Esses dados são coletados via função `criar_usuario()` no arquivo `user.py`.

2. **Carregamento dos Livros**:
   - O arquivo `livro.py` contém uma lista pré-definida de livros, cada um com informações sobre autor, gênero, ano de publicação e idade recomendada.

3. **Processo de Recomendação**:
   - A função `recomendar()` no arquivo `recomendacao.py` percorre a lista de livros e compara as preferências do usuário com as características de cada livro.
   - A escala de pontos funciona da seguinte forma:
     - 2 pontos se o autor do livro for o mesmo que o autor favorito do usuário.
     - 2 pontos se o gênero do livro for o gênero preferido do usuário.
     - 1 ponto se a idade do usuário for compatível com a idade recomendada do livro.
   - Com base nesses pontos, livros são recomendados ao usuário.

4. **Feedback**:
   - Após a recomendação, o sistema solicita feedback ao usuário sobre a qualidade das recomendações. Isso pode ser melhorado no futuro para permitir ajustes no algoritmo.

## Como Executar o Sistema

1. Certifique-se de que possui Python instalado em sua máquina.
2. Execute o arquivo `main.py`. O sistema solicitará as preferências do usuário e exibirá as recomendações com base nas suas escolhas.

## Possíveis Melhorias Futuras
- Implementação de uma interface gráfica para facilitar a interação.
- Aumento do banco de dados de livros para incluir mais opções.
- Integração com APIs de livrarias online para recomendações em tempo real.
- Adicionar a capacidade de armazenar perfis de usuários e histórico de recomendações.
