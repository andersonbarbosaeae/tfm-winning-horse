import streamlit as st

# Config
st.set_page_config(page_title='Predicción', page_icon='📊', layout='wide')

# Title
st.title('📊 Predicción')
st.write(
    """
    En esta sección podrás introducir los datos de una carrera y predecir el resultado de la misma.
    """
)

# Form
with st.form("template_form"):
    # Select box
    st.subheader('📝 Selección de variables')
    st.write(
        """
        Selecciona las variables que quieres utilizar para la predicción.
        """
    )
    # Select box
    variables = st.multiselect(
        'Variables',
        ('Edad', 'Sexo', 'Peso', 'Altura', 'Distancia', 'Hipódromo', 'Jockey', 'Entrenador', 'Carrera')
    )
    # Submit button
    submit_button = st.form_submit_button(label='🔎 Predecir')

# Content
if submit_button:
    st.balloons()
    st.subheader('🏆 Resultado')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.warning('**Primer Lugar: 23%**', icon="🥇")
    with c2:
        st.success('**Primeros 3: 32%**', icon="🥉")
    with c3:
        st.info('**Primeros 5: 40%**', icon="🏅")

