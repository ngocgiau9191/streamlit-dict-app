import streamlit as st
import pandas as pd

# Đọc dữ liệu từ file Excel
df = pd.read_excel("Data_tudien_Giau.xlsx")

st.title("📘 Tra từ điển Anh - Việt")

# Ô nhập từ tiếng Anh
keyword_en = st.text_input("🔍 Nhập từ tiếng Anh:")

if keyword_en:
    result = df[df['English'].str.lower() == keyword_en.lower()]
    if not result.empty:
        vietnamese = result.iloc[0]['Vietnamese']
        st.success(f"✅ Nghĩa tiếng Việt: **{vietnamese}**")
    else:
        st.warning("❌ Không có trong từ điển.")

# Thêm phần tra từ Việt - Anh
st.markdown("---")  # đường phân cách
st.title("📗 Tra từ điển Việt - Anh")

# Ô nhập từ tiếng Việt
keyword_vi = st.text_input("🔍 Nhập từ tiếng Việt:")

if keyword_vi:
    result = df[df['Vietnamese'].str.lower() == keyword_vi.lower()]
    if not result.empty:
        english = result.iloc[0]['English']
        st.success(f"✅ Nghĩa tiếng Anh: **{english}**")
    else:
        st.warning("❌ Không có trong từ điển.")
