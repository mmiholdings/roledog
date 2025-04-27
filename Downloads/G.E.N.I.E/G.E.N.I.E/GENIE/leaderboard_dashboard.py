
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🔁 GENIE Agent Leaderboard")

df = pd.read_csv("agent_performance.csv")
st.subheader("📈 Sharpe Ratio Trends")
st.line_chart(df.pivot(index='timestamp', columns='agent', values='sharpe'))

st.subheader("💰 PnL Comparison")
latest = df.sort_values("timestamp").groupby("agent").tail(1)
st.bar_chart(latest.set_index("agent")["pnl"])

st.subheader("📄 Claude Feedback Summary")
try:
    with open("agent_weights.md") as f:
        st.code(f.read())
except:
    st.warning("No summary yet. Trigger /genie-feedback API.")
