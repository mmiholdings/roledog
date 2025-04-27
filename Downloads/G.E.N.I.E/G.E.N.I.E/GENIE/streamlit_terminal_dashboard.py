import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="GENIE Terminal", layout="wide")

# ----- Header -----
st.markdown("""
    <h1 style='text-align: center; color: white;'>🧠 G.E.N.I.E Terminal Dashboard</h1>
    <p style='text-align: center; color: gray;'>Live Agent Status • Logs • Environment Control</p>
""", unsafe_allow_html=True)

# ----- Agent Sentiment -----
st.markdown("## 🧠 Macro Sentiment")
cols = st.columns(2)
with cols[0]:
    st.metric(label="Claude", value="0.81", delta="🧠 Market Confidence")
with cols[1]:
    st.metric(label="FinBERT Output", value="87.2%", delta="📊 Market Confidence")

# ----- Agent Leaderboard -----
st.markdown("## 🏆 Agent Intelligence")
leaderboard = pd.DataFrame({
    "Agent": ["Reggie", "Theo", "Ace", "Mo"],
    "Total PnL": ["$163.8k", "$49.4k", "$4.9k", "$4.9k"],
    "Avg Confidence": ["98.4%", "98.4%", "63.7%", "63.7%"],
    "Win Rate": ["100%", "10%", "75%", "75%"]
})
st.dataframe(leaderboard, use_container_width=True, hide_index=True)

# ----- Replay Simulation Toggle -----
st.markdown("## 🔄 Replay / Simulation")
st.toggle("Activate Replay Mode", value=False)

# ----- Alerts -----
st.markdown("## 🚨 Alerts")
alert_cols = st.columns(2)
with alert_cols[0]:
    st.warning("13:51 🔔 HIGH UNREALIZED LOSS")
    st.info("13:36 Strong Drop")
    st.success("12:24 HIGH CONFIDENCE")
with alert_cols[1]:
    st.warning("13:31 🔔 HIGH UNREAL. LOSS")
    st.info("12:36 Strong Drop")
    st.success("12:42 HIGH CONFID ENTRY")

# ----- Heatmap (Placeholder) -----
st.markdown("## 🌡️ Alerts % Anomalies Heatmap")
st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Heatmap.png", caption="Live Heatmap")

# ----- Footer -----
st.markdown(f"<small style='color: gray;'>Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>", unsafe_allow_html=True)
