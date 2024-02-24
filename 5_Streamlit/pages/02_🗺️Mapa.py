import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título e introducción
st.title("Visualización de Datos de Accidentes de Tráfico en Mapa Dinámico")
st.markdown("En esta sección, se presentan visualizaciones de puntos de siniestros viales con homicidios.")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)
# Mapa de puntos de interés
st.subheader("Mapa de Puntos de Victimas")
# Eliminar filas con valores no válidos en las columnas de coordenadas
h_hechos_limpios = h_hechos.dropna(subset=['pos x', 'pos y'])
h_hechos_limpios = h_hechos_limpios[(h_hechos_limpios['pos x'] != '.') & (h_hechos_limpios['pos y'] != '.')]
# Crear un DataFrame para los puntos de interés
puntos_interes = pd.DataFrame({
    'lat': h_hechos_limpios['pos y'],
    'lon': h_hechos_limpios['pos x'],
})
# Convertir las columnas de latitud y longitud a tipo numérico
puntos_interes['lat'] = pd.to_numeric(puntos_interes['lat'], errors='coerce')
puntos_interes['lon'] = pd.to_numeric(puntos_interes['lon'], errors='coerce')
# Mostrar el mapa en Streamlit
st.map(puntos_interes)
