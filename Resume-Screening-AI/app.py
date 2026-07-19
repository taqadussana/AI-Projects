import streamlit as st
import pandas as pd
import tempfile
import os
from parser import extract_pdf
from scorer import score_resume
from dashboard import metrics, top_candidates, skill_section, filter_candidates
from skills import compare_skills
from charts import score_chart, skill_chart, ats_gauge, score_trend
from recommendation import render_verdict
from suggestions import render_suggestions, render_resume_preview
from pdf_report import build_pdf_report

st.set_page_config(
    page_title="Resume Screening AI Pro",
    page_icon="🤖",
    layout="wide"
)

# Load CSS safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(BASE_DIR, "assets", "style.css")

st.write("Current directory:", os.getcwd())
st.write("App directory:", BASE_DIR)
st.write("CSS exists:", os.path.exists(CSS_FILE))

with open(CSS_FILE, "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🤖 Resume Screening AI Pro")
st.caption("AI-powered Resume Ranking System")
st.divider()

left, right = st.columns(2)
with left:
    job_file = st.file_uploader("📄 Upload Job Description (PDF)", type=["pdf"])
with right:
    resume_files = st.file_uploader(
        "📁 Upload Multiple Resumes (PDF)", type=["pdf"], accept_multiple_files=True
    )

if st.button("🚀 Analyze Resumes", width='stretch'):
    if not job_file:
        st.error("Please upload a Job Description.")
        st.stop()
    if not resume_files:
        st.error("Please upload at least one Resume.")
        st.stop()

    with st.spinner("🤖 AI is analyzing resumes..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_job:
            temp_job.write(job_file.read())
            job_path = temp_job.name
        job_text = extract_pdf(job_path)

        results = []
        for resume in resume_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_resume:
                temp_resume.write(resume.read())
                resume_path = temp_resume.name
            resume_text = extract_pdf(resume_path)

            score = score_resume(resume_text, job_text)
            skills = compare_skills(resume_text, job_text)

            results.append({
                "Candidate": resume.name.replace(".pdf", ""),
                "Match Score": score,
                "Skill Score": skills["skill_score"],
                "Matched Skills": ", ".join(skills["matched"]),
                "Missing Skills": ", ".join(skills["missing"]),
                "Resume Text": resume_text,
            })
            os.remove(resume_path)
        os.remove(job_path)

    df = pd.DataFrame(results)
    df = df.sort_values(by="Match Score", ascending=False)

    st.session_state["df"] = df
    st.session_state["job_text"] = job_text

if "df" in st.session_state:
    df = st.session_state["df"]
    job_text = st.session_state["job_text"]

    highest = df["Match Score"].max()
    average = round(df["Match Score"].mean(), 2)

    st.divider()
    metrics(len(df), highest, average)
    st.divider()
    top_candidates(df)
    st.divider()

    score_chart(df)
    score_trend(df)
    st.divider()

    st.subheader("🏆 Candidate Rankings")
    filtered_df = filter_candidates(df)
    st.dataframe(
        filtered_df.drop(columns=["Resume Text"]),
        width='stretch', hide_index=True
    )
    st.divider()

    st.subheader("🧠 AI Skill Analysis")
    if filtered_df.empty:
        st.warning("No candidates match your search/filter.")
    else:
        selected = st.selectbox("Choose Candidate", filtered_df["Candidate"])
        candidate = df[df["Candidate"] == selected].iloc[0]

        skill_section(candidate)

        gcol, vcol = st.columns([1.3, 1])
        with gcol:
            ats_gauge(candidate["Match Score"])
        with vcol:
            render_verdict(candidate["Match Score"], candidate["Skill Score"])

        skill_chart(candidate["Skill Score"])
        st.divider()

        render_resume_preview(candidate["Resume Text"])
        render_suggestions(candidate["Missing Skills"], candidate["Match Score"])
        
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.download_button(
            "📥 Download Results CSV",
            df.drop(columns=["Resume Text"]).to_csv(index=False),
            file_name="resume_scores.csv",
            mime="text/csv",
            width='stretch'
        )
    with c2:
        st.download_button(
            "📄 Download PDF Report",
            build_pdf_report(df),
            file_name="resume_report.pdf",
            mime="application/pdf",
            width='stretch'
        )
    st.success("Analysis Completed Successfully!")