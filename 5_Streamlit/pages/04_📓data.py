import streamlit as st
import pandas as pd

# URLs de los libros de Excel
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
url_lesiones = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/lesiones.xlsx"

# Leer los libros de Excel y obtener nombres de las hojas
xls_homicidios = pd.ExcelFile(url_homicidios)
xls_lesiones = pd.ExcelFile(url_lesiones)
nombres_hojas_homicidios = xls_homicidios.sheet_names
nombres_hojas_lesiones = xls_lesiones.sheet_names

# Barra lateral con botones para seleccionar el dataset
dataset_option = st.sidebar.radio("Seleccionar dataset:", ("Homicidios", "Lesiones"))

# Sección para visualización de datos
st.title("Visualización de Datos")

# Divisor
st.markdown("---")

# Visualización de datos según el dataset seleccionado
if dataset_option == "Homicidios":
    st.header("Dataset de Homicidios")
    opcion_homicidios = st.sidebar.selectbox("Seleccionar opción:", nombres_hojas_homicidios)
    df_homicidios = pd.read_excel(url_homicidios, sheet_name=opcion_homicidios)
    st.write(df_homicidios)  # Mostrar el DataFrame correspondiente a la hoja seleccionada
elif dataset_option == "Lesiones":
    st.header("Dataset de Lesiones")
    opcion_lesiones = st.sidebar.selectbox("Seleccionar opción:", nombres_hojas_lesiones)
    df_lesiones = pd.read_excel(url_lesiones, sheet_name=opcion_lesiones)
    st.write(df_lesiones)  # Mostrar el DataFrame correspondiente a la hoja seleccionada
