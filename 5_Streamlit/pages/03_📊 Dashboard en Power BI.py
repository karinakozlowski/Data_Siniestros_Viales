import streamlit as st

# Título e introducción
st.title("Dashboard de Power BI")
st.markdown("***")

# Reemplaza 'URL_DEL_DASHBOARD' con el enlace de tu dashboard de Power BI
power_bi_url = '<iframe title="Dashborad Kari DA" width="1140" height="541.25" src="https://app.powerbi.com/view?r=eyJrIjoiNDIwMDRmOTctMTE5Ny00M2JmLTk5OGUtODIwYjgzYTZiOTdiIiwidCI6IjRhMmE4MWRjLTE0MWQtNDM3My05MDgzLWQxNDY4YmRjYjE3NSIsImMiOjR9&pageName=ReportSectionf5026a0b02939272c525" frameborder="0" allowFullScreen="true"></iframe>'

# Usa el componente write para insertar el iframe
st.write(power_bi_url, unsafe_allow_html=True)

