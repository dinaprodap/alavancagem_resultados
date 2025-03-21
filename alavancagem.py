import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        margin: 5px 0;
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
moleculas = ["FOSBOVI CONF. PLUS", "FOSBOVI CONF. PRIME", "FOSBOVI CONF. PRIME 5.0"]

# Dicionários para armazenar os valores
precos = {}
consumos = {}
custos = {} 
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
            valor_inicial = 4.90 if molecula == "FOSBOVI CONF. PLUS" else (6.48 if molecula == "FOSBOVI CONF. PRIME" else 8.68)
            precos[molecula] = st.number_input(
                f"Preço de {molecula}",
                min_value=0.0,
                value=valor_inicial,
                step=0.1,
                key=f"preco_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[2]:
            valor_consumo = 250 if molecula == "FOSBOVI CONF. PLUS" else (290 if molecula == "FOSBOVI CONF. PRIME" else 260)
            consumos[molecula] = st.number_input(
                f"Consumo de {molecula}",
                min_value=0,
                value=valor_consumo,
                step=1,
                key=f"consumo_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[3]:
            valor_custo = 1.23 if molecula == "FOSBOVI CONF. PLUS" else (1.88 if molecula == "FOSBOVI CONF. PRIME" else 2.26)
            custos[molecula] = valor_custo  # Armazenar custo no dicionário de custos
            st.number_input(
                f"Custo de {molecula}",
                min_value=0.0,
                value=valor_custo,
                step=0.01,
                key=f"custo_tabela_{molecula}",
                label_visibility="collapsed"
            )
        with cols[4]:
            if molecula == "FOSBOVI CONF. PLUS":
                diferencial_tecnologico = 0.00
            else:
                diferencial_tecnologico = custos[molecula] - custos["FOSBOVI CONF. PLUS"]
            diferenciais[molecula] = diferencial_tecnologico  # Armazenar diferencial tecnológico
            st.markdown(f'<div class="diferencial-value">{diferencial_tecnologico:.2f}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-grid
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha produto-container

# Organização em abas
tab1, tab2 = st.tabs(["📝 Entrada de Dados", "📊 Resultados"])

with tab1:
    # Entrada de dados em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dados do Animal")
        
        # Inputs básicos
        pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
        
        # Criar linha para GMD
        gmd_col1, gmd_col2, gmd_col3 = st.columns(3)
        
        with gmd_col1:
            gmd = st.number_input("GMD (kg/dia)", min_value=0.0, value=1.551, step=0.001)
        with gmd_col2:
            gmd_mol2 = gmd * 1.077 * 1.02
            st.metric("GMD FOSBOVI CONF. PRIME (kg/dia)", f"{gmd_mol2:.3f}")
        with gmd_col3:
            gmd_mol3 = gmd * 1.118 * 1.02
            st.metric("GMD FOSBOVI CONF. PRIME 5.0 (kg/dia)", f"{gmd_mol3:.3f}")
        
        # Criar linha para rendimento de carcaça
        rendimento_col1, rendimento_col2, rendimento_col3 = st.columns(3)
        
        with rendimento_col1:
            rendimento_carcaca = st.number_input("Rendimento de Carcaça (%)", min_value=0.0, value=54.89, step=0.01)
        with rendimento_col2:
            rendimento_carcaca_mol2 = rendimento_carcaca * 1.009
            st.metric("Rendimento Carcaça FOSBOVI CONF. PRIME (%)", f"{rendimento_carcaca_mol2:.2f}")
        with rendimento_col3:
            rendimento_carcaca_mol3 = rendimento_carcaca * 1.0264
            st.metric("Rendimento Carcaça FOSBOVI CONF. PRIME 5.0 (%)", f"{rendimento_carcaca_mol3:.2f}")
        
        # Criar linha para pesos finais
        pv_final_col1, pv_final_col2, pv_final_col3 = st.columns(3)
        
        with pv_final_col1:
            pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
        
        # Calcular dias e pesos finais das outras moléculas
        dias = (pv_final - pv_inicial) / gmd
        pv_final_mol2 = pv_inicial + (gmd_mol2 * dias)
        pv_final_mol3 = pv_inicial + (gmd_mol3 * dias)
        
        with pv_final_col2:
            st.metric("PV Final FOSBOVI CONF. PRIME (Kg/Cab)", f"{pv_final_mol2:.1f}")
        with pv_final_col3:
            st.metric("PV Final FOSBOVI CONF. PRIME 5.0 (Kg/Cab)", f"{pv_final_mol3:.1f}")
    
        # Criar linha para pesos vivos finais em arrobas
        pv_final_arroba_col1, pv_final_arroba_col2, pv_final_arroba_col3 = st.columns(3)
        
        with pv_final_arroba_col1:
            st.metric("PV Final FOSBOVI CONF. PLUS (@/Cab)", f"{pv_final * rendimento_carcaca / 100 / 15:.2f}")
        with pv_final_arroba_col2:
            st.metric("PV Final FOSBOVI CONF. PRIME (@/Cab)", f"{pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15:.2f}")
        with pv_final_arroba_col3:
            st.metric("PV Final FOSBOVI CONF. PRIME 5.0 (@/Cab)", f"{pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15:.2f}")
    
    # Criar linha para consumo em %PV
    consumo_pv_col1, consumo_pv_col2, consumo_pv_col3 = st.columns(3)
    
    with consumo_pv_col1:
        consumo_pv_mol1 = st.number_input("Consumo (%PV) para FOSBOVI CONF. PLUS", min_value=0.0, value=2.31, step=0.01) / 100

    # Definir o consumo em porcentagem do peso vivo para cada molécula
    consumo_pv = {
        "FOSBOVI CONF. PLUS": consumo_pv_mol1,
        "FOSBOVI CONF. PRIME": consumo_pv_mol1 * 1.045,
        "FOSBOVI CONF. PRIME 5.0": consumo_pv_mol1 * 1.045
    }

    # Exibir consumo em %PV
    # with consumo_pv_col1:
    #     st.metric("Consumo (%PV) FOSBOVI CONF. PLUS", f"{consumo_pv['FOSBOVI CONF. PLUS']*100:.2f}%")
    with consumo_pv_col2:
        st.metric("Consumo (%PV) FOSBOVI CONF. PRIME", f"{consumo_pv['FOSBOVI CONF. PRIME']*100:.2f}%")
    with consumo_pv_col3:
        st.metric("Consumo (%PV) FOSBOVI CONF. PRIME 5.0", f"{consumo_pv['FOSBOVI CONF. PRIME 5.0']*100:.2f}%")

    # Calcular o consumo MS (Kg/Cab/dia) para cada molécula
    consumo_ms = {
        "FOSBOVI CONF. PLUS": consumo_pv["FOSBOVI CONF. PLUS"] * np.mean([pv_inicial, pv_final]),
        "FOSBOVI CONF. PRIME": consumo_pv["FOSBOVI CONF. PRIME"] * np.mean([pv_inicial, pv_final_mol2]),
        "FOSBOVI CONF. PRIME 5.0": consumo_pv["FOSBOVI CONF. PRIME 5.0"] * np.mean([pv_inicial, pv_final_mol3])
    }

    # Exibir consumo MS
    consumo_ms_col1, consumo_ms_col2, consumo_ms_col3 = st.columns(3)
    
    with consumo_ms_col1:
        st.metric("Consumo MS FOSBOVI CONF. PLUS (Kg/Cab/dia)", f"{consumo_ms['FOSBOVI CONF. PLUS']:.2f}")
    with consumo_ms_col2:
        st.metric("Consumo MS FOSBOVI CONF. PRIME (Kg/Cab/dia)", f"{consumo_ms['FOSBOVI CONF. PRIME']:.2f}")
    with consumo_ms_col3:
        st.metric("Consumo MS FOSBOVI CONF. PRIME 5.0 (Kg/Cab/dia)", f"{consumo_ms['FOSBOVI CONF. PRIME 5.0']:.2f}")

# Parâmetros principais em container separado
st.markdown("---")
st.subheader("Parâmetros Financeiros")

finance_col1, finance_col2, finance_col3 = st.columns(3)

with finance_col1:
    valor_venda_arroba = st.number_input("Valor de Venda da arroba (R$/@)", min_value=0.0, value=340.0, step=0.1, key="valor_venda_arroba_1")
with finance_col2:
    agio_percentual = st.number_input("Ágio para Animal Magro (%)", min_value=0.0, value=5.0, step=0.1, key="agio_percentual_1")
with finance_col3:
    custo_animal_magro = (valor_venda_arroba * (1 + agio_percentual/100)) * (pv_inicial/30)
    st.metric("Custo do Animal Magro (R$/cab)", f"R$ {custo_animal_magro:.2f}")

params_col1, params_col2, params_col3 = st.columns(3)

with params_col1:
    custeio_mol1 = st.number_input("Custeio (R$/Cab/dia) FOSBOVI CONF. PLUS", min_value=0.0, value=15.0, step=0.01, key="custeio_mol1_1")
with params_col2:
    custeio_mol2 = consumo_ms["FOSBOVI CONF. PRIME"] / consumo_ms["FOSBOVI CONF. PLUS"] * custeio_mol1
    st.metric("Custeio (R$/Cab/dia) FOSBOVI CONF. PRIME", f"{custeio_mol2:.2f}")
with params_col3:
    custeio_mol3 = consumo_ms["FOSBOVI CONF. PRIME 5.0"] / consumo_ms["FOSBOVI CONF. PLUS"] * custeio_mol1
    st.metric("Custeio (R$/Cab/dia) FOSBOVI CONF. PRIME 5.0", f"{custeio_mol3:.2f}")

# Calcular Custeio Final
custeio_final_col1, custeio_final_col2, custeio_final_col3 = st.columns(3)

with custeio_final_col1:
    custeio_final_mol1 = diferenciais["FOSBOVI CONF. PLUS"] + custeio_mol1
    st.metric("Custeio Final (R$/Cab/dia) FOSBOVI CONF. PLUS", f"{custeio_final_mol1:.2f}")
with custeio_final_col2:
    custeio_final_mol2 = diferenciais["FOSBOVI CONF. PRIME"] + custeio_mol2
    st.metric("Custeio Final (R$/Cab/dia) FOSBOVI CONF. PRIME", f"{custeio_final_mol2:.2f}")
with custeio_final_col3:
    custeio_final_mol3 = diferenciais["FOSBOVI CONF. PRIME 5.0"] + custeio_mol3
    st.metric("Custeio Final (R$/Cab/dia) FOSBOVI CONF. PRIME 5.0", f"{custeio_final_mol3:.2f}")


# Calcular valores para cada molécula
resultados = {}

for idx, molecula in enumerate(moleculas):
    # Cálculos básicos
    consumo_pv_atual = consumo_pv[molecula]
    
    if idx == 0:  # FOSBOVI CONF. PLUS
        peso_final_atual = pv_final
        gmd_atual = gmd
        rendimento_atual = rendimento_carcaca
    elif idx == 1:  # FOSBOVI CONF. PRIME
        peso_final_atual = pv_final_mol2
        gmd_atual = gmd_mol2
        rendimento_atual = rendimento_carcaca * 1.009
    else:  # FOSBOVI CONF. PRIME 5.0
        peso_final_atual = pv_final_mol3
        gmd_atual = gmd_mol3
        rendimento_atual = rendimento_carcaca * 1.0264
    
    # Cálculos derivados
    dias = (peso_final_atual - pv_inicial) / gmd_atual
    consumo_ms_atual = consumo_pv_atual * np.mean([pv_inicial, peso_final_atual])
    arrobas = ((peso_final_atual * rendimento_atual/100)/15) - (pv_inicial/30)
    
    # Cálculos financeiros
    custeio_atual = custeio_mol1 if idx == 0 else (consumo_ms_atual / resultados["FOSBOVI CONF. PLUS"]["consumo_ms"]) * custeio_mol1
    diferencial_tec = 0 if idx == 0 else diferenciais[molecula]
    custeio_final = custeio_atual + diferencial_tec
    
    custo_periodo = custeio_final * dias
    valor_arrobas = valor_venda_arroba * arrobas
    
    resultado = valor_arrobas - custo_periodo - custo_animal_magro
    
    # Armazenar resultados
    resultados[molecula] = {
        "consumo_pv": consumo_pv_atual,
        "consumo_ms": consumo_ms_atual,
        "peso_final": peso_final_atual,
        "gmd": gmd_atual,
        "dias": dias,
        "rendimento": rendimento_atual,
        "arrobas": arrobas,
        "custeio": custeio_atual,
        "custeio_final": custeio_final,
        "resultado": resultado,
        "rentabilidade_periodo": resultado/(valor_venda_arroba * peso_final_atual),
        "rentabilidade_mensal": ((1 + resultado/(valor_venda_arroba * peso_final_atual))**(1/(dias/30.4))) - 1,
        "eficiencia_biologica": (consumo_ms_atual * dias) / arrobas
    }
    
    if idx > 0:
        resultados[molecula].update({
            "arrobas_adicionais": arrobas - resultados["FOSBOVI CONF. PLUS"]["arrobas"],
            "receita_adicional": (arrobas - resultados["FOSBOVI CONF. PLUS"]["arrobas"]) * valor_venda_arroba,
            "custo_adicional": custo_periodo - resultados["FOSBOVI CONF. PLUS"]["custeio_final"] * dias,
            "incremento_lucro_adicional": resultado - resultados["FOSBOVI CONF. PLUS"]["resultado"],
            "custo_arroba_adicional": (custo_periodo - resultados["FOSBOVI CONF. PLUS"]["custeio_final"] * dias) / 
                                    (arrobas - resultados["FOSBOVI CONF. PLUS"]["arrobas"])
        })

# Custo da arroba produzida
custo_arroba_col1, custo_arroba_col2, custo_arroba_col3 = st.columns(3)

with custo_arroba_col1:
    custo_arroba_mol1 = (custeio_final_mol1 * dias) / resultados["FOSBOVI CONF. PLUS"]["arrobas"]
    st.metric("Custo da Arroba FOSBOVI CONF. PLUS (R$/@)", f"{custo_arroba_mol1:.2f}")
with custo_arroba_col2:
    custo_arroba_mol2 = (custeio_final_mol2 * dias) / resultados["FOSBOVI CONF. PRIME"]["arrobas"]
    st.metric("Custo da Arroba FOSBOVI CONF. PRIME (R$/@)", f"{custo_arroba_mol2:.2f}")
with custo_arroba_col3:
    custo_arroba_mol3 = (custeio_final_mol3 * dias) / resultados["FOSBOVI CONF. PRIME 5.0"]["arrobas"]
    st.metric("Custo da Arroba FOSBOVI CONF. PRIME 5.0 (R$/@)", f"{custo_arroba_mol3:.2f}")

# Custeio no período da arroba produzida
custeio_periodo_col1, custeio_periodo_col2, custeio_periodo_col3 = st.columns(3)

with custeio_periodo_col1:
    custeio_periodo_mol1 = custeio_final_mol1 * dias
    st.metric("Custeio no Período FOSBOVI CONF. PLUS (R$/Cab)", f"{custeio_periodo_mol1:.2f}")
with custeio_periodo_col2:
    custeio_periodo_mol2 = custeio_final_mol2 * dias
    st.metric("Custeio no Período FOSBOVI CONF. PRIME (R$/Cab)", f"{custeio_periodo_mol2:.2f}")
with custeio_periodo_col3:
    custeio_periodo_mol3 = custeio_final_mol3 * dias
    st.metric("Custeio no Período FOSBOVI CONF. PRIME 5.0 (R$/Cab)", f"{custeio_periodo_mol3:.2f}")

# Valor das arrobas produzidas
valor_arrobas_col1, valor_arrobas_col2, valor_arrobas_col3 = st.columns(3)

with valor_arrobas_col1:
    valor_arrobas_mol1 = valor_venda_arroba * resultados["FOSBOVI CONF. PLUS"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas FOSBOVI CONF. PLUS (R$/Cab)", f"{valor_arrobas_mol1:.2f}")
with valor_arrobas_col2:
    valor_arrobas_mol2 = valor_venda_arroba * resultados["FOSBOVI CONF. PRIME"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas FOSBOVI CONF. PRIME (R$/Cab)", f"{valor_arrobas_mol2:.2f}")
with valor_arrobas_col3:
    valor_arrobas_mol3 = valor_venda_arroba * resultados["FOSBOVI CONF. PRIME 5.0"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas FOSBOVI CONF. PRIME 5.0 (R$/Cab)", f"{valor_arrobas_mol3:.2f}")

# Resultado (R$/cab)
resultado_col1, resultado_col2, resultado_col3 = st.columns(3)

with resultado_col1:
    resultado_mol1 = valor_arrobas_mol1 - custeio_periodo_mol1
    st.metric("Resultado FOSBOVI CONF. PLUS (R$/Cab)", f"{resultado_mol1:.2f}")
with resultado_col2:
    resultado_mol2 = valor_arrobas_mol2 - custeio_periodo_mol2
    st.metric("Resultado FOSBOVI CONF. PRIME (R$/Cab)", f"{resultado_mol2:.2f}")
with resultado_col3:
    resultado_mol3 = valor_arrobas_mol3 - custeio_periodo_mol3
    st.metric("Resultado FOSBOVI CONF. PRIME 5.0 (R$/Cab)", f"{resultado_mol3:.2f}")

# Resultado com ágio
resultado_agio_col1, resultado_agio_col2, resultado_agio_col3 = st.columns(3)

with resultado_agio_col1:
    resultado_agio_mol1 = (pv_final * rendimento_carcaca / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol1
    st.metric("Resultado com Ágio FOSBOVI CONF. PLUS (R$/Cab)", f"{resultado_agio_mol1:.2f}")
with resultado_agio_col2:
    resultado_agio_mol2 = (pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol2
    st.metric("Resultado com Ágio FOSBOVI CONF. PRIME (R$/Cab)", f"{resultado_agio_mol2:.2f}")
with resultado_agio_col3:
    resultado_agio_mol3 = (pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol3
    st.metric("Resultado com Ágio FOSBOVI CONF. PRIME 5.0 (R$/Cab)", f"{resultado_agio_mol3:.2f}")

# Rentabilidade no período
rentabilidade_periodo_col1, rentabilidade_periodo_col2, rentabilidade_periodo_col3 = st.columns(3)

with rentabilidade_periodo_col1:
    pv_final_arroba_mol1 = pv_final * rendimento_carcaca / 100 / 15
    rentabilidade_periodo_agio_mol1 = resultado_agio_mol1 / (valor_venda_arroba * pv_final_arroba_mol1)
    st.metric("Rentabilidade no Período FOSBOVI CONF. PLUS (%)", f"{rentabilidade_periodo_agio_mol1 * 100:.2f}%")
with rentabilidade_periodo_col2:
    pv_final_arroba_mol2 = pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15
    rentabilidade_periodo_agio_mol2 = resultado_agio_mol2 / (valor_venda_arroba * pv_final_arroba_mol2)
    st.metric("Rentabilidade no Período FOSBOVI CONF. PRIME (%)", f"{rentabilidade_periodo_agio_mol2 * 100:.2f}%")
with rentabilidade_periodo_col3:
    pv_final_arroba_mol3 = pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15
    rentabilidade_periodo_agio_mol3 = resultado_agio_mol3 / (valor_venda_arroba * pv_final_arroba_mol3)
    st.metric("Rentabilidade no Período FOSBOVI CONF. PRIME 5.0 (%)", f"{rentabilidade_periodo_agio_mol3 * 100:.2f}%")

# Rentabilidade mensal
rentabilidade_mensal_col1, rentabilidade_mensal_col2, rentabilidade_mensal_col3 = st.columns(3)

with rentabilidade_mensal_col1:
    rentabilidade_mensal_mol1 = ((1 + rentabilidade_periodo_agio_mol1)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal FOSBOVI CONF. PLUS (%)", f"{rentabilidade_mensal_mol1 * 100:.2f}%")
with rentabilidade_mensal_col2:
    rentabilidade_mensal_mol2 = ((1 + rentabilidade_periodo_agio_mol2)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal FOSBOVI CONF. PRIME (%)", f"{rentabilidade_mensal_mol2 * 100:.2f}%")
with rentabilidade_mensal_col3:
    rentabilidade_mensal_mol3 = ((1 + rentabilidade_periodo_agio_mol3)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal FOSBOVI CONF. PRIME 5.0 (%)", f"{rentabilidade_mensal_mol3 * 100:.2f}%")

# Insights principais
insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    st.metric("GDC FOSBOVI CONF. PLUS (KG/DIA)", f"{(((pv_final * rendimento_carcaca/100)) - (pv_inicial/2))/resultados['FOSBOVI CONF. PLUS']['dias']:.3f}")
    st.metric("GDC FOSBOVI CONF. PRIME (KG/DIA)", f"{(((pv_final_mol2 * rendimento_carcaca_mol2/100)) - (pv_inicial/2))/resultados['FOSBOVI CONF. PRIME']['dias']:.3f}")
    st.metric("GDC FOSBOVI CONF. PRIME 5.0 (KG/DIA)", f"{(((pv_final_mol3 * rendimento_carcaca_mol3/100)) - (pv_inicial/2))/resultados['FOSBOVI CONF. PRIME 5.0']['dias']:.3f}")

with insight_col2:
    st.metric("Arrobas Produzidas FOSBOVI CONF. PLUS (@/Cab)", f"{resultados['FOSBOVI CONF. PLUS']['arrobas']:.2f}")
    st.metric("Arrobas Produzidas FOSBOVI CONF. PRIME (@/Cab)", f"{resultados['FOSBOVI CONF. PRIME']['arrobas']:.2f}")
    st.metric("Arrobas Produzidas FOSBOVI CONF. PRIME 5.0 (@/Cab)", f"{resultados['FOSBOVI CONF. PRIME 5.0']['arrobas']:.2f}")


with insight_col3:
    st.metric("Eficiência Biológica FOSBOVI CONF. PLUS (kgMS/@)", f"{resultados['FOSBOVI CONF. PLUS']['eficiencia_biologica']:.2f}")
    st.metric("Eficiência Biológica FOSBOVI CONF. PRIME (kgMS/@)", f"{resultados['FOSBOVI CONF. PRIME']['eficiencia_biologica']:.2f}")
    st.metric("Eficiência Biológica FOSBOVI CONF. PRIME 5.0 (kgMS/@)", f"{resultados['FOSBOVI CONF. PRIME 5.0']['eficiencia_biologica']:.2f}")
    

# Tab 2 - Resultados
with tab2:
    st.header("📈 Análise Comparativa", divider='rainbow')
    
    # Seção 1: Cards de Indicadores em colunas
    st.subheader("Indicadores de Performance")
    
    # Criar 5 colunas para os indicadores
    col_gmd, col_rend, col_gdc, col_efic, col_arr = st.columns(5)
    
    # GMD
    with col_gmd:
        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #2c5282; margin-bottom: 10px;">GMD (Kg/dia)</h4>
        """, unsafe_allow_html=True)
        
        for molecula in moleculas:
            st.markdown(metric_card(
                f"{molecula}", 
                resultados[molecula]['gmd'],
                suffix=" kg/dia"
            ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Rendimento de Carcaça
    with col_rend:
        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #2c5282; margin-bottom: 10px;">Rendimento de Carcaça</h4>
        """, unsafe_allow_html=True)
        
        for molecula in moleculas:
            st.markdown(metric_card(
                f"{molecula}", 
                resultados[molecula]['rendimento'],
                suffix=" %"
            ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # GDC
    with col_gdc:
        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #2c5282; margin-bottom: 10px;">GDC (Kg/dia)</h4>
        """, unsafe_allow_html=True)
        
        for molecula in moleculas:
            gdc = (((resultados[molecula]['peso_final'] * resultados[molecula]['rendimento']/100)) - 
                   (pv_inicial/2))/resultados[molecula]['dias']
            st.markdown(metric_card(
                f"{molecula}", 
                gdc,
                suffix=" kg/dia"
            ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Eficiência Biológica
    with col_efic:
        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #2c5282; margin-bottom: 10px;">Eficiência Biológica</h4>
        """, unsafe_allow_html=True)
        
        for molecula in moleculas:
            st.markdown(metric_card(
                f"{molecula}", 
                resultados[molecula]['eficiencia_biologica'],
                suffix=" kgMS/@"
            ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Arrobas Adicionais
    with col_arr:
        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h4 style="color: #2c5282; margin-bottom: 10px;">Arrobas Adicionais</h4>
        """, unsafe_allow_html=True)
        
        for molecula in moleculas:
            valor = resultados[molecula].get('arrobas_adicionais', 0)
            st.markdown(metric_card(
                f"{molecula}", 
                valor,
                suffix=" @/cab"
            ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Seção 2: Gráficos
    st.markdown("---")
    st.subheader("Análise Comparativa")

    # b) Incremento Lucro Adicional (R$/cab)
    col1, col2 = st.columns(2)
    with col1:
        fig_lucro = go.Figure()
        lucros = [0]  # Molécula 1 é referência
        incrementos = [0]  # Para armazenar os percentuais
        
        # Calcula os incrementos percentuais
        resultado_base = resultado_agio_mol1
        if resultado_base < 0:
            incremento_mol2 = (resultado_agio_mol2 / resultado_base - 1) * -1 * 100
            incremento_mol3 = (resultado_agio_mol3 / resultado_base - 1) * -1 * 100
        else:
            incremento_mol2 = (resultado_agio_mol2 / resultado_base - 1) * 100
            incremento_mol3 = (resultado_agio_mol3 / resultado_base - 1) * 100
        incrementos.extend([incremento_mol2, incremento_mol3])
        
        # Adiciona os valores de incremento em R$
        for molecula in moleculas[1:]:
            lucros.append(resultados[molecula]['incremento_lucro_adicional'])
        
        # Adiciona as barras
        fig_lucro.add_trace(go.Bar(
            x=moleculas,
            y=lucros,
            name='Incremento Lucro Adicional',
            marker_color='rgb(71, 135, 198)'  # Azul claro
        ))

        # Adiciona anotações para os valores em R$ e percentual no meio das barras
        for i, (valor, percentual) in enumerate(zip(lucros, incrementos)):
            if valor != 0:  # Apenas para valores não zero
                fig_lucro.add_annotation(
                    x=moleculas[i],
                    y=valor/2,  # Posição do valor em R$
                    text=f"+R$ {abs(valor):.2f}<br>(+{abs(percentual):.0f}%)",  # Valor em R$ e percentual
                    showarrow=False,
                    font=dict(size=14, color='white'),
                    align='center'
                )

        fig_lucro.update_layout(
            title='Incremento Lucro Adicional (R$/cab)',
            yaxis_title='R$/cab',
            showlegend=False
        )
        
        st.plotly_chart(fig_lucro, use_container_width=True, key="plot_incremento_lucro_adicional")

    # c) Custo x Receita Adicional
    with col2:
        fig_custoReceita = go.Figure()

        receitas = [0]  # Molécula 1 é referência
        custos = [0]    # Molécula 1 é referência
        for molecula in moleculas[1:]:
            receitas.append(resultados[molecula]['receita_adicional'])
            custos.append(resultados[molecula]['custo_adicional'])

        # Calcula as variações percentuais (Mol 3 em relação à Mol 2)
        var_receita = ((receitas[2] / receitas[1]) - 1) * 100 if receitas[1] != 0 else 0
        var_custo = ((custos[2] / custos[1]) - 1) * 100 if custos[1] != 0 else 0

        # Barra para Receita Adicional
        fig_custoReceita.add_trace(go.Bar(
            x=moleculas,
            y=receitas,
            name='Receita Adicional',
            text=[
                "",  # Mol 1
                f"R$ {abs(receitas[1]):.2f}",  # Mol 2
                f"R$ {abs(receitas[2]):.2f}<br>({var_receita:.1f}%)"  # Mol 3 com variação
            ],
            textposition='inside',
            textfont=dict(size=14, color='white'),
            insidetextanchor='middle',
            marker_color='rgb(71, 135, 198)'  # Azul claro
        ))

        # Barra para Custo Adicional
        fig_custoReceita.add_trace(go.Bar(
            x=moleculas,
            y=custos,
            name='Custo Adicional',
            text=[
                "",  # Mol 1
                f"R$ {abs(custos[1]):.2f}",  # Mol 2
                f"R$ {abs(custos[2]):.2f}<br>({var_custo:.1f}%)"  # Mol 3 com variação
            ],
            textposition='inside',
            textfont=dict(size=14, color='white'),
            insidetextanchor='middle',
            marker_color='rgb(35, 67, 98)'  # Azul escuro
        ))

        fig_custoReceita.update_layout(
            title='Custo x Receita Adicional',
            yaxis_title='R$/cab',
            showlegend=True,
            barmode='group',
            uniformtext=dict(mode='hide', minsize=10)
        )

        st.plotly_chart(fig_custoReceita, use_container_width=True, key="plot_custo_receita")


    # d) Performance: Arrobas x Custo
    col1, col2 = st.columns(2)
    with col1:
        fig_performance = go.Figure()

        # Preparar dados
        arrobas_base = [7.49] * 3  # 7.49 para todas as moléculas
        arrobas_adicionais = [0]  # Mol 1
        for mol in moleculas[1:]:
            arrobas_adicionais.append(resultados[mol]['arrobas_adicionais'])
        
        # Calcular custo da arroba adicional
        custos_arroba = [0]  # Primeiro valor igual ao da molécula 2
        custos_arroba.extend([
            resultados[mol]['custo_adicional'] / resultados[mol]['arrobas_adicionais'] 
            if resultados[mol]['arrobas_adicionais'] != 0 else 0 
            for mol in moleculas[1:]
        ])

        # Barra para Arrobas Base
        fig_performance.add_trace(go.Bar(
            x=moleculas,
            y=arrobas_base,
            name='Arrobas Base (@/cab)',
            text=[f"{valor:.2f}" for valor in arrobas_base],
            textposition='inside',
            textfont=dict(size=14, color='white'),
            insidetextanchor='middle',
            marker_color='rgb(71, 135, 198)'  # Azul claro
        ))

        # Barra para Arrobas Adicionais
        fig_performance.add_trace(go.Bar(
            x=moleculas,
            y=arrobas_adicionais,
            name='Arrobas Adicionais (@/cab)',
            text=[f"{valor:.2f}" if valor > 0 else "" for valor in arrobas_adicionais],
            textposition='inside',
            textfont=dict(size=14, color='white'),
            insidetextanchor='middle',
            marker_color='rgb(35, 67, 98)'  # Azul escuro
        ))

        # Adicionar linha de custo
        fig_performance.add_trace(go.Scatter(
            x=moleculas,
            y=custos_arroba,
            name='Custo @+ (R$/@)',
            mode='lines+markers+text',
            line=dict(color='orange', width=2),
            marker=dict(size=10, color='orange'),
            text=[f"R${custo:.2f}" for custo in custos_arroba],
            textposition='top center',
            textfont=dict(size=14, color='black'),
            yaxis='y2',
            showlegend=False
        ))

        fig_performance.update_layout(
            title='Performance',
            yaxis_title='Arrobas (@/cab)',
            yaxis2=dict(
                title='Custo @+ (R$/@)',
                overlaying='y',
                side='right'
            ),
            showlegend=True,
            barmode='stack',
            uniformtext=dict(mode='hide', minsize=10)
        )

        st.plotly_chart(fig_performance, use_container_width=True, key="plot_performance")
