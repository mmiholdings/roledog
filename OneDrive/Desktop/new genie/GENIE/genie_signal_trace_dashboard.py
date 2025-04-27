
import streamlit as st
import pandas as pd
import json

st.title("🧠 GENIE Signal → Execution Trace")

with open("trade_signal.json") as f:
    signal = json.load(f)

df = pd.read_csv("agent_performance.csv")

st.subheader("🔢 Signal Inputs")
st.write(signal)

st.subheader("📊 Agent PnL & Sharpe")
st.dataframe(df)

st.subheader("📄 Claude Summary (if any)")
try:
    with open("agent_weights.md") as f:
        st.code(f.read())
except:
    st.warning("No summary yet.")
