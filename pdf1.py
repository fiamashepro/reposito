import streamlit as st
import pdf

cliente= st.text_input("Nombre del cliente")
total=9147.6
archivo=pdf.armar_pdf(cliente, total)

st.download_button("Descargar PDF", archivo, file_name="presupuesto.pdf", mime="application/pdf")