import json
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.nlp_service import extract_keywords
from app.services.legal_mapper import map_to_sections
from app.utils.response_formatter import format_response

from app.models.db_config import SessionLocal
from app.models.case_log import CaseLog

router = APIRouter(prefix="/advisory", tags=["Legal Advisory"])

class IncidentInput(BaseModel):
    incident_text: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def get_advisory(input: IncidentInput, db: Session = Depends(get_db)):
    keywords = extract_keywords(input.incident_text)
    matches = map_to_sections(keywords)
    response = format_response(matches)

    log = CaseLog(
        incident_text=input.incident_text,
        advisory_output=json.dumps(response)
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return response
