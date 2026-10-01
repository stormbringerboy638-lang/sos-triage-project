from fastapi import FastAPI
from pydantic import BaseModel
from core_ai import process_sos
import json

app = FastAPI(title="SOS Triage AI Backend")

class SOSRequest(BaseModel):
    message: str
    api_key: str

@app.post("/triage")
def triage_message(req: SOSRequest):
    try:
        result_str = process_sos(req.message, req.api_key)
        result = json.loads(result_str)
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e), "raw": result_str if 'result_str' in locals() else ""}
