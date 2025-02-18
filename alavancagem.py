import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Alavancagem",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
    <style>
    /* Resetar cores de fundo */
    .stApp {
        background-color: #002A3B !important;
    }
    
    .main {
        background-color: #002A3B !important;
    }
    
    /* Container principal */
    div[data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin: 10px 0;
    }

    /* Inputs e Selects */
    .stTextInput > div > div, 
    .stNumberInput > div > div,
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 5px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }

    /* Container para inputs */
    .input-container {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }

    /* Textos e Labels */
    label, p, .stMarkdown {
        color: white !important;
    }

    .stTitle, .stHeader {
        color: white !important;
    }

    /* Métricas */
    [data-testid="stMetricValue"] {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 5px;
        color: white !important;
    }

    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.8) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 5px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: white;
        border-radius: 5px;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: rgba(255, 255, 255, 0.2);
    }

    /* Containers uniformes */
    .uniform-container {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Ajuste para inputs dentro dos containers */
    .uniform-container .stNumberInput,
    .uniform-container .stTextInput {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        padding: 5px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

def metric_card(title, value, prefix="", suffix=""):
    return f"""
    <div class="uniform-container">
        <div style="font-size: 0.9em; color: rgba(255,255,255,0.8);">{title}</div>
    <div style="background-color: white; padding: 10px; border-radius: 5px; 
                box-shadow: 0 1px 2px rgba(0,0,0,0.1); margin: 5px 0;">
        <div style="font-size: 0.9em; color: #666;">{title}</div>
        <div style="font-size: 1.1em; color: #2f855a; font-weight: bold;">
            {prefix}{value:.2f}{suffix}
        </div>
    </div>
    """

# Funções de cálculo existentes continuam aqui...
def calcular_consumo_ms(consumo_pv, pv_inicial, pv_final):
    return consumo_pv * ((pv_inicial + pv_final) / 2)
    
# Funções de cálculo
def calcular_consumo_ms(consumo_pv, pv_inicial, pv_final):
    return consumo_pv * ((pv_inicial + pv_final) / 2)

def calcular_pv_final_arroba(peso_final, rendimento):
    return (peso_final * rendimento/100) / 15

def calcular_eficiencia_biologica(consumo_ms, dias_confinamento, arrobas_produzidas):
    return (consumo_ms * dias_confinamento) / arrobas_produzidas

def calcular_custeio(consumo_ms, consumo_ms_base, custeio_base):
    return (consumo_ms / consumo_ms_base) * custeio_base

def calcular_gdc(peso_final, rendimento_carcaca, peso_inicial, dias):
    return (((peso_final * rendimento_carcaca/100)) - (peso_inicial/2))/dias

def calcular_arrobas_produzidas(peso_final, rendimento, peso_inicial):
    return ((peso_final * rendimento/100)/15) - (peso_inicial/30)

# Título da aplicação
st.title("🚀 Calculadora de Alavancagem")

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

# Definir variáveis globais
moleculas = ["Molecula 1", "Molecula 2", "Molecula 3"]

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Valores por Produto")
        precos = {}
        consumos = {}
        with st.container():
            for molecula in moleculas:
                st.markdown(f"### {molecula}")
                col_preco, col_consumo = st.columns(2)
                with col_preco:
                    precos[molecula] = st.number_input(
                        f"Preço de {molecula} (R$/ton)",
                        min_value=0.0,
                        value=5.0,
                        step=0.1,
                        key=f"preco_{molecula}"
                    )
                with col_consumo:
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
        agio_percentual = st.number_input("Ágio para Animal Magro (%)", min_value=0.0, value=5.0, step=0.1)
        agio_animal_magro = (agio_percentual / 100) * (pv_inicial/30 * valor_venda_arroba)

# Calcular valores base após entrada de dados
base_arrobas = 7.49
base_resultado = 903.27
base_custo = 1644.10

# Calcular arrobas_values após ter todas as variáveis necessárias
arrobas_values = {
    "Molecula 1": calcular_arrobas_produzidas(pv_final, rendimento_carcaca, pv_inicial),
    "Molecula 2": calcular_arrobas_produzidas(576.75, 55.38, pv_inicial),
    "Molecula 3": calcular_arrobas_produzidas(583.86, 56.34, pv_inicial)
}

# Insights principais
insight_col1, insight_col2, insight_col3, insight_col4 = st.columns(4)

with insight_col1:
    st.metric("Dias de Confinamento", "110")

with insight_col2:
    gdc = calcular_gdc(pv_final, rendimento_carcaca, pv_inicial, 110)
    st.metric("GDC (KG/DIA)", f"{gdc:.3f}")

with insight_col3:
    arrobas = calcular_arrobas_produzidas(pv_final, rendimento_carcaca, pv_inicial)
    st.metric("Arrobas Produzidas (@/Cab)", f"{arrobas:.2f}")

with insight_col4:
    st.metric("Diferencial Tecnológico (R$/cab/dia)", "0.00")

# Tab 2 - Resultados
with tab2:
    st.header("📈 Análise Comparativa", divider='rainbow')
    
    # Grid de resultados
    col1, col2, col3 = st.columns(3)
    
    # Dicionário para armazenar os resultados
    resultados = {}
    
    # Calcular resultados para cada molécula
    for idx, molecula in enumerate(moleculas):
        consumo_ms = calcular_consumo_ms(consumo_pv, pv_inicial, pv_final)
        pv_final_arroba = calcular_pv_final_arroba(pv_final, rendimento_carcaca)
        
        base_resultados = {
            "consumo_ms": consumo_ms,
            "pv_final_arroba": pv_final_arroba,
            "eficiencia_biologica": calcular_eficiencia_biologica(
                consumo_ms,
                110,
                arrobas_values[molecula]
            )
        }
        
        if idx == 0:
            resultados[molecula] = {
                **base_resultados,
                "incremento_lucro": 0,
                "arrobas_adicionais": 0,
                "receita_adicional": 0,
                "custo_adicional": 0,
                "incremento_lucro_adicional": 0,
                "custo_arroba_adicional": 0
            }
        else:
            custeio_atual = calcular_custeio(
                consumo_ms,
                resultados["Molecula 1"]["consumo_ms"],
                custeio
            )
            
            arrobas = 8.30 if idx == 1 else 8.93
            resultado = 1000.29 if idx == 1 else 1161.69
            custo = 1820.09 if idx == 1 else 1874.33
            
            resultados[molecula] = {
                **base_resultados,
                "incremento_lucro": ((resultado/base_resultado - 1) * 100),
                "arrobas_adicionais": arrobas - base_arrobas,
                "receita_adicional": (arrobas - base_arrobas) * valor_venda_arroba,
                "custo_adicional": custo - base_custo,
                "incremento_lucro_adicional": resultado - base_resultado,
                "custo_arroba_adicional": (custo - base_custo) / (arrobas - base_arrobas)
            }

    # Exibir resultados
    for idx, (molecula, res) in enumerate(resultados.items()):
        with [col1, col2, col3][idx]:
            st.markdown(f"#### {molecula}")
            st.markdown(metric_card("Incremento do Lucro", res["incremento_lucro"], suffix="%"), unsafe_allow_html=True)
            st.markdown(metric_card("Arrobas Adicionais", res["arrobas_adicionais"], suffix=" @/cab"), unsafe_allow_html=True)
            st.markdown(metric_card("Receita Adicional", res["receita_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Custo Adicional", res["custo_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Incremento Lucro", res["incremento_lucro_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Custo @Adicional", res["custo_arroba_adicional"], prefix="R$ "), unsafe_allow_html=True)
            st.markdown(metric_card("Consumo MS", res["consumo_ms"], suffix=" Kg/Cab/dia"), unsafe_allow_html=True)
            st.markdown(metric_card("PV Final", res["pv_final_arroba"], suffix=" @/Cab"), unsafe_allow_html=True)
            st.markdown(metric_card("Eficiência Biológica", res["eficiencia_biologica"], suffix=" kgMS/@"), unsafe_allow_html=True)

    # Parâmetros principais
    st.markdown("---")
    st.caption("Parâmetros Principais")
    params_col1, params_col2, params_col3 = st.columns(3)
    with params_col1:
        st.metric("GMD (kg/dia)", f"{gmd:.3f}")
    with params_col2:
        st.metric("Rendimento Carcaça", f"{rendimento_carcaca:.2f}%")
    with params_col3:
        st.metric("Valor Arroba", f"R$ {valor_venda_arroba:.2f}")
