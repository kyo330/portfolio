# app.py — Priyadharshini Ramesh Kumar | Streamlit Portfolio
# ---------------------------------------------------------
# How to run locally:
#   1) pip install -r requirements.txt  (or at minimum: pip install streamlit pillow)
#   2) streamlit run app.py
#
# Deploy (free) on Streamlit Community Cloud:
#   - Push this file (and your resume PDF) to a public GitHub repo
#   - In https://share.streamlit.io, pick the repo/branch, set Main file path to app.py
#
# Optional files to add next to app.py for best results:
#   - RameshKumar_Priyadharshini-Analyst.pdf  (or your preferred resume filename)
#   - /assets/profile.jpg  (a headshot)
#   - /assets/project_*.png (thumbnails)
#
# Tip: Update the PROJECTS list below with real links (GitHub, demo, paper) as you publish them.

from __future__ import annotations
import os
import textwrap
from pathlib import Path
from typing import List, Dict

import streamlit as st
from PIL import Image

# -----------------------------
# Page & Global Config
# -----------------------------
st.set_page_config(
    page_title="Priyadharshini Ramesh Kumar — Portfolio",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# THEME TWEAKS (CSS)
# -----------------------------
PRIMARY = "#463F3A"        # from your palette
ACCENT = "#E0AFA0"
BG_SOFT = "#F7F4F3"

st.markdown(
    f"""
    <style>
      .app-title h1 {{
        margin-bottom: 0.25rem;
      }}
      .app-subtitle {{
        color: {PRIMARY};
        font-weight: 600;
        margin-top: 0.1rem;
        margin-bottom: 0.5rem;
      }}
      .chip {{
        display: inline-block; padding: 0.2rem 0.55rem; margin: 0 0.25rem 0.25rem 0;
        border-radius: 999px; background: {BG_SOFT}; border: 1px solid #e8e8e8; font-size: 0.82rem;
      }}
      .card-grid {{
        display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1rem; width: 100%;
      }}
      .card {{
        border-radius: 16px; padding: 1rem; background: white; border: 1px solid #eee;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
      }}
      .card h4 {{ margin: 0 0 0.4rem 0; }}
      .pill {{
        display:inline-block; background:{ACCENT}; color:#1b1b1b; padding:0.15rem 0.5rem; border-radius:999px; font-size:0.75rem;
        margin-right:0.35rem; margin-bottom:0.35rem; opacity:0.9;
      }}
      .soft {{ background:{BG_SOFT}; border: 1px solid #ececec; border-radius: 16px; padding: 1rem; }}
      .footer {text-align:center; color:#666; font-size:0.85rem; margin-top: 2rem;}
      .profile-img {{ width: 128px; height: 128px; border-radius: 50%; object-fit: cover; border: 3px solid {ACCENT}; }}
      .profile-placeholder {{ width:128px; height:128px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:{BG_SOFT}; border:3px dashed {ACCENT}; color:#555; font-weight:600; }}
      .download-note {{ font-size:0.9rem; color:#666; }}
      .section-title {{ margin-top: 0.25rem; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# CONTENT DATA (edit me!)
# -----------------------------
NAME = "Priyadharshini Ramesh Kumar"
TITLE = "Data Scientist / Data Analyst"
LOCATION = "College Station, TX, USA"
EMAIL = "priyadharshini01.r3034@gmail.com"
PHONE = "+1-979-218-2333"
LINKEDIN = "https://linkedin.com/in/priyadharshini-r330"
GITHUB = "https://github.com/kyo330"
RESUME_FILENAME = "RameshKumar_Priyadharshini-Analyst.pdf"  # place next to app.py

SKILLS_PRIMARY = [
    "Python", "R", "SQL", "Pandas", "NumPy", "scikit-learn", "TensorFlow", "Keras",
    "Matplotlib", "Seaborn", "Tableau", "GeoPandas",
]
SKILLS_CLOUD = ["AWS S3", "Lambda", "EC2", "RDS", "Spark", "Hadoop", "PostgreSQL", "MySQL"]
SKILLS_SOFT = ["Cross-functional teamwork", "Problem solving", "Leadership mindset", "Adaptability"]

PROJECTS: List[Dict] = [
    {
        "title": "4D Thunderstorm Visualizations",
        "period": "Aug 2024 – Dec 2024",
        "summary": "Interactive geospatial + temporal visualizations (Python, GeoPandas, Leaflet) to support emergency response; classified lightning strikes into risk zones.",
        "highlights": [
            "Built real-time dashboard for storm evolution",
            "Rule-based geospatial risk classification",
        ],
        "tags": ["Geospatial", "Visualization", "Python", "Leaflet"],
        "links": {
            "Code": "",
            "Demo": "",
        },
        "thumb": "assets/project_thunder.png",
    },
    {
        "title": "Semiconductor Supply Chain Risk Model",
        "period": "Feb 2024 – Apr 2024",
        "summary": "Three-node scenario model for disruptions; improved predictive accuracy and supported strategic decisions (SGL @ Texas A&M).",
        "highlights": [
            "Curve fitting for scenario evaluation",
            "Data exploration & preprocessing for quality",
        ],
        "tags": ["Modeling", "Analytics", "Supply Chain"],
        "links": {
            "Report": "",
            "Slides": "",
        },
        "thumb": "assets/project_sgl.png",
    },
    {
        "title": "Indian Sign Language Recognition",
        "period": "Jan 2022 – Nov 2022",
        "summary": "Deep learning pipeline on 10k+ labeled images; achieved ~92% accuracy with Keras and systematic error analysis.",
        "highlights": [
            "Data annotation pipeline (10,000+ images)",
            "+12% accuracy via hyperparameter tuning",
        ],
        "tags": ["Computer Vision", "Deep Learning", "Keras"],
        "links": {
            "Paper": "",
            "Code": "",
        },
        "thumb": "assets/project_isl.png",
    },
    {
        "title": "Air Pollutant Correlation & Prediction",
        "period": "Aug 2023 – Dec 2023",
        "summary": "Feature engineering + ML models (R²≈0.87) to predict air quality metrics and inform environmental policy analysis.",
        "highlights": [
            "Correlation analysis & feature selection",
            "Scikit-learn regression models",
        ],
        "tags": ["Machine Learning", "Analytics"],
        "links": {
            "Notebook": "",
        },
        "thumb": "assets/project_air.png",
    },
]

EXPERIENCE = [
    {
        "role": "Research Assistant",
        "org": "Department of Atmospheric Sciences, Texas A&M University",
        "loc": "Texas, USA",
        "period": "Aug 2024 – Present",
        "bullets": [
            "Analyzed lightning + precipitation data to enhance storm pattern detection and risk-zone mapping.",
            "Built real-time dashboard (Python, GeoPandas, Leaflet) for 4D storm evolution.",
            "Engineered a high-performance pipeline to optimize rendering & query efficiency.",
        ],
    },
    {
        "role": "Research Assistant",
        "org": "Stochastic Geomechanics Laboratory (SGL), Texas A&M University",
        "loc": "Texas, USA",
        "period": "Feb 2024 – Apr 2024",
        "bullets": [
            "Improved dataset quality for more accurate supply chain risk assessments.",
            "Refined a three-node model for semiconductor supply chain disruptions.",
            "Applied curve fitting to evaluate logistics scenarios.",
        ],
    },
    {
        "role": "Research Assistant (CHANAKYA Fellow)",
        "org": "TIH-IoT, IIT Bombay",
        "loc": "India",
        "period": "Jan 2022 – Nov 2022",
        "bullets": [
            "Developed Keras CNN for Indian Sign Language images (≈92% accuracy).",
            "Led data annotation of 10k+ images; mentored student contributors.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Texas A&M University",
        "degree": "M.S., Data Science (GPA: 3.91/4.0)",
        "period": "Aug 2023 – Dec 2024",
        "bullets": [
            "Data Mining & Analysis, Statistical Computing (R & Python), AI, Math Foundations for DS",
        ],
    },
    {
        "school": "Anna University",
        "degree": "B.E., Computer Science & Engineering (GPA: 8.78/10)",
        "period": "Aug 2019 – Jun 2023",
        "bullets": [
            "Machine Learning, Big Data Analysis, Probability & Statistics, NLP",
        ],
    },
]

# -----------------------------
# Utilities
# -----------------------------

def load_image(path: str) -> Image.Image | None:
    try:
        return Image.open(path)
    except Exception:
        return None


def file_bytes(path: str) -> bytes | None:
    try:
        return Path(path).read_bytes()
    except Exception:
        return None


# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 5], vertical_alignment="center")
with col1:
    img = load_image("assets/profile.jpg")
    if img:
        st.image(img, use_column_width=False, output_format="PNG", caption="")
    else:
        st.markdown('<div class="profile-placeholder">Add profile.jpg</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='app-title'><h1>{NAME}</h1></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='app-subtitle'>{TITLE} · {LOCATION}</div>", unsafe_allow_html=True)
    st.write(
        f"📧 [{EMAIL}](mailto:{EMAIL})  ·  📞 {PHONE}  ·  🔗 [LinkedIn]({LINKEDIN})  ·  💻 [GitHub]({GITHUB})"
    )
    st.divider()

# -----------------------------
# Sidebar Navigation & Filters
# -----------------------------
with st.sidebar:
    st.header("Navigate")
    nav = st.radio("", ["About", "Projects", "Experience", "Education", "Skills", "Contact / Resume"], index=0)
    st.write("")
    st.header("Project Filter")
    all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    selected_tags = st.multiselect("Tags", options=all_tags, default=[])

# -----------------------------
# Sections
# -----------------------------
if nav == "About":
    st.subheader("About")
    st.markdown(
        """
        I’m a graduate **Data Scientist** with a strong foundation in analytics, geospatial modeling,
        and machine learning. I enjoy turning complex, messy datasets into clear, actionable insights
        — from atmospheric risk mapping to supply chain resilience and inclusive AI.
        """
    )
    st.markdown(
        """
        **What I’m focused on right now:** building robust data pipelines, shipping helpful visualizations,
        and collaborating across disciplines to deliver results that matter.
        """
    )
    st.markdown("\n")
    st.markdown("#### Quick Highlights")
    hl_cols = st.columns(3)
    hl_cards = [
        ("⚡ Storm Risk Dashboard", "Built a real-time geospatial dashboard for 4D storm evolution & risk zones"),
        ("📦 Supply Chain Modeling", "Refined predictive models for semiconductor disruptions"),
        ("🤟 Inclusive AI", "ISL image classification pipeline (~92% accuracy)")
    ]
    for i, (title, desc) in enumerate(hl_cards):
        with hl_cols[i % 3]:
            st.markdown(f"<div class='soft'><b>{title}</b><br><span>{desc}</span></div>", unsafe_allow_html=True)

elif nav == "Projects":
    st.subheader("Projects")
    filtered = [p for p in PROJECTS if all(t in p["tags"] for t in selected_tags)] if selected_tags else PROJECTS
    st.markdown("<div class='card-grid'>", unsafe_allow_html=True)
    for p in filtered:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<h4>{p['title']}</h4>")
        st.caption(p["period"])    
        if p.get("thumb") and Path(p["thumb"]).exists():
            st.image(p["thumb"], use_column_width=True)
        st.write(p["summary"]) 
        if p.get("highlights"):
            st.markdown("**Highlights**")
            for h in p["highlights"]:
                st.write("• ", h)
        if p.get("tags"):
            st.markdown("".join([f"<span class='pill'>{t}</span>" for t in p["tags"]]), unsafe_allow_html=True)
        # Links
        if p.get("links"):
            link_strs = []
            for k, v in p["links"].items():
                if v:
                    link_strs.append(f"[{k}]({v})")
            if link_strs:
                st.write(" ".join(link_strs))
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif nav == "Experience":
    st.subheader("Experience")
    for exp in EXPERIENCE:
        with st.expander(f"{exp['role']} — {exp['org']}  ·  {exp['period']}"):
            st.caption(exp["loc"])
            for b in exp["bullets"]:
                st.write("• ", b)

elif nav == "Education":
    st.subheader("Education")
    for edu in EDUCATION:
        with st.expander(f"{edu['school']} — {edu['degree']}  ·  {edu['period']}"):
            for b in edu["bullets"]:
                st.write("• ", b)

elif nav == "Skills":
    st.subheader("Skills")
    st.markdown("**Core**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in SKILLS_PRIMARY]), unsafe_allow_html=True)
    st.markdown("**Cloud / Data**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in SKILLS_CLOUD]), unsafe_allow_html=True)
    st.markdown("**Strengths**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in SKILLS_SOFT]), unsafe_allow_html=True)

elif nav == "Contact / Resume":
    st.subheader("Contact")
    with st.form("contact_form"):
        c_name = st.text_input("Your name")
        c_email = st.text_input("Your email")
        c_msg = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            subject = f"Portfolio inquiry from {c_name or 'someone'}"
            body = textwrap.shorten(c_msg or "(no message)", width=1500)
            mailto = f"mailto:{EMAIL}?subject={subject}&body={body}"
            st.success("Click the link below to send via your email client:")
            st.write(f"👉 [Compose email]({mailto})")

    st.markdown("\n")
    st.subheader("Resume")
    resume_bytes = file_bytes(RESUME_FILENAME)
    if resume_bytes:
        st.download_button(
            label="⬇️ Download my resume (PDF)",
            data=resume_bytes,
            file_name=RESUME_FILENAME,
            mime="application/pdf",
        )
        st.markdown(f"<span class='download-note'>Make sure this is your latest resume. Replace <code>{RESUME_FILENAME}</code> in the app folder to update.</span>", unsafe_allow_html=True)
    else:
        st.info(
            f"Add your resume PDF next to app.py as '{RESUME_FILENAME}' to enable the download button."
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    f"<div class='footer'>© {NAME} — Built with Streamlit · <a href='{LINKEDIN}'>LinkedIn</a> · <a href='{GITHUB}'>GitHub</a></div>",
    unsafe_allow_html=True,
)
