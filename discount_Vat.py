import streamlit as st

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

full_price = st.number_input(
    "กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=1000.00, step=1.00, format="%.2f"
)

discount_percent = st.number_input(
    "กรอกส่วนลด (%):",
    min_value=0.0,
    max_value=100.0,
    value=20.00,
    step=1.00,
    format="%.2f",
)

st.divider() 


discount_amount = full_price * (discount_percent / 100)
price_after_discount = full_price - discount_amount
vat_amount = price_after_discount * 0.07
net_price = price_after_discount + vat_amount


st.write(f"• ส่วนลด ({discount_percent:.0f}%): -{discount_amount:,.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {price_after_discount:,.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat_amount:,.2f} บาท")


st.subheader(f"• ราคาสุทธิที่ต้องจ่าย: {net_price:,.2f} บาท")

st.divider()  

st.caption("thanakrit boonruang เลขที่ 33 ม.4/5")
