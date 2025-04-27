
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample Claude sentiment data
claude_data = pd.DataFrame({
    "timestamp": pd.date_range("2024-06-01", periods=10),
    "sentiment": [0.3, 0.5, 0.8, 0.7, 0.2, -0.1, -0.4, 0.0, 0.6, 0.9]
})

# Sample Jurassic directional bias
jurassic_data = pd.DataFrame({
    "timestamp": pd.date_range("2024-06-01", periods=10),
    "bias": ["Bullish", "Bullish", "Bullish", "Neutral", "Bearish", "Bearish", "Bearish", "Neutral", "Bullish", "Bullish"]
})

# Sample PnL data
pnl_data = pd.DataFrame({
    "timestamp": pd.date_range("2024-06-01", periods=10),
    "pnl": [0, 120, 300, 250, 200, 100, 50, 150, 300, 500]
})

# Create Streamlit dashboard
st.title("GENIE AI Trading Dashboard")

# Claude Sentiment Trend
st.subheader("Claude Market Sentiment Trend")
fig1, ax1 = plt.subplots()
ax1.plot(claude_data["timestamp"], claude_data["sentiment"], marker="o", linestyle='-')
ax1.axhline(0, color="gray", linestyle="--")
ax1.set_ylabel("Sentiment Score (-1 = Bearish, +1 = Bullish)")
ax1.set_xlabel("Date")
st.pyplot(fig1)

# Jurassic Directional Bias
st.subheader("Jurassic SEC/Dark Pool Bias")
bias_counts = jurassic_data["bias"].value_counts()
fig2, ax2 = plt.subplots()
bias_counts.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Frequency")
ax2.set_title("Jurassic Directional Bias")
st.pyplot(fig2)

# GENIE PnL Overlay
st.subheader("GENIE Strategy PnL Over Time")
fig3, ax3 = plt.subplots()
ax3.plot(pnl_data["timestamp"], pnl_data["pnl"], marker="o", linestyle='-', color='green')
ax3.set_ylabel("Cumulative PnL ($)")
ax3.set_xlabel("Date")
st.pyplot(fig3)
