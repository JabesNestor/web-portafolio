
import streamlit as st 
from PIL import Image
# Proyectos
st.title("Proyectos")

with st.container():
    st.write("---")
    st.header("Aquí están algunos de los proyectos en los que he trabajado:")
    st.write("#")
    st.write("#")
# Proyecto: predicion de robos
    # imagen
    image_column, text_column = st.columns((3, 2))
    with image_column:
        image = Image.open("imagenes/crimen.jpg")
        st.image(image, use_column_width=True)

    with text_column:
        st.subheader("Crime analysis 🔎")
        st.write("""
- **Descripción**: Proyecto de predicción de robos utilizando técnicas de aprendizaje supervisado.
- **Tecnologías**: Python, Scikit-Learn, Pandas, Matplotlib.
- **Resultados**: El modelo de regresión logística alcanzó una precisión general del 95%, una predicción de robos del 98% y una predicción de no robos del 75%.

    [Link del proyecto](https://github.com/JabesNestor/crime-analysis-eda-ml)
""")

st.write("#")
st.write("#")
# Proyecto: IGN
 # espacios antes de comenzar 
 #imagenes
image_column, text_column = st.columns((3,2))
with image_column:
    image = Image.open("imagenes/Dashboard_IGN.png")
    st.image(image, use_column_width=True)
#columna de texto
with text_column:
    st.subheader("Dashboard IGN 📈")
    st.write("""
    - **Descripción**: Es un dashboard interactivo utilizando datos de IGN.
    - **Características**: Análisis de lanzamientos, géneros y tendencias.
    - **Tecnologías**: Tableau
    - **Experiencia**: ¡Proyecto divertido que combina mi pasión por gaming y datos! 
    
        [Link del proyecto](https://public.tableau.com/app/profile/jabes.nestor.frias.martinez/viz/IGN20Years/Dashboard1)
    """)
