import streamlit as st
import pandas as pd
import difflib

# ======= STYLE: nền xanh lá nhạt và gạch phân cách =======
st.markdown("""
<style>
body {
    background-color: #e6f4ea;
}
hr {
    border: none;
    border-top: 1px solid #b2d8b2;
    width: 60%;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ======= HIỂN THỊ LOGO Ở GIỮA =======
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    st.image("logoVienfinal.png", width=80)

# ======= CHÚ THÍCH TRUNG TÂM, VIỆN =======
st.markdown("""
<div style='text-align: center; font-size:13px; color:gray; line-height:1.3;'>
    Viện Nghiên cứu Cao su Việt Nam<br>
    Trung tâm Nghiên cứu và Chuyển giao Tiến bộ Kỹ thuật
</div>
""", unsafe_allow_html=True)

# ======= GẠCH NGANG NGĂN CÁCH =======
st.markdown("<hr>", unsafe_allow_html=True)

# ======= TIÊU ĐỀ CHÍNH =======
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:36px; font-weight: bold;'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</span><br>
    <span style='font-size:18px; color:gray;'>📘 Tra từ điển chuyên ngành cao su Anh – Việt</span>
</div>
""", unsafe_allow_html=True)

# ======= ĐỌC DỮ LIỆU TỪ EXCEL =======
df = pd.read_excel("Data_tudien_Giau.xlsx")

# ======= TRA TỪ TIẾNG ANH =======
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

# ======= PHÂN CÁCH GIỮA HAI KHỐI =======
st.markdown("---")

# ======= TIÊU ĐỀ PHỤ: VIỆT – ANH =======
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:18px; color:gray;'>📗 Tra từ điển chuyên ngành cao su Việt – Anh</span>
</div>
""", unsafe_allow_html=True)

# ======= TRA TỪ TIẾNG VIỆT =======
keyword_vi = st.text_input("🔍 Nhập từ tiếng Việt:")
if keyword_vi:
    vietnamese_words = df['Vietnamese'].dropna().str.lower().tolist()
    close_matches = difflib.get_close_matches(keyword_
