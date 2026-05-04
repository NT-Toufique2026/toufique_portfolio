import streamlit as st
import os

# 00. PAGE CONFIG
st.set_page_config(page_title="Md. Toufique Hossain | Executive Portfolio", layout="wide")

# Styling: Ensuring no extra gaps and premium look
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        background-image: linear-gradient(rgba(13, 17, 23, 0.96), rgba(13, 17, 23, 0.96)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }
    .main-title { font-size: 3.5rem; font-weight: 900; color: #ffcc00; letter-spacing: -1px; line-height: 1.1; margin-top: -20px; }
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
    }
    
    .expertise-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 20px; border-radius: 12px; border-bottom: 3px solid #ffcc00;
        height: 100%; transition: 0.3s;
    }
    
    .article-box {
        background: rgba(255, 255, 255, 0.02);
        padding: 12px 18px; border-radius: 8px; margin-bottom: 10px;
        border-left: 3px solid #ffcc00; transition: 0.2s;
        display: block; text-decoration: none;
    }
    .article-box:hover { background: rgba(255, 204, 0, 0.1); }
    .article-link { color: #60a5fa !important; font-weight: 500; text-decoration: none; }
    
    .edu-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 15px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Image Helper
def get_img(search_terms):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        for term in search_terms:
            if term.lower() in f.lower(): return f
    return None

# 01. HERO SECTION
with st.container():
    col_img, col_txt = st.columns([1, 2.2])
    with col_img:
        pic = get_img(["toufique-jpg", "image_b66a27"])
        if pic: st.image(pic, width=380)
    with col_txt:
        st.markdown("<h1 class='main-title'>Md. Toufique Hossain</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Senior Development Leader & Programme Operations Strategist</p>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color: #9ca3af; font-size: 1.1rem; line-height: 1.6;'>
        Fourteen years of leadership in combining financial governance with social intelligence. 
        Managing <b>USD 15M+</b> multi-donor portfolios while shaping policy through evidence-based advocacy.
        </p>
        <p style='color: #d1d5db; font-size: 0.9rem;'>
        📧 toufique2010@gmail.com | 📞 +880 1779 700 327 | 📍 Dhaka, Bangladesh | 
        <a href='https://www.linkedin.com/in/toufique-hossain-7b560140/' style='color:#ffcc00;'>LinkedIn Profile</a>
        </p>
        """, unsafe_allow_html=True)

# 02. CORE IMPACT
st.markdown("<div class='section-header'>🎯 Strategic Core Competencies</div>", unsafe_allow_html=True)
e1, e2, e3 = st.columns(3)
with e1:
    st.markdown("<div class='expertise-card'><b>Strategic Programme Leadership</b><br><small>End-to-end management of multi-sectoral programmes (WASH, Livelihoods, Climate Resilience).</small></div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='expertise-card'><b>Resource Mobilisation</b><br><small>Secured <b>USD 15M+</b> from World Bank, USAID, GIZ, and GAIN.</small></div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='expertise-card'><b>MEAL & AI Innovation</b><br><small>Real-time dashboards & paperless microfinance systems.</small></div>", unsafe_allow_html=True)

# 03. PROFESSIONAL MILESTONES
st.markdown("<div class='section-header'>💼 Experience</div>", unsafe_allow_html=True)
# WAVE Foundation
cw1, cw2 = st.columns([1, 4])
with cw1:
    wave_l = get_img(["WAVE LOGO"])
    if wave_l: st.image(wave_l, width=130)
with cw2:
    st.subheader("Deputy Coordinator — WAVE Foundation (2018 – Present)")
    st.markdown("- Managing $15M multi-donor portfolio. Led Digital Transformation in Microfinance.")

# BRAC International
cb1, cb2 = st.columns([1, 4])
with cb1:
    brac_l = get_img(["BRAC LOGO"])
    if brac_l: st.image(brac_l, width=130)
with cb2:
    st.subheader("Young Professional — BRAC International (2011 – 2015)")
    st.markdown("- Global MIS coordination across 5 country offices (Africa & Asia).")

# 04. THOUGHT LEADERSHIP (The missing parts)
st.markdown("<div class='section-header'>📝 Policy Advocacy & Research</div>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["📰 National Columns", "📊 Google Scholar & Books", "📺 TV Appearances"])

with tab1:
    st.markdown("### Featured Publications in National Media")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <a href='https://www.tbsnews.net/author/md-toufique-hossain' class='article-box'><span class='article-link'>The Business Standard: Author Archive</span></a>
        <a href='https://thefinancialexpress.com.bd/views/analysis/spin-off-effect-on-lower-income-groups-1605888994' class='article-box'><span class='article-link'>Financial Express: Spin-off Effect Analysis</span></a>
        <a href='https://today.thefinancialexpress.com.bd/features-analysis/trumps-second-term-the-implications-for-others-1741975274' class='article-box'><span class='article-link'>Financial Express: Trump’s 2nd Term Implications</span></a>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <a href='https://epaper.daily-sun.com/view/7/61676/2025-02-18' class='article-box'><span class='article-link'>Daily Sun: International Relations Analysis</span></a>
        <a href='https://www.prothomalo.com/opinion/column/8tyv0229rj' class='article-box'><span class='article-link'>Prothom Alo: Policy Perspective (Bangla)</span></a>
        <a href='https://bonikbarta.com/editorial/f2WqYrUw1a1fFhza' class='article-box'><span class='article-link'>Banik Barta: Financial Sector Editorial</span></a>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Academic Research & Scholarly Impact")
    st.markdown("""
    <div class='expertise-card'>
    <b>Google Scholar Profile:</b> Access 12+ Peer-Reviewed Research Papers.<br>
    <a href='https://scholar.google.com/citations?hl=en&user=3qtQiPAAAAAJ' target='_blank' style='color:#ffcc00; font-weight:bold;'>Go to Google Scholar Profile ↗️</a>
    </div><br>
    <div class='expertise-card'>
    <b>Published Book:</b> Bangladesh Share Market: Looking Ahead After Two Big Crashes.<br>
    <a href='https://www.amazon.com/-/es/Md-Toufique-Hossain/dp/9849048565' target='_blank' style='color:#ffcc00; font-weight:bold;'>View Book on Amazon ↗️</a>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### TV Media & Policy Talkshows")
    v1, v2, v3 = st.columns(3)
    with v1: 
        st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")
        st.caption("Talkshow on National Economy")
    with v2: 
        st.video("https://www.youtube.com/watch?v=gx4uO1DYkuQ")
        st.caption("Policy Debate: Social Development")
    with v3: 
        st.video("https://www.youtube.com/watch?v=GZYm33tvWls")
        st.caption("Analysis on International Relations")

# 05. EDUCATION & CERTS
st.markdown("<div class='section-header'>🎓 Education & Certifications</div>", unsafe_allow_html=True)
# (Previous Education and Certification code here...)
ce1, ce2 = st.columns([1, 2])
with ce1:
    st.markdown("<div class='edu-card'><b>MBA in AIS & PGD in IR</b><br>University of Dhaka</div>", unsafe_allow_html=True)
with ce2:
    st.markdown("Certifications: Digital Finance (Tufts), AI (Google), MEAL (PRIA India), Climate Finance (UNDP).")

# 06. ACADEMIC LOGOS
st.markdown("<div class='section-header'>🏫 Academic Engagement</div>", unsafe_allow_html=True)
l1, l2, l3, l4 = st.columns(4)
for i, name in enumerate(["South Asia", "Royal University", "Canadian", "Dhaka"]):
    with [l1,l2,l3,l4][i]:
        logo = get_img([name])
        if logo: st.image(logo, width=180)

st.markdown("<br><hr><center style='color: #6b7280;'>Md. Toufique Hossain | 2026 Portfolio</center>", unsafe_allow_html=True)