from fastapi import FastAPI
from routers import api_router

app = FastAPI(
    title="SDRCloud FastAPI Application",
    description="A FastAPI project with modular design for scalable applications.",
    version="1.0.0",
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Retail Admin API is running"}


@app.on_event("startup")
async def startup_event():
    print("Application has started successfully!")


@app.on_event("shutdown")
async def shutdown_event():
    print("Application is shutting down!")
