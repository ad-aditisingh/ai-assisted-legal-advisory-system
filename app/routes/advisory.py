import json
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.nlp_service import extract_keywords
from app.services.legal_mapper import map_to_sections
from app.utils.response_formatter import format_response
from app.models.database import get_connection

router = APIRouter(prefix="/advisory", tags=["Legal Advisory"])

class IncidentInput(BaseModel):
    incident_text: str

@router.post("/")
def get_advisory(input: IncidentInput):
    keywords = extract_keywords(input.incident_text)
    matches = map_to_sections(keywords)
    response = format_response(matches)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO case_logs (incident_text, advisory_output) VALUES (?, ?)",
        (input.incident_text, json.dumps(response))
    )
    conn.commit()
    conn.close()

    return response
