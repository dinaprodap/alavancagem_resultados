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
        consumo_ms = st.number_input("Consumo MS (Kg/Cab/dia)", min_value=0.0, value=10.9725, step=0.01)
        pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
        pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)

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

    # Resultados por molécula
    for molecula in moleculas:
        st.markdown(f"### Resultados para {molecula}")
        cols = st.columns(3)
        
        # Exemplo de cálculos (substitua pelos seus cálculos reais)
        incremento_lucro = 10.5  # Exemplo
        arrobas_adicionais = 2.3  # Exemplo
        receita_adicional = 450.0  # Exemplo
        
        with cols[0]:
            st.markdown(metric_card("Incremento do Lucro", incremento_lucro, suffix="%"), unsafe_allow_html=True)
        with cols[1]:
            st.markdown(metric_card("Arrobas Adicionais", arrobas_adicionais, suffix=" @/cab"), unsafe_allow_html=True)
        with cols[2]:
            st.markdown(metric_card("Receita Adicional", receita_adicional, prefix="R$ "), unsafe_allow_html=True)

    # Tabela de resultados detalhados
    st.subheader("📋 Detalhamento Completo")
    dados = {
        "Parâmetro": ["Consumo (%PV)", "Consumo MS (Kg/Cab/dia)", "Peso Vivo Inicial", "Peso Vivo Final"],
        "Valor": [consumo_pv, consumo_ms, pv_inicial, pv_final]
    }
    df_resultado = pd.DataFrame(dados)
    st.dataframe(
        df_resultado,
        use_container_width=True,
        hide_index=True
    )

# Adicionar footer
st.markdown("---")
st.markdown("*Desenvolvido com ❤️ para otimização de resultados*")
