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
moleculas = ["Molecula 1", "Molecula 2", "Molecula 3"]

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
            if molecula == "Molecula 1":
                diferencial_tecnologico = 0.00
            else:
                diferencial_tecnologico = custos[molecula] - custos["Molecula 1"]
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
            st.metric("GMD Mol 2 (kg/dia)", f"{gmd_mol2:.3f}")
        with gmd_col3:
            gmd_mol3 = gmd * 1.118 * 1.02
            st.metric("GMD Mol 3 (kg/dia)", f"{gmd_mol3:.3f}")
        
        # Criar linha para rendimento de carcaça
        rendimento_col1, rendimento_col2, rendimento_col3 = st.columns(3)
        
        with rendimento_col1:
            rendimento_carcaca = st.number_input("Rendimento de Carcaça (%)", min_value=0.0, value=54.89, step=0.01)
        with rendimento_col2:
            rendimento_carcaca_mol2 = rendimento_carcaca * 1.009
            st.metric("Rendimento Carcaça Mol 2 (%)", f"{rendimento_carcaca_mol2:.2f}")
        with rendimento_col3:
            rendimento_carcaca_mol3 = rendimento_carcaca * 1.0264
            st.metric("Rendimento Carcaça Mol 3 (%)", f"{rendimento_carcaca_mol3:.2f}")
        
        # Criar linha para pesos finais
        pv_final_col1, pv_final_col2, pv_final_col3 = st.columns(3)
        
        with pv_final_col1:
            pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
        
        # Calcular dias e pesos finais das outras moléculas
        dias = (pv_final - pv_inicial) / gmd
        pv_final_mol2 = pv_inicial + (gmd_mol2 * dias)
        pv_final_mol3 = pv_inicial + (gmd_mol3 * dias)
        
        with pv_final_col2:
            st.metric("PV Final Mol 2 (Kg/Cab)", f"{pv_final_mol2:.1f}")
        with pv_final_col3:
            st.metric("PV Final Mol 3 (Kg/Cab)", f"{pv_final_mol3:.1f}")
    
        # Criar linha para pesos vivos finais em arrobas
        pv_final_arroba_col1, pv_final_arroba_col2, pv_final_arroba_col3 = st.columns(3)
        
        with pv_final_arroba_col1:
            st.metric("PV Final Mol 1 (@/Cab)", f"{pv_final * rendimento_carcaca / 100 / 15:.2f}")
        with pv_final_arroba_col2:
            st.metric("PV Final Mol 2 (@/Cab)", f"{pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15:.2f}")
        with pv_final_arroba_col3:
            st.metric("PV Final Mol 3 (@/Cab)", f"{pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15:.2f}")
    
    # Criar linha para consumo em %PV
    consumo_pv_col1, consumo_pv_col2, consumo_pv_col3 = st.columns(3)
    
    with consumo_pv_col1:
        consumo_pv_mol1 = st.number_input("Consumo (%PV) para Molecula 1", min_value=0.0, value=2.31, step=0.01) / 100

    # Definir o consumo em porcentagem do peso vivo para cada molécula
    consumo_pv = {
        "Molecula 1": consumo_pv_mol1,
        "Molecula 2": consumo_pv_mol1 * 1.045,
        "Molecula 3": consumo_pv_mol1 * 1.045
    }

    # Exibir consumo em %PV
   # with consumo_pv_col1:
   #     st.metric("Consumo (%PV) Mol 1", f"{consumo_pv['Molecula 1']*100:.2f}%")
    with consumo_pv_col2:
        st.metric("Consumo (%PV) Mol 2", f"{consumo_pv['Molecula 2']*100:.2f}%")
    with consumo_pv_col3:
        st.metric("Consumo (%PV) Mol 3", f"{consumo_pv['Molecula 3']*100:.2f}%")

    # Calcular o consumo MS (Kg/Cab/dia) para cada molécula
    consumo_ms = {
        "Molecula 1": consumo_pv["Molecula 1"] * np.mean([pv_inicial, pv_final]),
        "Molecula 2": consumo_pv["Molecula 2"] * np.mean([pv_inicial, pv_final_mol2]),
        "Molecula 3": consumo_pv["Molecula 3"] * np.mean([pv_inicial, pv_final_mol3])
    }

    # Exibir consumo MS
    consumo_ms_col1, consumo_ms_col2, consumo_ms_col3 = st.columns(3)
    
    with consumo_ms_col1:
        st.metric("Consumo MS Mol 1 (Kg/Cab/dia)", f"{consumo_ms['Molecula 1']:.2f}")
    with consumo_ms_col2:
        st.metric("Consumo MS Mol 2 (Kg/Cab/dia)", f"{consumo_ms['Molecula 2']:.2f}")
    with consumo_ms_col3:
        st.metric("Consumo MS Mol 3 (Kg/Cab/dia)", f"{consumo_ms['Molecula 3']:.2f}")

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
    custeio_mol1 = st.number_input("Custeio (R$/Cab/dia) Mol 1", min_value=0.0, value=15.0, step=0.01, key="custeio_mol1_1")
