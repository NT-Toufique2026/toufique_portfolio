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
    .info-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 20px; border-radius: 15px; border-top: 4px solid #ffcc00;
        height: 100%;
    }
    .article-item {
        background: rgba(255, 255, 255, 0.03);
        padding: 10px 15px; border-radius: 8px; margin-bottom: 8px;
        border-left: 3px solid #ffcc00;
    }
    .article-item a { color: #60a5fa !important; text-decoration: none; font-weight: 600; font-size: 1rem; }
    .article-item a:hover { color: #ffcc00 !important; }
    </style>
    """, unsafe_allow_html=True)

# Helper function for Image Finding
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

# 02. EXPERIENCE (Restored full details)
st.markdown("<div class='section-header'>💼 Professional Leadership</div>", unsafe_allow_html=True)
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
    - **Financial Governance:** Ensuring robust financial compliance and audit-readiness for international development projects.
    - **Stakeholder Engagement:** Building strategic partnerships with government agencies and international NGOs.
    """)

st.markdown("<hr style='border: 0.5px solid #333'>", unsafe_allow_html=True)
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
    - **Process Improvement:** Implemented streamlined data management protocols to improve field-level reporting accuracy.
    - **Capacity Building:** Conducted financial literacy workshops for field staff to enhance institutional efficiency.
    """)

# 03. GLOBAL CERTS & EDUCATION
st.markdown("<div class='section-header'>🎓 Global Expertise & Education</div>", unsafe_allow_html=True)
c_edu, c_cert = st.columns([1, 2.2])
with c_edu:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    du = get_img("Dhaka University")
    if du: st.image(du, width=75)
    st.markdown("### Academic\n**MBA in AIS**\nDhaka University | GPA 3.85\n\n**PGD in International Relations**")
    st.markdown("</div>", unsafe_allow_html=True)
with c_cert:
    st.markdown("<div class='info-card'><h3>Certifications</h3>", unsafe_allow_html=True)
    l1, l2, l3 = st.columns(3)
    with l1: 
        tft = get_img("Tufts")
        if tft: st.image(tft, width=90)
        st.caption("Tufts University, USA")
    with l2: 
        goog = get_img("Google")
        if goog: st.image(goog, width=90)
        st.caption("AI & ML")
    with l3: 
        undp = get_img("UNDP")
        if undp: st.image(undp, width=120)
        st.caption("UNDP BIOFIN")
    st.markdown("</div>", unsafe_allow_html=True)

# 04. ACADEMIC ENGAGEMENT (University Logos)
st.markdown("<div class='section-header'>🏫 Academic Engagement (Guest Lecturer)</div>", unsafe_allow_html=True)
v_col1, v_col2, v_col3 = st.columns(3)
with v_col1:
    img1 = get_img("South Asia")
    if img1: st.image(img1, width=160)
    else: st.write("**University of South Asia**")
with v_col2:
    img2 = get_img("Royal University")
    if img2: st.image(img2, width=160)
    else: st.write("**Royal University of Dhaka**")
with v_col3:
    img3 = get_img("Canadian University")
    if img3: st.image(img3, width=160)
    else: st.write("**Canadian University of Bangladesh**")

# 05. ALL ARTICLES (Full Links Restored)
st.markdown("<div class='section-header'>📝 Policy Columns & Publications</div>", unsafe_allow_html=True)
tab_column, tab_scholar = st.tabs(["📰 National Columns (Full List)", "📊 Google Scholar"])

with tab_column:
    col_a, col_b = st.columns(2)
    with col_a:
        arts = [
            ("Financial Express: Trump's 2nd Term", "https://today.thefinancialexpress.com.bd/features-analysis/trumps-second-term-the-implications-for-others-1741975274"),
            ("The Business Standard: Author Archive", "https://www.tbsnews.net/author/md-toufique-hossain"),
            ("Daily Observer: IMF Strategies", "https://observerbd.com/news/513265"),
            ("Prothom Alo: Policy Perspective", "https://www.prothomalo.com/opinion/column/8tyv0229rj")
        ]
        for title, link in arts:
            st.markdown(f"<div class='article-item'><a href='{link}' target='_blank'>● {title}</a></div>", unsafe_allow_html=True)
    with col_b:
        arts2 = [
            ("Financial Express: Lower income groups", "https://thefinancialexpress.com.bd/views/analysis/spin-off-effect-on-lower-income-groups-1605888994"),
            ("Banik Barta: Editorial", "https://bonikbarta.com/editorial/f2WqYrUw1a1fFhza"),
            ("Business Mirror: Banking Crisis", "https://epaper.bmirror.net/nogor-edition/2026-03-04/4"),
            ("Daily Observer: Share Market", "https://www.observerbd.com/details.php?id=305645")
        ]
        for title, link in arts2:
            st.markdown(f"<div class='article-item'><a href='{link}' target='_blank'>● {title}</a></div>", unsafe_allow_html=True)

with tab_scholar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("[![Scholar](https://img.shields.io/badge/Google_Scholar-Explore-blue)](https://scholar.google.com/citations?hl=en&user=3qtQiPAAAAAJ)")
    st.info("**Featured Book:** Bangladesh Share Market ([Rokomari Link](https://www.rokomari.com/book/80324/bangladesh-share-market-looking-ahead-after-two-big-crashes))")

# 06. TV MEDIA
st.markdown("<div class='section-header'>📺 TV Media Appearances</div>", unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)
with v1: st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")
with v2: st.video("https://www.youtube.com/watch?v=gx4uO1DYkuQ")
with v3: st.video("https://www.youtube.com/watch?v=GZYm33tvWls")

st.markdown("<br><hr><center style='color: #6b7280; padding-bottom: 50px;'>Md. Toufique Hossain | Portfolio 2026</center>", unsafe_allow_html=True)