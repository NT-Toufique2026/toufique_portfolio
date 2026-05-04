import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Md. Toufique Hossain | Portfolio", layout="wide")

# Advanced Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        background-image: linear-gradient(rgba(13, 17, 23, 0.95), rgba(13, 17, 23, 0.95)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }
    .main-header { font-size: 3.8rem; font-weight: 900; color: #ffcc00; margin-bottom: 0px; }
    .section-header {
        border-left: 8px solid #ffcc00;
        padding: 12px 20px;
        color: #ffffff;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 40px;
        text-transform: uppercase;
        background: rgba(255, 204, 0, 0.08);
    }
    .hero-container {
        background: rgba(255, 255, 255, 0.03);
        padding: 40px; border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .expertise-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 20px; border-radius: 12px; border-top: 3px solid #ffcc00;
        height: 100%; transition: 0.3s;
    }
    .expertise-card:hover { background: rgba(255, 255, 255, 0.08); transform: translateY(-5px); }
    .article-item {
        background: rgba(255, 255, 255, 0.03);
        padding: 10px 15px; border-radius: 8px; margin-bottom: 8px;
        border-left: 3px solid #ffcc00;
    }
    .article-item a { color: #60a5fa !important; text-decoration: none; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# Universal Image Finder Function
def get_img(search):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if search.lower() in f.lower(): return f
    return None

# 01. Hero Section
with st.container():
    col_img, col_txt = st.columns([1, 2.2])
    with col_img:
        pic = get_img("toufique-jpg")
        if pic: st.image(pic, width=380)
    with col_txt:
        st.markdown(f"""
            <div class='hero-container'>
                <h1 class='main-header'>Md. Toufique Hossain</h1>
                <h2 style='color: #e5e7eb; font-weight: 400; margin-top:0;'>Senior Development Leader | Strategic Programme Management Expert</h2>
                <p style='color: #9ca3af; font-style: italic; border-left: 4px solid #ffcc00; padding-left: 15px; font-size: 1.1rem; margin: 15px 0;'>
                "Organizations that sustain impact are those that combine financial governance with social intelligence."</p>
                <p style='color: #d1d5db;'>📍 Dhaka, Bangladesh | ✉️ toufique2010@gmail.com | 📞 +880 1779 700 327 | 
                <a href='https://www.linkedin.com/in/toufique-hossain-7b560140/' style='color:#0077b5; font-weight:bold;'>LinkedIn</a></p>
            </div>
            """, unsafe_allow_html=True)

# 02. CORE EXPERTISE (Added from your screenshot)
st.markdown("<div class='section-header'>🚀 Core Competencies</div>", unsafe_allow_html=True)
e1, e2, e3 = st.columns(3)
with e1:
    st.markdown("<div class='expertise-card'><b>Strategic Programme Leadership</b><br><small>End-to-end management of multi-sectoral programmes across 15 districts and 200,000+ households. Governed by SPHERE, CHS, and DEC standards.</small></div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='expertise-card'><b>Resource Mobilisation</b><br><small>USD 15M+ secured from World Bank, USAID, GIZ, GAIN, and Water.org. Expertise in donor negotiation and grant compliance.</small></div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='expertise-card'><b>MEAL Framework Architecture</b><br><small>Designed real-time risk dashboards and gender-disaggregated indicators for evidence-led adaptive management.</small></div>", unsafe_allow_html=True)

st.write("\n")
e4, e5 = st.columns(2)
with e4:
    st.markdown("<div class='expertise-card'><b>Policy Advocacy & Thought Leadership</b><br><small>12 peer-reviewed papers, 2 books, 100+ national columns, and 20+ TV appearances shaping the policy environment.</small></div>", unsafe_allow_html=True)
with e5:
    st.markdown("<div class='expertise-card'><b>AI, Digital Finance & Climate Innovation</b><br><small>Google AI & UNDP BIOFIN certified. Applied AI and digital tools to cut transaction costs by 60% at WAVE Foundation.</small></div>", unsafe_allow_html=True)

# 03. PROFESSIONAL LEADERSHIP
st.markdown("<div class='section-header'>💼 Professional Leadership</div>", unsafe_allow_html=True)
# WAVE Foundation
col1, col2 = st.columns([1, 4])
with col1: 
    wave = get_img("WAVE LOGO")
    if wave: st.image(wave, width=110)
with col2:
    st.subheader("Deputy Coordinator — WAVE Foundation")
    st.write("**Senior Management | 2018 - Present**")
    st.markdown("""
    - **Resource Mobilization:** Successfully raised and managed over **USD 15M+** from global donors including World Bank, USAID, GIZ, and GAIN.
    - **Strategic Oversight:** Leading multi-sectoral development portfolios across 15 districts, impacting over **200,000 households**.
    - **Digital Innovation:** Spearheaded the organizational shift to **Paperless Microfinance**, optimizing operational efficiency and transparency.
    - **Financial Governance:** Ensuring robust financial compliance and audit-readiness for high-value international development projects.
    """)

st.markdown("<hr style='border: 0.1px solid #333'>", unsafe_allow_html=True)
# BRAC
col3, col4 = st.columns([1, 4])
with col3: 
    brac = get_img("BRAC LOGO")
    if brac: st.image(brac, width=110)
with col4:
    st.subheader("Young Professional — BRAC International")
    st.write("**Management Traineeship | 2011 - 2015**")
    st.markdown("""
    - **Global Operations:** Standardized financial reporting systems across **5 BRAC International country offices**.
    - **Leadership Training:** Successfully completed high-intensity management training at **BRAC Learning Centre (BLC)**.
    - **Process Improvement:** Implemented streamlined data protocols to improve field-level reporting accuracy.
    """)

# 04. ACADEMIC ENGAGEMENT (University Logos)
st.markdown("<div class='section-header'>🏫 Academic Engagement (Guest Lecturer)</div>", unsafe_allow_html=True)
v_col1, v_col2, v_col3 = st.columns(3)
with v_col1:
    img1 = get_img("South Asia")
    if img1: st.image(img1, width=160)
with v_col2:
    img2 = get_img("Royal University")
    if img2: st.image(img2, width=160)
with v_col3:
    img3 = get_img("Canadian University")
    if img3: st.image(img3, width=160)

# 05. POLICY COLUMNS & PUBLICATIONS
st.markdown("<div class='section-header'>📝 Policy Columns & Publications</div>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📰 National Columns", "📊 Scholar & Books"])
with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        arts = [("Financial Express: Trump's 2nd Term", "https://today.thefinancialexpress.com.bd/features-analysis/trumps-second-term-the-implications-for-others-1741975274"),
                ("The Business Standard: Archive", "https://www.tbsnews.net/author/md-toufique-hossain"),
                ("Daily Observer: IMF Strategies", "https://observerbd.com/news/513265"),
                ("Prothom Alo: Policy Perspective", "https://www.prothomalo.com/opinion/column/8tyv0229rj")]
        for t, l in arts: st.markdown(f"<div class='article-item'><a href='{l}' target='_blank'>● {t}</a></div>", unsafe_allow_html=True)
    with col_b:
        arts2 = [("Financial Express: Spin-off effect", "https://thefinancialexpress.com.bd/views/analysis/spin-off-effect-on-lower-income-groups-1605888994"),
                 ("Banik Barta: Editorial", "https://bonikbarta.com/editorial/f2WqYrUw1a1fFhza"),
                 ("Business Mirror: Banking Crisis", "https://epaper.bmirror.net/nogor-edition/2026-03-04/4"),
                 ("Daily Observer: Share Market", "https://www.observerbd.com/details.php?id=305645")]
        for t, l in arts2: st.markdown(f"<div class='article-item'><a href='{l}' target='_blank'>● {t}</a></div>", unsafe_allow_html=True)

# 06. TV MEDIA
st.markdown("<div class='section-header'>📺 TV Media Appearances</div>", unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)
with v1: st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")
with v2: st.video("https://www.youtube.com/watch?v=gx4uO1DYkuQ")
with v3: st.video("https://www.youtube.com/watch?v=GZYm33tvWls")

st.markdown("<br><hr><center style='color: #6b7280; padding-bottom: 50px;'>Md. Toufique Hossain | Executive Portfolio 2026</center>", unsafe_allow_html=True)