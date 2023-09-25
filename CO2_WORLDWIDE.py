import requests
import os
import pandas as pd
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from  PIL import  Image as Pillow
import matplotlib.pyplot as plt
import plotly.express as px
from Data_Analisis_CO2 import data_pre_code, primeros_insights, barchart_countrys,area_chart_code

#Set up web
st.set_page_config(page_title="CO2 WORDLWIDE ANALISIS",
                    page_icon="🌱",
                    layout="wide")

email_address= "rfullivarri22@gmail.com"
url_animacion= "https://lottie.host/2d201ac4-c25d-48cb-933a-3049ac56335b/fgHSZdOUxA.json"
pdf_url= r"DataSets/CV-Ramiro Fernandez de Ullivarri PMO (1).pdf"

#Animaciones
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie= load_lottieurl(url_animacion)



#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/co2ww.css")

#Menu
def on_change(key):
    selection = st.session_state[key]

    return str(selection)

menuopt = ["Home","Data & Insight","About Me","Contact Me"]

selected5 = option_menu(None, options=menuopt,
                        icons=['house', 'data', "person", 'phone'],
                        on_change=on_change, key='menu_5', orientation="horizontal")



#HOME
def Home():
    home= st.container()
    home.markdown("<h1 style='text-align: center; font-size: 80px;'>CO2 WORLDWIDE ANALYSIS 🌎</h1>", unsafe_allow_html=True)
    #home.title("CO2 WORDLWIDE ANALSIS 🌎")
    home.header("Analisis sobre la emision de CO2")
    descripcion="""En CO2 WORLDWIDE, nos embarcamos en la misión de explorar la situación
                actual del dióxido de carbono en todo el mundo, un gas que afecta directamente
                a nuestro planeta. Con la mira puesta en la increíble cifra de más de 40 mil millones
                de toneladas de CO2 emitidas anualmente, nuestro objetivo principal es destacar la importancia
                de comprender estos números a través de datos y análisis sólidos. Nos adentramos en el 
               fascinante mundo de los datos para revelar patrones y tendencias que arrojarán luz sobre la
                problemática del CO2 y su impacto en nuestro entorno."""
    home.markdown(f'<div style="text-align: justify">{descripcion}</div>',unsafe_allow_html=True)
    #home.write("[Saber Mas >]")
    home.write("---")

    values =st.container()
    values.title("Objetivos 🎯")
    valor1, valor2, valor3 = st.columns(3)
    with valor1:
        st.header("Analisis 👩‍💻")
        text1="""Nuestro primer objetivo es aprender a realizar un análisis de datos de alta calidad. 
                 Esto implica explorar y procesar datos de manera rigurosa, aplicar técnicas estadísticas,
                  y utilizar herramientas como Pandas, Numpy y Matplotlib para obtener información valiosa. 
                 Queremos convertirnos en expertos en la manipulación de datos y en la generación de 
                 resultados confiables."""
        st.markdown(f'<div style="text-align: justify">{text1}</div>',unsafe_allow_html=True)

    with valor2:
        st.header("Insights ✨")
        text2="""En segundo lugar, nuestro objetivo es obtener valiosos conocimientos y 
                 conclusiones sobre el dióxido de carbono (CO2) a partir de nuestros análisis. 
                 Queremos descubrir patrones ocultos, identificar tendencias preocupantes o alentadoras, 
                 y, en última instancia, contribuir al entendimiento de la importancia de controlar
                  las emisiones de CO2 para el bienestar de nuestro planeta."""
        st.markdown(f'<div style="text-align: justify">{text2}</div>',unsafe_allow_html=True)

    with valor3:
        st.header("Difusión 🤲")
        text3= """Aumentar la conciencia pública sobre la problemática del CO2 y sus efectos en 
                 nuestro entorno. Buscamos informar y educar a la comunidad sobre los hallazgos y 
                 conclusiones que obtengamos a través de nuestro análisis de datos. Esto incluye la 
                 creación de contenido educativo, gráficos impactantes y presentaciones accesibles 
                 que ayuden a transmitir de manera efectiva la importancia de reducir las emisiones de CO2 
                 y adoptar prácticas más sostenibles. Queremos inspirar a las personas a tomar medidas
                  concretas para abordar este desafío global."""
        st.markdown(f'<div style="text-align: justify">{text3}</div>',unsafe_allow_html=True)

    st.write("---")
    datos =st.container()
    datos.markdown("<h1 style='text-align: center; font-size: 60px;'>Como vamos a hacerlo 📊</h1>", unsafe_allow_html=True)
    #datos.title("Como vamos a hacerlo 📊")
    datos.write("##")
    datos1, datos2 = st.columns(2)
    with datos1:
        #st.empty()
        textdata="""Nuestro análisis de datos comenzará con una exploración exhaustiva del conjunto de datos,
                  identificando su tamaño y las variables más relevantes. Luego, nos sumergiremos en el mundo
                  de la correlación para comprender las interacciones dentro de los datos. A continuación, 
                 emplearemos gráficos impactantes para ilustrar los datos y obtener conocimientos profundos. 
                 En cada etapa, te proporcionaremos códigos de Python utilizando bibliotecas como Pandas, Numpy, 
                 Matplotlib y Streamlit para que puedas seguir y aprender junto a nosotros. """
        st.markdown(f'<div style="text-align: justify; font-size: 23px">{textdata}</div>',unsafe_allow_html=True)
    with datos2:
        st_lottie(lottie,height= 400)
          
    # image_path = r"imagen/smartcity.png"
    # image = Pillow.open(image_path)
    # st.image(image, use_column_width=True, caption="Imagen Smart City")
    
    # contact=st.container()
    # contact.write("---")
    


