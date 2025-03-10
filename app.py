import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do Supabase usando as variáveis de ambiente
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

# Verificando se as variáveis de ambiente estão carregadas corretamente
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("As credenciais do Supabase não foram encontradas. Verifique as variáveis de ambiente.")
else:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Configuração da página
    st.set_page_config(page_title="Dashboard com Supabase", layout="wide")

    st.title("Dashboard de Análise de Dados com Supabase")

    # Carregando dados do Supabase
    def get_data():
        response = supabase.table("movies_initial").select("*").execute()
        if response.data:
            return pd.DataFrame(response.data)
        return pd.DataFrame()

    df = get_data()

    if not df.empty:
        st.subheader("Visualização da Tabela")
        st.dataframe(df)

        # Criando dois gráficos
        fig1 = px.bar(df, x="title", y="year", title="Gráfico de Barras")
        fig2 = px.line(df, x="genre", y="director", title="Gráfico de Linhas")

        # Exibindo os gráficos
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado no Supabase.")
