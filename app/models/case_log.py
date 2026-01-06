from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime

from app.models.db_config import Base

class CaseLog(Base):
    __tablename__ = "case_logs"

    id = Column(Integer, primary_key=True, index=True)
    incident_text = Column(Text, nullable=False)
    advisory_output = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
