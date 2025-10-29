import streamlit as st
import requests
import time
import os

# Use container-internal networking
API_URL = "http://127.0.0.1:8000/generate"  # Changed from localhost

st.set_page_config(page_title="GameLoreGPT", layout="centered")
st.title("GameLoreGPT")
st.write("Generate backstories, quests, and world lore for your indie game.")

prompt = st.text_area("Enter your idea", placeholder="A rogue alchemist in a floating city...", height=120)
version = st.selectbox("Model Version", ["v1", "v2", "canary"])

if st.button("Generate Lore"):
    if prompt.strip():
        with st.spinner("Starting AI engine..."):
            # Wait for FastAPI to be ready
            for _ in range(30):
                try:
                    resp = requests.get("http://127.0.0.1:8000/", timeout=1)
                    if resp.status_code == 200:
                        break
                except:
                    time.sleep(1)
            else:
                st.error("Backend not responding. Check logs.")
                st.stop()

        with st.spinner("Generating lore..."):
            try:
                resp = requests.post(API_URL, json={"prompt": prompt, "model_version": version})
                if resp.ok:
                    st.success("Lore generated!")
                    st.markdown(resp.json()["lore"])
                else:
                    st.error(f"API Error: {resp.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
    else:
        st.warning("Please enter a prompt.")