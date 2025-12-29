from fastapi import FastAPI
from app.modules.schools.router import router as schools_router

app = FastAPI(title="School Connect API")

app.include_router(schools_router)
