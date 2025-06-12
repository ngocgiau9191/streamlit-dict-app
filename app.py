import streamlit as st
import pandas as pd
import difflib

# Căn giữa logo RRIV và thu nhỏ kích thước
st.markdown("""
<div style='text-align: center;'>
 st.image('logoVienfinal.png' width='100')
</div>
""", unsafe_allow_html=True)

# Tiêu đề chính + phụ đề (căn giữa)
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:36px; font-weight: bold;'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</span><br>
    <span style='font-size:18px; color:gray;'>📘 Tra từ điển chuyên ngành cao su Anh – Việt</span>
</div>
""", unsafe_allow_html=True)

# Đọc dữ liệu từ file Excel
df = pd.read_excel("Data_tudien_Giau.xlsx")

# Ô nhập từ tiếng Anh
keyword_en = st.text_input("🔍 Nhập từ tiếng Anh:")

if keyword_en:
    english_words = df['English'].dropna().str.lower().tolist()
    close_matches = difflib.get_close_matches(keyword_en.lower(), english_words, n=1, cutoff=0.6)

    if close_matches:
        match = close_matches[0]
        result = df[df['English'].str.lower() == match]
        vietnamese = result.iloc[0]['Vietnamese']
        st.success(f"✅ Bạn có ý muốn tra từ: **{match}**\n\nNghĩa tiếng Việt: **{vietnamese}**")
    else:
        st.warning("❌ Không tìm thấy từ gần đúng trong từ điển.")

# Phân cách
st.markdown("---")

# Tiêu đề phụ: từ điển Việt - Anh (căn giữa, cùng style)
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:18px; color:gray;'>📗 Tra từ điển chuyên ngành cao su Việt – Anh</span>
</div>
""", unsafe_allow_html=True)

# Ô nhập từ tiếng Việt
keyword_vi = st.text_input("🔍 Nhập từ tiếng Việt:")

if keyword_vi:
    vietnamese_words = df['Vietnamese'].dropna().str.lower().tolist()
    close_matches = difflib.get_close_matches(keyword_vi.lower(), vietnamese_words, n=1, cutoff=0.6)

    if close_matches:
        match = close_matches[0]
        result = df[df['Vietnamese'].str.lower() == match]
        english = result.iloc[0]['English']
        st.success(f"✅ Bạn có ý muốn tra từ: **{match}**\n\nNghĩa tiếng Anh: **{english}**")
    else:
        st.warning("❌ Không tìm thấy từ gần đúng trong từ điển.")
