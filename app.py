import streamlit as st
#st -> steamlit es una abreviacion xd
st.title("kioskito de fama")

cliente=st.text_input("tu nombre wachin: ")

cantidad=st.number_input("cantidad de alfajores:" , 0, step=1)

total=cantidad * 1500

st.write(f"total pagar: {total},{cliente}, ¡gracias por su compra! :3 ")

