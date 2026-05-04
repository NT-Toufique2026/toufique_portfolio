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
    .article-item {
        background: rgba(255, 255, 255, 0.03);
        padding: 10px 15px; border-radius: 8px; margin-bottom: 8px;
        border-left: 3px solid #ffcc00;
    }
    .article-item a { color: #60a5fa !important; text-decoration: none; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# Helper function to find images regardless of extra spaces or case
def get_image(search_term):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if search_term.lower() in f.lower():
            return f
    return None

# 01. Hero Section
with st.container():
    col_img, col_txt = st.columns([1, 2.2])
    with col_img:
        img_path = get_image("toufique-jpg")
        if img_path: st.image(img_path, width=380)
        else: st.image("https://via.placeholder.com/400", width=380)
    with col_txt:
        st.markdown(f"""
            <div class='hero-container'>
                <h1 class='main-header'>Md. Toufique Hossain</h1>
                <h2 style='color: #e5e7eb; font-weight: 400; margin-top:0;'>Senior Development Leader | Strategic Programme Management Expert</h2>
                <p style='color: #d1d5db;'>📍 Dhaka, Bangladesh | ✉️ toufique2010@gmail.com | 📞 +880 1779 700 327 | 
                <a href='https://www.linkedin.com/in/toufique-hossain-7b560140/' style='color:#0077b5; font-weight:bold;'>LinkedIn</a></p>
            </div>
            """, unsafe_allow_html=True)

# 02. EXPERIENCE
st.markdown("<div class='section-header'>💼 Professional Leadership</div>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1: 
    wave_img = get_image("WAVE LOGO")
    if wave_img: st.image(wave_img, width=110)
with col2:
    st.subheader("Deputy Coordinator — WAVE Foundation")
    st.write("**Senior Management | 2018 - Present**")
    st.write("Successfully managed USD 15M+ portfolios and led digital transformations.")

st.markdown("<hr style='border: 0.5px solid #333'>", unsafe_allow_html=True)
col3, col4 = st.columns([1, 4])
with col3: 
    brac_img = get_image("BRAC LOGO")
    if brac_img: st.image(brac_img, width=110)
with col4:
    st.subheader("Young Professional — BRAC International")
    st.write("**Management Traineeship | 2011 - 2015**")

# 04. ACADEMIC ENGAGEMENT
st.markdown("<div class='section-header'>🏫 Academic Engagement (Guest Lecturer)</div>", unsafe_allow_html=True)
st.write("\n")
v_col1, v_col2, v_col3 = st.columns(3)

with v_col1:
    img = get_image("South Asia")
    if img: st.image(img, width=160)
    else: st.write("**University of South Asia**")

with v_col2:
    img = get_image("Royal University")
    if img: st.image(img, width=160)
    else: st.write("**Royal University of Dhaka**")

with v_col3:
    img = get_image("Canadian University")
    if img: st.image(img, width=160)
    else: st.write("**Canadian University of Bangladesh**")

# 05. ARTICLES
st.markdown("<div class='section-header'>📝 Policy Columns & Publications</div>", unsafe_allow_html=True)
st.write("Explore full list in tabs below:")
tab1, tab2 = st.tabs(["📰 National Columns", "📊 Scholar"])
with tab1:
    st.markdown("<div class='article-item'><a href='https://www.tbsnews.net/author/md-toufique-hossain' target='_blank'>● The Business Standard Author Archive</a></div>", unsafe_allow_html=True)
    st.markdown("<div class='article-item'><a href='https://today.thefinancialexpress.com.bd/features-analysis/trumps-second-term-the-implications-for-others-1741975274' target='_blank'>● Financial Express Analysis</a></div>", unsafe_allow_html=True)

# 06. TV MEDIA
st.markdown("<div class='section-header'>📺 TV Media Appearances</div>", unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)
with v1: st.video("https://www.youtube.com/watch?v=dyUHqGHcHm0")
with v2: st.video("https://www.youtube.com/watch?v=gx4uO1DYkuQ")
with v3: st.video("https://www.youtube.com/watch?v=GZYm33tvWls")

# Footer
st.markdown("<br><hr><center style='color: #6b7280; padding-bottom: 50px;'>Md. Toufique Hossain | Executive Portfolio 2026</center>", unsafe_allow_html=True)