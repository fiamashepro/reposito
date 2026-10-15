from fpdf import FPDF
def armar_pdf(cliente, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(0, 12 "KIOSKO CARLOS PAZ", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell (0,9, f"Cliente: {cliente}" , new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,9, f"TOTAL:${total:.2f}", new_x="LMARGIN", new_y="NEXT")
    return bytes(pdf.output())