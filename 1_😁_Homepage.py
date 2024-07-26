import streamlit as st 

# Bienvenido
st.title("Este mi portafolio de ciencia de datos")
st.write("Bienvenido a mi portafolio. Aquí encontrarás información sobre mí y los proyectos que he realizado.")


# sobre mí 

with st.container():
    st.write("---")
    st.header("Sobre mí")
    st.write("""
Soy un estudiante de estadística con mención en informática en la UASD, con una pasión por el análisis de datos y la ciencia de datos. 
He trabajado en varios proyectos de análisis de datos, incluyendo web scraping, análisis exploratorio de datos (EDA), Dashboards
y modelos de clasificación y regresión.
""")

# Habilidades 

with st.container():
    st.write("---")
    st.subheader("Herramientas que domino")
    st.write("""       
    - **Programacion**: Python, SQL.
    - **Visualizaciones**: Tablue, seaborn, Matplotlib, PowerBI.         
    - **Manejos de datos**: Numpy, Pandas.
    - **Otras herramientas**: Git, Juppyter Notebook.
    """)