with params_col2:
    custeio_mol2 = consumo_ms["Molecula 2"] / consumo_ms["Molecula 1"] * custeio_mol1
    st.metric("Custeio (R$/Cab/dia) Mol 2", f"{custeio_mol2:.2f}")
with params_col3:
    custeio_mol3 = consumo_ms["Molecula 3"] / consumo_ms["Molecula 1"] * custeio_mol1
    st.metric("Custeio (R$/Cab/dia) Mol 3", f"{custeio_mol3:.2f}")

# Calcular Custeio Final
custeio_final_col1, custeio_final_col2, custeio_final_col3 = st.columns(3)

with custeio_final_col1:
    custeio_final_mol1 = diferenciais["Molecula 1"] + custeio_mol1
    st.metric("Custeio Final (R$/Cab/dia) Mol 1", f"{custeio_final_mol1:.2f}")
with custeio_final_col2:
    custeio_final_mol2 = diferenciais["Molecula 2"] + custeio_mol2
    st.metric("Custeio Final (R$/Cab/dia) Mol 2", f"{custeio_final_mol2:.2f}")
with custeio_final_col3:
    custeio_final_mol3 = diferenciais["Molecula 3"] + custeio_mol3
    st.metric("Custeio Final (R$/Cab/dia) Mol 3", f"{custeio_final_mol3:.2f}")


# Calcular valores para cada molécula
resultados = {}

for idx, molecula in enumerate(moleculas):
    # Cálculos básicos
    consumo_pv_atual = consumo_pv[molecula]
    
    if idx == 0:  # Molécula 1
        peso_final_atual = pv_final
        gmd_atual = gmd
        rendimento_atual = rendimento_carcaca
    elif idx == 1:  # Molécula 2
        peso_final_atual = pv_final_mol2
        gmd_atual = gmd_mol2
        rendimento_atual = rendimento_carcaca * 1.009
    else:  # Molécula 3
        peso_final_atual = pv_final_mol3
        gmd_atual = gmd_mol3
        rendimento_atual = rendimento_carcaca * 1.0264
    
    # Cálculos derivados
    dias = (peso_final_atual - pv_inicial) / gmd_atual
    consumo_ms_atual = consumo_pv_atual * np.mean([pv_inicial, peso_final_atual])
    arrobas = ((peso_final_atual * rendimento_atual/100)/15) - (pv_inicial/30)
    
    # Cálculos financeiros
    custeio_atual = custeio_mol1 if idx == 0 else (consumo_ms_atual / resultados["Molecula 1"]["consumo_ms"]) * custeio_mol1
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
            "incremento_lucro": ((resultado/resultados["Molecula 1"]["resultado"] - 1) * 100),
            "arrobas_adicionais": arrobas - resultados["Molecula 1"]["arrobas"],
            "receita_adicional": (arrobas - resultados["Molecula 1"]["arrobas"]) * valor_venda_arroba,
            "custo_adicional": custo_periodo - resultados["Molecula 1"]["custeio_final"] * dias,
            "incremento_lucro_adicional": resultado - resultados["Molecula 1"]["resultado"],
            "custo_arroba_adicional": (custo_periodo - resultados["Molecula 1"]["custeio_final"] * dias) / 
                                    (arrobas - resultados["Molecula 1"]["arrobas"])
        })

# Custo da arroba produzida
custo_arroba_col1, custo_arroba_col2, custo_arroba_col3 = st.columns(3)

with custo_arroba_col1:
    custo_arroba_mol1 = (custeio_final_mol1 * dias) / resultados["Molecula 1"]["arrobas"]
    st.metric("Custo da Arroba Mol 1 (R$/@)", f"{custo_arroba_mol1:.2f}")
