
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Plataforma iCPO-A Unificada")

st.title("📊 Plataforma iCPO-A • Diagnóstico, Predição e Antifragilidade")

# Criar abas
abas = st.tabs(["🧭 Pré-iCPO", "📈 iCPO Preditivo", "🔮 iCPO-A Antifrágil"])

# ABA 1 — Pré-iCPO
with abas[0]:
    st.header("🧭 Pré-iCPO — Diagnóstico Inicial do Projeto")
    escopo = st.text_area("Descreva o escopo do projeto:")
    recursos = st.slider("Quantos recursos estão disponíveis (1-10)?", 1, 10, 5)
    restricoes = st.multiselect("Quais restrições principais existem?", ["Orçamento", "Prazo", "Equipe", "Tecnologia"])
    criticidade = st.radio("Nível de criticidade do projeto:", ["Baixa", "Média", "Alta"])

    if st.button("Gerar Diagnóstico"):
        st.success("Diagnóstico gerado com base nos dados inseridos:")
        st.markdown(f"**Escopo**: {escopo if escopo else 'não especificado'}")
        st.markdown(f"**Recursos disponíveis**: {recursos}/10")
        st.markdown(f"**Restrições identificadas**: {', '.join(restricoes) if restricoes else 'nenhuma'}")
        st.markdown(f"**Criticidade**: {criticidade}")
        st.info("➡️ Avance para a aba **iCPO** para aplicar o modelo preditivo.")

# ABA 2 — iCPO Preditivo Clássico
with abas[1]:
    st.header("📈 iCPO — Modelo Preditivo com Módulos")

    st.markdown("### Peso de cada módulo:")
    pesos = {
        "Escopo": st.slider("Peso - Escopo", 0, 10, 7),
        "Prazo": st.slider("Peso - Prazo", 0, 10, 6),
        "Custo": st.slider("Peso - Custo", 0, 10, 5),
        "Risco": st.slider("Peso - Risco", 0, 10, 4),
        "Equipe": st.slider("Peso - Equipe", 0, 10, 5),
        "Comunicação": st.slider("Peso - Comunicação", 0, 10, 6),
        "Stakeholders": st.slider("Peso - Stakeholders", 0, 10, 7)
    }

    if st.button("Calcular Resultado Preditivo"):
        score = sum(pesos.values()) / 70 * 100
        st.metric("📊 Índice Preditivo do Projeto", f"{score:.1f} %")
        if score < 50:
            st.error("⚠️ Risco elevado de falha. Reavalie premissas.")
        elif score < 75:
            st.warning("🔶 Projeto em atenção. Exige monitoramento contínuo.")
        else:
            st.success("✅ Boa perspectiva de sucesso.")

# ABA 3 — iCPO-A Antifrágil (módulo quântico)
with abas[2]:
    st.header("🔮 iCPO-A — Módulo Antifrágil com Simulação")

    estados = st.text_input("Estados possíveis (separados por vírgula)", "antecipar, manter, postergar")
    estados_lista = [s.strip() for s in estados.split(",") if s.strip()]
    variavel_colapso = st.text_input("Condição de colapso (ex: desvio >= 10)", "desvio >= 10")
    valor_real = st.number_input("Valor real observado para 'desvio'", value=12)
    contexto = {"desvio": valor_real}

    resultado = estados_lista[0] if eval(variavel_colapso, {}, contexto) else "manter"
    st.success(f"📌 Decisão colapsada: **{resultado}**")

    st.markdown("### Simulação com Amplificação + Ruído")
    n_sim = st.slider("Número de Simulações", 1000, 20000, 10000, step=1000)
    limite_extremo = st.slider("Amplificação de eventos com |impacto| >", 0.0, 2.0, 0.2, step=0.1)
    base = np.random.normal(loc=0, scale=1, size=n_sim)
    pesos = np.where(abs(base) > limite_extremo, 2.0, 1.0)
    amplificado = base * pesos

    intensidade = st.selectbox("Intensidade do ruído", ["leve", "moderada", "intensa"])
    alpha_beta = {"leve": (3, 5), "moderada": (2, 5), "intensa": (1, 3)}
    alpha, beta = alpha_beta[intensidade]
    ruido = np.random.beta(alpha, beta, size=len(amplificado))
    com_ruido = amplificado + ruido * np.sign(np.random.randn(len(amplificado)))

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(amplificado, bins=50, alpha=0.6, label="Amplificado")
    ax.hist(com_ruido, bins=50, alpha=0.6, label="Com Ruído")
    ax.axvline(0, color="gray", linestyle="--")
    ax.set_title("Distribuição de Impactos")
    ax.legend()
    st.pyplot(fig)
