import streamlit as st
import pandas as pd
import difflib

# ========== GIAO DIỆN SÁNG/TỐI ==========
theme = st.radio("🎨 Chọn giao diện:", ["🌿 Sáng", "🌙 Tối"], horizontal=True)

if theme == "🌿 Sáng":
    background_color = "#e6f4ea"
    text_color = "black"
    hr_color = "#b2d8b2"
    link_color = "blue"
else:
    background_color = "#2c2c2c"
    text_color = "white"
    hr_color = "#888"
    link_color = "#66ccff"

# ========== CSS TOÀN TRANG ==========
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    max-width: 960px;
    margin: auto;
    background-color: {background_color};
    color: {text_color};
}}

body {{
    background-color: {background_color};
    color: {text_color};
}}

label, .stTextInput label {{
    color: {text_color} !important;
}}

a {{
    color: {link_color} !important;
}}

hr {{
    border: none;
    border-top: 1px solid {hr_color};
    width: 60%;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 25px;
}}

.big-title {{
    font-size: 28px;
    font-weight: bold;
    text-align: center;
}}

.small-note {{
    font-size: 14px;
    text-align: center;
    color: {text_color};
}}

div.footer-note {{
    font-size: 12px;
    text-align: center;
    color: {text_color};
    margin-top: 40px;
}}
</style>
""", unsafe_allow_html=True)

# ========== LOGO ==========
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    st.image("logoVienfinal.png", width=80)

st.markdown(f"""
<div class='small-note'>
    Viện Nghiên cứu Cao su Việt Nam<br>
    Trung tâm Nghiên cứu và Chuyển giao Tiến bộ Kỹ thuật
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ========== TIÊU ĐỀ ==========
st.markdown(f"""
<div class='big-title'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</div>
<div class='small-note'>📘📗 Tra từ điển chuyên ngành cao su Anh – Việt & Việt – Anh</div>
""", unsafe_allow_html=True)

# ========== ĐỌC FILE ==========
df = pd.read_excel("Data_tudien_Giau.xlsx")

# ========== HIỂN THỊ 2 Ô TRA SONG SONG ==========
col_en, col_vi = st.columns(2)

with col_en:
    st.markdown(f"<div class='small-note'>📘 Anh → Việt</div>", unsafe_allow_html=True)
    keyword_en = st.text_input("🔍 Nhập từ tiếng Anh:")
    if keyword_en:
        english_words = df['English'].dropna().str.lower().tolist()
        match_en = difflib.get_close_matches(keyword_en.lower(), english_words, n=1, cutoff=0.6)
        if match_en:
            result = df[df['English'].str.lower() == match_en[0]]
            st.success(f"✅ **{match_en[0]}** → **{result.iloc[0]['Vietnamese']}**")
        else:
            st.warning("❌ Không tìm thấy.")

with col_vi:
    st.markdown(f"<div class='small-note'>📗 Việt → Anh</div>", unsafe_allow_html=True)
    keyword_vi = st.text_input("🔍 Nhập từ tiếng Việt:")
    if keyword_vi:
        vietnamese_words = df['Vietnamese'].dropna().str.lower().tolist()
        match_vi = difflib.get_close_matches(keyword_vi.lower(), vietnamese_words, n=1, cutoff=0.6)
        if match_vi:
            result = df[df['Vietnamese'].str.lower() == match_vi[0]]
            st.success(f"✅ **{match_vi[0]}** → **{result.iloc[0]['English']}**")
        else:
            st.warning("❌ Không tìm thấy.")

# ========== CHÂN TRANG ==========
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div class='footer-note'>
    Thiết kế bởi <b>Phạm Thị Ngọc Giàu</b><br>
    📧 Email: <a href='mailto:ngocgiau.pham.rriv@gmail.com'>ngocgiau.pham.rriv@gmail.com</a>
</div>
""", unsafe_allow_html=True)
