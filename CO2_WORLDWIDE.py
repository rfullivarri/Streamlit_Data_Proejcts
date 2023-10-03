import requests
import os
import pandas as pd
import numpy as np
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression
from  PIL import  Image as Pillow
import plotly.express as px
from Data_Analisis_CO2 import data_pre_code, primeros_insights, barchart_countrys,area_chart_code,regression_model,histograma_code,ajuste_code

#Set up web
st.set_page_config(page_title="CO2 WORDLWIDE ANALISIS",
                    page_icon="🌱",
                    layout="wide")

email_address= "rfullivarri22@gmail.com"
url_animacion= "https://lottie.host/2d201ac4-c25d-48cb-933a-3049ac56335b/fgHSZdOUxA.json"
url_animacion2="https://lottie.host/f75d7b0d-c780-4eea-ab6c-12bb50e05e86/7zuGX4AEBT.json"
url_animacion3="https://lottie.host/2d7bb8cf-97a8-4edc-b8d4-0f06d644a265/kU7yIyXa6B.json"
url_animacion4="https://lottie.host/dbf8d8a4-2eb6-4234-8c34-235c0e7d0bcd/lJfUkLvumW.json"
url_animacion5="https://lottie.host/e9b9a412-7bc0-4c0c-9357-eb37b5dc6b43/eUrtcdExIJ.json"
#pdf_url= r"DataSets/CV-Ramiro Fernandez de Ullivarri PMO (1).pdf"

#Animaciones
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie= load_lottieurl(url_animacion)
lottie2= load_lottieurl(url_animacion2)
lottie3= load_lottieurl(url_animacion3)
lottie4= load_lottieurl(url_animacion4)
lottie5= load_lottieurl(url_animacion5)


#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/co2ww.css")

#MENU
def on_change(key):
    selection = st.session_state[key]

    return str(selection)
menuopt = ["Home","Data & Insight","About Me"]
selected5 = option_menu(None, options=menuopt,
                        icons=['house', 'data', "person"],#, 'phone'],
                        on_change=on_change, key='menu_5', orientation="horizontal")








