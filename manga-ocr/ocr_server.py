from fastapi import FastAPI, UploadFile, File
from paddleocr import PaddleOCR
from PIL import Image
import io
import base64

app = FastAPI()
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # اضبط اللغات لاحقًا إذا احتجت

@app.post("/ocr")
async def run_ocr(file: UploadFile = File(...)):
    data = await file.read()
    img = Image.open(io.BytesIO(data)).convert("RGB")
    result = ocr.ocr(img, cls=True)
    out = []
    for line in result:
        box = line[0]
        text = line[1][0]
        xs = [int(p[0]) for p in box]
        ys = [int(p[1]) for p in box]
        x1,y1,x2,y2 = min(xs), min(ys), max(xs), max(ys)
        out.append({"box":[x1,y1,x2,y2],"text":text})
    return {"result": out}
