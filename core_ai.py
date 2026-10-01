import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import chromadb

def process_sos(sos_message: str, google_api_key: str):
    os.environ["GOOGLE_API_KEY"] = google_api_key
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
    
    # Setup local Vector DB (Chroma)
    chroma_client = chromadb.Client()
    collection_name = "iks_triage_collection"
    
    # Delete if exists for clean state in this demo
    try:
        chroma_client.delete_collection(name=collection_name)
    except:
        pass
        
    collection = chroma_client.create_collection(name=collection_name)
    
    # Load IKS Data
    with open("iks_triage_data.json", "r") as f:
        triage_data = json.load(f)
        
    for i, item in enumerate(triage_data):
        collection.add(
            documents=[item["condition"]],
            metadatas=[{"priority": item["priority"], "department": item["department"], "iks_concept": item["iks_concept"]}],
            ids=[str(i)]
        )
        
    # Retrieve context via Vector Embeddings
    results = collection.query(query_texts=[sos_message], n_results=1)
    
    context = "No direct IKS match found."
    if results['metadatas'] and len(results['metadatas'][0]) > 0:
        meta = results['metadatas'][0][0]
        context = f"Matched IKS Rule: {meta['iks_concept']}, Suggested Priority: {meta['priority']}, Dept: {meta['department']}"

    prompt = f'''You are an AI SOS Triage Assistant based on Indian Knowledge System (IKS) - Sushruta Samhita principles.
    Analyze the incoming SOS message: "{sos_message}"
    Retrieved IKS Vector Context: {context}
    
    Output a valid JSON object strictly with the following keys:
    - "Priority": (P1 to P5, where P1 is critical)
    - "Agency": (Medical, Fire, or Police)
    - "Summary": (Brief 1-sentence summary)
    - "IKS_Reasoning": (How Sushruta's triage logic applies here based on the context)
    
    Return ONLY valid JSON. No markdown formatting like ```json ... ```. Just the raw JSON object.
    '''
    
    response = llm.invoke(prompt)
    text = response.content.strip()
    if text.startswith("```json"):
        text = text[7:-3]
    elif text.startswith("```"):
        text = text[3:-3]
        
    return text
