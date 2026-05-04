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
    
    .stApp::before {
        content: "IDEA • DATA • ECONOMICS • STRATEGY";
        position: fixed;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%) rotate(-25deg);
        font-size: 7vw; font-weight: 900;
        color: rgba(255, 255, 255, 0.02);
        white-space: nowrap; z-index: -1; pointer-events: none;
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
        transition: 0.3s; height: 100%;
    }
    .info-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.07); }

    .article-item {
        background: rgba(255, 255, 255, 0.03);
        padding: 10px 15px; border-radius: 8px; margin-bottom: 8px;
        border-left: 3px solid #ffcc00;
    }
    .article-item a { color: #60a5fa !important; text-decoration: none; font-weight: 600; font-size: 1rem; }
    .article-item a:hover { color: #ffcc00 !important; }
    </style>
    """, unsafe_allow_html=True)

# 01. Hero Section
with st.container():
    col_img, col_txt = st.columns([1, 2.2])
    with col_img:
        st.image("toufique-jpg.png" if os.path.exists("toufique-jpg.png") else "https://via.placeholder.com/400", width=380)
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

# 02. EXPERIENCE
st.markdown("<div class='section-header'>💼 Professional Leadership</div>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1: st.image("WAVE LOGO.jpeg", width=110)
with col2:
    st.subheader("Deputy Coordinator — WAVE Foundation")
    st.write("**Senior Management | 2018 - Present**")
    st.markdown("""
    - **Resource Mobilization:** Successfully raised and managed over **USD 15M+** from global donors including World Bank, USAID, GIZ, and GAIN.
    - **Strategic Oversight:** Leading multi-sectoral development portfolios across 15 districts, impacting over **200,000 households**.
    - **Digital Innovation:** Spearheaded the organizational shift to **Paperless Microfinance**, optimizing operational efficiency and transparency.
    - **Financial Governance:** Ensuring robust financial compliance and audit-readiness for high-value international development projects.
    - **Stakeholder Engagement:** Building strategic partnerships with government agencies and international NGOs to drive sustainable social impact.
    """)

st.markdown("<hr style='border: 0.5px solid #333'>", unsafe_allow_html=True)
col3, col4 = st.columns([1, 4])
with col3: st.image("BRAC LOGO.png", width=110)
with col4:
    st.subheader("Young Professional — BRAC International")
    st.write("**Management Traineeship | 2011 - 2015**")
    st.markdown("""
    - **Global Operations:** Standardized financial reporting and operational monitoring systems across **5 BRAC International country offices**.
    - **Leadership Training:** Successfully completed high-intensity management and residential leadership training at **BRAC Learning Centre (BLC)**.
    - **Process Improvement:** Implemented streamlined data management protocols to improve field-level reporting accuracy.
    - **Cross-Cultural Management:** Collaborated with diverse international teams to align local operations with global organizational standards.
    - **Capacity Building:** Conducted financial literacy and management workshops for field staff to enhance institutional efficiency.
    """)

# 03. GLOBAL CERTS & EDUCATION
st.markdown("<div class='section-header'>🎓 Global Expertise & Education</div>", unsafe_allow_html=True)
c_edu, c_cert = st.columns([1, 2.2])
with c_edu:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    if os.path.exists("Dhaka University Logo.png"):
        st.image("Dhaka University Logo.png", width=75)
    st.markdown("### Academic")
    st.markdown("**MBA in AIS**")
    st.write("Dhaka University | GPA 3.85")
    st.write("**PGD in International Relations**")
    st.markdown("</div>", unsafe_allow_html=True)

with c_cert:
    st.markdown("<div class='info-card'><h3>Certifications</h3>", unsafe_allow_html=True)
    l1, l2, l3 = st.columns(3)
    with l1: 
        st.image("Tufts University,Fletcher School_FinTech.jpg", width=90)
        st.caption("**Tufts University, Fletcher School, USA, Digital Money**") # Updated
    with l2: 
        st.image("Google.jpeg", width=90)
        st.caption("**AI & Machine Learning**") # Confirmed
    with l3: 
        st.image("UNDP_BIOFIN.png", width=120)
        st.caption("UNDP BIOFIN")
    st.markdown("</div>", unsafe_allow_html=True)

# 04. ALL ARTICLES & POLICY COLUMNS
st.markdown("<div class='section-header'>📝 Policy Columns & Publications</div>", unsafe_allow_html=True)
tab_column, tab_scholar = st.tabs(["📰 National Columns (Full List)", "📊 Google Scholar & Books"])

with tab_column:
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### Economic Policy & Governance")
        articles = [
            ("Financial Express: Trump's 2nd Term Implications", "https://today.thefinancialexpress.com.bd/features-analysis/trumps-second-term-the-implications-for-others-1741975274"),
            ("The Business Standard: Author Archive (All Articles)", "https://www.tbsnews.net/author/md-toufique-hossain"),
            ("Daily Observer: IMF and Growth Strategies", "https://observerbd.com/news/513265"),
            ("Prothom Alo: Policy Perspective (Bangla)", "https://www.prothomalo.com/opinion/column/8tyv0229rj"),
            ("Daily Sun: International Relations Analysis", "https://epaper.daily-sun.com/view/7/61676/2025-02-18")
        ]
        for title, link in articles:
            st.markdown(f"<div class='article-item'><a href='{link}' target='_blank'>● {title}</a></div>", unsafe_allow_html=True)

    with col_b:
        st.write("### Financial Markets & Analysis")
        articles_2 = [
            ("Financial Express: Spin-off effect on lower income", "https://thefinancialexpress.com.bd/views/analysis/spin-off-effect-on-lower-income-groups-1605888994"),
            ("Banik Barta: Financial Sector Editorial", "https://bonikbarta.com/editorial/f2WqYrUw1a1fFhza"),
            ("Business Mirror: Banking Sector Crisis", "https://epaper.bmirror.net/nogor-edition/2026-03-04/4"),
            ("Business Mirror: Economic Commentary", "https://epaper.bmirror.net/nogor-edition/2026-02-09/4"),
            ("Daily Observer: Post-Crash Share Market Analysis", "https://www.observerbd.com/details.php?id=305645")
        ]
        for title, link in articles_2:
            st.markdown(f"<div class='article-item'><a href='{link}' target='_blank'>● {title}</a></div>", unsafe_allow_html=True)

with tab_scholar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("[![Scholar](https://img.shields.io/badge/Google_Scholar-Explore_Papers-blue?style=for-the-badge&logo=google-scholar)](https://scholar.google.com/citations?hl=en&user=3qtQiPAAAAAJ)")
    st.info("**Featured Book:** Bangladesh Share Market: Looking Ahead after Two Big Crashes ([Rokomari Link](https://www.rokomari.com/book/80324/bangladesh-share-market-looking-ahead-after-two-big-crashes))")

# 05. TV MEDIA
st.markdown("<div class='section-header'>📺 TV Media Appearances</div>", unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)
with v1: st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")
with v2: st.video("https://www.youtube.com/watch?v=gx4uO1DYkuQ")
with v3: st.video("https://www.youtube.com/watch?v=GZYm33tvWls")

# Footer
st.markdown("<br><hr><center style='color: #6b7280; padding-bottom: 50px;'>Md. Toufique Hossain | Executive Portfolio 2026</center>", unsafe_allow_html=True)