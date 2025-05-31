import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.set_page_config(page_title="Formulário de Dificuldades", layout="centered")
st.title("📚 Formulário de Dificuldades Acadêmicas")

st.markdown("Preencha o formulário abaixo para que possamos entender suas dificuldades e ajudar melhor! 💡")

# Inicializar sessão para armazenar dados se ainda não existir
if 'dados' not in st.session_state:
    st.session_state['dados'] = []

# Formulário
with st.form("formulario"):
    nome = st.text_input("Nome do aluno")
    contato = st.text_input("Meio de contato (e-mail, telefone, etc.)")
    materia = st.selectbox("Matéria com dificuldade", ["Matemática", "Física", "Química", "Biologia", "Português", "História", "Geografia", "Outra"])
    enviado = st.form_submit_button("ENVIAR")

    if enviado:
        if nome and contato:
            st.session_state['dados'].append({
                "Nome": nome,
                "Contato": contato,
                "Matéria": materia
            })
            st.success("Dados enviados com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

# Exibir tabela de dados
if st.session_state['dados']:
    df = pd.DataFrame(st.session_state['dados'])
    st.subheader("📋 Dados recebidos")
    st.dataframe(df, use_container_width=True)

    # Gráfico de barras com quantitativo por matéria
    st.subheader("📊 Alunos com dificuldade por matéria")
    grafico = px.bar(
        df.groupby("Matéria").size().reset_index(name='Quantidade'),
        x='Matéria',
        y='Quantidade',
        title="Distribuição de dificuldades por matéria",
        color='Matéria'
    )
    st.plotly_chart(grafico, use_container_width=True)
else:
    st.info("Nenhum dado enviado ainda. Preencha o formulário acima para começar.")