import streamlit as st
import os

# 00. PAGE CONFIG
st.set_page_config(page_title="Md. Toufique Hossain | Executive Portfolio", layout="wide")

# Advanced Styling (Cleaning the Mess)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        background-image: linear-gradient(rgba(13, 17, 23, 0.96), rgba(13, 17, 23, 0.96)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }
    .main-title { font-size: 3.5rem; font-weight: 900; color: #ffcc00; letter-spacing: -1px; line-height: 1.1; margin-top: -10px; }
    .sub-title { font-size: 1.4rem; color: #e5e7eb; font-weight: 300; margin-bottom: 20px; }
    
    .section-header {
        border-left: 6px solid #ffcc00;
        padding: 10px 20px;
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 800;
        margin-top: 50px;
        margin-bottom: 25px;
        text-transform: uppercase;
        background: rgba(255, 204, 0, 0.05);
        letter-spacing: 1px;
    }
    
    .hero-box { padding: 10px 0px; } /* Removed the background box from top */
    
    .expertise-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 20px; border-radius: 12px; border-bottom: 3px solid #ffcc00;
        height: 100%; transition: 0.3s;
    }
    .expertise-card:hover { background: rgba(255, 255, 255, 0.08); transform: translateY(-5px); }
    
    .article-box {
        background: rgba(255, 255, 255, 0.02);
        padding: 12px 18px; border-radius: 8px; margin-bottom: 10px;
        border-left: 3px solid #ffcc00; transition: 0.2s;
    }
    .article-box:hover { background: rgba(255, 204, 0, 0.1); }
    .article-link { color: #60a5fa !important; text-decoration: none; font-weight: 500; font-size: 0.95rem; }
    
    .edu-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 15px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Smart Image Helper
def get_img(search_terms):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        for term in search_terms:
            if term.lower() in f.lower(): return f
    return None

# 01. EXECUTIVE IDENTITY (Hero Section)
with st.container():
    col_img, col_txt = st.columns([1, 2.2])
    with col_img:
        # Reference: image_b66a27.jpg (Your profile picture)
        pic = get_img(["toufique-jpg", "image_b66a27"])
        if pic: st.image(pic, width=380)
    with col_txt:
        st.markdown("<div class='hero-box'>", unsafe_allow_html=True)
        st.markdown("<h1 class='main-title'>Md. Toufique Hossain</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Senior Development Leader & Programme Operations Strategist</p>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color: #9ca3af; font-size: 1.1rem; line-height: 1.6;'>
        Fourteen years of leadership in combining financial governance with social intelligence. 
        Managing <b>USD 15M+</b> multi-donor portfolios while shaping policy through evidence-based advocacy.
        </p>
        <p style='color: #d1d5db; font-size: 0.9rem;'>
        📍 Dhaka, Bangladesh | ✉️ toufique2010@gmail.com | 📞 +880 1779 700 327 | 
        <a href='https://www.linkedin.com/in/toufique-hossain-7b560140/' style='color:#ffcc00;'>LinkedIn Profile</a>
        </p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# 02. STRATEGIC CORE COMPETENCIES
st.markdown("<div class='section-header'>🎯 Strategic Core Competencies</div>", unsafe_allow_html=True)
e1, e2, e3 = st.columns(3)
with e1:
    st.markdown("<div class='expertise-card'><b>Strategic Programme Leadership</b><br><small>End-to-end management of multi-sectoral programmes (WASH, Livelihoods, Climate Resilience) across 15 districts.</small></div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='expertise-card'><b>Resource Mobilisation</b><br><small>Secured <b>USD 15M+</b> from World Bank, USAID, GIZ, and GAIN. Full-cycle expertise from grant compliance.</small></div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='expertise-card'><b>MEAL Framework Architecture</b><br><small>Deploying real-time risk dashboards to transition institutional culture toward evidence-led management.</small></div>", unsafe_allow_html=True)

# 03. PROFESSIONAL JOURNEY
st.markdown("<div class='section-header'>💼 Institutional Leadership & Impact</div>", unsafe_allow_html=True)

# WAVE Foundation
col_w1, col_w2 = st.columns([1, 4])
with col_w1:
    wave_l = get_img(["WAVE LOGO"])
    if wave_l: st.image(wave_l, width=150)
with col_w2:
    st.subheader("Deputy Coordinator — WAVE Foundation")
    st.info("Senior Management | Research & Donor Partnerships | 2018 – Present")
    st.markdown("""
    *   **Strategic Funding:** Secured **USD 15M+** from World Bank, USAID, GIZ, and Water.org.
    *   **Portfolio Oversight:** Directed multi-sectoral operations reaching **200,000+ households**.
    *   **Digital Transformation:** Spearheaded organizational shift to **Paperless Microfinance**.
    *   **Risk & Compliance:** Established rigorous internal control systems and risk mitigation protocols.
    *   **Stakeholder Advocacy:** Led national-level policy dialogues and consortium meetings.
    """)

st.write("\n")

# BRAC International
col_b1, col_b2 = st.columns([1, 4])
with col_b1:
    brac_l = get_img(["BRAC LOGO"])
    if brac_l: st.image(brac_l, width=150)
with col_b2:
    st.subheader("Young Professional — BRAC International")
    st.info("Management Traineeship & Global Coordination | 2011 – 2015")
    st.markdown("""
    *   **Institutional DNA:** Selected for management traineeship at **BRAC Learning Centre (BLC)**.
    *   **Global Coordination:** Supported monitoring across **5 BRAC International country offices**.
    *   **System Integration:** Synchronized MIS and financial reporting processes for **10,000+ participants**.
    *   **Operational Efficiency:** Identified process bottlenecks and implemented streamlined documentation.
    """)

# 04. ACADEMIC & CERTIFICATIONS
st.markdown("<div class='section-header'>🎓 Education & Global Certifications</div>", unsafe_allow_html=True)
c_edu, c_cert = st.columns([1, 1.8])

with c_edu:
    st.markdown("### Higher Education")
    du_l = get_img(["Dhaka University Logo"])
    if du_l: st.image(du_l, width=100)
    st.markdown("""
    <div class='edu-card'><b>PG Diploma in International Relations</b><br>University of Dhaka</div>
    <div class='edu-card'><b>MBA in AIS (GPA 3.85)</b><br>University of Dhaka</div>
    """, unsafe_allow_html=True)

with c_cert:
    st.markdown("### Global Certifications")
    l1, l2, l3, l4 = st.columns(4)
    with l1:
        tft = get_img(["Tufts"])
        if tft: st.image(tft, width=110); st.caption("Digital Finance")
    with l2:
        goog = get_img(["Google"])
        if goog: st.image(goog, width=110); st.caption("AI & ML")
    with l3:
        undp = get_img(["UNDP_BIOFIN"])
        if undp: st.image(undp, width=130); st.caption("Climate Finance")
    with l4:
        meal_l = get_img(["PRIYA"]) 
        if meal_l: st.image(meal_l, width=110); st.caption("MEAL & Impact")

# 05. ACADEMIC ENGAGEMENT LOGOS
st.markdown("<div class='section-header'>🏫 Academic Engagement</div>", unsafe_allow_html=True)
v_col1, v_col2, v_col3 = st.columns(3)
with v_col1:
    img1 = get_img(["South Asia"])
    if img1: st.image(img1, width=200)
with v_col2:
    img2 = get_img(["Royal University"])
    if img2: st.image(img2, width=200)
with v_col3:
    img3 = get_img(["Canadian University"])
    if img3: st.image(img3, width=200)

# 06. THOUGHT LEADERSHIP
st.markdown("<div class='section-header'>📝 Policy Advocacy & Publications</div>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📰 National Policy Columns", "📊 Scholar & Books"])
with tab1:
    ca, cb = st.columns(2)
    with ca:
        links1 = [
            ("The Business Standard Archive", "https://www.tbsnews.net/author/md-toufique-hossain"),
            ("Daily Sun: IR Analysis", "https://epaper.daily-sun.com/view/7/61676/2025-02-18")
        ]
        for text, url in links1: st.markdown(f"<div class='article-box'><a class='article-link' href='{url}'>● {text}</a></div>", unsafe_allow_html=True)
    with cb:
        st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")

with tab2:
    st.info("Author of 12 Peer-Reviewed Papers and 2 Books on Economics.")
    st.markdown("[View on Amazon](https://www.amazon.com/-/es/Md-Toufique-Hossain/dp/9849048565)")

# FOOTER
st.markdown("<br><hr><center style='color: #6b7280; padding-bottom: 50px;'>Md. Toufique Hossain | Executive Portfolio 2026</center>", unsafe_allow_html=True)