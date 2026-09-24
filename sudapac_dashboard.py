# -*- coding: utf-8 -*-
"""
Sudapac Dashboard — واجهة لوحة التحكم المركزية للمنصة (Streamlit UI)
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sudapac OS", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stSidebarView"], .stApp { direction: RTL; text-align: right; font-family: 'Cairo', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 مركز تحكم Sudapac اللوجستي الذكي")
st.subheader("إدارة الامتثال وكروت التشغيل الفورية — الرياض")

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric(label="🛂 بوابات المستودعات", value="مسموح آلياً")
with col2: st.metric(label="📊 كروت التشغيل TGA", value="مطابقة وسارية")
with col3: st.metric(label="🚨 تصعيد لتدخل بشري", value="0 حرج")
with col4: st.metric(label="🧾 فواتير مفحوصة (ZATCA)", value="مطابقة 100%")

st.divider()
st.header("🔀 التدفق الميداني والعمليات اللحظية")
st.success("✅ شاحنة نقل ثقيل (قاطرة ومقطورة) دخلت المستودع بنجاح ومطابقة لمواصفات وزارة النقل.")
