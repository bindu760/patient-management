from fastapi import FastAPI
from routers import patient

app = FastAPI(
    title="Patient Management API",
    description="A simple API to manage patient records",
    version="1.0.0"
)


# Register patient router
app.include_router(patient.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Patient Management API",
        "status": "Running"
    }