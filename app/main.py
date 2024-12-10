from fastapi import FastAPI
from app.routes import user_routes, service_routes, appointments_routes

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(service_routes.router, prefix="/services", tags=["Services"])


# app.include_router(providers.router, prefix="/api/v1", tags=["Providers"])
# app.include_router(customers.router, prefix="/api/v1", tags=["Customers"])
app.include_router(appointments_routes.router, prefix="/api/v1", tags=["Appointments"])

@app.get("/")
async def root():
    return {"message": "Welcome to ZETAONE!"}
