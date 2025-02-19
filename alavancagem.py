import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Alavancagem",
    layout="wide"
)

# CSS personalizado para a tela toda dentro de um quadrado arredondado
st.markdown("""
    <style>
    .stApp {
        background-color: #002A3B;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .container {
        background-color: #f0f9ff;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
        width: 90%;
        max-width: 1200px;
    }
    .produto-container {
        background-color: #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)


# Título da aplicação
st.title("🚀 Calculadora de Alavancagem")

# Fecha o container arredondado
st.markdown('</div>', unsafe_allow_html=True)

# Definir variáveis globais
moleculas = ["Molecula 1", "Molecula 2", "Molecula 3"]

# Dicionários para armazenar os valores
precos = {}
consumos = {}
diferenciais = {}

# Container de Produtos
with st.container():
    # Cabeçalho
    st.markdown("""
        <div class="produto-header">
            <h3 style="margin:0">Valores por Produto</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Grid de inputs
    st.markdown('<div class="produto-grid">', unsafe_allow_html=True)
    
    # Inputs para cada molécula
    for molecula in moleculas:
        cols = st.columns([2, 1, 1, 1])
        
        with cols[0]:
            st.markdown(f'<div class="input-field">{molecula}</div>', unsafe_allow_html=True)
        with cols[1]:
            precos[molecula] = st.number_input(
                f"Preço de {molecula}",
                min_value=0.0,
                value=5.0,
                step=0.1,
                key=f"preco_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[2]:
            consumos[molecula] = st.number_input(
                f"Consumo de {molecula}",
                min_value=0,
                value=250,
                step=1,
                key=f"consumo_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[3]:
            diferenciais[molecula] = st.number_input(
                f"Diferencial de {molecula}",
                min_value=0.0,
                value=0.0,
                step=0.01,
                key=f"diferencial_tabela_{molecula}",
                label_visibility="collapsed"
            )
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-grid
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-container

# Definição das funções

def calcular_arrobas_produzidas(peso_final, rendimento, peso_inicial):
    return ((peso_final * rendimento/100)/15) - (peso_inicial/30)

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dados do Animal")
        consumo_pv = st.number_input("Consumo (%PV)*", min_value=0.0, value=0.0231, step=0.0001)
        pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
        pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
        rendimento_carcaca = st.number_input("Rendimento de Carcaça (%)", min_value=0.0, value=54.89, step=0.01)

# Parâmetros principais em container separado
st.markdown("---")
st.subheader("Parâmetros Principais")
params_col1, params_col2, params_col3, params_col4 = st.columns(4)

with params_col1:
    custeio = st.number_input("Custeio (R$/Cab/dia)", min_value=0.0, value=15.0, step=0.01)
with params_col2:    
    valor_venda_arroba = st.number_input("Valor de Venda da arroba (R$/@)", min_value=0.0, value=340.0, step=0.1)
with params_col3:
    agio_percentual = st.number_input("Ágio para Animal Magro (%)", min_value=0.0, value=5.0, step=0.1)
with params_col4:
    agio_animal_magro = (agio_percentual / 100) * (pv_inicial/30 * valor_venda_arroba)
    st.metric("Ágio Animal Magro", f"R$ {agio_animal_magro:.2f}")

# Calcular arrobas_values após ter todas as variáveis necessárias
arrobas_values = {
    "Molecula 1": calcular_arrobas_produzidas(pv_final, rendimento_carcaca, pv_inicial),
    "Molecula 2": calcular_arrobas_produzidas(576.75, 55.38, pv_inicial),
    "Molecula 3": calcular_arrobas_produzidas(583.86, 56.34, pv_inicial)
}
