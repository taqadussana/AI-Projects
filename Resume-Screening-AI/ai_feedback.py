import streamlit as st


def get_ai_feedback(resume_text, job_text, api_key):
    if not api_key:
        return False, "No OpenAI API key configured — showing rule-based suggestions instead."

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = (
            "You are a resume reviewer. In under 120 words, give 3 concrete, "
            "specific suggestions to improve this resume for the target job.\n\n"
            f"JOB DESCRIPTION:\n{job_text[:2000]}\n\nRESUME:\n{resume_text[:2000]}"
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            timeout=20,
        )
        return True, response.choices[0].message.content.strip()

    except Exception as e:
        return False, f"AI feedback unavailable right now ({type(e).__name__}) — showing rule-based suggestions instead."


def render_ai_feedback_toggle(resume_text, job_text):
    use_ai = st.checkbox("🤖 Use OpenAI for natural-language feedback (requires API key in secrets)", value=False)
    if not use_ai:
        return None

    api_key = st.secrets.get("OPENAI_API_KEY", None) if hasattr(st, "secrets") else None
    ok, message = get_ai_feedback(resume_text, job_text, api_key)
    if ok:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("**🤖 AI Feedback**")
        st.write(message)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info(message)
    return ok