# portifoliofecaf
Documentação do Projeto: Dashboard de Análise de Dados com Supabase
Objetivo do Projeto
Este projeto tem como objetivo construir um dashboard interativo utilizando Streamlit e Supabase para análise de dados de filmes. Através desse painel, os usuários podem visualizar informações sobre filmes, como ano de lançamento, gênero e outros atributos, além de explorar gráficos que fornecem insights valiosos para análise de tendências no cinema.

Tecnologias Utilizadas
Streamlit : Framework para construir interfaces web de forma simples.
Supabase : Backend que fornece banco de dados PostgreSQL, autenticação e APIs.
Plotly : Biblioteca para visualização interativa de gráficos.
Pandas : Biblioteca para manipulação de dados.
Configuração do Projeto
1. Instalação de Dependências
Clone o repositório e instale as dependências:

git clone <repositório-do-projeto>
cd <diretório-do-projeto>
pip install -r requirements.txt

2. Definição de Variáveis ​​de Ambiente
Crie um arquivo .envna raiz do projeto com as variáveis ​​de ambiente permitidas para o Supabase:

texto simples

NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key

3. Execução do Projeto
Para iniciar o painel, execute o seguinte comando:

streamlit run app.py

4. Acesso ao Dashboard
O painel estará disponível http://localhost:8501 após a execução do comando acima.

Capturas de Tela do Dashboard
Tela Inicial

Gráficos de Análise

Visões SQL Utilizadas
Consulta Principal (Tabela movies_initial)
A tabela movies_initial contém os seguintes dados sobre os filmes:

id : Identificador único do filme.
título : Título do filme.
ano : Ano de lançamento.
gênero : Gênero do filme.
diretor : Diretor do filme.
Elenco : Elenco principal.
runtime : Duração do filme.
A consulta que extrai os dados para o dashboard é:

SQLite

SELECT * FROM movies_initial;
Consulta de Análise por Gênero e Ano
Para análise de tendências ao longo do tempo, uma consulta pode ser realizada para verificar a distribuição de filmes por gênero e ano:

SQLite

SELECT year, genre, COUNT(*) AS num_movies
FROM movies_initial
GROUP BY year, genre
ORDER BY year, num_movies DESC;
Possíveis Insights Obtidos dos Dados
A análise dos dados pode fornecer os seguintes insights:

Distribuição de Filmes por Gênero ao Longo do Tempo : identificar quais gêneros são mais comuns em cada década.
Tendências de Lançamento : Observar os períodos de maior número de lançamentos de filmes e como isso se correlaciona com os anos de sucesso no cinema.
Diretores Mais Produtivos : Avaliar quais diretores têm o maior número de lançamentos ao longo dos anos.
Popularidade por País e Idioma : Investiga quais países produzidos mais filmes e os idiomas mais comuns nos lançamentos.
Esse formato oferece uma visão mais completa sobre o seu projeto, fornecimento mais claro para quem utilizar ou revisar o código. Isso ajuda na escalabilidade do projeto, caso novas funcionalidades ou requisitos sejam adicionais no futuro.
