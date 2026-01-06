from app.models.db_config import engine, Base
from app.models.case_log import CaseLog
from app.models.legal_provision import LegalProvision

def init_db():
    """
    Initializes all database tables.
    This includes:
    - Case logs (dynamic)
    - Legal provisions (authoritative, read-only)
    """
    Base.metadata.create_all(bind=engine)
