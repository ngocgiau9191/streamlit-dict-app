
import streamlit as st
import pandas as pd

# Đọc dữ liệu từ file Excel
df = pd.read_excel("Data_tudien_Giau.xlsx")

st.title("📘 Tra từ điển Anh - Việt")

# Nhập từ tiếng Anh
keyword = st.text_input("🔍 Nhập từ tiếng Anh:")

if keyword:
    result = df[df['English'].str.lower() == keyword.lower()]
    if not result.empty:
        vietnamese = result.iloc[0]['Vietnamese']
        st.success(f"✅ Nghĩa tiếng Việt: **{vietnamese}**")
    else:
        st.warning("❌ Không có trong từ điển.")
