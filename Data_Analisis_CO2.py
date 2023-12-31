import pandas as pd
import numpy as np
import streamlit as st

#CARGO LA BD
df= pd.read_csv(r"DataSets/CO2 WORLD 1990 2023.csv")


def data_preparation():
    #ME FIJO QUE FORMATO Y VALORES TIENEN LAS COLUMNAS
    # for col in df.columns:
    #     print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)

    #GENERO UNA VARIABLE CON LAS COLUMNAS A CONVERTIR EN NUMERO
    num_columns= ['Density\n (P/Km2)', 'Agricultural Land( %)',
           'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
           'Co2-Emissions 2023', 'CPI', 'CPI Change (%)',
           'Fertility Rate', 'Forested Area (%)',
           'Gross primary education enrollment (%)',
           'Gross tertiary education enrollment (%)', 'Infant mortality',
           'Life expectancy', 'Maternal mortality ratio',
           'Out of pocket health expenditure',
           'Physicians per thousand', 'Population',
           'Population: Labor force participation (%)', 'Tax revenue (%)',
           'Total tax rate', 'Unemployment rate', 'Urban_population','GDP',
           'Co2-Emissions 2021', 'Co2-Emissions 2020','Co2-Emissions 2019', 
           'Co2-Emissions 2018', 'Co2-Emissions 2017','Minimum wage','Gasoline Price',
           'Co2-Emissions 2016', 'Co2-Emissions 2015', 'Co2-Emissions 2014',
           'Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
           'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008',
           'Co2-Emissions 2007', 'Co2-Emissions 2006', 'Co2-Emissions 2005',
           'Co2-Emissions 2004', 'Co2-Emissions 2003', 'Co2-Emissions 2002',
           'Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
           'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996',
           'Co2-Emissions 1995', 'Co2-Emissions 1994', 'Co2-Emissions 1993',
           'Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']

    co2_columns= ['Co2-Emissions 2023','Co2-Emissions 2021', 'Co2-Emissions 2020',
           'Co2-Emissions 2019', 'Co2-Emissions 2018', 'Co2-Emissions 2017',
           'Co2-Emissions 2016', 'Co2-Emissions 2015', 'Co2-Emissions 2014',
           'Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
           'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008',
           'Co2-Emissions 2007', 'Co2-Emissions 2006', 'Co2-Emissions 2005',
           'Co2-Emissions 2004', 'Co2-Emissions 2003', 'Co2-Emissions 2002',
           'Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
           'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996',
           'Co2-Emissions 1995', 'Co2-Emissions 1994', 'Co2-Emissions 1993',
           'Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']

    #SACO COMAS % Y SIGNO $ PARA PODER MANIPULAR LA BD
    comma_cols=[]
    percent_cols=[]
    dollar_cols=[]
    for col in df.columns:
        if df[col].dtype=="object":
            if df[col].str.contains(',').any():
                comma_cols.append(col)
            elif df[col].str.contains('%').any():
                percent_cols.append(col)
            elif df[col].str.contains('$').any():
                dollar_cols.append(col)


    for col in percent_cols:
        df[col]=df[col].str.replace("%","")

    for col in dollar_cols:
        df[col]=df[col].str.replace("$","")

    for col in comma_cols:
        df[col]=df[col].str.replace(",","")

    df["GDP"]=df["GDP"].str.replace("$","")


    #CONVIERTO TODAS LAS COLUMNAS NUMERICAS EN DATO NUMERICO
    for i in num_columns:
        df[str(i)] = pd.to_numeric(df[str(i)], errors='coerce')

    for c in co2_columns:
        df[str(c)]= df[str(c)]/100

    # for col in df.columns:
    #     print(col,"  ",df[col][1],"  ",df[str(col)].dtype)
    
    return(df.to_csv('CO2_WORLDWIDE_90_23.csv', index=False))




