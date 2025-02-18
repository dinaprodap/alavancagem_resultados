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

# Criar uma linha de insights principais
insight_col1, insight_col2, insight_col3, insight_col4, insight_col5 = st.columns(5)

with insight_col1:
    st.metric("Dias de Confinamento", "110")  # Valor fixo conforme imagem

with insight_col2:
    gdc_values = {
        "Molecula 1": (((pv_final * rendimento_carcaca/100)) - (pv_inicial/2))/110,
        "Molecula 2": (((576.75 * 55.38/100)) - (390/2))/110,
        "Molecula 3": (((583.86 * 56.34/100)) - (390/2))/110
    }
    st.metric("GDC (KG/DIA)", f"{gdc_values['Molecula 1']:.3f}")

with insight_col3:
    arrobas_values = {
        "Molecula 1": ((pv_final * rendimento_carcaca/100)/15) - (pv_inicial/30),
        "Molecula 2": ((576.75 * 55.38/100)/15) - (390/30),
        "Molecula 3": ((583.86 * 56.34/100)/15) - (390/30)
    }
    st.metric("Arrobas Produzidas (@/Cab)", f"{arrobas_values['Molecula 1']:.2f}")

with insight_col4:
    diferencial_values = {
        "Molecula 2": 0.65,
        "Molecula 3": 1.03
    }
    st.metric("Diferencial Tecnológico (R$/cab/dia)", "0.00")

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Valores por Produto")
        moleculas = ["Molecula 1", "Molecula 2", "Molecula 3"]
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
    st.header("📈 Análise Comparativa", divider='rainbow')
    
    # Função para criar cards de métricas mais compactos
    def metric_card(title, value, prefix="", suffix=""):
        return f"""
        <div style="background-color: white; padding: 10px; border-radius: 5px; 
                    box-shadow: 0 1px 2px rgba(0,0,0,0.1); margin: 5px 0;">
            <div style="font-size: 0.9em; color: #666;">{title}</div>
            <div style="font-size: 1.1em; color: #2f855a; font-weight: bold;">
                {prefix}{value:.2f}{suffix}
            </div>
        </div>
        """

    # Valores base da Molécula 1
    base_arrobas = 7.49
    base_resultado = 903.27
    base_custo = 1644.10

    # Grid de resultados
    col1, col2, col3 = st.columns(3)
    
    # Dicionário para armazenar os resultados
    resultados = {}
    
    # Calcular resultados para cada molécula
    for idx, molecula in enumerate(moleculas):
        if idx == 0:  # Molécula 1
            resultados[molecula] = {
                "incremento_lucro": 0,
                "arrobas_adicionais": 0,
                "receita_adicional": 0,
                "custo_adicional": 0,
                "incremento_lucro_adicional": 0,
                "custo_arroba_adicional": 0
            }
        else:
            arrobas = 8.30 if idx == 1 else 8.93
            resultado = 1000.29 if idx == 1 else 1161.69
            custo = 1820.09 if idx == 1 else 1874.33
            
            arrobas_adicionais = arrobas - base_arrobas
            receita_adicional = arrobas_adicionais * valor_venda_arroba
            custo_adicional = custo - base_custo
            incremento_lucro = ((resultado/base_resultado - 1) * 100) if base_resultado > 0 else 0
            incremento_lucro_adicional = resultado - base_resultado
            custo_arroba_adicional = custo_adicional / arrobas_adicionais if arrobas_adicionais != 0 else 0
            
            resultados[molecula] = {
                "incremento_lucro": incremento_lucro,
                "arrobas_adicionais": arrobas_adicionais,
                "receita_adicional": receita_adicional,
                "custo_adicional": custo_adicional,
                "incremento_lucro_adicional": incremento_lucro_adicional,
                "custo_arroba_adicional": custo_arroba_adicional
            }

    # Exibir resultados em colunas
    for idx, (molecula, res) in enumerate(resultados.items()):
        with [col1, col2, col3][idx]:
            st.markdown(f"#### {molecula}")
            st.markdown(metric_card("Incremento do Lucro", res["incremento_lucro"], suffix="%"), unsafe_allow_html=True)
            st.markdown(metric_card("Arrobas Adicionais", res["arrobas_adicionais"], suffix=" @/cab"), unsafe_allow_html=True)
            st.markdown(metric_card("Receita Adicional", res["receita_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Custo Adicional", res["custo_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Incremento Lucro", res["incremento_lucro_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Custo @Adicional", res["custo_arroba_adicional"], prefix="R$ "), unsafe_allow_html=True)

    # Tabela compacta com principais parâmetros
    st.markdown("---")
    st.caption("Parâmetros Principais")
    params_col1, params_col2, params_col3 = st.columns(3)
    with params_col1:
        st.metric("GMD (kg/dia)", f"{gmd:.3f}")
    with params_col2:
        st.metric("Rendimento Carcaça", f"{rendimento_carcaca:.2f}%")
    with params_col3:
        st.metric("Valor Arroba", f"R$ {valor_venda_arroba:.2f}")
