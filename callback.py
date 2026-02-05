import requests

GUVI_ENDPOINT = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

def send_callback(session_id, total_messages, intelligence):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": total_messages,
        "extractedIntelligence": intelligence,
        "agentNotes": "Scammer used urgency and account-blocking tactics"
    }

    try:
        requests.post(GUVI_ENDPOINT, json=payload, timeout=5)
    except Exception:
        pass