#HOME
def Home():
    home= st.container()
    titulo,logo=st.columns((4,1))
    titulo.write("##")
    titulo.write("##")
    titulo.markdown(f"<h1 style='text-align: center; font-size: 70px;'>CO2 WORLDWIDE ANALYSIS</h1>", unsafe_allow_html=True)
    with logo:
        st_lottie(lottie4,width=150)
    #home.title("CO2 WORDLWIDE ANALSIS 🌎")
    st.header("Por que")
    descripcion="""CO2 WORLDWIDE tiene como mision explorar la situacion actual del dioxido
      de carbono en el mundo, un gas que afecta directamente al planeta. Con la mirada puesta en la 
      increible cifra de mas de 40.000 millones  de toneladas de CO2 emitidas anualmente, el objetivo 
      principal de este analisis es destacar la importancia de comprender estos numeros atraves de datos 
      y analisis solidos. Se busca adentrarse en el facinante mundo de los datos para revelar patrones y 
      tendencias que aclararan la problemantica del CO2 y su impracto en el entorno"""
    st.markdown(f'<div style="text-align: justify">{descripcion}</div>',unsafe_allow_html=True)
    st.write("##")
    kaggle1,pytt2,text21= st.columns((1,0.5,4))
    kaggle1.image(r"Images/kaggle_logo_icon_168474.png")
    #pytt2.write("##")
    pytt2.image(r"Images/Python-logo-notext.svg.png",width=60)
    k_y_text="""Se utilizará una base de datos de Kaggle y Python como lenguaje de programación para llevar
      a cabo el análisis de las emisiones de CO2 de varios países. Esta combinación permitirá adquirir
        experiencia y mejorar habilidades en ciencia de datos, al mismo tiempo que enriquecerá el portafolio 
        profesional
                """
    text21.markdown(f'<div style="text-align: justify">{k_y_text}</div>',unsafe_allow_html=True)
    
    st.write("---")

    values =st.container()
    values.title("Objetivos 🎯")
    valor1, valor2, valor3 = st.columns(3)
    with valor1:
        st.header("Analisis 👩‍💻")
        text1="""Aprenderemos a realizar un análisis de datos de alta calidad utilizando Python. 
                 Esto implica explorar y procesar datos de manera rigurosa, aplicar técnicas estadísticas,
                  y utilizar herramientas como Pandas, Numpy y Plotly para obtener información valiosa. 
                 Queremos convertirnos en expertos en la manipulación de datos y en la generación de 
                 resultados confiables."""
        st.markdown(f'<div style="text-align: justify">{text1}</div>',unsafe_allow_html=True)

    with valor2:
        st.header("Insights ✨")
        text2="""Se buscará obtener conocimientos y conclusiones valiosas sobre el dióxido de carbono (CO2)
          a través de los análisis realizados. El objetivo es descubrir patrones ocultos, identificar 
          tendencias preocupantes o alentadoras y, en última instancia, contribuir al entendimiento de la
            importancia de controlar las emisiones de CO2 para el bienestar del planeta."""
        st.markdown(f'<div style="text-align: justify">{text2}</div>',unsafe_allow_html=True)

    with valor3:
        st.header("Difusión 🤲")
        text3= """La intención es informar y educar a la comunidad acerca de los hallazgos y conclusiones
          obtenidos mediante el análisis de datos. Esto incluirá la creación de contenido educativo,
            la presentación de gráficos impactantes y la disponibilidad del código realizado en Python 
            para su reproducción y revisión en caso de ser necesario."""
        st.markdown(f'<div style="text-align: justify">{text3}</div>',unsafe_allow_html=True)

    st.write("---")
    datos =st.container()
    datos.markdown("<h1 style='text-align: center; font-size: 60px;'>Como se va a hacer 📊</h1>", unsafe_allow_html=True)
    #datos.title("Como vamos a hacerlo 📊")
    datos.write("##")
    datos1, datos2 = st.columns(2)
    with datos1:
        datos1.write("##")
        textdata="""El análisis de datos comenzará con una exploración exhaustiva del conjunto de datos, 
        identificando su tamaño y las variables más relevantes. 
        Luego, se examinarán las correlaciones dentro de los datos y se emplearán gráficos 
        para ilustrar los patrones y obtener conocimientos. 
                 """
        st.markdown(f'<div style="text-align: justify; font-size: 22px">{textdata}</div>',unsafe_allow_html=True)
    with datos2:
        st_lottie(lottie,height= 300)
    st.write("##")
    st.write("##")
    datos3, datos4 = st.columns(2)
    with datos3:
        st_lottie(lottie2,height= 200)
    textdata2="""En cada etapa, se proporcionarán códigos de Python utilizando bibliotecas como
      Pandas, Numpy, Plotly y Streamlit para facilitar el seguimiento y el aprendizaje.
                """
    #datos4.write("##")
    #datos4.write("##")
    datos4.markdown(f'<div style="text-align: justify; font-size: 22px">{textdata2}</div>',unsafe_allow_html=True)      
    
    code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
    datos4.markdown(code_style, unsafe_allow_html=True)
    datos4.code("print('Hello Wolrd')",language="python")
  