data_pre_code="""
    #ME FIJO QUE FORMATO Y VALORES TIENEN LAS COLUMNAS
    for col in df.columns:
        print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)

    #GENERO UNA VARIABLE CON LAS COLUMNAS A CONVERTIR EN NUMERO
    num_columns= ['Density\n (P/Km2)', 'Agricultural Land( %)',
           'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
           'Co2-Emissions 2023', 'CPI', 'CPI Change (%)',Fertility Rate', 'Forested Area (%)',
           'Gross primary education enrollment (%)','Gross tertiary education enrollment (%)',
            'Infant mortality','Life expectancy', 'Maternal mortality ratio',
           'Out of pocket health expenditure','Physicians per thousand', 'Population',
           'Population: Labor force participation (%)', 'Tax revenue (%)','Total tax rate', 
           'Unemployment rate', 'Urban_population','GDP','Co2-Emissions 2021', 'Co2-Emissions 2020',
           'Co2-Emissions 2019', 'Co2-Emissions 2018', 'Co2-Emissions 2017',
           'Minimum wage','Gasoline Price','Co2-Emissions 2016', 'Co2-Emissions 2015',
            'Co2-Emissions 2014',...]

    co2_columns= ['Co2-Emissions 2023','Co2-Emissions 2021', 'Co2-Emissions 2020',
           'Co2-Emissions 2019', 'Co2-Emissions 2018', 'Co2-Emissions 2017',
           'Co2-Emissions 2016', 'Co2-Emissions 2015', 'Co2-Emissions 2014',
           'Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
           'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008',
           'Co2-Emissions 2007', 'Co2-Emissions 2006', 'Co2-Emissions 2005',
           'Co2-Emissions 2004', 'Co2-Emissions 2003', 'Co2-Emissions 2002',
           'Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
           'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996',
           'Co2-Emissions 1995', 'Co2-Emissions 1994', 'Co2-Emissions 1993',
           'Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']            

    #SACO COMAS % Y SIGNO $ PARA PODER MANIPULAR LA BD
    comma_cols=[]
    percent_cols=[]
    dollar_cols=[]
    for col in df.columns:
        if df[col].dtype=="object":
            if df[col].str.contains(",").any():
                comma_cols.append(col)
            elif df[col].str.contains("%").any():
                percent_cols.append(col)
            elif df[col].str.contains("$").any():
                dollar_cols.append(col)

    for col in percent_cols:
            df[col]=df[col].str.replace("%","")

        for col in dollar_cols:
            df[col]=df[col].str.replace("$","")

        for col in comma_cols:
            df[col]=df[col].str.replace(",","")

        df["GDP"]=df["GDP"].str.replace("$","")


    #CONVIERTO TODAS LAS COLUMNAS NUMERICAS EN DATO NUMERICO
    for i in num_columns:
        df[str(i)] = pd.to_numeric(df[str(i)], errors='coerce')
    for c in co2_columns:
        df[str(c)]= df[str(c)]/100


    #CONTROL    
    for col in df.columns:
        print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)
    """

