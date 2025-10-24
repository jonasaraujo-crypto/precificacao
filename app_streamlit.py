import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Painel de Precificação Senac 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# ESTILO CSS PERSONALIZADO
# =========================
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1C2A39;
        color: white;
        padding-top: 20px;
    }
    .sidebar-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #F5F5F5;
    }
    .main-title {
        background-color: #2F65CC;
        color: white;
        padding: 20px;
        border-radius: 6px;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 25px;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .orange {
        color: #FF5A00;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# MENU LATERAL
# =========================
with st.sidebar:
    st.markdown("### SENAC\nPainel de Precificação 2026")
    menu_principal = option_menu(
        menu_title=None,
        options=["Simulador", "Cadastros", "Diretrizes", "Chamados", "Tabela Final"],
        icons=["calculator", "database", "gear", "envelope", "table"],
        menu_icon="cast",
        default_index=0,
    )

# =========================
# CONTEÚDO PRINCIPAL
# =========================
if menu_principal == "Simulador":
    st.markdown('<div class="main-title">Simulador</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Simulador de Precificação")
        st.selectbox("Categoria *", ["Selecione", "Livre", "Técnico"])
        st.selectbox("Nível do Instrutor *", ["Selecione", "Nível I", "Nível II", "Nível III"])
        st.text_input("Título do Curso *", placeholder="Ex: Desenvolvimento Web Full Stack")
        colA, colB = st.columns(2)
        with colA:
            st.number_input("Carga Horária (horas) *", 0)
        with colB:
            st.number_input("Alunos Previstos *", 0)
        colC, colD = st.columns(2)
        with colC:
            st.number_input("Material de Consumo (R$/turma)", 0)
        with colD:
            st.number_input("Material Didático (R$/aluno)", 0)
        st.text_input("Segmento / Eixo / Tipologia", placeholder="Ex: Tecnologia da Informação")
        st.button("📊 Calcular Preço")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card" style="text-align:center;"><h4 style="color:#FF5A00;">📈 Resultado</h4><p>Preencha os dados e clique em <b>Calcular Preço</b></p></div>', unsafe_allow_html=True)

elif menu_principal == "Cadastros":
    st.markdown('<div class="main-title">Profissionais</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h4>Tabela de Profissionais</h4>', unsafe_allow_html=True)
    st.dataframe([
        {"Nível": "NÍVEL I", "Descrição": "Formação Inicial e Continuada - FIC", "Modalidade": "Horista", "Valor Hora": "R$ 51,00", "Total com Encargos": "R$ 63,24"},
        {"Nível": "NÍVEL II", "Descrição": "Formação Técnica de Nível Médio", "Modalidade": "Horista", "Valor Hora": "R$ 68,00", "Total com Encargos": "R$ 84,32"},
        {"Nível": "NÍVEL III", "Descrição": "Especialização Técnica", "Modalidade": "Horista", "Valor Hora": "R$ 87,00", "Total com Encargos": "R$ 107,88"},
    ])
    st.markdown('</div>', unsafe_allow_html=True)

elif menu_principal == "Diretrizes":
    st.markdown('<div class="main-title">Markup</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h4>Gestão de Rubricas</h4>', unsafe_allow_html=True)
    st.dataframe([
        {"Categoria": "LIVRES", "Rubrica": "Marketing", "Percentual": "4%"},
        {"Categoria": "LIVRES", "Rubrica": "Evasão", "Percentual": "5%"},
        {"Categoria": "LIVRES", "Rubrica": "Margem", "Percentual": "10%"},
    ])
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="main-title">Em desenvolvimento...</div>', unsafe_allow_html=True)


if st.button("Calcular Preço"):
    st.success(f"✅ Simulação criada para o curso **{course_name}** ({selected_level})")
    st.write(f"- Carga horária: {hours}h")
    st.write(f"- Número de alunos: {students}")
