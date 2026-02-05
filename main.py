from fastapi import FastAPI, Request, Header, HTTPException
from memory import add_message, get_turn_count, get_conversation
from scam_detection import is_scam
from agent import generate_reply
from intelligence import extract_intelligence
from callback import send_callback
import os

app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.post("/honeypot")
async def honeypot(
    request: Request,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    body = await request.json()

    session_id = body["sessionId"]
    msg = body["message"]
    sender = msg["sender"]
    text = msg["text"]

    add_message(session_id, sender, text)

    if is_scam(text):
        turn = get_turn_count(session_id)
        reply = generate_reply(turn)
        add_message(session_id, "user", reply)

        # Send callback only after meaningful engagement
        if turn >= 3:
            intelligence = extract_intelligence(text)
            send_callback(
                session_id,
                len(get_conversation(session_id)),
                intelligence
            )

        # 🔒 AUTOMATED TESTER RESPONSE (STRICT)
        return {
            "status": "success",
            "reply": reply
        }

    return {
        "status": "success",
        "reply": "Okay."
    }
