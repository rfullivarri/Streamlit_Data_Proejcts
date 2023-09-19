import pandas as pd
import numpy as np
import streamlit as st

#CARGO LA BD
df= pd.read_csv(r"DataSets/CO2 WORLD 1990 2023.csv")

def data_preparation():
    #ME FIJO QUE FORMATO Y VALORES TIENEN LAS COLUMNAS
    #for col in df.columns:
        #print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)

    #GENERO UNA VARIABLE CON LAS COLUMNAS A CONVERTIR EN NUMERO
    num_columns= ['Density\n (P/Km2)', 'Agricultural Land( %)',
           'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
           'Co2-Emissions 2023', 'CPI', 'CPI Change (%)',
           'Fertility Rate', 'Forested Area (%)',
           'Gasoline Price', 'GDP', 'Gross primary education enrollment (%)',
           'Gross tertiary education enrollment (%)', 'Infant mortality',
           'Life expectancy', 'Maternal mortality ratio',
           'Minimum wage', 'Out of pocket health expenditure',
           'Physicians per thousand', 'Population',
           'Population: Labor force participation (%)', 'Tax revenue (%)',
           'Total tax rate', 'Unemployment rate', 'Urban_population', 'Latitude',
           'Longitude', 'Co2-Emissions 2021', 'Co2-Emissions 2020',
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
        df[col]=df[col].str.replace("$","",regex=True)

    for col in comma_cols:
        df[col]=df[col].str.replace(",","")

    df["GDP"]=df["GDP"].str.replace("$","",regex=True)

    #CONVIERTO TODAS LAS COLUMNAS NUMERICAS EN DATO NUMERICO
    for i in num_columns:
        df[str(i)] = pd.to_numeric(df[str(i)], errors='coerce')

    # for col in df.columns:
    #     print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)
    return(df)
# dfi= data_preparation()
# co2_23= dfi["Co2-Emissions 2021"].sum()
# print(round(co2_23,1))




data_pre_code="""
    #ME FIJO QUE FORMATO Y VALORES TIENEN LAS COLUMNAS
    for col in df.columns:
        print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)

    #GENERO UNA VARIABLE CON LAS COLUMNAS A CONVERTIR EN NUMERO
    num_columns= ['Density (P/Km2)', 'Agricultural Land( %)',
           'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
           'Co2-Emissions 2023', 'CPI', 'CPI Change (%)',
           'Fertility Rate', 'Forested Area (%)',
           'Gasoline Price', 'GDP', 'Gross primary education enrollment (%)',
           'Gross tertiary education enrollment (%)', 'Infant mortality',
           'Life expectancy', 'Maternal mortality ratio',
           'Minimum wage', 'Out of pocket health expenditure',
           'Physicians per thousand', 'Population',
           'Population: Labor force participation (%)', 'Tax revenue (%)',
           'Total tax rate', 'Unemployment rate', 'Urban_population', 'Latitude',
           'Longitude', 'Co2-Emissions 2021', 'Co2-Emissions 2020',
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
        df[col]=df[col].str.replace("$","",regex=True)

    for col in comma_cols:
        df[col]=df[col].str.replace(",","")

    df["GDP"]=df["GDP"].str.replace("$","",regex=True)

    #CONVIERTO TODAS LAS COLUMNAS NUMERICAS EN DATO NUMERICO
    for i in num_columns:
        df[str(i)] = pd.to_numeric(df[str(i)], errors='coerce')

    for col in df.columns:
        print(col,"  ",df[str(col)][1],"  ",df[str(col)].dtype)
"""





# df["Co2-Emissions 2023"]= df["Co2-Emissions 2023"]/1000

# #print(df.dtypes)
# df23= df[["Co2-Emissions 2023","Co2-Emissions 2018"]]
# print(df23)

# # df["diferencias"]= df["Co2-Emissions 2023"]-df["Co2-Emissions 2023.1"]

# # print(df["diferencias"])
# # df_china= df[df["Country"]=="Cape Verde"]
# # print(df_china)
# # df_china= df_china["Co2-Emissions 2023.1"].sum()
# # print(df_china)
# #print(df["Co2-Emissions 2021"].sum())






