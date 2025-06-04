import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="Simulação Quântico-Inspirada - iCPO-A")

st.title("🔮 Simulação Quântico-Inspirada - iCPO-A")

# Módulo 1: Decisão Quântica (Superposição)
st.header("1. Decisão Quântica (Superposição)")
estados = st.text_input("Estados possíveis (separados por vírgula)", "antecipar, manter, postergar")
estados_lista = [s.strip() for s in estados.split(",") if s.strip() != ""]
variavel_colapso = st.text_input("Condição de colapso (ex: desvio >= 10)", "desvio >= 10")
valor_real = st.number_input("Valor real observado para 'desvio'", value=12)
contexto = {"desvio": valor_real}
resultado = estados_lista[0] if eval(variavel_colapso, {}, contexto) else "manter"
st.success(f"📌 Decisão colapsada: **{resultado}**")

# Módulo 2: Monte Carlo com Amplificação
st.header("2. Simulação Monte Carlo com Amplificação")
n_sim = st.slider("Número de Simulações", 1000, 20000, 10000, step=1000)
limite_extremo = st.slider("Amplificação de eventos com |impacto| >", 0.0, 2.0, 0.2, step=0.1)
base = np.random.normal(loc=0, scale=1, size=n_sim)
pesos = np.where(abs(base) > limite_extremo, 2.0, 1.0)
amplificado = base * pesos

# Módulo 3: Injeção de Ruído
st.header("3. Injeção de Ruído Controlado")
intensidade = st.selectbox("Intensidade do ruído", ["leve", "moderada", "intensa"])
alpha_beta = {"leve": (3, 5), "moderada": (2, 5), "intensa": (1, 3)}
alpha, beta = alpha_beta[intensidade]
ruido = np.random.beta(alpha, beta, size=len(amplificado))
com_ruido = amplificado + ruido * np.sign(np.random.randn(len(amplificado)))

# Gráfico de distribuição
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(amplificado, bins=50, alpha=0.6, label="Amplificado")
ax.hist(com_ruido, bins=50, alpha=0.6, label="Com Ruído")
ax.axvline(0, color="gray", linestyle="--")
ax.set_title("Distribuição de Impactos - iCPO-A")
ax.set_xlabel("Impacto Simulado")
ax.set_ylabel("Frequência")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Módulo 4: Fragilidade e Curvatura
st.header("4. Análise de Fragilidade e Curvatura")
st.write("Função de teste: f(x) = x²")
def f(x): return x**2
x_vals = np.linspace(1, 10, 10)

def analisar_fragilidade_e_curvatura(f, x_vals):
    resultados = []
    for x in x_vals:
        fx = f(x)
        fnx = f(-x)
        f0 = f(0)
        if abs(fnx) > fx:
            tipo = "Frágil"
        elif abs(fnx) < fx:
            tipo = "Antifrágil"
        else:
            tipo = "Robusto"
        curvatura = f(x) + f(-x) - 2 * f0
        forma = "Convexa" if curvatura > 0 else "Côncava" if curvatura < 0 else "Linear"
        resultados.append({
            "x": x,
            "f(x)": fx,
            "f(-x)": fnx,
            "|f(-x)|": abs(fnx),
            "Tipo (Taleb)": tipo,
            "Curvatura": round(curvatura, 4),
            "Forma": forma
        })
    return pd.DataFrame(resultados)

df_resultado = analisar_fragilidade_e_curvatura(f, x_vals)
st.dataframe(df_resultado)

# Gráfico da função f(x) e f(-x)
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(x_vals, [f(x) for x in x_vals], label="f(x)", marker="o")
ax2.plot(x_vals, [f(-x) for x in x_vals], label="f(-x)", marker="x")
ax2.axhline(0, color="gray", linestyle="--")
ax2.set_title("Resposta Simétrica - f(x) e f(-x)")
ax2.set_xlabel("x (variação)")
ax2.set_ylabel("f(x)")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)