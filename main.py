from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from claude import claude_guess

app = FastAPI()

@app.get("/guess/{action}")
def guess(action: str):
    result = claude_guess(action)
    return {"guess": result}


@app.get("/explain/{action}")
def explain(action: str):
    return {
        "explanation": f"Claude thinks this action relates to common movie themes like {action}."
    }


@app.get("/chat")
def chat():
    return {"message": "Claude says: Hmm… interesting acting! 🤔"}



@app.get("/duel/{action}")
def duel(action: str):
    return {
        "Claude": claude_guess(action),
        "OpenAI": "Avengers"
    }