import streamlit as st
import os

# 00. PAGE CONFIG
st.set_page_config(page_title="Md. Toufique Hossain | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# 01. STYLING ENGINE (The Smart Look)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at top left, #1a1c2c, #0d1117);
        color: #e6edf3;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
        transition: 0.4s ease;
    }
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 204, 0, 0.3);
        transform: translateY(-5px);
    }

    .main-title { 
        font-size: 3.8rem; font-weight: 800; 
        background: linear-gradient(to right, #ffcc00, #f39c12);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    .tagline { font-size: 1.2rem; color: #8b949e; font-weight: 300; letter-spacing: 1px; }

    .section-label {
        color: #ffcc00; font-size: 0.9rem; font-weight: 700; 
        text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px;
    }

    .experience-title { color: #ffffff; font-weight: 600; font-size: 1.3rem; }
    .experience-org { color: #ffcc00; font-size: 1rem; margin-bottom: 10px; }
    
    /* Article links */
    .article-box {
        padding: 10px 15px; border-radius: 8px; background: rgba(255,255,255,0.02);
        border-left: 3px solid #ffcc00; margin-bottom: 10px; text-decoration: none; display: block;
    }
    .article-box:hover { background: rgba(255,204,0,0.1); }
    
    hr { border: 0; height: 1px; background: rgba(255,255,255,0.1); margin: 40px 0; }
    </style>
""", unsafe_allow_html=True)

# Helper function for images
def get_img(terms):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        for t in terms:
            if t.lower() in f.lower(): return f
    return None

# 02. HERO SECTION
with st.container():
    c1, c2 = st.columns([1, 2.5], gap="large")
    with c1:
        profile_pic = get_img(["toufique-jpg"])
        if profile_pic:
            st.image(profile_pic, use_container_width=True)
    with c2:
        st.markdown("<h1 class='main-title'>Md. Toufique Hossain</h1>", unsafe_allow_html=True)
        st.markdown("<p class='tagline'>Senior Development Leader & Strategic Consultant</p>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 1.1rem; line-height: 1.7; color: #9ca3af;'>
            14 years of driving high-impact programmes in Bangladesh. Expert in managing <b>$15M+ portfolios</b> 
            and blending financial governance with grassroots social engineering. 
            Shaping policy through media advocacy and digital innovation.
            </p>
        """, unsafe_allow_html=True)
        
        # Quick Contact
        st.markdown("""
            <p style='font-size: 0.9rem;'>
            📧 toufique2010@gmail.com | 📞 +880 1779 700 327 | 📍 Dhaka, Bangladesh
            </p>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 03. CORE IMPACT (Cards)
st.markdown("<p class='section-label'>Expertise</p>", unsafe_allow_html=True)
i1, i2, i3 = st.columns(3)
with i1:
    st.markdown("<div class='glass-card'><b>Programme Leadership</b><br><small style='color:#8b949e;'>Managing multi-sectoral operations across 15+ districts.</small></div>", unsafe_allow_html=True)
with i2:
    st.markdown("<div class='glass-card'><b>Resource Mobilization</b><br><small style='color:#8b949e;'>Secured funding from World Bank, USAID, GIZ & GAIN.</small></div>", unsafe_allow_html=True)
with i3:
    st.markdown("<div class='glass-card'><b>Digital Finance</b><br><small style='color:#8b949e;'>Pioneer in paperless microfinance & AI-driven governance.</small></div>", unsafe_allow_html=True)

# 04. PROFESSIONAL JOURNEY
st.markdown("<p class='section-label'>Experience</p>", unsafe_allow_html=True)

# WAVE Foundation
with st.container():
    w1, w2 = st.columns([1, 5])
    with w1:
        wave_logo = get_img(["WAVE LOGO"])
        if wave_logo: st.image(wave_logo, width=100)
    with w2:
        st.markdown("<div class='experience-title'>Deputy Coordinator</div>", unsafe_allow_html=True)
        st.markdown("<div class='experience-org'>WAVE Foundation | 2018 – Present</div>", unsafe_allow_html=True)
        st.markdown("""
        - Leading **$15M+ portfolio** management for WASH, Climate Resilience, and Livelihoods.
        - Strategic lead for donor compliance (World Bank, USAID, GIZ).
        - Architect of **Digital Microfinance** shift, ensuring 100% transparency.
        """)

st.write("") # Spacer

# BRAC International
with st.container():
    b1, b2 = st.columns([1, 5])
    with b1:
        brac_logo = get_img(["BRAC LOGO"])
        if brac_logo: st.image(brac_logo, width=100)
    with b2:
        st.markdown("<div class='experience-title'>Young Professional</div>", unsafe_allow_html=True)
        st.markdown("<div class='experience-org'>BRAC International | 2011 – 2015</div>", unsafe_allow_html=True)
        st.markdown("- Coordinated global MIS for Africa and Asia operations.")

st.markdown("<hr>", unsafe_allow_html=True)

# 05. ACADEMIC ENGAGEMENT & LOGOS
st.markdown("<p class='section-label'>Academic Partnerships</p>", unsafe_allow_html=True)
uni_cols = st.columns(5)
unis = ["Canadian", "Royal University", "South Asia", "Dhaka University", "Google"]
for i, uni in enumerate(unis):
    with uni_cols[i]:
        logo = get_img([uni])
        if logo: st.image(logo, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 06. THOUGHT LEADERSHIP (Simplified Links)
st.markdown("<p class='section-label'>Policy Advocacy & Media</p>", unsafe_allow_html=True)
pub_left, pub_right = st.columns(2)

with pub_left:
    st.markdown("### 📰 National Columns")
    links = [
        ("The Business Standard Archive", "https://www.tbsnews.net/author/md-toufique-hossain"),
        ("Financial Express: Spin-off Effects", "https://thefinancialexpress.com.bd/views/analysis/spin-off-effect-on-lower-income-groups-1605888994"),
        ("Daily Sun: IR Analysis", "https://epaper.daily-sun.com/view/7/61676/2025-02-18")
    ]
    for text, url in links:
        st.markdown(f"<a href='{url}' class='article-box' style='color: #60a5fa; text-decoration:none;'>{text}</a>", unsafe_allow_html=True)

with pub_right:
    st.markdown("### 📺 Media Presence")
    st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")

# 07. FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<center style='color:#4b5563; font-size:0.8rem;'>Md. Toufique Hossain &copy; 2026 | Optimized for Web Deployment</center>", unsafe_allow_html=True)