SCAM_KEYWORDS = [
    "blocked", "verify", "urgent", "account",
    "upi", "bank", "suspended", "immediately"
]

def is_scam(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in SCAM_KEYWORDS)
