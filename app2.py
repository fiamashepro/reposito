import streamlit as st
PRECIO_GAS=2800
PRECIO_ALF= 1500
 
st.title("Kiosco Carlos Paz")
cliente= st.text_input("pedido de: ")
cantidad_alf= st.number_input("Cantidad de alfajores", min_value=0, step=1)
total_alf=PRECIO_ALF*cantidad_alf

cantidad_gas=st.number_input("cantidad de gaseosas", min_value=0, step=1)
total_gas=PRECIO_GAS*cantidad_gas

st.write(f"total alfajores:  {total_alf}")
st.write(f"total gaseosas:  {total_gas}")


total= total_alf + total_gas
st.write(f"Total a pagar: ${total}")

