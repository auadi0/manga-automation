from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

app = FastAPI()
MODEL = "Helsinki-NLP/opus-mt-en-ar"  # إنجليزي→عربي، غيّر إذا احتجت زوج لغات آخر
tokenizer = MarianTokenizer.from_pretrained(MODEL)
model = MarianMTModel.from_pretrained(MODEL)

class Req(BaseModel):
    text: str

@app.post("/translate")
def translate(req: Req):
    tokens = tokenizer([req.text], return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    out = tokenizer.decode(translated[0], skip_special_tokens=True)
    return {"translated": out}
