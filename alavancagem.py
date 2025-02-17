import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Alavancagem",
    layout="wide"
)

# CSS personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f0f9ff;
    }
    .stTitle {
        color: #2c5282;
    }
    .stHeader {
        color: #234e52;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .metric-value {
        color: #2f855a;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Título da aplicação
st.title("🚀 Calculadora de Alavancagem")

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Valores por Produto")
        moleculas = ["Molecula 1", "Modelula 2", "Modelula 3"]
        precos = {}
        consumos = {}
        for molecula in moleculas:
            with st.container():
                st.markdown(f"### {molecula}")
                precos[molecula] = st.number_input(
                    f"Preço de {molecula} (R$/ton)",
                    min_value=0.0,
                    value=5.0,
                    step=0.1,
                    key=f"preco_{molecula}"
                )
                consumos[molecula] = st.number_input(
                    f"Consumo de {molecula} (g/cab/dia)",
                    min_value=0,
                    value=250,
                    step=1,
                    key=f"consumo_{molecula}"
                )

    with col2:
        st.subheader("Parâmetros Principais")
        consumo_pv = st.number_input("Consumo (%PV)*", min_value=0.0, value=0.0231, step=0.0001)
        pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
        pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
        gmd = st.number_input("GMD (kg/dia)", min_value=0.0, value=1.551, step=0.001)
        rendimento_carcaca = st.number_input("Rendimento de Carcaça (%)", min_value=0.0, value=54.89, step=0.01)
        custeio = st.number_input("Custeio (R$/Cab/dia)", min_value=0.0, value=15.0, step=0.01)
        valor_venda_arroba = st.number_input("Valor de Venda da arroba (R$/@)", min_value=0.0, value=340.0, step=0.1)
        agio_animal_magro = st.number_input("Ágio para Animal Magro (R$/cab)", min_value=0.0, value=4641.0, step=0.1)

with tab2:
    # Organização dos resultados em cards
    st.header("📈 Análise de Resultados")
    
    col1, col2, col3 = st.columns(3)
    
    # Função para criar cards de métricas
    def metric_card(title, value, prefix="", suffix=""):
        return f"""
        <div class="metric-card">
            <h3>{title}</h3>
            <div class="metric-value">{prefix}{value:.2f}{suffix}</div>
        </div>
        """

    # Função para calcular incremento lucro
    def calcular_incremento_lucro(base, comparacao):
        if base < 0:
            return (comparacao/base - 1) * -1
        return comparacao/base - 1

    # Valores base da Molécula 1
    base_arrobas = 7.49
    base_resultado = 903.27
    base_custo = 1644.10

    # Resultados por molécula
    for idx, molecula in enumerate(moleculas):
        st.markdown(f"### Resultados para {molecula}")
        cols = st.columns(3)
        
        if idx == 0:  # Molécula 1
            incremento_lucro = 0
            arrobas_adicionais = 0
            receita_adicional = 0
            custo_adicional = 0
            incremento_lucro_adicional = 0
            custo_arroba_adicional = 0
        elif idx == 1:  # Molécula 2
            arrobas_adicionais = 8.30 - base_arrobas
            receita_adicional = arrobas_adicionais * valor_venda_arroba
            custo_adicional = 1820.09 - base_custo
            incremento_lucro = calcular_incremento_lucro(base_resultado, 1000.29) * 100
            incremento_lucro_adicional = 1000.29 - base_resultado
            custo_arroba_adicional = custo_adicional / arrobas_adicionais if arrobas_adicionais != 0 else 0
        else:  # Molécula 3
            arrobas_adicionais = 8.93 - base_arrobas
            receita_adicional = arrobas_adicionais * valor_venda_arroba
            custo_adicional = 1874.33 - base_custo
            incremento_lucro = calcular_incremento_lucro(base_resultado, 1161.69) * 100
            incremento_lucro_adicional = 1161.69 - base_resultado
            custo_arroba_adicional = custo_adicional / arrobas_adicionais if arrobas_adicionais != 0 else 0
        
        with cols[0]:
            st.markdown(metric_card("Incremento do Lucro", incremento_lucro, suffix="%"), unsafe_allow_html=True)
        with cols[1]:
            st.markdown(metric_card("Arrobas Adicionais", arrobas_adicionais, suffix=" @/cab"), unsafe_allow_html=True)
        with cols[2]:
            st.markdown(metric_card("Receita Adicional", receita_adicional, prefix="R$ "), unsafe_allow_html=True)
        
        # Métricas adicionais
        cols2 = st.columns(3)
        with cols2[0]:
            st.markdown(metric_card("Custo Adicional", custo_adicional, prefix="R$ "), unsafe_allow_html=True)
        with cols2[1]:
            st.markdown(metric_card("Incremento Lucro Adicional", incremento_lucro_adicional, prefix="R$ "), unsafe_allow_html=True)
        with cols2[2]:
            st.markdown(metric_card("Custo da Arroba Adicional", custo_arroba_adicional, prefix="R$ "), unsafe_allow_html=True)

    # Tabela de resultados detalhados
    st.subheader("📋 Detalhamento Completo")
    dados = {
        "Parâmetro": ["Consumo (%PV)", "GMD (kg/dia)", "Rendimento de Carcaça (%)", 
                     "Custeio (R$/Cab/dia)", "Valor de Venda da arroba (R$/@)", 
                     "Ágio Animal Magro (R$/cab)"],
        "Valor": [consumo_pv, gmd, rendimento_carcaca, custeio, 
                 valor_venda_arroba, agio_animal_magro]
    }
    df_resultado = pd.DataFrame(dados)
    st.dataframe(
        df_resultado,
        use_container_width=True,
        hide_index=True
    )
