"""
==============================================================
  AI-Based Smart Career Counseling Expert System
  Streamlit GUI — KRR Project
==============================================================
  Run: streamlit run app.py
==============================================================
"""

import streamlit as st
from knowledge_base import (
    KNOWLEDGE_BASE, ALL_SKILLS, ALL_INTERESTS,
    ALL_PERSONALITIES, DOMAINS,
)
from inference_engine import run_inference_engine, get_domain_filtered

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Career Counseling System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
}

/* ── Dark background ── */
.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1321 50%, #0a1628 100%);
    color: #e8eaf0;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #1a1f3a 0%, #0f1729 100%);
    border: 1px solid rgba(108, 99, 255, 0.3);
    border-radius: 20px;
    padding: 40px 50px;
    margin-bottom: 30px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 50% 50%, rgba(108,99,255,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6C63FF, #00B4D8, #6C63FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    color: #8892a4;
    font-size: 1.05rem;
    font-weight: 300;
    letter-spacing: 0.5px;
}
.hero-badge {
    display: inline-block;
    background: rgba(108,99,255,0.15);
    border: 1px solid rgba(108,99,255,0.4);
    color: #a89cff;
    padding: 4px 16px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 16px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ── Section Headers ── */
.section-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: #6C63FF;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin: 24px 0 12px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(108,99,255,0.4), transparent);
    margin-left: 10px;
}

