# app.py — Priyadharshini Ramesh Kumar | Streamlit Portfolio

import streamlit as st
from pathlib import Path
import textwrap
from PIL import Image

st.set_page_config(
    page_title="Priyadharshini Ramesh Kumar — Portfolio",
    page_icon="💡",
    layout="wide",
)

# -----------------------------
# CSS Styling (fixed error: removed bare .footer selector issue)
# -----------------------------
st.markdown(
    """
    <style>
      .app-title h1 {margin-bottom: 0.25rem;}
      .app-subtitle {color: #463F3A; font-weight: 600; margin-top: 0.1rem; margin-bottom: 0.5rem;}
      .chip {display:inline-block; padding:0.2rem 0.55rem; margin:0 0.25rem 0.25rem 0; border-radius:999px; background:#F7F4F3; border:1px solid #e8e8e8; font-size:0.82rem;}
      .card-grid {display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap:1rem;}
      .card {border-radius:16px; padding:1rem; background:white; border:1px solid #eee; box-shadow:0 2px 10px rgba(0,0,0,0.04);}
      .pill {display:inline-block; background:#E0AFA0; color:#1b1b1b; padding:0.15rem 0.5rem; border-radius:999px; font-size:0.75rem; margin-right:0.35rem; margin-bottom:0.35rem; opacity:0.9;}
      .soft {background:#F7F4F3; border:1px solid #ececec; border-radius:16px; padding:1rem;}
      .profile-img {width:128px; height:128px; border-radius:50%; object-fit:cover; border:3px solid #E0AFA0;}
      .profile-placeholder {width:128px; height:128px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:#F7F4F3; border:3px dashed #E0AFA0; color:#555; font-weight:600;}
      .download-note {font-size:0.9rem; color:#666;}
      .section-title {margin-top:0.25rem;}
      .footer-text {text-align:center; color:#666; font-size:0.85rem; margin-top:2rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Content Data
# -----------------------------
NAME = "Priyadharshini Ramesh Kumar"
TITLE = "Data Scientist / Data Analyst"
LOCATION = "College Station, TX, USA"
EMAIL = "priyadharshini01.r3034@gmail.com"
PHONE = "+1-979-218-2333"
LINKEDIN = "https://linkedin.com/in/priyadharshini-r330"
GITHUB = "https://github.com/kyo330"
RESUME_FILENAME = "RameshKumar_Priyadharshini-Data_Analyst.pdf"

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 5])
with col1:
    img_path = Path("assets/profile.jpg")
    if img_path.exists():
        st.image(str(img_path), use_column_width=False)
    else:
        st.markdown('<div class="profile-placeholder">Add profile.jpg</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='app-title'><h1>{NAME}</h1></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='app-subtitle'>{TITLE} · {LOCATION}</div>", unsafe_allow_html=True)
    st.write(f"📧 [{EMAIL}](mailto:{EMAIL})  ·  📞 {PHONE}  ·  🔗 [LinkedIn]({LINKEDIN})  ·  💻 [GitHub]({GITHUB})")
    st.divider()

# -----------------------------
# About
# -----------------------------
st.subheader("About")
st.write("Graduate Data Scientist with experience in geospatial modeling, supply chain resilience, and inclusive AI.")

# -----------------------------
# Resume Download
# -----------------------------
st.subheader("Resume")
resume_path = Path(RESUME_FILENAME)
if resume_path.exists():
    st.download_button(
        label="⬇️ Download my resume (PDF)",
        data=resume_path.read_bytes(),
        file_name=RESUME_FILENAME,
        mime="application/pdf",
    )
    st.markdown(f"<span class='download-note'>Replace <code>{RESUME_FILENAME}</code> in the app folder to update.</span>", unsafe_allow_html=True)
else:
    st.info(f"Add {RESUME_FILENAME} next to app.py to enable the download button.")

# -----------------------------
# Footer
# -----------------------------
st.markdown(f"<div class='footer-text'>© {NAME} — Built with Streamlit · <a href='{LINKEDIN}'>LinkedIn</a> · <a href='{GITHUB}'>GitHub</a></div>", unsafe_allow_html=True)
