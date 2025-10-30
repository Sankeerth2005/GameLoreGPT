# frontend/streamlit_app.py
import streamlit as st
import requests
import time

API_URL = "http://localhost:8000/generate"

st.set_page_config(page_title="GameLoreGPT", layout="centered")
st.title("GameLoreGPT")
st.write("Generate backstories, quests, and world lore for your indie game.")

prompt = st.text_area("Enter your idea", height=120, placeholder="A rogue AI in a neon city...")
version = st.selectbox("Model Version", ["v1 (TinyLlama)", "v2 (Phi-2)"])

if st.button("Generate Lore"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Starting AI..."):
            for _ in range(20):
                try:
                    if requests.get("http://localhost:8000/").ok:
                        break
                except:
                    time.sleep(1)
            else:
                st.error("Backend not running on port 8000")
                st.stop()

        with st.spinner("Generating..."):
            payload = {"prompt": prompt, "model_version": "v1" if "v1" in version else "v2"}
            try:
                resp = requests.post(API_URL, json=payload, timeout=60)
                if resp.ok:
                    data = resp.json()
                    st.success(f"Generated with **{version}**")
                    st.markdown(data["lore"])
                else:
                    st.error(f"API Error: {resp.text}")
            except Exception as e:
                st.error(f"Failed: {e}")