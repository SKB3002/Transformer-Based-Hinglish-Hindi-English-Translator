from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import hinglish_to_english

app = FastAPI(title="Hinglish → Hindi → English Translator")

class InputText(BaseModel):
    text: str

@app.post("/translate")
def translate(input: InputText):
    result = hinglish_to_english(input.text)
    return result
