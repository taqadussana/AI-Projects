import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def score_chart(df):
    fig = px.bar(
        df, x="Candidate", y="Match Score", color="Match Score",
        text="Match Score", title="📊 Resume Match Scores"
    )
    fig.update_layout(height=500, xaxis_title="Candidate", yaxis_title="Match %", template="plotly_dark")
    st.plotly_chart(fig, width="stretch")


def skill_chart(skill_score):
    fig = px.pie(
        names=["Matched", "Missing"], values=[skill_score, 100 - skill_score],
        hole=0.65, title="🧠 Skill Match"
    )
    fig.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig, width="stretch")


def score_trend(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Candidate"], y=df["Match Score"],
        mode="lines+markers", name="Match Score",
        line=dict(color="#7c6fff", width=3), marker=dict(size=9),
    ))
    fig.add_trace(go.Scatter(
        x=df["Candidate"], y=df["Skill Score"],
        mode="lines+markers", name="Skill Score",
        line=dict(color="#5eead4", width=3, dash="dot"), marker=dict(size=9),
    ))
    fig.update_layout(
        title="📈 Score Trend Across Candidates",
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)", height=380,
        legend=dict(orientation="h", y=1.15),
    )
    st.plotly_chart(fig, width="stretch")


def ats_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"suffix": "%", "font": {"size": 40}},
        title={"text": "🎯 ATS Compatibility"},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#8993ab"},
            "bar": {"color": "#7c6fff"},
            "bgcolor": "rgba(255,255,255,0.03)",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 50], "color": "rgba(255,122,138,0.25)"},
                {"range": [50, 75], "color": "rgba(255,200,87,0.25)"},
                {"range": [75, 100], "color": "rgba(94,234,212,0.25)"},
            ],
            "threshold": {"line": {"color": "white", "width": 3}, "value": score},
        },
    ))
    fig.update_layout(
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#edeff7"}, height=320, margin=dict(l=30, r=30, t=60, b=10),
    )
    st.plotly_chart(fig, width="stretch")