from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ADK Agent is running 🚀"}

@app.get("/agent")
def agent(query: str):
    return {
        "input": query,
        "response": f"Hello! You said: {query}"
    }