#DATA INSIGHTS
def Data_Insight():
    values =st.container()
    values.title("Data & Insight 🚀")
    values.markdown("<div style='text-align: center; font-size: 20px;'>En primer lugar, se preparará la base de datos para su posterior análisis. Esto implicará la limpieza de datos, la corrección de tipos de datos y la eliminación de comas, puntos y símbolos ($, %, &, etc.)<div>", unsafe_allow_html=True)
    values.write("##")
    #EXPANCION CODIGO
    with values.expander("Ver Codigo <> Depuracion de DB"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(data_pre_code,language="python")
    #DF DEPURADO
    df= pd.read_csv(r"CO2_WORLDWIDE_90_23.csv")
    st.markdown("<h1 style='text-align: right; font-size: 13px;'>*Los valores None no los necesitamos para este analisis*</h1>", unsafe_allow_html=True)
    st.dataframe(df)

#PRIMEROS INSIGHTS
    st.header(""" Primeros Insights 👨‍💻""")
    st.write("##")
    empty1,insight_1, insight_2, insight_3, empty2= st.columns((0.5,2,2,2,0.5))
    empty1.empty()
    style_metric_cards( background_color = "#66806A",
                        border_size_px = 1,
                        border_color= "#FFF1AF",
                        border_radius_px= 9,
                        border_left_color= "#FFF1AF",
                        box_shadow = False)
    with insight_1:
        #Countrys
        centrar_texto_css = """<style>.centrar-texto {text-align: center;}</style>"""
        insight_1.markdown(centrar_texto_css, unsafe_allow_html=True)
        insight_1.metric(label="**COUNTRIES**", value=f'{len(df["Country"].unique())}', delta="FOR ANALYSIS", delta_color="off")

    with insight_2:
        #CO2 (mT)
        centrar_texto_css = """<style>.centrar-texto {text-align: center;}</style>"""
        insight_2.markdown(centrar_texto_css, unsafe_allow_html=True)
        co2_23= str(round(df["Co2-Emissions 2023"].sum(),1))
        delta=str(round(df["Co2-Emissions 2021"].sum()-df["Co2-Emissions 2023"].sum(),1))
        insight_2.metric(label="**CO2 WORLDWIDE (Millons Tn) in 2023**", value=co2_23, delta=f'{delta} (2021)*',delta_color="inverse")

    with insight_3:
        #80/20
        centrar_texto_css = """<style>.centrar-texto {text-align: center;}</style>"""
        insight_3.markdown(centrar_texto_css, unsafe_allow_html=True)
        insight_3.metric(label="**COUNTRIES WHO MAKE 80/20**", value="30" , delta="OF CO2 WORLDWIDE",delta_color="off")
    empty2.empty()
    st.write("##")
    #EXPANCION CODIGO
    with st.expander("Ver Codigo </> Insight"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(primeros_insights,language="python")

#GRAFICO1
    st.write("##")
    column_1 , column_2= st.columns(2)
    column_1.subheader("""TOP 10 paises de **mayor** emision de CO2 2023🍂""")
    df_co2_23_by_country= (df.sort_values(by="Co2-Emissions 2023",ascending=False)).set_index("Country").head(10)
    df_co2_23_by_country = df_co2_23_by_country[::-1] #invertir el df para grafico de barras
    #Crear el gráfico de barras verticales con Plotly
    fig = px.bar(df_co2_23_by_country, x="Co2-Emissions 2023", y=df_co2_23_by_country.index, orientation="h",
             text="Co2-Emissions 2023", color_discrete_sequence=["#FFF1AF"])
    #Personaliza la apariencia del gráfico
    fig.update_layout(  xaxis_title="Co2-Emissions 2023 (Tn)",
                        yaxis_title="Country",
                        paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
                        plot_bgcolor="rgba(0,0,0,0)",   # Fondo transparente
                        font=dict(color="white"))       # Color de las etiquetas en blanco
    #Muestra el gráfico en Streamlit
    column_1.plotly_chart(fig, use_container_width=True)
#GRAFICO2
    st.write("##")
    column_2.subheader("""TOP 10 paises de **menor** emision de CO2 2023🍃""")
    df_co2_23_by_country= (df.sort_values(by="Co2-Emissions 2023",ascending=False)).set_index("Country").tail(10)
    #df_co2_23_by_country = df_co2_23_by_country[::-1] #invertir el df para grafico de barras
    #Crear el gráfico de barras verticales con Plotly
    fig2 = px.bar(df_co2_23_by_country, x="Co2-Emissions 2023", y=df_co2_23_by_country.index, orientation="h",
             text="Co2-Emissions 2023", color_discrete_sequence=["#FFF1AF"])
    #Personaliza la apariencia del gráfico
    fig2.update_layout(  xaxis_title="Co2-Emissions 2023 (Tn)",
                        yaxis_title="Country",
                        paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
                        plot_bgcolor="rgba(0,0,0,0)",   # Fondo transparente
                        font=dict(color="white"))       # Color de las etiquetas en blanco
    # Muestra el gráfico en Streamlit
    column_2.plotly_chart(fig2, use_container_width=True)
    #EXPANCION CODIGO
    with st.expander("Ver Codigo </> Bar Chart"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(barchart_countrys,language="python")
#GRAFICO3
    st.write("##")
    st.write("##")
    st.subheader("""Crecimiento de CO2 desde 1990 a 2023""")

    area_chart=df[['Co2-Emissions 2023','Co2-Emissions 2021', 'Co2-Emissions 2020','Co2-Emissions 2019', 
           'Co2-Emissions 2018', 'Co2-Emissions 2017','Co2-Emissions 2016', 'Co2-Emissions 2015',
           'Co2-Emissions 2014','Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
           'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008','Co2-Emissions 2007',
           'Co2-Emissions 2006', 'Co2-Emissions 2005','Co2-Emissions 2004', 'Co2-Emissions 2003', 
           'Co2-Emissions 2002','Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
           'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996','Co2-Emissions 1995', 
           'Co2-Emissions 1994', 'Co2-Emissions 1993','Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']]

    col_name= {'Co2-Emissions 2023':'2023','Co2-Emissions 2021':'2021', 'Co2-Emissions 2020':'2020',
               'Co2-Emissions 2019':'2019', 'Co2-Emissions 2018':'2019', 'Co2-Emissions 2017':'2017',
               'Co2-Emissions 2016':'2016', 'Co2-Emissions 2015':'2015', 'Co2-Emissions 2014':'2014',
               'Co2-Emissions 2013':'2013', 'Co2-Emissions 2012':'2012', 'Co2-Emissions 2011':'2011',
               'Co2-Emissions 2010':'2010', 'Co2-Emissions 2009':'2009', 'Co2-Emissions 2008':'2008',
               'Co2-Emissions 2007':'2007', 'Co2-Emissions 2006':'2006', 'Co2-Emissions 2005':'2005',
               'Co2-Emissions 2004':'2004', 'Co2-Emissions 2003':'2003', 'Co2-Emissions 2002':'2002',
               'Co2-Emissions 2001':'2001', 'Co2-Emissions 2000':'2000', 'Co2-Emissions 1999':'1999',
               'Co2-Emissions 1998':'1998', 'Co2-Emissions 1997':'1997', 'Co2-Emissions 1996':'1996',
               'Co2-Emissions 1995':'1995', 'Co2-Emissions 1994':'1994', 'Co2-Emissions 1993':'1993',
               'Co2-Emissions 1992':'1992', 'Co2-Emissions 1991':'1991', 'Co2-Emissions 1990':'1990'}

    area_chart.rename(columns=col_name,inplace=True)
    area_chart=area_chart.sum().T

    fig3 = px.area(area_chart, color_discrete_sequence=["#FFF1AF"],log_y=True)

    fig3.update_layout( xaxis_title="years",
                        yaxis_title="CO2",
                        paper_bgcolor="rgba(0,0,0,0)",  
                        plot_bgcolor="rgba(0,0,0,0)",   
                        font=dict(color="white"))       

    st.plotly_chart(fig3, use_container_width=True)
    #EXPANCION CODIGO
    with st.expander("Ver Codigo </> Area Chart"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(area_chart_code,language="python")
    st.write("##")
    st.write("##")
#MATRIZ DE CORRELACION
    st.header("Next steps 🧭")
    st.write("##")
    st.markdown("<div style='text-align: center; font-size: 20px;'>Para una comprensión más profunda de los datos, se ha generado una matriz de correlación que revela las relaciones lineales entre las variables.<div>", unsafe_allow_html=True)
    columas__mx_corr = ['Density\n (P/Km2)', 'Agricultural Land( %)',
                        'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
                        'Co2-Emissions 2023', 'CPI', 'CPI Change (%)',
                        'Fertility Rate', 'Forested Area (%)',
                        'Gasoline Price', 'GDP', 'Infant mortality','Minimum wage',
                        'Life expectancy', 'Maternal mortality ratio','Population',
                        'Population: Labor force participation (%)', 'Tax revenue (%)',
                        'Unemployment rate', 'Urban_population']

    #adapramos las columnas que solo son numericas (int o float)
    df_corr = df[columas__mx_corr]
    df_corr = df_corr.apply(pd.to_numeric, errors='coerce')
    correlation_matrix = df_corr.corr()
    # Crea un gráfico de correlación con Plotly
    fig = make_subplots(rows=1, cols=1)
    # Añade la matriz de correlación como un heatmap
    heatmap = go.Heatmap(z=correlation_matrix.values,
                         x=correlation_matrix.columns,
                         y=correlation_matrix.columns,
                         colorscale='Plasma')
    fig.add_trace(heatmap)
    # Personaliza el diseño del gráfico
    fig.update_layout(
        title="Matriz de Correlación",
        xaxis_title="Variables",
        yaxis_title="Variables",
        font=dict(color="black"),  # Color del texto
        width=700,  # Ancho personalizado
        height=700)
    
    fig.update_yaxes(tickangle=45)  # Rota las etiquetas del eje y
    fig.update_xaxes(tickangle=45)  # Rota las etiquetas del eje x
    # Muestra el gráfico en Streamlit
    corr= st.container()
    corr.plotly_chart(fig, use_container_width=True)

#RESULTADO DE MATRIZ DE CORRELACION
    colu1, colu2 =st.columns(2)
    correlat="""Se ha identificado que 3 variables están fuertemente correlacionadas con las emisiones
      de CO2."""
    correlat2="""- A mayor GDP mayor emision de CO2."""
    correlat4="""- A mayor poplacion x pais, mayor emision de CO2."""
    correlat5="""- A mayor cocentracion urbana es aun mayor la emision de CO2."""

    correlat3="""Por razones prácticas, solo se analizará la relación entre CO2 y el Producto Interno Bruto (GDP)
        de un país utilizando un Modelo de Regresión Lineal. Además, se evaluará la precisión del modelo
          para determinar su confiabilidad."""
    colu1.write("##")
    colu1.write("##")
    colu1.markdown(f"<div style='text-align: justify; font-size: 20px;'>{correlat}</div>", unsafe_allow_html=True)
    colu1.write("##")
    colu1.markdown(f"<div style='text-align: left; font-size: 20px;'>{correlat2}</div>", unsafe_allow_html=True)
    colu1.markdown(f"<div style='text-align: left; font-size: 20px;'>{correlat4}</div>", unsafe_allow_html=True)
    colu1.markdown(f"<div style='text-align: left; font-size: 20px;'>{correlat5}</div>", unsafe_allow_html=True)
    colu1.write("##")
    colu1.markdown(f"<div style='text-align: justify; font-size: 20px;'>{correlat3}</div>", unsafe_allow_html=True)
    
    colu2.image(r"Images/White Gradient Creative Professional Modern Business Company Corporate Presentation Template.png",width=350)
    st.write("##")
    st.write("##")

#MODELO DE REGRESION LINEAL
    st.markdown("<h2 style='text-align: left; font-size: 35px;'>Modelo de Regresion Lineal 🖇</h2>", unsafe_allow_html=True)
    st.write("##")
    colmol1,colmol2= st.columns(2)
    with colmol1:
        st_lottie(lottie3,height= 400)
    textregre="""Un modelo de regresión lineal es una herramienta estadística utilizada 
    para comprender y modelar la relación entre una variable dependiente (la que se desea predecir)
    y una o más variables independientes (predictoras). Su objetivo principal es identificar y cuantificar
    la relación lineal entre estas variables, lo que permite hacer predicciones o estimaciones de la
    variable dependiente en función de los valores de las variables independientes. En esencia, un
    modelo de regresión lineal se utiliza para comprender cómo los cambios en una o varias variables
    predictoras se relacionan con cambios en la variable que se quiere predecir, lo que resulta útil en
    tareas como la predicción de ventas, el análisis de tendencias, la evaluación del impacto de
    variables y la toma de decisiones basada en datos."""
    colmol2.write("##")

    colmol2.markdown(f"<div style='text-align: justify; font-size: 20px;'>{textregre}</div>", unsafe_allow_html=True)
    
    st.write("##")
    st.write("##")

#ARMADO DEL MODELO
    st.subheader("Utilizando la libreria de Scikit-Leard se realiza el Modelos")
    code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
    st.markdown(code_style, unsafe_allow_html=True)
    st.code(regression_model,language="python")
    st.write("##")

#ANALISIS DE VARIACIONES
    st.subheader("Luego se analiza si el modelo esta alineado a la realidad")
    st.write("Para eso primero se realiza un análisis variaciones. Las variaciones son la diferencia entre los valores observados y los valores predichos por el modelo. Se puede obtenerlas de la siguiente manera:")
    code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
    st.markdown(code_style, unsafe_allow_html=True)
    st.code("residuos = y - modelo.predict(x)",language="python")
    st.write("Donde *Y* son los valores observados (CO2 en este caso) y *modelo.predict(x)* son las predicciones del modelo para los mismos valores de *X* (GDP en este caso).")
    st.write("##")
    st.write("##")

#GRAFICO 3 HISTOGRAMA
    colres1,colres2 = st.columns(2)
    colres1.subheader("Despues se grafica las variaciones")
    histograf="""Una forma común de evaluar la calidad del ajuste es graficar las variaciones.
              Se puede usar un histograma para visualizar la distribución de las variaciones.
              Un patrón no ideal sería que las variaciones estén distribuidos de manera aleatoria alrededor de cero y no muestren ningún patrón evidente. En este caso
              el se observa claramente el patron de una curva de distribucion normal o gausseana.
                    """
    colres1.write("##")
    colres1.write("##")
    colres1.write("##")
    colres1.markdown(f"<div style='text-align: justify; font-size: 20px;'>{histograf}</div>", unsafe_allow_html=True)
    with colres2:
            x = df['GDP'].values.reshape(-1, 1) # Variables independientes 
            y = df['Co2-Emissions 2023'].values # Variables dependiente
            modelo = LinearRegression()
            modelo.fit(x, y)
            residuos = y - modelo.predict(x)
            histogram_fig = px.histogram(x=residuos, nbins=30, color_discrete_sequence=["#FFF1AF"])
            histogram_fig.update_layout(xaxis_title="Residuos",
                                        yaxis_title="Frecuencia",
                                        title="Histograma de residuos",
                                        paper_bgcolor="rgba(0,0,0,0)",  
                                        plot_bgcolor="rgba(0,0,0,0)",   
                                        font=dict(color="white") 
                                            )
            st.plotly_chart(histogram_fig, use_container_width=True)
    #EXPANCION CODIGO
    with st.expander("Ver Codigo </> Histograma Chart"):
        code_style = """
        <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                color: #FFFFFF !important; /* Color del texto blanco */}
        </style>
                 """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(histograma_code,language="python")
    rtohisto="""Se observa en el histograma que no hay una gran dispersion en los datos, pero esto no
                es suficiente para considerar el modelo alineado a la realidad."""
    st.markdown(f"<div style='text-align: center; font-size: 30px;'>{rtohisto}</div>", unsafe_allow_html=True)
    st.write("##")
    st.write("##")

#COHEFICIENTE DE DETERMINACION R2
    st.subheader("Ahora se evalúa la de calidad de ajuste de las variaciones")
    ajuste="""Evaluar estadísticas de calidad del ajuste, como el coeficiente de determinación (R^2).
             Esta métricas te darán una idea de cuánta variabilidad de los 
                datos es explicada por el modelo y cuán bien se ajusta a los datos en un valor porcentual"""
    st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{ajuste}</div>", unsafe_allow_html=True)
    code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
    st.markdown(code_style, unsafe_allow_html=True)
    st.code(ajuste_code,language="python")
    empi1,col5,empi2=st.columns((1,1,1))
    empi1.empty()
    col5.markdown(centrar_texto_css, unsafe_allow_html=True)
    col5.metric(label="**Coeficiente de determinación R^2**", value=f'0.8167%')
    empi2.empty()
    st.write("##")
    coefi="""Un coeficiente de determinación (R^2) de 0.8167 es relativamente alto, 
    lo que sugiere que tu modelo de regresión lineal explica una gran parte de la variabilidad en los datos.
    Esto permite considerar el modelo aceptable para predecir datos"""
    st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{coefi}</div>", unsafe_allow_html=True)
    st.write("##")
    st.subheader("Estimacion de la emision de CO2 apartir del GDP de un pais")
    coefi="""Con este breve y simple analisis pudimos generar un modelos de machine learning que puede predecir 
            con un 80% de certeza la emision de CO2 de un pais apartir del su GDP"""
    st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{coefi}</div>", unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    
    nuevo_GDP = st.number_input("Ingrese el nuevo valor de GDP en millones de USD")


    if st.button("Realizar predicción de CO2"):
        # Realizar la predicción cuando se presione el botón
        prediccion_CO2 = modelo.predict(np.array([[nuevo_GDP]]))
        prediccion_CO2 = round(prediccion_CO2[0], 10)
        st.write(f"Predicción de CO2 en millones de toneladas: {prediccion_CO2}")




    








#ABOUT ME
def About_Me():
    about = st.container()
    st.header("About Me")
    emppp1,image_colum, emppp2  = st.columns(3)
    emppp1.empty()
    with image_colum:
        image_path = r"Images/yoyoyo.png"
        image = Pillow.open(image_path)
        st.image(image, width=400)#,use_column_width=True)
    emppp2.empty()
        
    st.write("---")
    aboutmetext=""" 
            Soy Ramiro Fernández de Ullivarri, un profesional con experiencia sólida en Gestión de Proyectos. Mi enfoque no se limita únicamente a las habilidades técnicas;
              también tengo una comprensión profunda de las necesidades del equipo y una visión clara de los objetivos empresariales.
            Me apasiona mantenerme actualizado con las últimas tecnologías que impactan en el mercado, siempre buscando innovaciones 
            que simplifiquen nuestras vidas y mejoren la eficiencia de nuestras conexiones."""
    
    aboutmetext2="""Como Ingeniero Industrial con un enfoque en el Análisis de Datos, hace un tiempo me eh enfocado 
     en explorar el emocionante mundo de la programación en Python y el análisis de datos. 
      Estoy emocionado por las oportunidades futuras y confío en que mi experiencia y dedicación seguirán 
      siendo un motor para el éxito en los proyectos venideros."""
    st.markdown(f'<div style="text-align: justify; font-size: 23px">{aboutmetext}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: justify; font-size: 23px">{aboutmetext2}</div>',unsafe_allow_html=True)
    st.write("##")
    with open(r"DataSets/CV-Ramiro Fernández de Ullivarri PMO.pdf", "rb") as file:
        descargarCV= st.download_button(
        label="Descargar CV",
        data=file,
        file_name="CV-Ramiro Fernandez de Ullivarri PMO.pdf",
        mime="pdf")

    st.write("---")


    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, center_column , right_column = st.columns((1,2,1))
    with center_column:
        st.header("Dejame tus comentarios!")
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    with left_column:
        st.empty() 

    



if on_change("menu_5") == "Home":
    Home()
elif on_change("menu_5") == "Data & Insight":
    Data_Insight() 
elif on_change("menu_5") == "About Me":
    About_Me()     
else:
    Home()


