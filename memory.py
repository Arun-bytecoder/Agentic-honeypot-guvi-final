from collections import defaultdict

conversation_store = defaultdict(list)

def add_message(session_id, sender, text):
    conversation_store[session_id].append({
        "sender": sender,
        "text": text
    })

def get_turn_count(session_id):
    return len(conversation_store[session_id])

def get_conversation(session_id):
    return conversation_store[session_id]
