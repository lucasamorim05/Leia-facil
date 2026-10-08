from main import simplifica

import streamlit as st

st.title("Leia fácil")


direita, esquerda = st.columns(2)

with direita:
    st.write("Texto original")
    texto_usuario = st.text_area("Digite o texto aqui")
    resultado = simplifica(texto_usuario)

    
with esquerda:
    
    st.write("Texto simplificado")
    st.write(resultado)

