import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Calculadora de Alavancagem")

# Seção de entrada de dados
st.header("Entrada de Dados")

# Entrada para os preços e consumos das moléculas
st.subheader("Valores por Produto")
moleculas = ["Molecula 1", "Modelula 2", "Modelula 3"]
precos = {}
consumos = {}
for molecula in moleculas:
    precos[molecula] = st.number_input(f"Preço de {molecula} (R$/ton)", min_value=0.0, value=5.0, step=0.1)
    consumos[molecula] = st.number_input(f"Consumo de {molecula} (g/cab/dia)", min_value=0, value=250, step=1)

# Demais parâmetros
st.subheader("Outros Parâmetros")
consumo_pv = st.number_input("Consumo (%PV)*", min_value=0.0, value=0.0231, step=0.0001)
consumo_ms = st.number_input("Consumo MS (Kg/Cab/dia)", min_value=0.0, value=10.9725, step=0.01)
pv_inicial = st.number_input("Peso Vivo Inicial (Kg/Cab)", min_value=0, value=390, step=1)
pv_final = st.number_input("Peso Vivo Final (Kg/Cab)", min_value=0, value=560, step=1)
pv_final_arroba = st.number_input("Peso Vivo Final (@/Cab)", min_value=0.0, value=20.49, step=0.01)
gmd = st.number_input("GMD (Kg/dia)*", min_value=0.0, value=1.551, step=0.001)
periodo = st.number_input("Período de Confinamento (dias)", min_value=0.0, value=109.61, step=0.01)
rendimento = st.number_input("Rendimento de Carcaça (%)*", min_value=0.0, value=0.5489, step=0.0001)
gdc = st.number_input("GDC - Ganho Diário de Carcaça (Kg/dia)", min_value=0.0, value=1.025, step=0.001)
arrobas_produzidas = st.number_input("Arrobas Produzidas (@/Cab)", min_value=0.0, value=7.49, step=0.01)
ef_biologica = st.number_input("Eficiência Biológica (kgMS/@ produzida)", min_value=0.0, value=160.52, step=0.01)
custeio_dia = st.number_input("Custeio (R$/Cab/dia)", min_value=0.0, value=15.0, step=0.1)
diferencial_tecnologico = st.number_input("Diferencial Tecnológico (R$/cab/dia)", min_value=0.0, value=0.65, step=0.01)
custeio_final = st.number_input("Custeio Final (R$/Cab/dia)", min_value=0.0, value=16.0, step=0.1)
custo_arroba = st.number_input("Custo da Arroba produzida (R$/@)", min_value=0.0, value=160.0, step=0.1)
custeio_periodo = st.number_input("Custeio no período (R$/Cab)", min_value=0.0, value=1700.0, step=1.0)
valor_venda_arroba = st.number_input("Valor de Venda da arroba (R$/@)", min_value=0.0, value=250.0, step=1.0)
valor_arrobas_produzidas = st.number_input("Valor das Arrobas Produzidas (R$/cab)", min_value=0.0, value=1873.0, step=1.0)
resultado = st.number_input("Resultado (R$/Cab)", min_value=-10000.0, value=173.0, step=1.0)
agio_animal_magro = st.number_input("Ágio para Animal Magro (R$/cab)", min_value=0.0, value=50.0, step=1.0)

# Cálculos automáticos
dados = {
    "Parâmetro": ["Consumo (%PV)", "Consumo MS (Kg/Cab/dia)", "Peso Vivo Inicial", "Peso Vivo Final", "Peso Vivo Final (@/Cab)",
                   "GMD (Kg/dia)", "Período de Confinamento", "Rendimento de Carcaça (%)", "GDC - Ganho Diário de Carcaça (Kg/dia)",
                   "Arrobas Produzidas (@/Cab)", "Eficiência Biológica (kgMS/@ produzida)", "Custeio (R$/Cab/dia)", "Diferencial Tecnológico (R$/cab/dia)",
                   "Custeio Final (R$/Cab/dia)", "Custo da Arroba produzida (R$/@)", "Custeio no período (R$/Cab)",
                   "Valor de Venda da arroba (R$/@)", "Valor das Arrobas Produzidas (R$/cab)", "Resultado (R$/Cab)", "Ágio para Animal Magro (R$/cab)"],
    "Valor": [consumo_pv, consumo_ms, pv_inicial, pv_final, pv_final_arroba, gmd, periodo, rendimento, gdc,
               arrobas_produzidas, ef_biologica, custeio_dia, diferencial_tecnologico, custeio_final, custo_arroba,
               custeio_periodo, valor_venda_arroba, valor_arrobas_produzidas, resultado, agio_animal_magro]
}

# Exibição dos cálculos
st.header("Resultados")
df_resultado = pd.DataFrame(dados)
st.dataframe(df_resultado)