#DATA INSIGHTS
def Data_Insight():
    values =st.container()
    values.title("Data & Insight 🚀")
    values.write("Primero preparamos la DB para que podemos trabajar con ella. Depuramos tipo de datos, comas, puntos y simbolos ($,%,& ect)")
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
    values.write("Asi queda la DB lista para usar")
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
        insight_2.metric(label="**CO2 WORLDWIDE (Tn) in 2023**", value=co2_23, delta=f'{delta} (2021)*',delta_color="inverse")

    with insight_3:
        #80/20
        centrar_texto_css = """<style>.centrar-texto {text-align: center;}</style>"""
        insight_3.markdown(centrar_texto_css, unsafe_allow_html=True)
        insight_3.metric(label="**COUNTRIES WHO MAKE 80/20**", value="30" , delta="WORLDWIDE",delta_color="off")
    empty2.empty()
    #EXPANCION CODIGO
    with st.expander("Ver Codigo <> Insight"):
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
    #HIGH CO2 BY COUNTRY
    column_1.header(""" TOP 10 paises de **mayor** emision de CO2 (2023) 🍂""")
    df_co2_23_by_country= (df.sort_values(by="Co2-Emissions 2023",ascending=False)).set_index("Country").head(10)
    df_co2_23_by_country = df_co2_23_by_country[::-1] #invertir el df para grafico de barras
    # 2. Crear el gráfico de barras verticales con Plotly
    fig = px.bar(df_co2_23_by_country, x="Co2-Emissions 2023", y=df_co2_23_by_country.index, orientation="h",
             text="Co2-Emissions 2023", color_discrete_sequence=["#FFF1AF"])
    # Personaliza la apariencia del gráfico
    fig.update_layout(  xaxis_title="Co2-Emissions 2023 (Tn)",
                        yaxis_title="Country",
                        paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
                        plot_bgcolor="rgba(0,0,0,0)",   # Fondo transparente
                        font=dict(color="white"))       # Color de las etiquetas en blanco
    # Muestra el gráfico en Streamlit
    column_1.plotly_chart(fig, use_container_width=True)
