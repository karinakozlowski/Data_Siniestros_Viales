import streamlit as st

# Título e introducción
st.title("Dashboard de Power BI")
st.markdown("***")


# Insertar el dashboard de Power BI utilizando un iframe
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMTAwZGZkMWQtMWVkNy00ZjZjLThkZWEtNTA1ZDRlNmFmZDNkIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9",
                        width=800,
                        height=600)
