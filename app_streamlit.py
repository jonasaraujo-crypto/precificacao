import streamlit as st
import requests

# URL da API Flask no Render
API_URL = "https://precificacao-app.onrender.com"

st.set_page_config(page_title="Painel de Precificação", layout="wide")

st.title("💰 Painel de Precificação Senac 2026")
st.caption("Integração: Flask + PostgreSQL + Streamlit")

# --- Carregar níveis do backend ---
st.subheader("Níveis Profissionais")
try:
    resp = requests.get(f"{API_URL}/levels")
    if resp.status_code == 200:
        levels = resp.json()
        if levels:
            for lvl in levels:
                st.write(f"**{lvl['name']}** - R$ {lvl['hourly_total']}/h")
        else:
            st.info("Nenhum nível cadastrado ainda.")
    else:
        st.error("Erro ao acessar API de níveis.")
except Exception as e:
    st.error(f"Erro de conexão: {e}")

# --- Formulário de simulação ---
st.subheader("Simulação de Preço")

course_name = st.text_input("Nome do Curso")
hours = st.number_input("Carga Horária", min_value=1, value=40)
students = st.number_input("Número de Alunos", min_value=1, value=20)

level_names = []
try:
    level_names = [lvl["name"] for lvl in levels]
except:
    level_names = ["NÍVEL I", "NÍVEL II", "NÍVEL III"]

selected_level = st.selectbox("Nível do Instrutor", level_names)

if st.button("Calcular Preço"):
    st.success(f"✅ Simulação criada para o curso **{course_name}** ({selected_level})")
    st.write(f"- Carga horária: {hours}h")
    st.write(f"- Número de alunos: {students}")
