import streamlit as st
import pandas as pd
import difflib

# 🖼️ Logo ở giữa (cột 4 của 7 cột)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    st.image("logoVienfinal.png", width=80)

# 📝 Chú thích logo không chia cột, canh giữa toàn trang
st.markdown("""
<div style='text-align: center; font-size:13px; color:gray; line-height:1.3;'>
    Viện Nghiên cứu Cao su Việt Nam<br>
    Trung tâm Nghiên cứu và Chuyển giao Tiến bộ Kỹ thuật
</div>
""", unsafe_allow_html=True)

# ➖ Gạch phân cách mềm bên dưới phần giới thiệu
st.markdown("""
<hr style='border: none; border-top: 1px solid #ccc; width: 60%; margin: auto; margin-top: 10px; margin-bottom: 25px;'>
""", unsafe_allow_html=True)

# 🎯 Tiêu đề chính
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:36px; font-weight: bold;'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</span><br>
    <span style='font-size:18px; color:gray;'>📘 Tra từ điển chuyên ngành cao su Anh – Việt</span>
</div>
""", unsafe_allow_html=True)
