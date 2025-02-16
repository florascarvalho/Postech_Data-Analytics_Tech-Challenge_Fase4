import streamlit as st

st.markdown(
    """
    <div style="background-color:#D3D3D3; padding:15px; border-radius:10px;">
        <h2 style="color:#333333; text-align:center;">Tech Challenge - Fase 04</h2>
         <h3 style="color:#333333; text-align:center;"> Análise de Dados de Preço do Petróleo Brent</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Divisor de página
st.markdown(
    """
    <hr style="border: 3px solid #007BFF;">
    """,
    unsafe_allow_html=True
)
st.title("📌 Objetivos")

st.markdown("""
Como parte do desenvolvimento das ferramentas estudadas nesta fase, o projeto proposto nos desafia a nos aprofundar no mercado de petróleo.  

As entregas principais estão segmentadas em seis partes, sendo elas:

1. **Criar um Dashboard interativo**  
2. **No Dashboard, criar um storytelling** que traga informações que afetem o preço do barril de petróleo, como por exemplo, situações econômicas, geopolíticas e demanda global  
3. **Elaborar um modelo de Machine Learning** que preveja o preço do barril de petróleo (Brent) diariamente  
4. **Realizar um deploy em produção do modelo**  
5. **Realizar um MVP do modelo em produção utilizando o Streamlit**  
6. **Elaborar um vídeo de até 5 minutos**, explicando o desenvolvimento  
""")
st.title("📌 Metodologia")

st.markdown("""
Para a elaboração do Dashboard foi utilizado o Power BI. 
O Machine Learning foi desenvolvido em Python, utilizando o Google Colab.
O deploy e MVP foram disponibilizados nesta aplicação do Streamlit.
""")
st.write("")
st.write("")
st.markdown("""
### 🔗 Repositório do Projeto no Github, com os códigos utilizados para o projeto:
[Postech_Data-Analytics_Tech-Challenge_Fase4](https://github.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4)
""")