with custo_arroba_col2:
    custo_arroba_mol2 = (custeio_final_mol2 * dias) / resultados["Molecula 2"]["arrobas"]
    st.metric("Custo da Arroba Mol 2 (R$/@)", f"{custo_arroba_mol2:.2f}")
with custo_arroba_col3:
    custo_arroba_mol3 = (custeio_final_mol3 * dias) / resultados["Molecula 3"]["arrobas"]
    st.metric("Custo da Arroba Mol 3 (R$/@)", f"{custo_arroba_mol3:.2f}")

# Custeio no período da arroba produzida
custeio_periodo_col1, custeio_periodo_col2, custeio_periodo_col3 = st.columns(3)

with custeio_periodo_col1:
    custeio_periodo_mol1 = custeio_final_mol1 * dias
    st.metric("Custeio no Período Mol 1 (R$/Cab)", f"{custeio_periodo_mol1:.2f}")
with custeio_periodo_col2:
    custeio_periodo_mol2 = custeio_final_mol2 * dias
    st.metric("Custeio no Período Mol 2 (R$/Cab)", f"{custeio_periodo_mol2:.2f}")
with custeio_periodo_col3:
    custeio_periodo_mol3 = custeio_final_mol3 * dias
    st.metric("Custeio no Período Mol 3 (R$/Cab)", f"{custeio_periodo_mol3:.2f}")

# Valor das arrobas produzidas
valor_arrobas_col1, valor_arrobas_col2, valor_arrobas_col3 = st.columns(3)

