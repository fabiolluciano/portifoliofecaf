# portifoliofecaf


Documentação do Projeto: Análise de Dados de Filmes até 2016

## 1. TÍTULO: 
Análise de Dados de Filmes até 2016 com Streamlit e PostgreSQL

## 2. DESCRIÇÃO DO PROJETO:
O objetivo deste projeto foi realizar uma análise interativa de filmes lançados até 2016, utilizando dados como título, ano, gênero, diretor, e avaliação. A análise foi feita com dados extraídos de um banco de dados PostgreSQL e visualizados com gráficos interativos utilizando a biblioteca Plotly, integrados em um dashboard feito com Streamlit.

## 3. CONFIGURAÇÃO E EXECUÇÃO DO PROJETO:
### 3.1. Pré-Requisitos:
- Python 3.7 ou superior
- Bibliotecas: pandas, plotly, streamlit, sqlalchemy, psycopg2
- PostgreSQL configurado e dados de filmes disponíveis

### 3.2. Configuração do Ambiente:
1. Instale as bibliotecas necessárias:
    ```bash
    pip install pandas psycopg2-binary sqlalchemy streamlit plotly
    ```
   
2. Configure o banco de dados PostgreSQL e carregue os dados de filmes.

### 3.3. Execução do Dashboard:
1. Crie o script `app.py` contendo a lógica para carregar e processar os dados do PostgreSQL.
2. Importe as bibliotecas necessárias no Python:
    ```python
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    from sqlalchemy import create_engine
    ```

3. Configure a conexão com o banco de dados PostgreSQL e carregue as visualizações:
    ```python
    engine = create_engine('postgresql://user:password@localhost:5432/database')
    ```

4. Utilize o Streamlit para criar o dashboard com os gráficos interativos:
    ```python
    st.title('Dashboard de Análise de Filmes')
    ```

5. Exiba os gráficos interativos:
    ```python
    fig1 = px.bar(df_avg_temp, x='title', y='year')
    st.plotly_chart(fig1)
    ```

### 3.4. Execução do Dashboard no Streamlit:
Para rodar o dashboard, execute o seguinte comando no terminal:
```bash
streamlit run app.py
```

### 3.5. Capturas de Tela:
![Dashboard de Filmes](link_para_imagem)

## 4. VIEWS SQL:

1. **avg_temp_por_dispositivo**: Calcula a média de temperatura por dispositivo.
    ```sql
    CREATE VIEW avg_temp_por_dispositivo AS
    SELECT device_id, AVG(temperature) as avg_temp
    FROM temperature_readings
    GROUP BY device_id;
    ```

2. **leituras_por_hora**: Contagem de leituras por hora.
    ```sql
    CREATE VIEW leituras_por_hora AS
    SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
    FROM temperature_readings
    GROUP BY hora;
    ```

3. **temp_max_min_por_dia**: Calcula as temperaturas máximas e mínimas por dia.
    ```sql
    CREATE VIEW temp_max_min_por_dia AS
    SELECT DATE(timestamp) AS data, MAX(temperature) AS temp_max, MIN(temperature) AS temp_min
    FROM temperature_readings
    GROUP BY data;
    ```

### 4.1. Propósito das Views:
- **avg_temp_por_dispositivo**: A média de temperatura por dispositivo pode ser útil para identificar dispositivos com leituras mais altas ou mais baixas.
- **leituras_por_hora**: Entender os padrões de leituras ao longo do dia pode ajudar a identificar picos de temperatura ou falhas em dispositivos.
- **temp_max_min_por_dia**: Observar a variação da temperatura máxima e mínima ao longo do tempo pode fornecer insights sobre o comportamento térmico em diferentes dias.

## 5. POSSÍVEIS INSIGHTS:
- **Análise do Gênero dos Filmes**: Verificando a distribuição dos filmes por gênero ao longo dos anos, podemos identificar tendências e mudanças nas preferências do público.
- **Desempenho dos Filmes**: Comparar o desempenho de filmes em termos de avaliação e bilheteira pode ajudar a entender o que atrai mais os espectadores.

## 6. ENVIANDO PARA O GITHUB:
1. Crie um novo repositório no GitHub.
2. Execute os seguintes comandos Git para enviar seu código:
    ```bash
    git add .
    git commit -m "Projeto de Análise de Filmes até 2016"
    git remote add origin URL_DO_SEU_REPOSITORIO
    git push -u origin main
    ```

### 6.1. Dicas:
- Mantenha seu código limpo, bem comentado e siga boas práticas de programação Python.
- Organize seu código de forma modular para facilitar futuras alterações ou escalabilidade.

## 7. CONCLUSÃO:
Esse projeto resultou em um dashboard interativo, utilizando dados de filmes até 2016, com o objetivo de proporcionar insights sobre tendências cinematográficas e permitir uma análise profunda dos filmes, suas classificações, e os fatores que influenciam suas avaliações.

---

Se precisar de mais algum ajuste ou adição, estou à disposição!
