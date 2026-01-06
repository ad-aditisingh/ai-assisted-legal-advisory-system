from sqlalchemy import Column, Integer, String, Text, Index
from app.models.db_config import Base

class LegalProvision(Base):
    """
    Stores authoritative statutory provisions from the
    Bharatiya Nyaya Sanhita (BNS).

    This table is READ-ONLY after ingestion.
    The system does not modify or interpret this data.
    """

    __tablename__ = "legal_provisions"

    id = Column(Integer, primary_key=True, index=True)

    # Law identity
    law_code = Column(String(10), nullable=False)            # "BNS"
    section_number = Column(String(20), nullable=False)     # e.g. "103"
    section_title = Column(String(255), nullable=False)

    # Authoritative legal text (verbatim from official source)
    official_text = Column(Text, nullable=False)

    # Structural information
    chapter_number = Column(String(20), nullable=True)
    chapter_title = Column(String(255), nullable=True)

    # Classification for navigation (NOT legal authority)
    category = Column(String(100), nullable=False)

    # Source integrity
    source_reference = Column(String(255), nullable=False)

# -------------------------
# Indexing Strategy
# -------------------------

# Fast lookup by section number
Index("idx_bns_section_number", LegalProvision.section_number)

# Core navigation index (used by AI / keyword mapping)
Index("idx_bns_category", LegalProvision.category)

# Structural browsing support
Index("idx_bns_chapter_number", LegalProvision.chapter_number)
