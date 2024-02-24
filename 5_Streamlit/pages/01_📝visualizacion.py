import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Título e introducción
st.title("Visualización de Datos de Accidentes de Tráfico")
st.markdown("En esta sección, se presentan visualizaciones y análisis de datos relacionados con los accidentes de tráfico.")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)

# Mostrar dataset
if st.checkbox("Mostrar dataset"):
    st.write(h_hechos)

# Mostrar head o tail del dataset
if st.checkbox("Ver las primeras o últimas filas del dataset"):
    option = st.radio("Seleccione una opción:", ("Head", "Tail"))
    if option == "Head":
        st.write(h_hechos.head())
    elif option == "Tail":
        st.write(h_hechos.tail())

# Dimensión del dataset
dim = st.radio("Dimensión a mostrar:", ("Filas", "Columnas"))
if dim == "Filas":
    st.write("Cantidad de filas:", h_hechos.shape[0])
else:
    st.write("Cantidad de columnas:", h_hechos.shape[1])

h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Dia'] = h_hechos['FECHA'].dt.day
h_hechos['Mes'] = h_hechos['FECHA'].dt.month
h_hechos['Año'] = h_hechos['FECHA'].dt.year

st.subheader("Cantidad de víctimas por día y por año")

# Widget de selección para el año
años_únicos = h_hechos['Año'].unique()
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos)

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = h_hechos[h_hechos['Año'] == año_seleccionado]

# Visualización de víctimas por día en el año seleccionado
st.set_option('deprecation.showPyplotGlobalUse', False)  # Desactivar advertencia
plt.figure(figsize=(10, 6))
datos_por_dia = datos_año_seleccionado.groupby('Dia')['N_VICTIMAS'].sum()
sns.barplot(x=datos_por_dia.index, y=datos_por_dia.values, palette='viridis')
plt.title(f'Distribución de víctimas por día en el año {año_seleccionado}')
plt.xlabel('Día del mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 32))  # Mostrar todos los días en el eje x
st.pyplot(plt)

# Título e introducción
st.subheader("Cantidad de víctimas por mes y por año")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)
# Calcular día, mes y año
h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Año'] = h_hechos['FECHA'].dt.year

# Calcular día, mes y año
h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Dia'] = h_hechos['FECHA'].dt.day
h_hechos['Mes'] = h_hechos['FECHA'].dt.month
h_hechos['Año'] = h_hechos['FECHA'].dt.year

# Obtener años únicos como cadenas de texto
años_únicos = h_hechos['Año'].unique().astype(str)

# Widget de selección para el año
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos, key="year_selector")

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = h_hechos[h_hechos['Año'] == int(año_seleccionado)]

# Visualización de víctimas por mes en el año seleccionado
plt.figure(figsize=(10, 6))
datos_por_mes = datos_año_seleccionado.groupby('Mes')['N_VICTIMAS'].sum()
sns.barplot(x=datos_por_mes.index, y=datos_por_mes.values, palette='viridis')
plt.title(f'Distribución de víctimas por mes en el año {año_seleccionado}')
plt.xlabel('Mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 13))  # Mostrar todos los meses en el eje x
st.pyplot(plt)





# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)

# Agrupar por comuna y sumar el número de víctimas
victimas_por_comuna = h_hechos.groupby('COMUNA')['N_VICTIMAS'].sum().reset_index()

# Gráfico de barras del número de víctimas por comuna
st.subheader("Número Total de Víctimas por Comuna")
plt.figure(figsize=(12, 8))
sns.barplot(data=victimas_por_comuna, x='COMUNA', y='N_VICTIMAS', palette='viridis')
plt.title("Número Total de Víctimas por Comuna")
plt.xlabel("Comuna")
plt.ylabel("Número Total de Víctimas")
plt.xticks(rotation=45)
st.pyplot(plt)

