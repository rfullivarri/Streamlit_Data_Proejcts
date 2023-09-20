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
    insight_1, insight_2, insight_3 = st.columns(3)
    with insight_1:
        centrar_texto_css = "<style>.centrar-texto {text-align: center;}</style>"
        st.markdown(centrar_texto_css, unsafe_allow_html=True)
        #Countrys
        st.metric(label="**Countrys**", value=str(len(df["Country"].unique())))

    with insight_2:
        centrar_texto_css = "<style>.centrar-texto {text-align: center;}</style>"
        st.markdown(centrar_texto_css, unsafe_allow_html=True)
        #CO2 (mT)
        co2_23= str(round(df["Co2-Emissions 2023"].sum(),1))
        delta=str(round(df["Co2-Emissions 2021"].sum()-df["Co2-Emissions 2023"].sum(),1))
        st.metric(label="**CO2 WORLDWIDE (Tn) in 2023**", value=co2_23, delta=f'{delta} (2021)*')

    with insight_3:
        st.empty()
                    """

barchart_countrys="""
    #HIGH CO2 BY COUNTRY
    df_co2_23_by_country= (df.sort_values(by="Co2-Emissions 2023",ascending=False)).set_index("Country").head(10)
    df_co2_23_by_country = df_co2_23_by_country[::-1] #invertir el df para grafico de barras
    # 2. Crear el gráfico de barras verticales con Plotly
    fig = px.bar(df_co2_23_by_country, x="Co2-Emissions 2023", y=df_co2_23_by_country.index, orientation="h",
             text="Co2-Emissions 2023", color_discrete_sequence=["#FFB8F4"])
    # Personaliza la apariencia del gráfico
    fig.update_layout(
    xaxis_title="Co2-Emissions 2023",
    yaxis_title="Country",
    paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
    plot_bgcolor="rgba(0,0,0,0)",   # Fondo transparente
    font=dict(color="white"))       # Color de las etiquetas en blanco

    # Muestra el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
                    """






