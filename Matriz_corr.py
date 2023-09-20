import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from Data_Analisis_CO2 import data_preparation

df= pd.read_csv(r"CO2_WORLDWIDE_90_23.csv")

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
                     colorscale='Viridis')

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




