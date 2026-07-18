import streamlit as st


def get_verdict(match_score, skill_score):
    overall = match_score * 0.6 + skill_score * 0.4

    if overall >= 75:
        return {"label": "Hire", "emoji": "⭐", "css": "verdict-hire",
                "reason": "Strong overall match with the job requirements."}
    if overall >= 50:
        return {"label": "Maybe", "emoji": "🤔", "css": "verdict-maybe",
                "reason": "Partial match — worth a closer look or interview."}
    return {"label": "Reject", "emoji": "🚫", "css": "verdict-reject",
            "reason": "Low alignment with the job requirements."}


def render_verdict(match_score, skill_score):
    v = get_verdict(match_score, skill_score)
    st.markdown(f"""
        <div class="glass-card verdict-card {v['css']}">
            <div class="verdict-emoji">{v['emoji']}</div>
            <div class="verdict-label">{v['label']}</div>
            <div class="verdict-reason">{v['reason']}</div>
        </div>
    """, unsafe_allow_html=True)