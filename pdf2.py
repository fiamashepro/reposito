import streamlit as st
from fpdf import FPDF

NOMBRE_KIOSCO= "Kiosco Carlos Paz"

LOGO=st.image

producto=["Alfajor"]


def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def armar_pdf(numero, fecha, cliente, cantidad, precio, subtotal, descuento, iva, total):
    pdf= FPDF()
    pdf.add_page()
    
    pdf.image(LOGO, x=10, y=10, w=28 )
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, NOMBRE_KIOSCO, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0,7, f"Presupuesto N {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.In(15)

    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    renglon(pdf, f"{cantidad} x {producto}", f"${precio:.2f} c/u")
    pdf.In(4)

    renglon(pdf, "Subtotal", f"${subtotal:.2f}")
    renglon(pdf, "Descuento", f"-{descuento:>2f}")
    renglon(pdf, "IVA 21%", f"${iva:.2f}")
    pdf.set_font("Helvetica", "B", 14)
    renglon(pdf, "TOTAL", f"${total:.2f}")

    pdf.In(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0,6, "Presupuesto valido por 7 dias.", new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())