def parse_intent(text: str) -> dict:
    text = text.lower()

    company = None
    if "apple" in text:
        company = "Apple"
    elif "tesla" in text:
        company = "Tesla"
    elif "google" in text:
        company = "Google"

    if not company:
        raise ValueError("Company not detected")

    limit = 5
    for word in text.split():
        if word.isdigit():
            limit = int(word)

    return {
        "company": company,
        "limit": limit
    }
