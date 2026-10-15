import streamlit as st

productos = ["Alfajor", "Gaseosa", "Chicle"]
precios = [1500, 2800, 500]


st.title("Kiosco Carlos Paz")
cliente = st.text_input("Nombre del cliente")
producto = st.selectbox("Producto", productos)
cantidad = st.number_input("Cantidad", min_value=0, step=1)
pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])


precio = 0
for i in range(len(productos)):
 if productos[i] == producto:
  precio = precios[i]
subtotal = cantidad * precio
if pago == "Efectivo":
 total = subtotal - subtotal * 10 // 100 # 10% de descuento
else:
 total = subtotal
st.divider()
if cantidad == 0:
 st.warning("Elegí una cantidad")
else:
 st.metric("Total a pagar", f"${total}")
 st.success(f"Pedido de {cliente}: {cantidad} x {producto}")


#st.image("loll.png", width=500)