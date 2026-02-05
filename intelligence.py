import re

def extract_intelligence(text: str):
    return {
        "bankAccounts": re.findall(r"\b\d{4}-\d{4}-\d{4}\b", text),
        "upiIds": re.findall(r"\b[\w.-]+@[\w.-]+\b", text),
        "phoneNumbers": re.findall(r"\+91\d{10}", text),
        "phishingLinks": re.findall(r"https?://\S+", text),
        "suspiciousKeywords": []
    }