#GRAFICO2
    st.write("##")
    column_2.header("""  TOP 10 paises de **menor** emision de CO2 (2023) 🍃""")
    df_co2_23_by_country= (df.sort_values(by="Co2-Emissions 2023",ascending=False)).set_index("Country").tail(10)
    df_co2_23_by_country = df_co2_23_by_country[::-1] #invertir el df para grafico de barras
    # 2. Crear el gráfico de barras verticales con Plotly
    fig2 = px.bar(df_co2_23_by_country, x="Co2-Emissions 2023", y=df_co2_23_by_country.index, orientation="h",
             text="Co2-Emissions 2023", color_discrete_sequence=["#FFF1AF"])
    # Personaliza la apariencia del gráfico
    fig2.update_layout(  xaxis_title="Co2-Emissions 2023 (Tn)",
                        yaxis_title="Country",
                        paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
                        plot_bgcolor="rgba(0,0,0,0)",   # Fondo transparente
                        font=dict(color="white"))       # Color de las etiquetas en blanco
    # Muestra el gráfico en Streamlit
    column_2.plotly_chart(fig2, use_container_width=True)
     #EXPANCION CODIGO
    with st.expander("Ver Codigo <> Bar Chart"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(barchart_countrys,language="python")
#GRAFICO3
    st.write("##")
    st.header("""Crecimiento de CO2 desde 1990 a 2023""")
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
    with st.expander("Ver Codigo <> Area Chart"):
        code_style = """
            <style>.stApp pre {background-color: #2E2E2E !important; /* Color de fondo oscuro */
                    color: #FFFFFF !important; /* Color del texto blanco */}
            </style>
                     """
        st.markdown(code_style, unsafe_allow_html=True)
        st.code(area_chart,language="python")
#MATRIZ DE CORRELACION
    st.header("Next steps 🧭")
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Queremos ir un paso mas alla. Para eso necesitamos entender mejor los datos.Por eso hicimos esta matriz de correlacion para entender que datos estas realcionados linealmente.</h2>", unsafe_allow_html=True)
    # st.write("""Queremos ir con el analisis un paso mas alla. Para eso necesitamos entender mejor los datos.
    #            Por eso hicimo esta matriz de correlacion para entender que datos estas realcionados linealmente.
    #         """)
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
        width=800,  # Ancho personalizado
        height=800,  # Altura personalizada
    )
    fig.update_yaxes(tickangle=45)  # Rota las etiquetas del eje y
    fig.update_xaxes(tickangle=45)  # Rota las etiquetas del eje x

    # Muestra el gráfico en Streamlit
    corr= st.container()
    corr.plotly_chart(fig, use_container_width=True)
    colu1, colu2 =st.columns(2)
    colu1.write("vemos...")
    colu2.image(r"Images/White Gradient Creative Professional Modern Business Company Corporate Presentation Template.png")




















    

    #, """'Co2-Emissions 2012', 'Co2-Emissions 2011','Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008','Co2-Emissions 2007', 'Co2-Emissions 2006', 'Co2-Emissions 2005','Co2-Emissions 2004', 'Co2-Emissions 2003', 'Co2-Emissions 2002','Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999','Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996','Co2-Emissions 1995', 'Co2-Emissions 1994', 'Co2-Emissions 1993','Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990'"""

    # category= df["Category"].unique()
    # subcategory= df["Subcategory"].unique()
    # #action= df["Action"].isin(["off","on"])
    # action= df["Action"]!= "none"
    
    # column_1,column_2 =st.columns(2)
    # with column_1:
    #     option1 = st.selectbox('Category',(category))
    #     st.write('You selected:', option1)
    # with column_2:
    #     option2 = st.selectbox('Subcategory',(subcategory))
    #     st.write('You selected:', option2)
    
    # filtro= df[(df["Category"]==option1)&(df["Subcategory"]==option2)&(action)] 
    # st.bar_chart(filtro,x="Action",y="Action_needed", color=['#BD9EE5'])

    #"#FFB8F4"
   #["#121B29","#2F3D5B", "#6E679A", "#BD9EE5", "#F8CCED"]




#ABOUT ME
def About_Me():
    about = st.container()
    about.write("---")
    image_colum, text_colum  = st.columns((1,3))
    with image_colum:
        image_path = r"Images/yo.jpeg"
        image = Pillow.open(image_path)
        st.image(image, use_column_width=True)
        
    with text_colum:
        st.header("About Me 🔍")
        aboutmetext=""" 
                Soy Ramiro Fernandez de Ullivarri, un profesional con experiencia en Gestión de Proyectos. 
                 Mi enfoque no se limita solo a las habilidades técnicas, sino que también comprendo las 
                 necesidades del equipo y la visión empresarial. Me apasiona mantenerme al día con 
                 las últimas tecnologías que impactan en el mercado, siempre buscando innovaciones 
                 que simplifiquen nuestras vidas y nos conecten de formas más efectivas.
                """
        aboutmetext2="""Soy un Ingeniero Industrial enfocado enfocado en el analisis de datos con una pasión por 
                    la innovación y la mejora continua. Hace mas de un año que ingrese a el mundo apasionante de data analisis 
                    con Python y la programacion.Estoy emocionado por las oportunidades futuras y 
                    estoy seguro de que mi experiencia y dedicación seguirán impulsando el éxito en los proyectos 
                    venideros."""
        st.markdown(f'<div style="text-align: justify; font-size: 23px">{aboutmetext}</div>',unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: justify; font-size: 23px">{aboutmetext2}</div>',unsafe_allow_html=True)

        st.write("##")
        with open("DataSets/CV-Ramiro Fernandez de Ullivarri PMO (1).pdf", "rb") as file:
            descargarCV= st.download_button(
            label="Descargar CV",
            data=file,
            file_name="CV-Ramiro Fernandez de Ullivarri PMO.pdf",
            mime="pdf")

        st.write("---") 

    
       


#CONTACT US
def Contact_Me():
    contact=st.container()
    contact.write("---")
    
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
elif on_change("menu_5") == "Contact Me":
    Contact_Me()         
else:
    st.empty()


