import streamlit as st

abas = st.tabs(["🧩 Metodologia", "📈 Previsão do Preço do Petróleo", "🖥️ Código Utilizado"])

with abas[0]:  # Primeira aba
    st.header("🛠️ Metodologia Adotada para a Solução do Problema")
    import streamlit as st

    st.markdown(
        """
        <div style="background-color:#D3D3D3; padding:15px; border-radius:10px;">
            <h2 style="color:#333333; text-align:center;">Metodologia</h2>
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

    st.title("📌 ARIMA/SARIMAX")

    st.markdown("""
    Os modelos ARIMA (AutoRegressive Integrated Moving Average) e SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous variables) são usados para análise e 
    previsão de séries temporais. 
                        
    """)
    st.write("### Modelo ARIMA")

    st.write("""
    O Modelo ARIMA (p, d, q) é um modelo estatístico para séries temporais. Deve ser aplicado sempre antes da aplicação do SARIMAX, pois visa o tratamento dos dados,
    garantindo maior confiabilidade nas predições.
    O primeiro passo realizado é verificar se a série é estacionária ou não. Para esse modelo de predição, ela deverá ser estacionária, e caso não seja, deerão ser removidas
    as tendências da amostragem.""")

    st.write("")         
    st.write("Para realizar o teste de estacionariedade, é aplicado o teste de Dickey-Fuller (Teste ADF), onde:")
    st.write("")  
    st.write("• Hipótese nula (H₀): A série tem raiz unitária (não é estacionária).")
    st.write("")                   
    st.write("• Hipótese alternativa (H₁): A série é estacionária.")
    st.write("")  
    st.write("• Se o p-valor < 0.05, rejeitamos H₀ e consideramos a série estacionária.")        
    st.write("")  
    st.write("Além desse teste, no modelo ARIMA é definido os parâmetros p, d, q, que são:") 
    st.write("p → Número de defasagens na parte autorregressiva (Usamos PACF para escolher).")
    st.write("")  
    st.write("d → Número de diferenciações para tornar a série estacionária (Usamos Dickey-Fuller).")
    st.write("")  
    st.write("q → Número de defasagens nos erros passados (Usamos ACF para escolher).")

    st.write("### Modelo SARIMAX")
    st.write("""
    O Modelo SARIMAX é uma extensão do SARIMA. É aplicável para dados temporais em que na predição se espera a variação sazonal e/ou tendências.
    Logo é um modelo adequado para nosso projeto, no qual se deseja obter o preço futuro do Barril de Petróleo, que pode ter grandes oscilações entre os períodos impactados por eventos externos.   

    Os parâmetro utilizados para o cálculo foram os que tiveram o melhor retorno na modelagem do ARIMA.       
    """)

    st.write("### Métricas de Performance")
    st.write("""
    Para os modelos de ARIMA/ SARIMAX, uma boa prática é calcular as métricas de performance, para avaliar a confiabilidade do modelo.
    Foram adotas as seguintes:        
    """)         

    st.write("• MAE (Erro Médio Absoluto)")
    st.write("""
    Mede o erro médio entre os valores reais e os previstos. Quanto menor o valor de MAE, mais precisas são as previsões.
    """)
    st.write("") 
    st.write("• MSE (Erro Quadrático Médio)")
    st.write("""
    Calcula a média quadrática dos erros. Quanto maior seu valor, menos confiável serão as predições.
    """)
    st.write("") 
    st.write("• RMSE (Raiz do Erro Quadrático Médio)")
    st.write("""
    É similar ao MSE, mas ajusta a escala do erro para se tornar mais próxima dos dados originais.
    Quanto maior seu valor, menos confiável serão as predições.
    """)  
    st.write("")       
    st.write("• MAPE (Erro Percentual Médio Absoluto)")
    st.write("""
    Mede o erro em relação ao valor real, expressando-o em porcentagem.
    Útil para comparar modelos, pois mostra quão distante, em média, a previsão está do realizado.
    """)
    st.write("") 
    st.write("• WMAPE (Erro Percentual Médio Ponderado)")
    st.write("""
    Funciona de forma semelhante ao MAPE, porém considera a importância valor real ao calcular o erro.
    Aplicável quando há muita variação nos dados, pois evita distorções causadas por outliers.
    """)

with abas[1]:  # Primeira aba

    import streamlit as st
    import pandas as pd
    import plotly.express as px
    from datetime import datetime

    st.markdown(
        """
        <div style="background-color:#D3D3D3; padding:15px; border-radius:10px;">
            <h2 style="color:#333333; text-align:center;">Previsão do Preço do Barril de Petróleo</h2>
            <h3 style="color:#333333; text-align:center;">Utilizando o modelo preditivo ARIMA/SARIMAX</h3>
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


    # URL do CSV
    CSV_URL = "https://raw.githubusercontent.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/main/bases_dados/previsoes.csv"

    # Carregar os dados
    @st.cache_data
    def load_data():
        df = pd.read_csv(CSV_URL)
        df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")  # Converter para datetime com formato ano-mês-dia
        return df

    df = load_data()

    # Definir limite de data máxima
    max_date = datetime(2025, 4, 4)

    # Criar input de data no Streamlit
    data_escolhida = st.date_input("Escolha uma data entre 04/02/2025 e 04/04/2025", max_value=max_date)

    data_escolhida = pd.to_datetime(data_escolhida)  # Converter input para datetime compatível

    # Filtrar os dados até a data escolhida
    df_filtrado = df[df["data"] <= data_escolhida]

    if not df_filtrado.empty:
        # Criar gráfico
        fig = px.line(df_filtrado, x="data", y="preco", title="Evolução do Preço")
        fig.update_traces(mode="lines+markers")
        fig.update_layout(xaxis_title="Data", yaxis_title="Preço")
        
        # Exibir gráfico
        st.plotly_chart(fig)

        # Mostrar o preço exato na data escolhida
        valor_na_data = df[df["data"] == data_escolhida]
        if not valor_na_data.empty:
            preco = valor_na_data.iloc[0]["preco"]
            st.write(f"### A previsão do preço em {data_escolhida.strftime('%d/%m/%Y')} é de **U$ {preco:.2f}**")
        else:
            st.write("Não há preço registrado exatamente para esta data.")
    else:
        st.write("### Nenhum dado disponível para o período selecionado.")

with abas[2]:
    import streamlit as st

    st.title("📄 Notebook utilizado para a modelagem em PDF")

    # Caminho do arquivo PDF (certifique-se de que está no mesmo diretório)
    pdf_path = "codigo.pdf"

    # Abrir o arquivo PDF no navegador
    with open(pdf_path, "rb") as file:
        pdf_bytes = file.read()
        st.download_button("📥 Baixar o PDF", pdf_bytes, "notebook.pdf", "application/pdf")

    # Exibir o PDF dentro da página
    st.components.v1.iframe(f"file:///{pdf_path}", width=700, height=500)
