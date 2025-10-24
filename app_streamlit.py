import streamlit as st
from streamlit_option_menu import option_menu

# =========================
# CONFIGURAÇÃO GERAL
# =========================
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
    /* ======= BARRA LATERAL ======= */
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

    /* ======= CABEÇALHO PRINCIPAL ======= */
    .main-title {
        background-color: #2F65CC;
        color: white;
        padding: 18px 25px;
        border-radius: 8px;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 25px;
        letter-spacing: 0.3px;
    }

    /* ======= CARDS ======= */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* ======= CAMPOS E BOTÕES ======= */
    input, select, textarea {
        border-radius: 6px !important;
    }
    button[kind="primary"] {
        background-color: #2F65CC !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        padding: 8px 20px !important;
    }
    button:hover {
        background-color: #204FA0 !important;
    }

    /* ======= RESULTADO ======= */
    .resultado {
        text-align: center;
        padding: 30px;
    }
    .resultado h4 {
        color: #FF5A00;
        font-size: 22px;
        margin-bottom: 10px;
    }
    .resultado p {
        color: #333;
        font-size: 15px;
    }

    /* ======= GERAL ======= */
    html, body, [class*="css"] {
        font-family: "Open Sans", sans-serif;
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
            st.number_input("Carga Horária (horas) *", min_value=0)
        with colB:
            st.number_input("Alunos Previstos *", min_value=0)

        colC, colD = st.columns(2)
        with colC:
            st.number_input("Material de Consumo (R$/turma)", min_value=0.0, step=0.01)
        with colD:
            st.number_input("Material Didático (R$/aluno)", min_value=0.0, step=0.01)

        st.text_input("Segmento / Eixo / Tipologia", placeholder="Ex: Tecnologia da Informação")

        st.button("📊 Calcular Preço")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('''
            <div class="card resultado">
                <h4>📈 Resultado</h4>
                <p>Preencha os dados e clique em <b>Calcular Preço</b></p>
            </div>
        ''', unsafe_allow_html=True)

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

