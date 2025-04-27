import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import json
import os

st.set_page_config(layout="wide")
st.title("🔐 GENIE Live Dashboard")

# Auth Setup
with open("dashboard/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"], config["cookie"]["name"], config["cookie"]["key"], config["cookie"]["expiry_days"]
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.success(f"Welcome {name}!")

    agents = ["Mo", "Reggie", "Ace", "Theo", "Rocco"]
    cols = st.columns(len(agents))

    for idx, agent in enumerate(agents):
        try:
            with open(f"buffer/{agent.lower()}.json") as f:
                signal = json.load(f)
                cols[idx].metric(label=f"{agent}", value=f"${signal['pnl']}", delta=f"{signal['confidence']*100:.0f}% Conf")
                cols[idx].text(f"{signal['bias']} @ {signal['entry']} → {signal['exit']}")
        except:
            cols[idx].warning(f"{agent}: No data")
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")