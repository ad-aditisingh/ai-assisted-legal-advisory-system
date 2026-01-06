DISCLAIMER = (
    "This is an informational and advisory reference only. "
    "It does not constitute legal advice. "
    "Actual applicability depends on investigation and judicial interpretation. "
    "Consult a qualified legal professional."
)

def format_response(matches):
    if not matches:
        return {
            "message": "No applicable legal sections identified based on the input.",
            "disclaimer": DISCLAIMER
        }

    advisory_results = []
    for match in matches:
        advisory_results.append({
            "section": match["section_number"],
            "title": match["title"],
            "explanation": match["description"],
            "note": "This section may apply based on commonly observed legal interpretations."
        })

    return {
        "advisory_results": advisory_results,
        "disclaimer": DISCLAIMER
    }
