import streamlit as st

st.set_page_config(page_title="Exemplo Streamlit", layout="wide")

st.title("Demo Streamlit")
st.header("Cabecalho")
st.subheader("Subcabecalho")
st.caption("Essa legenda ajuda a contextualizar a tela.")
st.markdown("**Markdown** tambem funciona dentro do app.")

nome = st.text_input("Nome")
idade = st.slider("Idade", 0, 100, 25)
area = st.selectbox("Area", ["Dados", "IA", "Produto"])
ativo = st.toggle("Ativar modo demonstracao", value=True)

col1, col2 = st.columns(2)
with col1:
    st.write("Coluna 1")
with col2:
    st.write("Coluna 2")

with st.sidebar:
    st.header("Configuracoes")
    top_k = st.slider("Top-K", 1, 10, 3)

if ativo:
    st.success(f"Nome={nome or 'nao informado'} | idade={idade} | area={area} | top_k={top_k}")
else:
    st.info("Modo demonstracao desativado.")