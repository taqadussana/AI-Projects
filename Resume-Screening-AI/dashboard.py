import html
import streamlit as st


def filter_candidates(df):
    c1, c2 = st.columns([2, 1])
    with c1:
        query = st.text_input("🔍 Search candidate name", "")
    with c2:
        min_score = st.slider("Minimum Match Score", 0, 100, 0)

    filtered = df[df["Match Score"] >= min_score]
    if query.strip():
        filtered = filtered[filtered["Candidate"].str.contains(query.strip(), case=False, na=False)]
    return filtered


def metrics(count, highest, average):
    col1, col2, col3 = st.columns(3)
    col1.metric("📋 Candidates Screened", count)
    col2.metric("🏆 Highest Match", f"{highest}%")
    col3.metric("📊 Average Match", f"{average}%")


def _podium_card(rank, name, score, skill_score):
    medal = {1: "🥇", 2: "🥈", 3: "🥉"}[rank]
    safe_name = html.escape(str(name))
    return f"""<div class="podium-card rank-{rank}">
        <div class="rank-badge">{medal}</div>
        <div class="podium-name" title="{safe_name}">{safe_name}</div>
        <div class="podium-score">{score}%</div>
        <div class="podium-score-label">Match Score</div>
        <div class="podium-bar-track"><div class="podium-bar-fill" style="width:{skill_score}%;"></div></div>
    </div>"""


def top_candidates(df):
    st.subheader("🏅 Top Candidates")
    top = df.head(3).reset_index(drop=True)
    if top.empty:
        st.info("No candidates to display yet.")
        return
    cards = "".join(
        _podium_card(i + 1, row["Candidate"], row["Match Score"], row["Skill Score"])
        for i, row in top.iterrows()
    )
    st.markdown(f'<div class="podium-wrap">{cards}</div>', unsafe_allow_html=True)


def skill_section(candidate):
    matched = [s.strip() for s in str(candidate.get("Matched Skills", "")).split(",") if s.strip()]
    missing = [s.strip() for s in str(candidate.get("Missing Skills", "")).split(",") if s.strip()]
    matched_html = "".join(f'<span class="pill pill-matched">✓ {html.escape(s)}</span>' for s in matched) or "None found"
    missing_html = "".join(f'<span class="pill pill-missing">✗ {html.escape(s)}</span>' for s in missing) or "None missing"

    st.markdown(f"""<div class="glass-card">
        <b>{html.escape(str(candidate['Candidate']))}</b><br>
        <span class="mono-score">Match: {candidate['Match Score']}% · Skill: {candidate['Skill Score']}%</span>
        <p style="margin-top:0.8rem;">Matched Skills</p>
        <div class="pill-row">{matched_html}</div>
        <p style="margin-top:0.8rem;">Missing Skills</p>
        <div class="pill-row">{missing_html}</div>
    </div>""", unsafe_allow_html=True)