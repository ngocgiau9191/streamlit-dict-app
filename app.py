import streamlit as st
import pandas as pd
import difflib

# Căn giữa logo vào cột số 4 trong 7 cột, thêm 2 dòng mô tả
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    st.image("logoVienfinal.png", width=80)
    st.markdown("""
    <div style='text-align: center; font-size:13px; color:gray; line-height:1.2;'>
        Viện Nghiên cứu Cao su Việt Nam<br>
        Trung tâm Nghiên cứu và Chuyển giao Tiến bộ Kỹ thuật
    </div>
    """, unsafe_allow_html=True)

# Tiêu đề chính + phụ đề (căn giữa)
st.markdown("""
<div style='text-align: center;'>
    <span style='font-size:36px; font-weight: bold;'>🧑‍🤝‍🧑 CLB Tiếng Anh – TT NCCG TBKT</span><br>
    <span style='font-size:18px; color:gray;'>📘 Tra từ điển chuyên ngành cao su Anh – Việt</span>
</div>
""", unsafe_allow_html=True)
