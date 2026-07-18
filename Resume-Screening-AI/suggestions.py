import streamlit as st


def generate_suggestions(missing_skills, match_score):
    tips = []

    if missing_skills:
        shown = missing_skills[:5]
        tips.append(f"Add or highlight experience with: {', '.join(shown)}.")
    if match_score < 50:
        tips.append("Rework the resume summary to mirror key phrases from the job description.")
    if match_score < 75:
        tips.append("Quantify achievements with numbers (%, $, time saved) to strengthen impact.")
    if not missing_skills and match_score >= 75:
        tips.append("Strong match — consider tailoring the top section to the specific role title.")

    tips.append("Keep formatting simple (no tables/images) so ATS systems can parse it correctly.")
    return tips


def render_suggestions(missing_skills_str, match_score):
    missing = [s.strip() for s in str(missing_skills_str).split(",") if s.strip()]
    tips = generate_suggestions(missing, match_score)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("**💡 AI Improvement Suggestions**")
    for tip in tips:
        st.markdown(f"- {tip}")
    st.markdown('</div>', unsafe_allow_html=True)


def render_resume_preview(resume_text):
    with st.expander("📝 Resume Text Preview"):
        preview = (resume_text or "").strip()
        if not preview:
            st.info("No extractable text found in this resume.")
            return
        st.text(preview[:3000] + ("..." if len(preview) > 3000 else ""))