import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Análise", layout="wide")
st.title("📊 Dashboard Automático de Análise de Dados")

# Upload
arquivo = st.file_uploader("Carregue seu arquivo (Excel, CSV ou JSON)", type=["csv","xlsx","json"])

if arquivo:
    # Ingestão
    if arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo)
    elif arquivo.name.endswith(".xlsx"):
        df = pd.read_excel(arquivo)
    elif arquivo.name.endswith(".json"):
        df = pd.read_json(arquivo)

    # Tratamento de cabeçalhos
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Limpeza
    df = df.drop_duplicates()
    df = df.fillna(0)

    # Painel de estatísticas
    st.subheader("📈 Estatísticas Descritivas")
    st.write(df.describe())

    # Gráfico 1: Distribuição por categoria
    if "categoria" in df.columns and "valor_total" in df.columns:
        st.subheader("💰 Receita por Categoria")
        receita_categoria = df.groupby("categoria")["valor_total"].sum().sort_values(ascending=False)
        fig1, ax1 = plt.subplots()
        sns.barplot(x=receita_categoria.index, y=receita_categoria.values, ax=ax1)
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    # Gráfico 2: Produtos mais vendidos
    if "produto" in df.columns and "quantidade" in df.columns:
        st.subheader("📦 Top Produtos Vendidos")
        produtos_top = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(10)
        fig2, ax2 = plt.subplots()
        sns.barplot(x=produtos_top.index, y=produtos_top.values, ax=ax2)
        plt.xticks(rotation=45)
        st.pyplot(fig2)

    # Gráfico 3: Evolução temporal
    if "data_venda" in df.columns and "valor_total" in df.columns:
        st.subheader("📅 Evolução Mensal de Vendas")
        df["data_venda"] = pd.to_datetime(df["data_venda"])
        df["mes"] = df["data_venda"].dt.to_period("M")
        receita_mensal = df.groupby("mes")["valor_total"].sum()
        fig3, ax3 = plt.subplots()
        receita_mensal.plot(kind="line", marker="o", ax=ax3)
        plt.title("Receita Mensal")
        st.pyplot(fig3)
