
def extract_highlights(text):
    lines = text.split(".")
    return [line.strip() for line in lines if "remember" in line.lower() or "note" in line.lower()]
