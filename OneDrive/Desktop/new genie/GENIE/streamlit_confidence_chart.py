import streamlit as st
import os
import json
import pandas as pd
import plotly.express as px

st.title("📈 GENIE Agent Confidence Tracking")

agents = ["Mo", "Ace", "Reggie"]
data = []

for agent in agents:
    path = f"signals/{agent.lower()}.json"
    if os.path.exists(path):
        with open(path) as f:
            sig = json.load(f)
            data.append({
                "Agent": agent,
                "Confidence": sig.get("confidence", 0),
                "Time": sig.get("timestamp", "")
            })

df = pd.DataFrame(data)
fig = px.bar(df, x="Agent", y="Confidence", color="Agent", title="Live Confidence by Agent")
st.plotly_chart(fig)