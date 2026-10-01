# AI-Based Emergency SOS Triage & Response Prioritizer

**Student Name:** Sahayaraj Nadar  
**Roll Number:** 19068  
**Class:** TY IT (IKS Individual Project)  

## 🚀 Project Description
An intelligent system designed to parse, classify, and prioritize emergency distress signals in real-time. By leveraging LLMs and RAG, it processes natural language SOS inputs and assigns a priority level (P1-Critical to P5-Minor).

## 🧠 IKS Connection (Sushruta Samhita)
This project integrates principles from the *Sushruta Samhita* regarding wound classification (*Vrana*) and vital points (*Marma*). The AI cross-references incoming SOS messages against an IKS-based vector database (ChromaDB) to immediately flag critical injuries based on ancient medical wisdom.

## 🛠 Technologies & Tech Stack
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **AI/LLM:** Google Gemini API
* **Framework:** LangChain
* **Vector Database:** ChromaDB
* **Language:** Python

## 📦 Installation and Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-link>
   cd sos-triage-project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ How to run and use the project

You need to run **TWO** terminals (one for the backend API, one for the frontend UI).

**Terminal 1 (Start the FastAPI Backend):**
```bash
uvicorn backend:app --reload
```
*The backend will run on http://localhost:8000*

**Terminal 2 (Start the Streamlit Frontend):**
```bash
streamlit run app.py
```
*The Streamlit frontend will open in your browser automatically (usually http://localhost:8501).*

## 🔑 Environment Variables / Secrets
* `GOOGLE_API_KEY`: Input your Gemini API Key directly in the Streamlit Sidebar UI. (Never hardcode secrets into the source code as per submission rules).

## 🌐 Live Deployment
* [Insert your live hosted link here before submission]