with valor_arrobas_col1:
    valor_arrobas_mol1 = valor_venda_arroba * resultados["Molecula 1"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas Mol 1 (R$/Cab)", f"{valor_arrobas_mol1:.2f}")
with valor_arrobas_col2:
    valor_arrobas_mol2 = valor_venda_arroba * resultados["Molecula 2"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas Mol 2 (R$/Cab)", f"{valor_arrobas_mol2:.2f}")
with valor_arrobas_col3:
    valor_arrobas_mol3 = valor_venda_arroba * resultados["Molecula 3"]["arrobas"]
    st.metric("Valor das Arrobas Produzidas Mol 3 (R$/Cab)", f"{valor_arrobas_mol3:.2f}")

# Resultado (R$/cab)
resultado_col1, resultado_col2, resultado_col3 = st.columns(3)

with resultado_col1:
    resultado_mol1 = valor_arrobas_mol1 - custeio_periodo_mol1
    st.metric("Resultado Mol 1 (R$/Cab)", f"{resultado_mol1:.2f}")
with resultado_col2:
    resultado_mol2 = valor_arrobas_mol2 - custeio_periodo_mol2
    st.metric("Resultado Mol 2 (R$/Cab)", f"{resultado_mol2:.2f}")
with resultado_col3:
    resultado_mol3 = valor_arrobas_mol3 - custeio_periodo_mol3
    st.metric("Resultado Mol 3 (R$/Cab)", f"{resultado_mol3:.2f}")

# Resultado com ágio
resultado_agio_col1, resultado_agio_col2, resultado_agio_col3 = st.columns(3)

with resultado_agio_col1:
    resultado_agio_mol1 = (pv_final * rendimento_carcaca / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol1
    st.metric("Resultado com Ágio Mol 1 (R$/Cab)", f"{resultado_agio_mol1:.2f}")
with resultado_agio_col2:
    resultado_agio_mol2 = (pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol2
    st.metric("Resultado com Ágio Mol 2 (R$/Cab)", f"{resultado_agio_mol2:.2f}")
with resultado_agio_col3:
    resultado_agio_mol3 = (pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15) * valor_venda_arroba - custo_animal_magro - custeio_periodo_mol3
    st.metric("Resultado com Ágio Mol 3 (R$/Cab)", f"{resultado_agio_mol3:.2f}")

# Rentabilidade no período
rentabilidade_periodo_col1, rentabilidade_periodo_col2, rentabilidade_periodo_col3 = st.columns(3)

with rentabilidade_periodo_col1:
    pv_final_arroba_mol1 = pv_final * rendimento_carcaca / 100 / 15
    rentabilidade_periodo_agio_mol1 = resultado_agio_mol1 / (valor_venda_arroba * pv_final_arroba_mol1)
    st.metric("Rentabilidade no Período Mol 1 (%)", f"{rentabilidade_periodo_agio_mol1 * 100:.2f}%")
with rentabilidade_periodo_col2:
    pv_final_arroba_mol2 = pv_final_mol2 * rendimento_carcaca_mol2 / 100 / 15
    rentabilidade_periodo_agio_mol2 = resultado_agio_mol2 / (valor_venda_arroba * pv_final_arroba_mol2)
    st.metric("Rentabilidade no Período Mol 2 (%)", f"{rentabilidade_periodo_agio_mol2 * 100:.2f}%")
with rentabilidade_periodo_col3:
    pv_final_arroba_mol3 = pv_final_mol3 * rendimento_carcaca_mol3 / 100 / 15
    rentabilidade_periodo_agio_mol3 = resultado_agio_mol3 / (valor_venda_arroba * pv_final_arroba_mol3)
    st.metric("Rentabilidade no Período Mol 3 (%)", f"{rentabilidade_periodo_agio_mol3 * 100:.2f}%")

# Rentabilidade mensal
rentabilidade_mensal_col1, rentabilidade_mensal_col2, rentabilidade_mensal_col3 = st.columns(3)

with rentabilidade_mensal_col1:
    rentabilidade_mensal_mol1 = ((1 + rentabilidade_periodo_agio_mol1)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal Mol 1 (%)", f"{rentabilidade_mensal_mol1 * 100:.2f}%")
with rentabilidade_mensal_col2:
    rentabilidade_mensal_mol2 = ((1 + rentabilidade_periodo_agio_mol2)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal Mol 2 (%)", f"{rentabilidade_mensal_mol2 * 100:.2f}%")
with rentabilidade_mensal_col3:
    rentabilidade_mensal_mol3 = ((1 + rentabilidade_periodo_agio_mol3)**(1/(dias/30.4))) - 1
    st.metric("Rentabilidade Mensal Mol 3 (%)", f"{rentabilidade_mensal_mol3 * 100:.2f}%")

# Insights principais
insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    st.metric("GDC Mol 1 (KG/DIA)", f"{(((pv_final * rendimento_carcaca/100)) - (pv_inicial/2))/resultados['Molecula 1']['dias']:.3f}")
    st.metric("GDC Mol 2 (KG/DIA)", f"{(((pv_final_mol2 * rendimento_carcaca_mol2/100)) - (pv_inicial/2))/resultados['Molecula 2']['dias']:.3f}")
    st.metric("GDC Mol 3 (KG/DIA)", f"{(((pv_final_mol3 * rendimento_carcaca_mol3/100)) - (pv_inicial/2))/resultados['Molecula 3']['dias']:.3f}")

with insight_col2:
    st.metric("Arrobas Produzidas Mol 1 (@/Cab)", f"{resultados['Molecula 1']['arrobas']:.2f}")
    st.metric("Arrobas Produzidas Mol 2 (@/Cab)", f"{resultados['Molecula 2']['arrobas']:.2f}")
    st.metric("Arrobas Produzidas Mol 3 (@/Cab)", f"{resultados['Molecula 3']['arrobas']:.2f}")


with insight_col3:
    st.metric("Eficiência Biológica Mol 1 (kgMS/@)", f"{resultados['Molecula 1']['eficiencia_biologica']:.2f}")
    st.metric("Eficiência Biológica Mol 2 (kgMS/@)", f"{resultados['Molecula 2']['eficiencia_biologica']:.2f}")
    st.metric("Eficiência Biológica Mol 3 (kgMS/@)", f"{resultados['Molecula 3']['eficiencia_biologica']:.2f}")
    

# Tab 2 - Resultados
with tab2:
    st.header("📈 Análise Comparativa", divider='rainbow')
    
    # Seção 1: Cards de Indicadores
    st.subheader("Indicadores de Performance")
    
    # Função para criar sparkline
    def create_sparkline(valores, height=50):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            y=valores,
            mode='lines+markers',
            line=dict(color='#2f855a', width=2),
            marker=dict(color='#2f855a', size=6)
        ))
        fig.update_layout(
            height=height,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        return fig

    # Definir métricas
    metricas = [
        ('gmd', 'GMD', 'kg/dia'),
        ('rendimento', 'Rendimento de Carcaça', '%'),
        ('gdc', 'GDC', 'kg/dia'),
        ('eficiencia_biologica', 'Eficiência Biológica', 'kgMS/@'),
        ('arrobas_adicionais', 'Arrobas Adicionais', '@/cab')
    ]

    # Container para os cards
    for metrica, titulo, sufixo in metricas:
        st.markdown(f"### {titulo}")
        
        valores_ref = []  # Para armazenar valores para o sparkline
        
        for molecula in moleculas:
            col1, col2 = st.columns([4, 1])
            
            with col1:
                if metrica == 'gdc':
                    valor = (((resultados[molecula]['peso_final'] * resultados[molecula]['rendimento']/100)) - 
                            (pv_inicial/2))/resultados[molecula]['dias']
                elif metrica == 'arrobas_adicionais':
                    valor = resultados[molecula].get('arrobas_adicionais', 0)
                else:
                    valor = resultados[molecula][metrica]
                
                valores_ref.append(valor)
                st.metric(f"{molecula}", f"{valor:.3f} {sufixo}")
            
            # Mostrar sparkline apenas para moléculas 2 e 3
            if molecula != "Molecula 1":
                with col2:
                    st.plotly_chart(create_sparkline([valores_ref[0], valor]), use_container_width=True)
        
        st.markdown("---")

        col1, col2 = st.columns([3, 1])
        
        with col1:
            for idx, molecula in enumerate(moleculas):
                valores = []
                if metrica == 'gmd':
                    valor = resultados[molecula]['gmd']
                elif metrica == 'rendimento':
                    valor = resultados[molecula]['rendimento']
                elif metrica == 'gdc':
                    valor = (((resultados[molecula]['peso_final'] * resultados[molecula]['rendimento']/100)) - 
                            (pv_inicial/2))/resultados[molecula]['dias']
                elif metrica == 'eficiencia_biologica':
                    valor = resultados[molecula]['eficiencia_biologica']
                elif metrica == 'arrobas_adicionais':
                    valor = resultados[molecula].get('arrobas_adicionais', 0)
                
                valores.append(valor)
                
                # Criar card com valor e sparkline
                col_valor, col_spark = st.columns([2, 1])
                with col_valor:
                    st.metric(f"{molecula}", f"{valor:.3f} {sufixo}")
                if idx > 0:  # Só mostra sparkline para moléculas 2 e 3
                    with col_spark:
                        st.plotly_chart(create_sparkline([resultados['Molecula 1'][metrica], valor]))

    # Seção 2: Gráficos
    st.markdown("---")
    st.subheader("Análise Comparativa")

    # a) Incremento do Lucro (%)
    col1, col2 = st.columns(2)
    with col1:
        fig_incremento = go.Figure()
        incrementos = [0]  # Molécula 1 é referência
        for molecula in moleculas[1:]:
            incrementos.append(resultados[molecula]['incremento_lucro'])
        
        fig_incremento.add_trace(go.Bar(
            x=moleculas,
            y=incrementos,
            name='Incremento do Lucro (%)'
        ))
        fig_incremento.update_layout(
            title='Incremento do Lucro (%)',
            yaxis_title='Incremento (%)',
            showlegend=False
        )
        st.plotly_chart(fig_incremento)

    # b) Incremento Lucro Adicional (R$/cab)
    with col2:
        fig_lucro = go.Figure()
        lucros = [0]  # Molécula 1 é referência
        for molecula in moleculas[1:]:
            lucros.append(resultados[molecula]['incremento_lucro_adicional'])
        
        fig_lucro.add_trace(go.Bar(
            x=moleculas,
            y=lucros,
            name='Incremento Lucro Adicional'
        ))
        fig_lucro.add_trace(go.Scatter(
            x=moleculas,
            y=lucros,
            mode='lines+markers',
            name='Variação'
        ))
        fig_lucro.update_layout(
            title='Incremento Lucro Adicional (R$/cab)',
            yaxis_title='R$/cab',
            showlegend=True
        )
        st.plotly_chart(fig_lucro)

    # c) Custo x Receita Adicional
    fig_custoReceita = go.Figure()
    
    receitas = [0]  # Molécula 1 é referência
    custos = [0]    # Molécula 1 é referência
    for molecula in moleculas[1:]:
        receitas.append(resultados[molecula]['receita_adicional'])
        custos.append(resultados[molecula]['custo_adicional'])
    
    fig_custoReceita.add_trace(go.Bar(
        x=moleculas,
        y=receitas,
        name='Receita Adicional'
    ))
    fig_custoReceita.add_trace(go.Scatter(
        x=moleculas,
        y=custos,
        mode='lines+markers',
        name='Custo Adicional',
        line=dict(color='red')
    ))
    
    fig_custoReceita.update_layout(
        title='Custo x Receita Adicional',
        yaxis_title='R$/cab',
        showlegend=True
    )
    
    st.plotly_chart(fig_custoReceita, use_container_width=True)
