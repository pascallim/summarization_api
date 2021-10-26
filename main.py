from fastapi import FastAPI

from routers import documents

app = FastAPI()

# API Routes
app.include_router(documents.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Squirro's API coding challenge!"}
