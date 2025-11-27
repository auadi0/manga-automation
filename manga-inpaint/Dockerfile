FROM python:3.10-slim
RUN apt-get update && apt-get install -y git ffmpeg
RUN pip install --no-cache-dir fastapi uvicorn pillow
COPY inpaint_server.py /inpaint_server.py
# في حال أردت تضمين LaMa كاملاً يجب إضافته هنا أو سحب repo LaMa داخل Dockerfile
CMD ["uvicorn","inpaint_server:app","--host","0.0.0.0","--port","5000","--workers","1"]