primeros_insights="""
#PRIMEROS INSIGHTS
    st.write("##")
    st.write("##")
    st.header(" Conclusiones & Insights 👨‍💻")
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
    #PAISES
        insight_1.metric(label="**PAISES**", value=f'🌎{len(df["Country"].unique())}', delta="EN EL ANALISIS", delta_color="off")

    with insight_2:
    #CO2 (mT)
        co2_23= str(round(df["Co2-Emissions 2023"].sum(),1))
        delta=str(round(df["Co2-Emissions 2021"].sum()-df["Co2-Emissions 2023"].sum(),1))
        insight_2.metric(label="**CO2 WORLDWIDE (Millones Tn) HASTA JUNIO 2023**", value=co2_23, delta=f'{delta} (2021)*',delta_color="off")
        co2_text_23=" En solo 6 meses se emitío el 97% de CO2 generado en 2021. Datos hasta junio 2023"
        insight_2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{co2_text_23}</div>", unsafe_allow_html=True)
    with insight_3:
    #80/20
        insight_3.metric(label="**PAISES QUE HACEN EL 80/20**", value="🗺30" , delta="DE CO2 WORLDWIDE",delta_color="off")
        insight_3.markdown(f"<div style='text-align: justify; font-size: 15px;'>El 80% de la emision de CO2 mundial esta consentrada en 30 paises.</div>",unsafe_allow_html=True)
    empty2.empty()
    
    st.divider()

    empty111,insight_111, insight_222, insight_333, empty222= st.columns((0.5,2,2,2,0.5))
    empty111.empty()
    with insight_111:
    #GDP
        insight_111.metric(label="**CORRELACION GDP & CO2**", value=f'➕💰=➕CO2', delta="MATRIZ ECONOMICA", delta_color="off")
        gdp_text="La relación lineal entre GDP (Producto Interno Bruto) y CO2 se debe a que las economías
          más fuertes suelen ser las más activas y demandan más energía, generada mediante métodos convencionales 
          como el uso de carbón y gas."
        insight_111.markdown(f"<div style='text-align: justify; font-size: 15px;'>{gdp_text}</div>", unsafe_allow_html=True)
        

    with insight_222:
    #POBLACION HURBANA
        insight_222.metric(label="**POBLACION URBANA**", value=f'➕🚻=➕CO2', delta="+ CONSCETRACION URBANA + CO2", delta_color="off")
        city_text=" A mayor concentracion de poblacion en las ciudades se denota un gran aumento del CO2 debido
        a las actividades que se realizan en la ciudad como entretenimiento y trabajo"
        insight_222.markdown(f"<div style='text-align: justify; font-size: 15px;'>{city_text}</div>", unsafe_allow_html=True)
    
    with insight_333:
    #PERO DECADA
        insight_333.metric(label="**PEOR DECADA DE C02**", value=f'2000-2010', delta="55% DE LOS ULTIMOS 30 AÑOS", delta_color="off")
        decade_text=" Entre 2000 y 2010 se emitio el 55% de CO2 de las ultimas 3 decadas, mas del doble que en las otras 2 decadas analzadas"
        insight_333.markdown(f"<div style='text-align: justify; font-size: 15px;'>{city_text}</div>", unsafe_allow_html=True)
    
    empty222.empty()
    st.write("##")
    st.write("##")
                    """

barchart_countrys="""
    column_1 , column_2= st.columns(2)

    #GRAPH 1
    column_1.header(" TOP 10 paises de **mayor** emision de CO2 (2023) 🍂")
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


    #GRAPH 2
    st.write("##")
    column_2.header("  TOP 10 paises de **menor** emision de CO2 (2023) 🍃")
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
                    """

area_chart_code="""
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

                """

regression_model="""
                    import pandas as pd
                    from sklearn.linear_model import LinearRegression
                    import numpy as np
                    
                    df= pd.read_csv(r"CO2_WORLDWIDE_90_23.csv")
                    
                    x = df['GDP'].values.reshape(-1, 1) # Variables independientes 
                    y = df['Co2-Emissions 2023'].values # Variables dependiente
                    
                    #Realizamos el modelos
                    modelo = LinearRegression()
                    modelo.fit(x, y)"""

histograma_code="""

histogram_fig = px.histogram(x=residuos, 
                            nbins=30, 
                            color_discrete_sequence=["#FFF1AF"])
    histogram_fig.update_layout(xaxis_title="Residuos",
                                yaxis_title="Frecuencia",
                                title="Histograma de residuos",
                                paper_bgcolor="rgba(0,0,0,0)",  
                                plot_bgcolor="rgba(0,0,0,0)",   
                                font=dict(color="white") 
                                    )
    st.plotly_chart(histogram_fig, use_container_width=True)

        """

ajuste_code="""r2 = r2_score(y, modelo.predict(x))

print(f"Coeficiente de determinación (R^2): {r2}")

"""