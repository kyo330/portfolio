from __future__ import annotations
import textwrap
from pathlib import Path
from typing import List, Dict
import streamlit as st

st.set_page_config(
    page_title="Priyadharshini Ramesh Kumar — Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

PRIMARY = "#463F3A"
ACCENT = "#E0AFA0"
BG_SOFT = "#F7F4F3"
BORDER = "#E7E5E4"

st.markdown(
    f"""
    <style>
  :root {{
    --primary: {PRIMARY};
    --accent: {ACCENT};
    --bg-soft: {BG_SOFT};
    --border: {BORDER};
  }}

  html, body, [class*="css"] {{
    font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, 'Helvetica Neue', Arial, 'Noto Sans', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
    color: #1b1b1b;
  }}

  .block-container {{
    max-width: 1120px;
    padding-top: 1rem !important;
  }}

  .app-title h1 {{
    margin-bottom: .2rem;
    letter-spacing: .2px;
    font-weight: 700;
  }}
  .app-subtitle {{
    color: var(--primary);
    font-weight: 600;
    margin-top: .1rem;
    margin-bottom: .8rem;
  }}

  .card-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 1.2rem;
  }}
  .card {{
    border-radius: 16px;
    padding: 1.2rem 1.1rem;
    background: #fff;
    border: 1px solid var(--border);
    box-shadow: 0 6px 18px rgba(0,0,0,.06);
    transition: transform .15s ease, box-shadow .15s ease;
  }}
  .card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(0,0,0,.08);
  }}

  .chip {{
    display: inline-block;
    padding: .22rem .6rem;
    margin: 0 .35rem .4rem 0;
    border-radius: 999px;
    background: var(--bg-soft);
    border: 1px solid var(--border);
    font-size: .82rem;
    font-weight: 500;
  }}
  .pill {{
    display: inline-block;
    background: var(--accent);
    color: #1b1b1b;
    padding: .18rem .6rem;
    border-radius: 999px;
    font-size: .75rem;
    margin-right: .35rem;
    margin-bottom: .35rem;
    opacity: .95;
    font-weight: 600;
  }}
  .soft {{
    background: var(--bg-soft);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1rem;
  }}

  .profile-img {{
    width: 128px; height: 128px; border-radius: 50%; object-fit: cover; border: 3px solid var(--accent);
  }}
  .profile-placeholder {{
    width: 128px; height: 128px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: var(--bg-soft); border: 3px dashed var(--accent); color: #555; font-weight: 600;
  }}

  .footer-text {{
    text-align: center; color: #666; font-size: .9rem; margin-top: 2rem; padding-top: .75rem; border-top: 1px solid var(--border);
  }}

  a, a:visited {{
    color: var(--primary);
    text-decoration: none;
    border-bottom: 1px solid rgba(70,63,58,.18);
    transition: border-color .15s ease;
  }}
  a:hover {{ border-bottom-color: var(--primary); }}

  .section {{ margin-top: .9rem; }}

  .stButton>button, .stDownloadButton>button {{
    border-radius: 999px;
    padding: .5rem 1rem;
    border: 1px solid var(--primary);
    background: var(--primary);
    color: #fff;
    font-weight: 600;
    transition: background .15s ease, transform .05s ease;
  }}
  .stButton>button:hover, .stDownloadButton>button:hover {{
    background: #302c29;
  }}
  .stButton>button:active, .stDownloadButton>button:active {{
    transform: translateY(1px);
  }}

  .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
    border-radius: 10px !important;
    border: 1px solid var(--border) !important;
  }}

  .st-expander {{
    border: 1px solid var(--border);
    border-radius: 12px;
    background: #fff;
  }}
</style>
    """,
    unsafe_allow_html=True,
)

NAME = "Priyadharshini Ramesh Kumar"
TITLE = "Data Scientist · Data Analyst"
LOCATION = "College Station, TX, USA"
EMAIL = "priyadharshini01.r3034@gmail.com"
PHONE = "+1-979-218-2333"
LINKEDIN = "https://linkedin.com/in/priyadharshini-r330"
GITHUB = "https://github.com/kyo330"
RESUME_FILENAME = "RameshKumar_Priyadharshini-Data_Analyst.pdf"

SKILLS_PRIMARY = [
    "Python", "R", "SQL", "Pandas", "NumPy", "scikit-learn", "TensorFlow", "Keras",
    "Matplotlib", "Seaborn", "Tableau", "GeoPandas",
]
SKILLS_CLOUD_DATA = ["AWS S3", "Lambda", "EC2", "RDS", "Spark", "Hadoop", "PostgreSQL", "MySQL"]
STRENGTHS = ["Cross-functional teamwork", "Problem solving", "Leadership mindset", "Adaptability"]

PROJECTS: List[Dict] = [
    {
        "title": "4D Thunderstorm Visualizations",
        "period": "Aug 2024 – Dec 2024",
        "summary": "Real-time geospatial + temporal dashboard (Python, GeoPandas, Leaflet) to support emergency response; classified lightning strikes into risk zones.",
        "highlights": [
            "Built a 4D storm evolution view",
            "Rule-based geospatial risk classification",
        ],
        "tags": ["Geospatial", "Visualization", "Python", "Leaflet"],
        "links": {"Demo": "", "Code": ""},
    },
    {
        "title": "Semiconductor Supply Chain Risk Model",
        "period": "Feb 2024 – Apr 2024",
        "summary": "Three-node scenario model for disruptions; improved predictive accuracy and supported strategic decisions (SGL @ Texas A&M).",
        "highlights": [
            "Curve fitting for scenario evaluation",
            "Data exploration & preprocessing",
        ],
        "tags": ["Modeling", "Analytics", "Supply Chain"],
        "links": {"Slides": "", "Report": ""},
    },
    {
        "title": "Indian Sign Language Recognition",
        "period": "Jan 2022 – Nov 2022",
        "summary": "Deep learning pipeline on 10k+ labeled images; ~92% accuracy with Keras and systematic error analysis.",
        "highlights": [
            "Annotation pipeline of 10,000+ images",
            "+12% accuracy via hyperparameter tuning",
        ],
        "tags": ["Computer Vision", "Deep Learning", "Keras"],
        "links": {"Paper": "", "Code": ""},
    },
    {
        "title": "Air Pollutant Correlation & Prediction",
        "period": "Aug 2023 – Dec 2023",
        "summary": "Feature engineering + ML models (R²≈0.87) to predict air quality and inform environmental policy analysis.",
        "highlights": [
            "Correlation analysis & feature selection",
            "Scikit-learn regression models",
        ],
        "tags": ["Machine Learning", "Analytics"],
        "links": {"Notebook": ""},
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
            "Engineered a high‑performance pipeline to optimize rendering & query efficiency.",
        ],
    },
    {
        "role": "Research Assistant",
        "org": "Stochastic Geomechanics Laboratory (SGL), Texas A&M University",
        "loc": "Texas, USA",
        "period": "Feb 2024 – Apr 2024",
        "bullets": [
            "Improved dataset quality for more accurate supply‑chain risk assessments.",
            "Refined a three‑node model for semiconductor disruptions.",
            "Applied curve fitting to evaluate logistics scenarios.",
        ],
    },
    {
        "role": "Research Assistant (CHANAKYA Fellow)",
        "org": "TIH‑IoT, IIT Bombay",
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

def read_bytes_safe(path: Path) -> bytes | None:
    try:
        return path.read_bytes()
    except Exception:
        return None

with st.sidebar:
    st.header("Navigate")
    page = st.radio("", ["About", "Projects", "Experience", "Education", "Skills", "Contact / Resume"], index=0)
    st.divider()
    st.header("Project Filter")
    all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    selected_tags = st.multiselect("Tags", options=all_tags, placeholder="Filter by tag…")

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
    st.write(
        f"📧 [{EMAIL}](mailto:{EMAIL})  ·  📞 {PHONE}  ·  🔗 [LinkedIn]({LINKEDIN})  ·  💻 [GitHub]({GITHUB})"
    )
    st.divider()

if page == "About":
    st.subheader("About")
    st.write(
        """
        Graduate **Data Scientist** with a strong foundation in analytics, geospatial modeling, and machine learning.
        I turn complex datasets into clear, actionable insights—from atmospheric risk mapping to supply-chain resilience and inclusive AI.
        Currently focused on robust data pipelines and decision-support visualizations that deliver measurable impact.
        """
    )
    st.markdown("#### Highlights")
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='soft'><b>⚡ Storm Risk Dashboard</b><br>Real‑time geospatial dashboard for 4D storm evolution & risk zones.</div>", unsafe_allow_html=True)
    c2.markdown("<div class='soft'><b>📦 Supply Chain Modeling</b><br>Refined predictive models for semiconductor disruptions.</div>", unsafe_allow_html=True)
    c3.markdown("<div class='soft'><b>🤟 Inclusive AI</b><br>ISL image classification pipeline (~92% accuracy).</div>", unsafe_allow_html=True)

elif page == "Projects":
    st.subheader("Projects")
    filtered = [p for p in PROJECTS if not selected_tags or all(t in p["tags"] for t in selected_tags)]
    st.markdown("<div class='card-grid'>", unsafe_allow_html=True)
    for p in filtered:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {p['title']}")
        st.caption(p["period"])
        st.write(p["summary"])
        if p.get("highlights"):
            st.markdown("**Highlights**")
            for h in p["highlights"]:
                st.write("• ", h)
        if p.get("tags"):
            st.markdown("".join([f"<span class='pill'>{t}</span>" for t in p["tags"]]), unsafe_allow_html=True)
        if p.get("links") and any(p["links"].values()):
            st.write(" ".join([f"[{k}]({v})" for k, v in p["links"].items() if v]))
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Experience":
    st.subheader("Experience")
    for exp in EXPERIENCE:
        with st.expander(f"{exp['role']} — {exp['org']}  ·  {exp['period']}"):
            st.caption(exp["loc"])
            for b in exp["bullets"]:
                st.write("• ", b)

elif page == "Education":
    st.subheader("Education")
    for edu in EDUCATION:
        with st.expander(f"{edu['school']} — {edu['degree']}  ·  {edu['period']}"):
            for b in edu["bullets"]:
                st.write("• ", b)

elif page == "Skills":
    st.subheader("Skills")
    st.markdown("**Core**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in SKILLS_PRIMARY]), unsafe_allow_html=True)
    st.markdown("**Cloud / Data**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in SKILLS_CLOUD_DATA]), unsafe_allow_html=True)
    st.markdown("**Strengths**")
    st.markdown("".join([f"<span class='chip'>{s}</span>" for s in STRENGTHS]), unsafe_allow_html=True)

elif page == "Contact / Resume":
    st.subheader("Contact")
    with st.form("contact_form"):
        c_name = st.text_input("Your name")
        c_email = st.text_input("Your email")
        c_msg = st.text_area("Message")
        submitted = st.form_submit_button("Compose Email")
        if submitted:
            subject = f"Portfolio inquiry from {c_name or 'someone'}"
            body = textwrap.shorten(c_msg or "(no message)", width=1500)
            mailto = f"mailto:{EMAIL}?subject={subject}&body={body}"
            st.success("Click the link below to send via your email client:")
            st.write(f"👉 [Compose email]({mailto})")
    st.markdown("\n")
    st.subheader("Resume")
    resume_path = Path(RESUME_FILENAME)
    data = read_bytes_safe(resume_path)
    if data is not None:
        st.download_button(
            label="⬇️ Download my resume (PDF)",
            data=data,
            file_name=RESUME_FILENAME,
            mime="application/pdf",
        )
        st.markdown(
            f"<span class='download-note'>Replace <code>{RESUME_FILENAME}</code> next to <code>app.py</code> to update.</span>",
            unsafe_allow_html=True,
        )
    else:
        st.info(f"Add {RESUME_FILENAME} next to app.py to enable the download button.")

st.markdown(
    f"<div class='footer-text'>© {NAME} — Built with Streamlit · <a href='{LINKEDIN}'>LinkedIn</a> · <a href='{GITHUB}'>GitHub</a></div>",
    unsafe_allow_html=True,
)