/* ── Career Result Cards ── */
.career-card {
    background: linear-gradient(135deg, #141929, #0f1522);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 22px 26px;
    margin-bottom: 16px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.career-card:hover {
    border-color: rgba(108,99,255,0.4);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(108,99,255,0.15);
}
.career-card-top {
    background: linear-gradient(135deg, #1e2547, #141d3a);
    border: 1px solid rgba(108,99,255,0.35);
    box-shadow: 0 4px 20px rgba(108,99,255,0.2);
}
.career-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: #f0f2ff;
}
.career-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #6C63FF, #00B4D8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.career-domain {
    display: inline-block;
    background: rgba(0,180,216,0.12);
    border: 1px solid rgba(0,180,216,0.3);
    color: #00B4D8;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 2px 3px;
}

/* ── Progress Bar ── */
.progress-container {
    background: rgba(255,255,255,0.06);
    border-radius: 8px;
    height: 10px;
    margin: 10px 0;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 8px;
    transition: width 0.6s ease;
}

/* ── Skill Tags ── */
.skill-tag-green {
    display: inline-block;
    background: rgba(46,196,182,0.12);
    border: 1px solid rgba(46,196,182,0.4);
    color: #2EC4B6;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 3px 3px;
}
.skill-tag-red {
    display: inline-block;
    background: rgba(230,57,70,0.12);
    border: 1px solid rgba(230,57,70,0.4);
    color: #E63946;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 3px 3px;
}
.skill-tag-purple {
    display: inline-block;
    background: rgba(108,99,255,0.12);
    border: 1px solid rgba(108,99,255,0.4);
    color: #a89cff;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 3px 3px;
}

/* ── Info Boxes ── */
.info-box {
    background: rgba(108,99,255,0.08);
    border-left: 3px solid #6C63FF;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 12px 0;
    color: #c4c8e0;
    font-size: 0.92rem;
}
.warning-box {
    background: rgba(244,162,97,0.08);
    border-left: 3px solid #F4A261;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 12px 0;
    color: #f0c08a;
    font-size: 0.92rem;
}
.success-box {
    background: rgba(46,196,182,0.08);
    border-left: 3px solid #2EC4B6;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 12px 0;
    color: #7de8df;
    font-size: 0.92rem;
}

/* ── Roadmap Steps ── */
.roadmap-step {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin: 10px 0;
}
.roadmap-num {
    background: linear-gradient(135deg, #6C63FF, #00B4D8);
    color: white;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    min-width: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
    font-weight: 700;
}
.roadmap-text {
    color: #c4c8e0;
    padding-top: 4px;
    font-size: 0.92rem;
}

/* ── Stat Card ── */
.stat-card {
    background: linear-gradient(135deg, #141929, #0f1522);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}
.stat-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: #6C63FF;
}
.stat-label {
    color: #8892a4;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* ── Sidebar Styling ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1321 0%, #0a0e1a 100%);
    border-right: 1px solid rgba(108,99,255,0.2);
}

/* ── Streamlit widget overrides ── */
.stMultiSelect [data-baseweb="tag"] {
    background: rgba(108,99,255,0.25) !important;
    border: 1px solid rgba(108,99,255,0.5) !important;
    color: #c4c8e0 !important;
}
.stSlider .st-bd { background: rgba(108,99,255,0.3) !important; }
div[data-testid="stMetricValue"] {
    color: #6C63FF !important;
    font-family: 'JetBrains Mono', monospace !important;
}
.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-family: 'Sora', sans-serif !important;
    padding: 12px 30px !important;
    font-size: 1rem !important;
    letter-spacing: 0.5px !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #7c75ff, #6C63FF) !important;
    box-shadow: 0 4px 20px rgba(108,99,255,0.4) !important;
    transform: translateY(-1px) !important;
}
.stTextInput input, .stNumberInput input {
    background: rgba(20,25,41,0.8) !important;
    border: 1px solid rgba(108,99,255,0.25) !important;
    color: #e8eaf0 !important;
    border-radius: 8px !important;
}
.stSelectbox select, div[data-baseweb="select"] {
    background: rgba(20,25,41,0.8) !important;
    color: #e8eaf0 !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(20,25,41,0.5);
    border-radius: 10px;
    padding: 4px;
    border: 1px solid rgba(108,99,255,0.2);
}
.stTabs [data-baseweb="tab"] {
    color: #8892a4 !important;
    font-weight: 600 !important;
    font-family: 'Sora', sans-serif !important;
    border-radius: 8px !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(108,99,255,0.25) !important;
    color: #a89cff !important;
}

/* ── Divider ── */
hr { border-color: rgba(108,99,255,0.15) !important; }

/* ── Expander ── */
details {
    background: rgba(20,25,41,0.5) !important;
    border: 1px solid rgba(108,99,255,0.2) !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# HERO BANNER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-badge">KRR Project — Expert System</div>
    <div class="hero-title">🎓 Smart Career Counseling System</div>
    <div class="hero-subtitle">
        AI-Based Expert System using Knowledge Representation &amp; Reasoning (KRR)<br>
        <span style="color:#6C63FF;font-weight:600;">Forward Chaining Inference Engine</span> &nbsp;•&nbsp; 
        10 Career Domains &nbsp;•&nbsp; Skill Gap Analysis &nbsp;•&nbsp; Roadmap Generator
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SIDEBAR — STUDENT INPUT FORM
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:10px 0 20px 0;'>
        <span style='font-size:2rem;'>👨‍🎓</span>
        <div style='font-size:1.1rem;font-weight:700;color:#a89cff;margin-top:6px;'>Student Profile</div>
        <div style='font-size:0.78rem;color:#8892a4;'>Fill in your details</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Personal Info ──
    st.markdown('<div class="section-header">📋 Personal Info</div>', unsafe_allow_html=True)
    student_name = st.text_input("Full Name", placeholder="e.g. Ahmad Ali", value="")
    
    degree_options = [
        "Computer Science", "Software Engineering", "Information Technology",
        "Electrical Engineering", "Business Administration",
        "Graphic Design / Fine Arts", "Other",
    ]
    degree = st.selectbox("Degree Program", degree_options)

    cgpa = st.slider(
        "CGPA", min_value=0.0, max_value=4.0, value=3.0, step=0.1,
        help="Your current Cumulative Grade Point Average",
    )

    # CGPA color indicator
    if cgpa >= 3.5:
        cgpa_color, cgpa_label = "#2EC4B6", "Excellent 🌟"
    elif cgpa >= 3.0:
        cgpa_color, cgpa_label = "#6C63FF", "Very Good ✨"
    elif cgpa >= 2.5:
        cgpa_color, cgpa_label = "#F4A261", "Good 👍"
    else:
        cgpa_color, cgpa_label = "#E63946", "Needs Improvement ⚠️"

    st.markdown(f"""
    <div style='background:rgba(20,25,41,0.6);border-radius:8px;padding:8px 14px;
                border-left:3px solid {cgpa_color};margin:-8px 0 12px 0;font-size:0.85rem;
                color:{cgpa_color};font-weight:600;'>
        CGPA: {cgpa:.1f} / 4.0 — {cgpa_label}
    </div>""", unsafe_allow_html=True)

    # ── Skills ──
    st.markdown('<div class="section-header">🛠️ Your Skills</div>', unsafe_allow_html=True)
    selected_skills = st.multiselect(
        "Select all skills you have",
        options=ALL_SKILLS,
        default=[],
        help="Choose every skill you are comfortable with",
    )

    # ── Interests ──
    st.markdown('<div class="section-header">💡 Your Interests</div>', unsafe_allow_html=True)
    selected_interests = st.multiselect(
        "Select your interest areas",
        options=ALL_INTERESTS,
        default=[],
        help="Choose areas you are genuinely passionate about",
    )

    # ── Personality ──
    st.markdown('<div class="section-header">🧠 Personality Traits</div>', unsafe_allow_html=True)
    selected_personality = st.multiselect(
        "Select your traits",
        options=ALL_PERSONALITIES,
        default=[],
        help="Pick traits that describe you best",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("🔍 Analyze My Profile", use_container_width=True)

    st.markdown("""
    <div style='text-align:center;margin-top:20px;padding:12px;
                background:rgba(108,99,255,0.06);border-radius:10px;
                border:1px solid rgba(108,99,255,0.15);'>
        <div style='font-size:0.72rem;color:#8892a4;line-height:1.6;'>
            <strong style='color:#a89cff;'>KRR Technique Used:</strong><br>
            Forward Chaining<br>
            Rule-Based Inference Engine<br>
            Weighted Scoring System
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────────────────────

if not analyze_btn and "results" not in st.session_state:
    # ── Welcome screen ──
    st.markdown('<div class="section-header">📚 How It Works</div>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    steps = [
        ("1️⃣", "Fill Profile", "Enter your CGPA, skills, interests & personality in the sidebar"),
        ("2️⃣", "Click Analyze", "Press the 'Analyze My Profile' button to start"),
        ("3️⃣", "View Results", "See top career recommendations with match percentages"),
        ("4️⃣", "Explore", "Check roadmap, skill gaps, and certifications"),
    ]
    for col, (icon, title, desc) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div class="career-card" style="text-align:center;padding:24px 16px;">
                <div style="font-size:2rem;margin-bottom:10px;">{icon}</div>
                <div style="font-weight:700;color:#f0f2ff;margin-bottom:6px;">{title}</div>
                <div style="font-size:0.82rem;color:#8892a4;line-height:1.5;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-header">🎯 Careers Covered</div>', unsafe_allow_html=True)
    career_cols = st.columns(5)
    all_careers = list(KNOWLEDGE_BASE.items())
    for i, (name, data) in enumerate(all_careers):
        with career_cols[i % 5]:
            st.markdown(f"""
            <div class="career-card" style="text-align:center;padding:16px 12px;">
                <div style="font-size:1.6rem;">{data['icon']}</div>
                <div style="font-size:0.82rem;font-weight:600;color:#c4c8e0;margin-top:6px;">{name}</div>
                <div style="font-size:0.72rem;color:#8892a4;margin-top:4px;">{', '.join(data['domains'])}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="margin-top:20px;">
        <strong>💡 KRR Concept:</strong> This system uses <strong>Forward Chaining Inference Engine</strong> — 
        it starts from known facts (your profile) and applies IF-THEN rules from the Knowledge Base 
        to derive career recommendations. Each career has weighted rules for skills (15pts), 
        interests (12pts), CGPA (10pts), and personality bonuses (5pts).
    </div>
    """, unsafe_allow_html=True)

else:
    # ── Run or reload analysis ──
    if analyze_btn:
        if not selected_skills:
            st.error("⚠️ Please select at least one skill from the sidebar!")
            st.stop()
        if not selected_interests:
            st.error("⚠️ Please select at least one interest from the sidebar!")
            st.stop()

        user_facts = {
            "name":        student_name.strip() if student_name.strip() else "Student",
            "cgpa":        cgpa,
            "degree":      degree,
            "skills":      selected_skills,
            "interests":   selected_interests,
            "personality": selected_personality,
        }
        results = run_inference_engine(user_facts)
        st.session_state["results"]    = results
        st.session_state["user_facts"] = user_facts

    results    = st.session_state["results"]
    user_facts = st.session_state["user_facts"]
    name       = user_facts["name"]
    top5       = results[:5]
    best       = results[0]

    # ── Profile Summary Strip ──
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#1a1f3a,#141d2f);border:1px solid rgba(108,99,255,0.3);
                border-radius:14px;padding:18px 24px;margin-bottom:24px;display:flex;
                flex-wrap:wrap;gap:12px;align-items:center;'>
        <div style='font-size:1.6rem;'>👤</div>
        <div>
            <div style='font-size:1.1rem;font-weight:700;color:#f0f2ff;'>{name}</div>
            <div style='font-size:0.82rem;color:#8892a4;'>{user_facts["degree"]} &nbsp;•&nbsp; CGPA {user_facts["cgpa"]:.1f}</div>
        </div>
        <div style='margin-left:auto;display:flex;flex-wrap:wrap;gap:6px;'>
            {"".join(f'<span class="skill-tag-purple">{s}</span>' for s in user_facts["skills"])}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats Row ──
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{best['percentage']}%</div>
            <div class="stat-label">Best Match</div></div>""", unsafe_allow_html=True)
    with s2:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{len([r for r in results if r['percentage']>=50])}</div>
            <div class="stat-label">Good Fits (&ge;50%)</div></div>""", unsafe_allow_html=True)
    with s3:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{len(user_facts['skills'])}</div>
            <div class="stat-label">Skills Entered</div></div>""", unsafe_allow_html=True)
    with s4:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{len(user_facts['interests'])}</div>
            <div class="stat-label">Interests Entered</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tabs ──
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏆 Top Careers",
        "📋 Detailed Report",
        "🗺️ Roadmap",
        "🔍 Skill Gap",
        "📊 All Results",
    ])

    # ═══════════════════════════════════════════════════
    # TAB 1 — TOP CAREERS
    # ═══════════════════════════════════════════════════
    with tab1:
        st.markdown('<div class="section-header">🏆 Top Career Recommendations</div>', unsafe_allow_html=True)
        
        for rank, res in enumerate(top5, 1):
            career    = res["career"]
            pct       = res["percentage"]
            rules     = res["rules"]
            medal     = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"][rank - 1]
            extra_cls = "career-card-top" if rank == 1 else ""

            # Color for progress bar
            if pct >= 80:
                bar_color = "linear-gradient(90deg,#6C63FF,#00B4D8)"
            elif pct >= 60:
                bar_color = "linear-gradient(90deg,#2EC4B6,#6C63FF)"
            elif pct >= 40:
                bar_color = "linear-gradient(90deg,#F4A261,#E63946)"
            else:
                bar_color = "linear-gradient(90deg,#E63946,#c1121f)"

            domains_html = "".join(f'<span class="career-domain">{d}</span>' for d in rules["domains"])

            st.markdown(f"""
            <div class="career-card {extra_cls}">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;">
                    <div>
                        <div class="career-name">{medal} {rules['icon']} {career}</div>
                        <div style="margin-top:6px;">{domains_html}</div>
                        <div style="margin-top:8px;font-size:0.85rem;color:#8892a4;">{rules['description']}</div>
                    </div>
                    <div style="text-align:right;">
                        <div class="career-pct">{pct}%</div>
                        <div style="font-size:0.75rem;color:#8892a4;">match score</div>
                    </div>
                </div>
                <div class="progress-container">
                    <div class="progress-fill" style="width:{pct}%;background:{bar_color};"></div>
                </div>
                <div style="display:flex;justify-content:space-between;font-size:0.82rem;color:#8892a4;margin-top:6px;">
                    <span>💰 {rules['salary_pkr']}</span>
                    <span>🌍 {rules['salary_usd']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Reasoning for top career ──
        st.markdown('<div class="section-header">🧠 AI Reasoning (Why This Career?)</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
            <strong>System selected <em>{best['career']}</em> for {name} because:</strong><br><br>
            {"<br>".join(f"✔ {r}" for r in best['reasons'])}
        </div>
        """, unsafe_allow_html=True)

        if best["missing"]:
            st.markdown(f"""
            <div class="warning-box">
                <strong>⚠️ To strengthen this match, {name} should also develop:</strong><br><br>
                {"<br>".join(f"• {m}" for m in best['missing'][:5])}
            </div>
            """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════
    # TAB 2 — DETAILED REPORT
    # ═══════════════════════════════════════════════════
    with tab2:
        # Select which career to detail
        career_names = [r["career"] for r in results]
        chosen = st.selectbox(
            "Select Career to View Full Report",
            options=career_names,
            index=0,
        )
        chosen_res   = next(r for r in results if r["career"] == chosen)
        chosen_rules = chosen_res["rules"]

        st.markdown(f"""
        <div class="career-card career-card-top" style="margin-top:16px;">
            <div style="font-size:3rem;text-align:center;">{chosen_rules['icon']}</div>
            <div class="career-name" style="text-align:center;font-size:1.5rem;margin:10px 0 6px;">{chosen}</div>
            <div style="text-align:center;margin-bottom:12px;">
                {"".join(f'<span class="career-domain">{d}</span>' for d in chosen_rules['domains'])}
            </div>
            <div style="text-align:center;font-size:0.9rem;color:#8892a4;">{chosen_rules['description']}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-header">💰 Salary</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="success-box">
                🇵🇰 <strong>Pakistan:</strong> {chosen_rules['salary_pkr']}<br>
                🌍 <strong>Remote/Global:</strong> {chosen_rules['salary_usd']}
            </div>""", unsafe_allow_html=True)

            st.markdown('<div class="section-header">👔 Job Roles</div>', unsafe_allow_html=True)
            roles_html = "".join(f'<span class="skill-tag-purple">{r}</span>' for r in chosen_rules["job_roles"])
            st.markdown(f"<div style='margin-top:8px;'>{roles_html}</div>", unsafe_allow_html=True)

        with c2:
            st.markdown('<div class="section-header">📊 Match Score</div>', unsafe_allow_html=True)
            pct = chosen_res["percentage"]
            bar_color = "#6C63FF" if pct >= 70 else "#F4A261" if pct >= 40 else "#E63946"
            st.markdown(f"""
            <div class="stat-card" style="margin-top:0;">
                <div style="font-size:3rem;font-weight:800;color:{bar_color};
                            font-family:'JetBrains Mono',monospace;">{pct}%</div>
                <div class="stat-label">Overall Match</div>
                <div class="progress-container" style="margin-top:12px;">
                    <div class="progress-fill" style="width:{pct}%;background:{bar_color};"></div>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">🧠 Reasoning Explanation</div>', unsafe_allow_html=True)
        for reason in chosen_res["reasons"]:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;
                        border-bottom:1px solid rgba(255,255,255,0.05);">
                <span style="color:#2EC4B6;font-size:1rem;">✔</span>
                <span style="color:#c4c8e0;font-size:0.9rem;">{reason}</span>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">🏆 Certifications</div>', unsafe_allow_html=True)
        for cert in chosen_rules["certifications"]:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:8px 12px;
                        background:rgba(108,99,255,0.06);border-radius:8px;margin:4px 0;">
                <span>📜</span>
                <span style="color:#c4c8e0;font-size:0.9rem;">{cert}</span>
            </div>""", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════
    # TAB 3 — ROADMAP
    # ═══════════════════════════════════════════════════
    with tab3:
        st.markdown('<div class="section-header">🗺️ Career Roadmap Generator</div>', unsafe_allow_html=True)
        
        road_career = st.selectbox(
            "Select Career for Roadmap",
            options=[r["career"] for r in results],
            index=0,
            key="road_sel",
        )
        road_rules = KNOWLEDGE_BASE[road_career]

        st.markdown(f"""
        <div class="info-box">
            📌 <strong>Roadmap for becoming a {road_career} {road_rules['icon']}</strong><br>
            Follow these steps in order. Focus on one step at a time.
        </div>""", unsafe_allow_html=True)

        for i, step in enumerate(road_rules["roadmap"], 1):
            st.markdown(f"""
            <div class="roadmap-step">
                <div class="roadmap-num">{i}</div>
                <div class="roadmap-text">{step}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">🏅 Target Certifications</div>', unsafe_allow_html=True)
        cert_cols = st.columns(len(road_rules["certifications"]))
        for col, cert in zip(cert_cols, road_rules["certifications"]):
            with col:
                st.markdown(f"""
                <div class="career-card" style="text-align:center;padding:18px 12px;">
                    <div style="font-size:1.8rem;margin-bottom:8px;">📜</div>
                    <div style="font-size:0.82rem;color:#c4c8e0;font-weight:600;">{cert}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">💰 Expected Earning</div>', unsafe_allow_html=True)
        ec1, ec2 = st.columns(2)
        with ec1:
            st.markdown(f"""<div class="career-card" style="text-align:center;">
                <div style="font-size:1.6rem;">🇵🇰</div>
                <div style="font-size:1.1rem;font-weight:700;color:#2EC4B6;margin:8px 0 4px;">{road_rules['salary_pkr']}</div>
                <div style="font-size:0.78rem;color:#8892a4;">Pakistan Market</div>
            </div>""", unsafe_allow_html=True)
        with ec2:
            st.markdown(f"""<div class="career-card" style="text-align:center;">
                <div style="font-size:1.6rem;">🌍</div>
                <div style="font-size:1.1rem;font-weight:700;color:#6C63FF;margin:8px 0 4px;">{road_rules['salary_usd']}</div>
                <div style="font-size:0.78rem;color:#8892a4;">Remote / Global</div>
            </div>""", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════
    # TAB 4 — SKILL GAP ANALYSIS
    # ═══════════════════════════════════════════════════
    with tab4:
        st.markdown('<div class="section-header">🔍 Skill Gap Analysis</div>', unsafe_allow_html=True)

        gap_career = st.selectbox(
            "Select Career for Skill Gap",
            options=[r["career"] for r in results],
            index=0,
            key="gap_sel",
        )
        gap_res   = next(r for r in results if r["career"] == gap_career)
        gap_rules = gap_res["rules"]

        g1, g2 = st.columns(2)
        with g1:
            st.markdown("""<div style='font-weight:700;color:#2EC4B6;font-size:0.95rem;
                            margin-bottom:12px;'>✅ Skills You Already Have</div>""",
                        unsafe_allow_html=True)
            if gap_res["matched_skills"]:
                for s in gap_res["matched_skills"]:
                    st.markdown(f"""
                    <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;
                                background:rgba(46,196,182,0.08);border:1px solid rgba(46,196,182,0.25);
                                border-radius:10px;margin:5px 0;">
                        <span style="font-size:1.2rem;">✅</span>
                        <span style="color:#7de8df;font-weight:600;">{s}</span>
                        <span style="color:#8892a4;font-size:0.78rem;margin-left:auto;">Required</span>
                    </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="warning-box">No required skills matched yet.</div>',
                            unsafe_allow_html=True)

        with g2:
            st.markdown("""<div style='font-weight:700;color:#E63946;font-size:0.95rem;
                            margin-bottom:12px;'>❌ Skills You Need to Develop</div>""",
                        unsafe_allow_html=True)
            if gap_res["gap_skills"]:
                for s in gap_res["gap_skills"]:
                    st.markdown(f"""
                    <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;
                                background:rgba(230,57,70,0.08);border:1px solid rgba(230,57,70,0.25);
                                border-radius:10px;margin:5px 0;">
                        <span style="font-size:1.2rem;">❌</span>
                        <span style="color:#ff8a8a;font-weight:600;">{s}</span>
                        <span style="color:#8892a4;font-size:0.78rem;margin-left:auto;">Missing</span>
                    </div>""", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="warning-box" style="margin-top:14px;">
                    <strong>⚠️ Weakness Analysis:</strong><br>
                    You are suitable for <strong>{gap_career}</strong>, but your 
                    <strong>{', '.join(gap_res['gap_skills'])}</strong> skill(s) need development. 
                    Focus on these to become a stronger candidate.
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">🎉 You have all required skills!</div>',
                            unsafe_allow_html=True)

        # Interest gap
        st.markdown('<div class="section-header">💡 Interest Alignment</div>', unsafe_allow_html=True)
        i1, i2 = st.columns(2)
        with i1:
            st.markdown("<div style='color:#2EC4B6;font-weight:600;margin-bottom:8px;'>✅ Matched Interests</div>",
                        unsafe_allow_html=True)
            if gap_res["matched_interests"]:
                for interest in gap_res["matched_interests"]:
                    st.markdown(f'<span class="skill-tag-green">{interest}</span>', unsafe_allow_html=True)
            else:
                st.markdown("<div style='color:#8892a4;font-size:0.85rem;'>None matched</div>",
                            unsafe_allow_html=True)
        with i2:
            st.markdown("<div style='color:#E63946;font-weight:600;margin-bottom:8px;'>❌ Missing Interests</div>",
                        unsafe_allow_html=True)
            if gap_res["gap_interests"]:
                for interest in gap_res["gap_interests"]:
                    st.markdown(f'<span class="skill-tag-red">{interest}</span>', unsafe_allow_html=True)
            else:
                st.markdown("<div style='color:#8892a4;font-size:0.85rem;'>All interests matched!</div>",
                            unsafe_allow_html=True)

        # Personality
        st.markdown('<div class="section-header">👤 Personality Analysis</div>', unsafe_allow_html=True)
        user_traits  = user_facts.get("personality", [])
        ideal_traits = gap_rules["personality_bonus"]
        matched_p    = [t for t in ideal_traits if t in user_traits]
        missing_p    = [t for t in ideal_traits if t not in user_traits]

        if matched_p:
            st.markdown(f"""
            <div class="success-box">
                ✔ Your personality traits <strong>({', '.join(matched_p)})</strong> 
                align well with <strong>{gap_career}</strong>!
            </div>""", unsafe_allow_html=True)
        if missing_p:
            st.markdown(f"""
            <div class="info-box">
                ℹ️ Ideal personality for <strong>{gap_career}</strong>: 
                {', '.join(f'<strong>{t}</strong>' for t in missing_p)}<br>
                <em>Note: Personality is a soft factor — not a hard requirement.</em>
            </div>""", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════
    # TAB 5 — ALL RESULTS TABLE
    # ═══════════════════════════════════════════════════
    with tab5:
        st.markdown('<div class="section-header">📊 All Career Rankings</div>', unsafe_allow_html=True)

        # Domain filter
        domain_filter = st.selectbox("Filter by Domain", DOMAINS, index=0, key="domain_filter")
        filtered = get_domain_filtered(results, domain_filter)

        for rank, res in enumerate(filtered, 1):
            career = res["career"]
            pct    = res["percentage"]
            rules  = res["rules"]

            if pct >= 70:
                bar_color = "linear-gradient(90deg,#6C63FF,#00B4D8)"
                label_color = "#a89cff"
            elif pct >= 50:
                bar_color = "linear-gradient(90deg,#2EC4B6,#6C63FF)"
                label_color = "#2EC4B6"
            elif pct >= 30:
                bar_color = "linear-gradient(90deg,#F4A261,#e07b3a)"
                label_color = "#F4A261"
            else:
                bar_color = "linear-gradient(90deg,#E63946,#c1121f)"
                label_color = "#E63946"

            domains_html = "".join(f'<span class="career-domain">{d}</span>' for d in rules["domains"])
            skills_html  = "".join(
                f'<span class="skill-tag-green">{s}</span>' for s in res["matched_skills"]
            ) + "".join(
                f'<span class="skill-tag-red">{s}</span>' for s in res["gap_skills"]
            )

            st.markdown(f"""
            <div class="career-card">
                <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
                    <div style="font-size:2rem;min-width:40px;text-align:center;">{rules['icon']}</div>
                    <div style="flex:1;min-width:160px;">
                        <div class="career-name" style="font-size:1rem;">#{rank} {career}</div>
                        <div style="margin-top:4px;">{domains_html}</div>
                    </div>
                    <div style="min-width:120px;">
                        <div style="font-family:'JetBrains Mono',monospace;font-size:1.4rem;
                                    font-weight:700;color:{label_color};">{pct}%</div>
                        <div class="progress-container" style="margin-top:4px;">
                            <div class="progress-fill" style="width:{pct}%;background:{bar_color};"></div>
                        </div>
                    </div>
                    <div style="min-width:200px;font-size:0.8rem;color:#8892a4;">
                        💰 {rules['salary_pkr']}
                    </div>
                </div>
                <div style="margin-top:10px;">{skills_html}</div>
            </div>""", unsafe_allow_html=True)

    # ── Footer ──
    st.markdown("""
    <div style='text-align:center;margin-top:40px;padding:20px;
                border-top:1px solid rgba(108,99,255,0.15);color:#8892a4;font-size:0.82rem;'>
        <strong style='color:#6C63FF;'>Smart Career Counseling Expert System</strong> &nbsp;•&nbsp; 
        KRR Project &nbsp;•&nbsp; Forward Chaining Inference Engine &nbsp;•&nbsp; 
        Knowledge Representation &amp; Reasoning
    </div>
    """, unsafe_allow_html=True)
