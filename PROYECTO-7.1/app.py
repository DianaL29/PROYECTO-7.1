import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el conjunto de datos
df = pd.read_csv("vehicles_us.csv")  

# Definir boton
button = st.button("Distribucion de edades")
scater = st.button("Model")

# Encabezado
st.header("Cuadro de Mandos: Análisis de Datos")

# Botón para mostrar un histogramaç
if button:
    st.write ("Creacion de histograma para el conjunto de datos de anuncios de ventas de coche")
    fig = px.histogram(df, x="odometer", nbins=50, title="Distribución de Precios")
    st.plotly_chart(fig,use_container_width=True)

if scater:
    st.write("Creacion de diagrama de dispercion para el conjunto de datos de ventas de coche")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig,use_container_width=True)