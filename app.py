import streamlit as st
import pandas as pd
import difflib

# ========== NÚT CHUYỂN CHẾ ĐỘ GIAO DIỆN ==========
theme = st.radio("🎨 Chọn giao diện:", ["🌿 Sáng", "🌙 Tối"], horizontal=True)

# ========== ÁP DỤNG NỀN THEO CHẾ ĐỘ ==========
if theme == "🌿 Sáng":
    background_color = "#e6f4ea"
    text_color = "black"
    hr_color = "#b2d8b2"
else:
    background_color = "#2c2c2c"
    text_color = "white"
    hr_color = "#888888"

# CSS tùy chỉnh giao diện
st.markdown(f"""
<style>
body {{
    background-color: {background_color} !important;
    color: {text_color};
}}
[data-testid="stAppViewContainer"] {{
    background-color: {background_color} !important;
    color: {text_color};
}}
hr {{
    border: none;
    border-top: 1px solid {hr_color};
    width: 60%;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 25px;
}}
</style>
""", unsafe_allow_html=True)

# ========== HIỂN THỊ LOGO TRUNG TÂM ==========
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    st.image("logoVienfinal.png", width=80)

# ========== CHÚ THÍCH LOGO ==========
st.markdown(f"""
<div style='text-align: center; font-size:13px; color:gray; line-height:1.3;'>
    Viện Nghiên cứu Cao su Việt Nam<br>
    Trung tâm Nghiên cứu và Chuyển giao Tiến bộ Kỹ thuật
</div>
""", unsafe_allow_html=True)

# ========== GẠCH NGANG TRANG TRÍ ==========
st.markdown("<hr>", unsafe_allow_html=True)

# ========== TIÊU ĐỀ CHÍNH ==========
st.markdown(f"""
<div style='text-align: center; color:{text_color};'>
    <span style='font-size:36px; font-weight: bold;'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</span><br>
    <span style='font-size:18px; color:gray;'>📘 Tra từ điển chuyên ngành cao su Anh – Việt</span>
</div>
""", unsafe_allow_html=True)

# ========== ĐỌC FILE EXCEL ==========
df = pd.read_excel("Data_tudien_Giau.xlsx")

# ========== TỪ ĐIỂN ANH – VIỆT ==========
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

# ========== GẠCH PHÂN CÁCH ==========
st.markdown("---")

# ========== TIÊU ĐỀ PHỤ ==========
st.markdown(f"""
<div style='text-align: center; color:gray;'>
    <span style='font-size:18px;'>📗 Tra từ điển chuyên ngành cao su Việt – Anh</span>
</div>
""", unsafe_allow_html=True)

# ========== TỪ ĐIỂN VIỆT – ANH ==========
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
