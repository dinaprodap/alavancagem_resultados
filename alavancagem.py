import streamlit as st
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
            if molecula == "Molecula 1":
                consumo_pv_mol1 = st.number_input(
                    "Consumo (%PV) para Molecula 1",
                    min_value=0.0,
                    value=2.31,
                    step=0.01,
                    key="consumo_pv_mol1",
                    label_visibility="collapsed"
                ) / 100
            else:
                st.markdown(f'<div class="input-field">Consumo (%PV) Mol {molecula[-1]}</div>', unsafe_allow_html=True)
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
    st.markdown('</...(3846 chars omitted)... 
    # Cálculos derivados
    dias = (peso_final_atual - pv_inicial) / gmd_atual
    consumo_ms = consumo_pv_atual * np.mean([pv_inicial, peso_final_atual])
    arrobas = ((peso_final_atual * rendimento_atual/100)/15) - (pv_inicial/30)
    
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
        "rentabilidade_periodo": resultado/(valor_venda_arroba * peso_final_atual),
        "rentabilidade_mensal": ((1 + resultado/(valor_venda_arroba * peso_final_atual))**(1/(dias/30.4))) - 1
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
    st.metric("GDC (KG/DIA)", f"{(((pv_final * rendimento_carcaca/100)) - (pv_inicial/2))/resultados['Molecula 1']['dias']:.3f}")

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
