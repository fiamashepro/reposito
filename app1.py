import streamlit as st
 
PRECIO_ALFAJOR = 1500
 
st.title("Kiosco Carlos Paz")
# pide un número entero desde 0
cliente= st.text_input("pedido de: ")
cantidad = st.number_input("Cantidad de alfajores", min_value=0, step=1)
total = cantidad * PRECIO_ALFAJOR
st.write(f"Total a pagar: ${total}")
