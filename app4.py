
from fpdf import FPDF
NOMBRE_KIOSKO = "Kiosko Carloz Paz" \
LOGO=st.image
"LOGO="logo.png"

def renglon(pdf, texto , valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0. 9 valor, align="R", new_x="LMARGIN", new_y="NEXT")

    def armar_pdf(numero, fecha,cliente,producto , cantidad, precio, subtotal, descuento, iva , total):
        pdf= FPDF()
        pdf.add.page()

        pdf.image(LOGO, x=10,w=28)
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 12, NOMBRE_KIOSKO, align="R" , new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 7, f"Presupuesto N {numero}", align="R",new_x="LMARGIN", new_y="NEXT")
        pdf.cell(o.7, f "fecha:{fecha}", align="R", new_x="LMARGIN" , new_y="NEXT")
        pdf.In(15)

        pdf.set_font("Helvetica", "", 12)
        renglon(pdf,"cliente", cliente)
        renglon(pdf, f"(cantidad) x (producto)", f"${precio:.2f} c/u")

        renglon(pdf , "subtotal", f"{subtotal:.2f}")
        renglon(pdf, "Descuento", f"-${descuento:. 2f}")
        renglon(pdf, "IVA 21% , f"$[iva:.2f]"")
        pdf.set_font("Helvetica", "B", 14)
        renglon(pdf , "TOTAL", f "&{total:.2f}")

        pdf.in(10)
        pdf.set_font("Helvetica", "I" , 9)
        pdf.cell(0, 6, "presupuestom válido por 7 dias.", new_x="LMARGIN", new_y="NEXT")

        return bytes(pdf.output())