import re

def extract_keywords(text: str):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    return list(set(words))
