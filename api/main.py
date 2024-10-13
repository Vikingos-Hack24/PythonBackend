from fastapi import FastAPI
from api.endpoints.quiz import router as quiz_router

app = FastAPI()

# Incluye el router de quiz
app.include_router(quiz_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}