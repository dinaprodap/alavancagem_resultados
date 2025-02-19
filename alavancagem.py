import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Alavancagem",
    layout="wide"
)

# CSS personalizado
st.markdown("""
    <style>
    .stApp {
        background-color: #002A3B;
    }
    .main {
        background-color: #f0f9ff;
        border-radius: 15px;
        padding: 20px;
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
    div[data-testid="stVerticalBlock"] {
        background-color: #f0f9ff;
        border-radius: 15px;
        padding: 20px;
    }
    .diferencial-value {
        font-size: 20px;
        font-weight: bold;
        color: #464646ee;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

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
            <h3 style="margin:0">Diferencial Tecnológico</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Grid de inputs
    st.markdown('<div class="produto-grid">', unsafe_allow_html=True)
    
    # Cabeçalhos das colunas
    col_headers = st.columns([2, 0.8, 0.8, 0.8, 2])
    with col_headers[0]:
        st.markdown('<div class="produto-label">Molécula</div>', unsafe_allow_html=True)
    with col_headers[1]:
        st.markdown('<div class="produto-label">Preço</div>', unsafe_allow_html=True)
    with col_headers[2]:
        st.markdown('<div class="produto-label">Consumo</div>', unsafe_allow_html=True)
    with col_headers[3]:
        st.markdown('<div class="produto-label">Custo</div>', unsafe_allow_html=True)
    with col_headers[4]:
        st.markdown('<div class="produto-label">Diferencial Tecnológico (R$/cab/dia)</div>', unsafe_allow_html=True)
    
    # Inputs para cada molécula
    for molecula in moleculas:
        cols = st.columns([2, 0.8, 0.8, 0.8, 2])
        
        with cols[0]:
            st.markdown(f'<div class="input-field">{molecula}</div>', unsafe_allow_html=True)
        with cols[1]:
            valor_inicial = 4.90 if molecula == "Molecula 1" else (6.48 if molecula == "Molecula 2" else 8.68)
            precos[molecula] = st.number_input(
                f"Preço de {molecula}",
                min_value=0.0,
                value=valor_inicial,
                step=0.1,
                key=f"preco_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[2]:
            valor_consumo = 250 if molecula == "Molecula 1" else (290 if molecula == "Molecula 2" else 260)
            consumos[molecula] = st.number_input(
                f"Consumo de {molecula}",
                min_value=0,
                value=valor_consumo,
                step=1,
                key=f"consumo_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[3]:
            valor_custo = 1.23 if molecula == "Molecula 1" else (1.88 if molecula == "Molecula 2" else 2.26)
            diferenciais[molecula] = st.number_input(
                f"Custo de {molecula}",
                min_value=0.0,
                value=valor_custo,
                step=0.01,
                key=f"diferencial_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[4]:
            if molecula == "Molecula 1":
                diferencial_tecnologico = 0.00
            else:
                diferencial_tecnologico = diferenciais[molecula] - diferenciais["Molecula 1"]
            st.markdown(f'<div class="diferencial-value">{diferencial_tecnologico:.2f}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-grid
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-container

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

def calcular_rentabilidade_periodo(resultado, valor_arroba, peso_final_arroba):
    return resultado/(valor_arroba * peso_final_arroba)

def calcular_rentabilidade_mensal(rentabilidade_periodo, dias):
    return ((1 + rentabilidade_periodo)**(1/(dias/30.4))) - 1

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

# Definir variáveis globais
moleculas = ["Molecula 1", "Molecula 2", "Molecula 3"]

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dados do Animal")
        consumo_pv = st.number_input("Consumo (%PV) - Molécula 1*", min_value=0.0, value=2.31, step=0.0001)
        consumo_pv_mol2 = consumo_pv * 1.045
        consumo_pv_mol3 = consumo_pv_mol2
        st.markdown(f"Consumo (%PV) - Molécula 2: {consumo_pv_mol2:.4f}")
        st.markdown(f"Consumo (%PV) - Molécula 3: {consumo_pv_mol3:.4f}")
        pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
        pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
        gmd = st.number_input("GMD (kg/dia)", min_value=0.0, value=1.551, step=0.001)
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

# Calcular valores para cada molécula
resultados = {}

for idx, molecula in enumerate(moleculas):
    # Cálculos básicos
    if idx == 0:  # Molécula 1
        consumo_pv_atual = consumo_pv
        peso_final_atual = pv_final
        gmd_atual = gmd
        rendimento_atual = rendimento_carcaca
    elif idx == 1:  # Molécula 2
        consumo_pv_atual = consumo_pv * 1.045
        gmd_atual = gmd * 1.077 * 1.02
        rendimento_atual = rendimento_carcaca * 1.009
    else:  # Molécula 3
        consumo_pv_atual = consumo_pv * 1.045  # Mesmo da Molécula 2
        gmd_atual = gmd * 1.118 * 1.02
        rendimento_atual = rendimento_carcaca * 1.0264
    
    # Cálculos derivados
    dias = (pv_final - pv_inicial) / gmd_atual if idx == 0 else resultados["Molecula 1"]["dias"]
    peso_final_atual = pv_inicial + (gmd_atual * dias) if idx > 0 else pv_final
    
    consumo_ms = calcular_consumo_ms(consumo_pv_atual, pv_inicial, peso_final_atual)
    arrobas = calcular_arrobas_produzidas(peso_final_atual, rendimento_atual, pv_inicial)
    
    # Cálculos financeiros
    custeio_atual = custeio if idx == 0 else (consumo_ms / resultados["Molecula 1"]["consumo_ms"]) * custeio
    diferencial_tec = 0 if idx == 0 else diferenciais[molecula]
    custeio_final = custeio_atual + diferencial_tec
    
    custo_periodo = custeio_final * dias
    valor_arrobas = valor_venda_arroba * arrobas
    custo_animal_magro = (valor_venda_arroba * (1 + agio_percentual/100)) * (pv_inicial/30)
    
    resultado = valor_arrobas - custo_periodo - custo_animal_magro
    
    # Armazenar resultados
    resultados[molecula] = {
        "consumo_pv": consumo_pv_atual,
        "consumo_ms": consumo_ms,
        "peso_final": peso_final_atual,
        "gmd": gmd_atual,
        "dias": dias,
        "rendimento": rendimento_atual,
        "arrobas": arrobas,
        "custeio": custeio_atual,
        "custeio_final": custeio_final,
        "resultado": resultado,
        "rentabilidade_periodo": calcular_rentabilidade_periodo(resultado, valor_venda_arroba, peso_final_atual),
        "rentabilidade_mensal": calcular_rentabilidade_mensal(
            calcular_rentabilidade_periodo(resultado, valor_venda_arroba, peso_final_atual),
            dias
        )
    }
    
    if idx > 0:
        resultados[molecula].update({
            "incremento_lucro": ((resultado/resultados["Molecula 1"]["resultado"] - 1) * 100),
            "arrobas_adicionais": arrobas - resultados["Molecula 1"]["arrobas"],
            "receita_adicional": (arrobas - resultados["Molecula 1"]["arrobas"]) * valor_venda_arroba,
            "custo_adicional": custo_periodo - resultados["Molecula 1"]["custeio_final"] * dias,
            "incremento_lucro_adicional": resultado - resultados["Molecula 1"]["resultado"],
            "custo_arroba_adicional": (custo_periodo - resultados["Molecula 1"]["custeio_final"] * dias) / 
                                    (arrobas - resultados["Molecula 1"]["arrobas"])
        })

# Insights principais
insight_col1, insight_col2, insight_col3, insight_col4 = st.columns(4)

with insight_col1:
    st.metric("Dias de Confinamento", f"{resultados['Molecula 1']['dias']:.0f}")

with insight_col2:
    st.metric("GDC (KG/DIA)", f"{calcular_gdc(pv_final, rendimento_carcaca, pv_inicial, resultados['Molecula 1']['dias']):.3f}")

with insight_col3:
    st.metric("Arrobas Produzidas (@/Cab)", f"{resultados['Molecula 1']['arrobas']:.2f}")

with insight_col4:
    st.metric("Diferencial Tecnológico (R$/cab/dia)", "0.00")

# Tab 2 - Resultados
with tab2:
    st.header("📈 Análise Comparativa", divider='rainbow')
    
    # Grid de resultados
    col1, col2, col3 = st.columns(3)
    
    # Exibir resultados
    for idx, (molecula, res) in enumerate(resultados.items()):
        with [col1, col2, col3][idx]:
            st.markdown(f"#### {molecula}")
            if idx > 0:
                st.markdown(metric_card("Incremento do Lucro", res["incremento_lucro"], suffix="%"), unsafe_allow_html=True)
                st.markdown(metric_card("Arrobas Adicionais", res["arrobas_adicionais"], suffix=" @/cab"), unsafe_allow_html=True)
                st.markdown(metric_card("Receita Adicional", res["receita_adicional"], prefix="R$ "), unsafe_allow_html=True)
                st.markdown(metric_card("Custo Adicional", res["custo_adicional"], prefix="R$ "), unsafe_allow_html=True)
                st.markdown(metric_card("Incremento Lucro", res["incremento_lucro_adicional"], prefix="R$ "), unsafe_allow_html=True)
                st.markdown(metric_card("Custo @Adicional", res["custo_arroba_adicional"], prefix="R$ "), unsafe_allow_html=True)
            
            st.markdown(metric_card("Consumo MS", res["consumo_ms"], suffix=" Kg/Cab/dia"), unsafe_allow_html=True)
            st.markdown(metric_card("PV Final", res["peso_final"]/15, suffix=" @/Cab"), unsafe_allow_html=True)
            st.markdown(metric_card("Eficiência Biológica", (res["consumo_ms"] * res["dias"])/res["arrobas"], suffix=" kgMS/@"), unsafe_allow_html=True)
            st.markdown(metric_card("Rentabilidade Período", res["rentabilidade_periodo"]*100, suffix="%"), unsafe_allow_html=True)
            st.markdown(metric_card("Rentabilidade Mensal", res["rentabilidade_mensal"]*100, suffix="%"), unsafe_allow_html=True)

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
