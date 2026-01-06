from app.models.db_config import engine, Base
from app.models.case_log import CaseLog

def init_db():
    Base.metadata.create_all(bind=engine)
