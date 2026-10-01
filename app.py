import streamlit as st
import requests

st.set_page_config(page_title="AI SOS Triage Dashboard", page_icon="🚨", layout="wide")

st.title("🚨 AI Emergency SOS Triage & Response Prioritizer")
st.markdown("**Powered by LangChain, Gemini, and IKS (Sushruta Samhita Triage Matrix)**")

# Sidebar for config
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")
st.sidebar.markdown("---")
st.sidebar.markdown("### System Status")
st.sidebar.success("Backend API: Waiting...")
st.sidebar.info("Vector DB: ChromaDB Ready")

# Main dashboard
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Incoming SOS Signal")
    sos_input = st.text_area("Operator / User Input:", height=150, placeholder="E.g., Deep cut on the neck, bleeding heavily after an accident.")
    submit_btn = st.button("Process & Triage", type="primary")

with col2:
    st.subheader("Triage Output (Live Dispatch)")
    if submit_btn:
        if not api_key:
            st.error("⚠️ Please provide a Google Gemini API Key in the sidebar.")
        elif not sos_input.strip():
            st.warning("Please enter an SOS message.")
        else:
            with st.spinner("Analyzing NLP and querying IKS Vector Database..."):
                try:
                    res = requests.post("http://localhost:8000/triage", json={"message": sos_input, "api_key": api_key})
                    
                    if res.status_code == 200:
                        response_data = res.json()
                        if response_data.get("status") == "success":
                            data = response_data["data"]
                            
                            # Priority colors
                            p_color = "red" if data.get("Priority") in ["P1", "P2"] else "orange" if data.get("Priority") == "P3" else "green"
                            
                            st.markdown(f"### Priority Level: <span style='color:{p_color}'>**{data.get('Priority', 'N/A')}**</span>", unsafe_allow_html=True)
                            st.info(f"**Dispatch Agency:** {data.get('Agency', 'N/A')}")
                            st.write(f"**Situation Summary:** {data.get('Summary', 'N/A')}")
                            st.success(f"**IKS Triage Reasoning:** {data.get('IKS_Reasoning', 'N/A')}")
                            
                        else:
                            st.error(f"Error parsing AI response: {response_data.get('message')} \n Raw Output: {response_data.get('raw')}")
                    else:
                        st.error("Failed to connect to FastAPI Backend. Make sure it is running on port 8000.")
                except requests.exceptions.ConnectionError:
                    st.error("🚨 Backend Server Not Reachable. Please run `uvicorn backend:app --reload` in a separate terminal.")
