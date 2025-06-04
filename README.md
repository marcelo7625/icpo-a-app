# iCPO-A App

Este repositório contém o app completo do modelo preditivo e antifrágil iCPO-A, incluindo:

- Decisão quântica via superposição
- Simulação de eventos extremos com amplificação (Monte Carlo)
- Injeção de ruído assimétrico
- Análise de fragilidade segundo Taleb (|f(-x)| vs f(x))
- Cálculo de curvatura (convexo/côncavo)

## Executar localmente

```bash
pip install -r requirements.txt
streamlit run streamlit_icpoa_completo.py
```

## Publicar no Streamlit Cloud

1. Suba os arquivos para um repositório GitHub
2. Vá até https://share.streamlit.io
3. Crie um novo app usando este repositório