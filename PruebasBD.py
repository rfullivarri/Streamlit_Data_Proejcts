import pandas as pd
import numpy as np
import streamlit as st

df= pd.read_csv(r"DataSets/CO2 WORLD 1990 2023 - World data 23.csv")

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

columnas_numericas = [ 'Density\n (P/Km2)',
       'Land Area(Km2)','Armed Forces size', 'Birth Rate','Co2-Emissions 2023', 'CPI', 'Fertility Rate',
       'Gasoline Price', 'GDP', 'Infant mortality', 'Life expectancy', 'Population', 'Tax revenue (%)',
       'Total tax rate', 'Unemployment rate', 'Urban_population', 'Co2-Emissions 2023.1', 'Co2-Emissions 2021',
       'Co2-Emissions 2018', 'Co2-Emissions 2015', 'Co2-Emissions 2014',
       'Co2-Emissions 2013', 'Co2-Emissions 2012', 'Co2-Emissions 2011',
       'Co2-Emissions 2010', 'Co2-Emissions 2009', 'Co2-Emissions 2008',
       'Co2-Emissions 2007', 'Co2-Emissions 2006', 'Co2-Emissions 2005',
       'Co2-Emissions 2004', 'Co2-Emissions 2003', 'Co2-Emissions 2002',
       'Co2-Emissions 2001', 'Co2-Emissions 2000', 'Co2-Emissions 1999',
       'Co2-Emissions 1998', 'Co2-Emissions 1997', 'Co2-Emissions 1996',
       'Co2-Emissions 1995', 'Co2-Emissions 1994', 'Co2-Emissions 1993',
       'Co2-Emissions 1992', 'Co2-Emissions 1991', 'Co2-Emissions 1990']

#convertir en numericas las columnas
for i in columnas_numericas:
    df[str(i)] = pd.to_numeric(df[str(i)], errors='coerce')

#print(df.dtypes)
print(df["Co2-Emissions 2023"].sum())






