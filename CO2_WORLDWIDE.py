import requests
import pandas as pd
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from  PIL import  Image as Pillow

#Set up web
st.set_page_config(page_title="CO2 WORDLWIDE ANALISIS",
                    page_icon="🌱",
                    layout="wide")

email_address= "rfullivarri22@gmail.com"
#url= "https://lottie.host/67d569c8-c019-491a-856f-fec548202ca7/PbNLOBxPif.json"

#Animaciones
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code !=200:
#         return None
#     return r.json()
# lottie= load_lottieurl(url)



#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("Styles/co2ww.css")

#Menu
def on_change(key):
    selection = st.session_state[key]

    return str(selection)

selected5 = option_menu(None, ["Home", "Data & Insight", 'About Me', 'Contact Me'],
                        icons=['house', 'data', "person", 'phone'],
                        on_change=on_change, key='menu_5', orientation="horizontal", )



#HOME
def Home():
    home= st.container()
    home.title("CO2 WORDLWIDE ANALSIS 🌎")
    home.header("Analisis sobre la emision de CO2 de cada pais a lo largo del tiempo")
    home.write("""En CO2 WORLDWIDE, nuestro objetivo principal es comprender la situación 
               actual del dióxido de carbono en todo el mundo y destacar su importancia mediante 
               datos y análisis sólidos. Nos sumergimos en el fascinante mundo de los datos para revelar 
               patrones y tendencias que arrojarán luz sobre la problemática del CO2.""")
    #home.write("[Saber Mas >]")
    home.write("---")

    values =st.container()
    values.title("Objetivos 🎯")
    valor1, valor2, valor3 = st.columns(3)
    with valor1:
        st.header("Analisis👩‍💻")
        st.write("""Nuestro análisis de datos comenzará con una exploración exhaustiva 
                 del conjunto de datos, identificando su tamaño y las variables
                 más relevantes""")
    with valor2:
        st.header("Insights✨")
        st.write("""nos sumergiremos en el mundo de la correlación para comprender
                  las interacciones dentro de los datos. A continuación, emplearemos 
                 gráficos impactantes para ilustrar los datos y obtener conocimientos profundos. 
                 En cada etapa, te proporcionaremos códigos de Python y las librerias que utilice
                para que puedas seguir y aprender junto a nosotros.""")
    with valor3:
        st.header("Algo mas🤲")
        st.write("""como mostrarlo""")
    st.write("---")

    # image_path = r"imagen/smartcity.png"
    # image = Pillow.open(image_path)
    # st.image(image, use_column_width=True, caption="Imagen Smart City")
    
    contact=st.container()
    contact.write("---")
    


#DATA INSIGHTS
def Data_Insight():
    values =st.container()
    values.title("Data & Insight🚀")
    values.write("Presentaremos una BD sobre los sensores en las diferentes habitaciones y mostraremos diferentes analisis apartir de datos encontrados")
    values.write("Tabla de datos de la BD")
    uploaded_file=pd.read_csv(r"smarthome.csv")
    #uploaded_file = st.file_uploader("Upload an article", type=("csv", "xlm","xlms"))
    if uploaded_file is not None:
        #df = pd.read_csv(uploaded_file)
        df = uploaded_file
        st.dataframe(df)
        st.write("Puedes seleccionar el producto y la habitacion que quieras ver su analisis")
        category= df["Category"].unique()
        subcategory= df["Subcategory"].unique()
        #action= df["Action"].isin(["off","on"])
        action= df["Action"]!= "none"

        
        column_1,column_2 =st.columns(2)
        with column_1:
            option1 = st.selectbox('Category',(category))
            st.write('You selected:', option1)
        with column_2:
            option2 = st.selectbox('Subcategory',(subcategory))
            st.write('You selected:', option2)
        
        filtro= df[(df["Category"]==option1)&(df["Subcategory"]==option2)&(action)] 
        st.bar_chart(filtro,x="Action",y="Action_needed", color=['#BD9EE5'])

    #"#FFB8F4"
   #["#121B29","#2F3D5B", "#6E679A", "#BD9EE5", "#F8CCED"]


#PRODUCTS
# def Products():

#         products= st.container()
#         products.title("Nuestros Productos 🛠")
#         products.write("---")
#     #ALEXA
#         image_column, text_column = st.columns((1,2))
#         with image_column:
#             image1_path = r"imagen/alexa.png"
#             image = Pillow.open(image1_path)
#             st.image(image, use_column_width=True, caption="Alexa Home Assitant")
#         with text_column:
#             st.subheader("Home Assistant 🗿")
#             st.write(""" 
#              El Home Assistant es el cerebro de tu hogar inteligente. 
#              Es una plataforma de código abierto que te permite controlar y automatizar todos los dispositivos conectados en tu casa
#               desde un solo lugar. Con Home Assistant, puedes crear escenas personalizadas, programar rutinas y tener un control total 
#              sobre la iluminación, la temperatura, la seguridad y mucho más.
#              """)
#             st.write("[Ver servicios >]")
#         st.write("---")

#     #NFC TAG
#         products.container()
#         image_column, text_column = st.columns((1,2))

#         with image_column:
#             image1_path = r"imagen/NFC.png"
#             image = Pillow.open(image1_path)
#             st.image(image, use_column_width=True, caption="NFC Tag")
#         with text_column:
#             st.subheader("NFC Tags 🧿")
#             st.write(""" 
#                       Los NFC Tags son pequeños adhesivos que contienen chips NFC (Near Field Communication). 
#                       Estos tags permiten la comunicación inalámbrica entre dispositivos cuando se acercan a ellos. 
#                       Son herramientas versátiles para automatizar tareas y mejorar la experiencia del usuario en tu hogar inteligente.
#                       """)
#             st.write("[Ver servicios >]")
#         st.write("---")


#     #SMART LIGHT
#         products.container()
#         image_column, text_column = st.columns((1,2))
#         with image_column:
#             image1_path = r"imagen/smartlight.jpeg"
#             image = Pillow.open(image1_path)
#             st.image(image, use_column_width=True, caption="Smart Lights")
#         with text_column:
#             st.subheader("Smarts Lights 💡")
#             st.write(""" 
#                      Las Smart Lights son bombillas LED inteligentes que te permiten ajustar el brillo,
#                      el color y la programación de la iluminación en tu hogar. 
#                      Estas bombillas son compatibles con asistentes de voz y aplicaciones móviles, 
#                      lo que te da un control completo sobre la iluminación de tu hogar
#                      """)
#             st.write("[Ver servicios >]")
#         st.write("---")



#ABOUT US
def About_Me():
    about = st.container()
    about.write("---")
    text_colum, image_colum = st.columns(2)
    with text_colum:
        st.header("Sobre Nosotros 🔍")
        st.write(""" 
                En [Nombre de la Startup], nuestra pasión es convertir casas en hogares inteligentes. 
                 Desde nuestro inicio en 2013, hemos estado liderando el camino en la industria de la domótica, 
                 brindando soluciones innovadoras y asesoramiento experto a nuestros clientes.
                """)
        st.write("[Saber Mas >]")
    with image_colum:
        st.empty()
        #st_lottie(lottie,height= 400)
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
        st.header("Ponte en contacto con nosotros!")
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


