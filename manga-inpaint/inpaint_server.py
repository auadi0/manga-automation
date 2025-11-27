from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid, io, os, subprocess

app = FastAPI()

@app.post("/inpaint")
async def inpaint(image: UploadFile = File(...), mask: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    image_path = f"/tmp/{uid}_image.png"
    mask_path = f"/tmp/{uid}_mask.png"
    out_path = f"/tmp/{uid}_out.png"
    with open(image_path, "wb") as f:
        f.write(await image.read())
    with open(mask_path, "wb") as f:
        f.write(await mask.read())
    # افتراضيًا نعيد الصورة نفسها إذا لم يكن inpaint محملاً (تسهيل الاختبار)
    # لو جهّزت LaMa داخل الحاوية، غيّر السطر التالي لينفّذ سكربت inpaint الفعلي
    subprocess.run(["cp", image_path, out_path])
    return FileResponse(out_path, media_type="image/png")
