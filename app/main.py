from fastapi import FastAPI
from app.routes import user_routes, service_routes

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(service_routes.router, prefix="/services", tags=["Services"])

@app.get("/")
async def root():
    return {"message": "Welcome to ZETAONE!"}
