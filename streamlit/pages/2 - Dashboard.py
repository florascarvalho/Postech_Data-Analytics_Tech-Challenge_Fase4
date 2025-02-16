
import streamlit as st

st.markdown(
    """
    <div style="background-color:#D3D3D3; padding:15px; border-radius:10px;">
        <h2 style="color:#333333; text-align:center;">Dashboard</h2>
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

st.title("📌 Apresentação dos Dados")

st.markdown("""
O Dashboard com informações evolutivas do preço de barril de petróleo (Brent), foi desenvolvido em Power BI. A fonte de dados principal, contendo os valores abertos por data,
foram disponibilizados pelo [IPEA](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view), e compreendem o período entre 20/05/1987 e 03/02/2025.

 Para melhor compreensão da variação de preços entre os períodos, foram incluídos os eventos do período em que afetaram diretamente os valores praticados. Eles serão abordados mais detalhadamente ainda nessa seção,
mas de forma geral, são fatores como conflitos armados, crises econômicas e questões geopolíticas.
            
""")

st.title("📌 Navegabilidade")

st.markdown("""
O Dashboard apresenta uma interface simples e intuitiva para o usuário final, e pode ser acessado através [deste link](https://github.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/tree/main/dashboard) disponível no Github.
Nele, é possível acompanhar a evolução de preços, tal como os valores de preços médio, mínimo e máximo de determinados períodos.     
""")
# URL da imagem no GitHub 
image_url = "https://raw.githubusercontent.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/main/streamlit/imagens/Evolutivo_1.jpg"
# Exibindo a imagem
st.image(image_url, caption="Análise do Preço do Petróleo - Visão Geral", use_column_width=True)

st.markdown("""
É possível filtrar o período desejado usando os parâmetros de Ano, Mês e Dia. Os filtros estão habilitados para múltipla seleção.        
""")
# URL da imagem no GitHub 
image_url_2 = "https://raw.githubusercontent.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/main/streamlit/imagens/Evolutivo_2.jpg"
# Exibindo a imagem
st.image(image_url_2, caption="Análise do Preço do Petróleo - Filtro de ano", use_column_width=True)

st.markdown("""
Da mesma forma, é possível selecionar os eventos em que se deseja verificar os preços e suas interferências. É possível filtrar mais de um.        
""")
# URL da imagem no GitHub 
image_url_3 = "https://raw.githubusercontent.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/main/streamlit/imagens/Evolutivo_3.jpg"
# Exibindo a imagem
st.image(image_url_3, caption="Análise do Preço do Petróleo - Filtro por Evento", use_column_width=True)

st.markdown("""
No Dashboard é possível ver a listagem dos eventos por ano. Quando aplicado filtro de data,por exemplo, a tabela retornará apenas os eventos daquele período.
""")
# URL da imagem no GitHub 
image_url_4 = "https://raw.githubusercontent.com/florascarvalho/Postech_Data-Analytics_Tech-Challenge_Fase4/main/streamlit/imagens/Evolutivo_4.jpg"
# Exibindo a imagem
st.image(image_url_4, caption="Amostra de Eventos considerados", use_column_width=True)


st.title("📌 Eventos Considerados")
st.markdown("""
Ao todo, foram considerados 09 eventos para nossa análise. Todos tiveram uma impotância em relação à alteração do preço do barril de petróleo - seja para aumentar ou diminuir o preço - e logo abaixo recebem
breve descrição.
""")

# Guerra Irã-Iraque (1980-1988)
st.write("### • Guerra Irã-Iraque (1980-1988)")
st.write("""
A guerra entre o Irã e o Iraque foi um conflito motivado por disputas territoriais e tensões políticas regionais. O Irã, após a Revolução Islâmica de 1979, entrou em confronto com o governo iraquiano, que procurava expandir seu poder e território. 
O conflito resultou milhares de mortes e não alterou significativamente as fronteiras ou o poder na região entre os dois países.
""")

# Guerra do Golfo (1990-1991)
st.write("### • Guerra do Golfo (1990-1991)")
st.write("""
 O Iraque invadiu o Kuwait, gerando uma resposta internacional coordenada por uma coalizão liderada pelos Estados Unidos. A intervenção militar foi justificada pelo desejo de restaurar a soberania do Kuwait 
e garantir o acesso contínuo ao petróleo. A guerra resultou na retirada das forças iraquianas, mas também em grande destruição no Iraque e aumento da presença militar dos EUA no Oriente Médio.
""")

# Invasão do Iraque (2003)
st.write("### • Invasão do Iraque (2003)")
st.write("""
A invasão do Iraque pelos Estados Unidos e seus aliados foi apresentada como uma ação para remover Saddam Hussein, em resposta aos atendados ocorridos em 11 de setembro de 2001. Contudo, muitos críticos 
apontaram que o verdadeiro motivo era garantir o controle sobre os recursos naturais do Iraque, especialmente o petróleo, e expandir a influência ocidental na região. A invasão e suas consequências geraram uma instabilidade prolongada e o 
crescimento de grupos extremistas, como o Estado Islâmico.
""")

# Ocupação do Iraque (2003-2011)
st.write("### • Ocupação do Iraque (2003-2011)")
st.write("""
Após a queda de Saddam Hussein, o Iraque foi ocupado por forças internacionais lideradas pelos Estados Unidos. A ocupação resultou em uma resistência interna significativa, 
em uma guerra civil e no fortalecimento de grupos extremistas. As tensões e o impacto social da ocupação ainda afetam o país até hoje.
""")

# Colapso do Lehman Brothers (2008)
st.write("### • Colapso do Lehman Brothers (2008)")
st.write("""
O colapso do banco Lehman Brothers foi um dos eventos centrais na crise financeira global de 2008. Ele revelou falhas estruturais nos mercados financeiros e na regulação do 
sistema bancário, resultando em uma recessão global. Embora o impacto tenha sido global, os efeitos mais severos foram sentidos em economias que dependiam 
do sistema financeiro americano, aumentando também o nível de desemprego.
""")

# Primavera Árabe (2010-2012)
st.write("### • Primavera Árabe (2010-2013)")
st.write("""
A Primavera Árabe foi uma série de movimentos populares que ocorreu em  alguns países árabes, motivados por insatisfação da população com os autoritários. 
As revoltas buscavam mais liberdade política e melhores condições de vida. Em alguns casos, como na Tunísia e no Egito, as manifestações levaram à queda de seus líderes, em outros - como na Síria- resultaram em conflitos prolongados e crises humanitárias.
""")

# Queda dos Preços do Petróleo (2014-2016)
st.write("### • Queda dos Preços do Petróleo (2014-2016)")
st.write("""
A queda nos preços do petróleo entre 2014 e 2016 teve um grande impacto nas economias que dependem desse commodity, como muitos países do Oriente Médio, Rússia e Venezuela. 
A desaceleração da economia global e o aumento da produção de petróleo dos EUA contribuíram para uma crise no setor, afetando principalmente as populações mais vulneráveis desses países, que enfrentaram uma instabilidade econômica.
""")

# Pandemia de COVID-19 (2019-2023)
st.write("### • Pandemia de COVID-19 (2019-2023)")
st.write("""
A pandemia de COVID-19 teve um impacto global profundo, com a propagação do vírus afetando a saúde pública, a economia e as relações sociais em todos os continentes. 
As consequências econômicas e sociais ainda estão sendo sentidas, e nesse recorte do setor petrolífero, é possível ver uma queda acentuada no início da pandemia, seguido de uma
elevação dos valores no primeiro semestre de 2022.
""")

# Invasão da Ucrânia pela Rússia (2022-Atualmente)
st.write("### • Invasão da Ucrânia pela Rússia (2022-Atualmente)")
st.write("""
A invasão da Ucrânia pela Rússia, em 2022, gerou um conflito em grande escala, com milhares de mortes e uma crise humanitária que afetou os paises envolvidos.
A guerra expôs as tensões geopolíticas entre a Rússia, Ucrânia e os países ocidentais, além de afetar a segurança energética e alimentar global.
""")