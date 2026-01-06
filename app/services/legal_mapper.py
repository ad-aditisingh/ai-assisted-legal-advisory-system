import json

with open("data/bns_sections.json", "r") as file:
    BNS_SECTIONS = json.load(file)

def map_to_sections(keywords):
    results = []

    for section in BNS_SECTIONS:
        score = 0
        for kw in section["keywords"]:
            if kw in keywords:
                score += 1

        if score > 0:
            results.append({
                "section_number": section["section_number"],
                "title": section["title"],
                "description": section["description"],
                "confidence": score
            })

    return sorted(results, key=lambda x: x["confidence"], reverse=True)
