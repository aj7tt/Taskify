# Import necessary modules and packages
from fastapi import FastAPI, Header
from starlette.responses import RedirectResponse


# Import database-related modules
import app.models.model as models
from app.configs.dbConfig import Base, engine
 

# Import routing for API endpoints
from app.api.api import router as apiRouter
from app.service.auth import get_current_user_authorizer

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root URL to redirect to documentation
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/health")
def healthCheck():
    return { "status": "200 ok"}

@app.get("/token")
def VerifyToken(payload = Header(None)):
    return get_current_user_authorizer(payload)

# Create database tables based on model definitions
Base.metadata.create_all(bind=engine)

# Include the router for various API endpoints
app.include_router(apiRouter)
