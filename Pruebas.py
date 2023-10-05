import requests
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from  PIL import  Image as Pillow
import matplotlib.pyplot as plt
import plotly.express as px
from Data_Analisis_CO2 import data_pre_code, primeros_insights, barchart_countrys
from sklearn.metrics import r2_score, mean_squared_error



personas=['rulo','cande','rodri','ari','ali','marco','nico','coni','santi','cati']
actividad=[2,2,2,1,2,2,2,1,0,1]


grupo= dict(zip(personas,actividad))

karting= []
bowling= []
ninguna=[]
for k, v in grupo.items():
    if v ==2:
        karting.append(k)
        bowling.append(k)
    elif v == 1:
      karting.append(k)
    else:
       ninguna.append(k)


print(f'Karting: {karting} \n')
print(f'Bowling: {bowling}\n')
print(f'None: {ninguna}')


# df= pd.read_csv(r"CO2_WORLDWIDE_90_23.csv")

# #print(df['Country'][0],df['GDP'][0])
# x = df['GDP'].values.reshape(-1, 1) # Variables independientes 
# y = df['Co2-Emissions 2023'].values # Variables dependiente

# modelo = LinearRegression()
# modelo.fit(x, y)

# nuevo_GDP = np.array([[990000000]])  # Ejemplo de un nuevo valor de GDP en millones de pesos
# prediccion_CO2 = modelo.predict(nuevo_GDP)
# prediccion_CO2 = round(prediccion_CO2[0], 5)  # Redondea a dos decimales

# print(f"Predicción de CO2 en millones de toneladas: {prediccion_CO2}")

#Evaluamos los residuos para saber si el modelo esta alineado a la realidad.
# residuos = y - modelo.predict(x)



# # Histograma de residuos
# histogram_fig = px.histogram(x=residuos, nbins=30)
# histogram_fig.update_layout(
#     xaxis_title="Residuos",
#     yaxis_title="Frecuencia",
#     title="Histograma de residuos"
# )
# histogram_fig.show()


# r2 = r2_score(y, modelo.predict(x))
# mse = mean_squared_error(y, modelo.predict(x))

# print(f"Coeficiente de determinación (R^2): {r2}")
# print(f"Error cuadrático medio (MSE): {mse}")




"""#Evaluamos los residuos para saber si el modelo esta alineado a la realidad.
residuos = y - modelo.predict(x)

# Histograma de residuos
histogram_fig = px.histogram(x=residuos, nbins=30)
histogram_fig.update_layout(
    xaxis_title="Residuos",
    yaxis_title="Frecuencia",
    title="Histograma de residuos"
)
histogram_fig.show()


r2 = r2_score(y, modelo.predict(x))
mse = mean_squared_error(y, modelo.predict(x))

print(f"Coeficiente de determinación (R^2): {r2}")
print(f"Error cuadrático medio (MSE): {mse}")


#Con el modelo podemos obtener predicciones de CO2 a partir de suponer valores de GDP 
nuevo_GDP = np.array([[1000]])  # Ejemplo de un nuevo valor de GDP en millones de pesos
prediccion_CO2 = modelo.predict(nuevo_GDP)
prediccion_CO2 = round(prediccion_CO2[0], 2)  # Redondea a dos decimales

                    """






# area_chart=df[['Co2-Emissions 2023','Co2-Emissions 2021', 'Co2-Emissions 2020','Co2-Emissions 2019', 
#            'Co2-Emissions 2018', 'Co2-Emissions 2017','Co2-Emissions 2016', 'Co2-Emissions 2015',
#            'Co2-Emissions 2014','Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
#            'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008','Co2-Emissions 2007',
#            'Co2-Emissions 2006', 'Co2-Emissions 2005','Co2-Emissions 2004', 'Co2-Emissions 2003', 
#            'Co2-Emissions 2002','Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
#            'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996','Co2-Emissions 1995', 
#            'Co2-Emissions 1994', 'Co2-Emissions 1993','Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']]

# col_name= {'Co2-Emissions 2023':'2023','Co2-Emissions 2021':'2021', 'Co2-Emissions 2020':'2020',
#            'Co2-Emissions 2019':'2019', 'Co2-Emissions 2018':'2019', 'Co2-Emissions 2017':'2017',
#            'Co2-Emissions 2016':'2016', 'Co2-Emissions 2015':'2015', 'Co2-Emissions 2014':'2014',
#            'Co2-Emissions 2013':'2013', 'Co2-Emissions 2012':'2012', 'Co2-Emissions 2011':'2011',
#            'Co2-Emissions 2010':'2010', 'Co2-Emissions 2009':'2009', 'Co2-Emissions 2008':'2008',
#            'Co2-Emissions 2007':'2007', 'Co2-Emissions 2006':'2006', 'Co2-Emissions 2005':'2005',
#            'Co2-Emissions 2004':'2004', 'Co2-Emissions 2003':'2003', 'Co2-Emissions 2002':'2002',
#            'Co2-Emissions 2001':'2001', 'Co2-Emissions 2000':'2000', 'Co2-Emissions 1999':'1999',
#            'Co2-Emissions 1998':'1998', 'Co2-Emissions 1997':'1997', 'Co2-Emissions 1996':'1996',
#            'Co2-Emissions 1995':'1995', 'Co2-Emissions 1994':'1994', 'Co2-Emissions 1993':'1993',
#            'Co2-Emissions 1992':'1992', 'Co2-Emissions 1991':'1991', 'Co2-Emissions 1990':'1990'}

# area_chart.rename(columns=col_name,inplace=True)
# area_chart=area_chart.sum().T

# fig3 = px.area(area_chart, color_discrete_sequence=["#FFF1AF"],log_y=True)
    
# fig3.update_layout( xaxis_title="years",
#                     yaxis_title="CO2",
#                     paper_bgcolor="rgba(0,0,0,0)",  
#                     plot_bgcolor="rgba(0,0,0,0)",   
#                     font=dict(color="white"))       

# st.plotly_chart(fig3, use_container_width=True)