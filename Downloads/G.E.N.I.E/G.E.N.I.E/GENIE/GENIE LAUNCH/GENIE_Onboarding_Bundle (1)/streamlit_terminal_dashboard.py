import streamlit as st

st.set_page_config(page_title="GENIE Terminal", layout="wide")

st.title("🧠 G.E.N.I.E Terminal Dashboard")

st.markdown("### Live Agent Status • Logs • Environment Control")
col1, col2 = st.columns(2)
with col1:
    st.subheader("📊 Agent Intelligence")
    st.dataframe({
        'Agent': ['Mo', 'Reggie', 'Theo'],
        'PnL': [3120, 4280, -200],
        'Confidence': ['84%', '90%', '61%'],
        'Win Rate': ['74%', '83%', '42%']
    })
with col2:
    st.subheader("🌐 Macro Sentiment")
    st.metric("Claude Macro Index", value="0.81", delta="+0.04")
    st.metric("FinBERT Output", value="87.2%", delta="+2.1%")

st.markdown("---")
st.markdown("✅ All systems operational.")