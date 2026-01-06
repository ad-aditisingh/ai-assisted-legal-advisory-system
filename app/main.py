from fastapi import FastAPI
from app.routes.advisory import router as advisory_router
from app.models.database import init_db

app = FastAPI(
    title="AI-Assisted Legal Advisory System",
    description="Advisory-only legal decision support under BNS",
    version="1.0"
)

init_db()
app.include_router(advisory_router)

@app.get("/")
def root():
    return {
        "message": "Legal Advisory System is running",
        "disclaimer": "This system provides informational content only."
    }
