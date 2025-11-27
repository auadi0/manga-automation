FROM python:3.10-slim
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0
RUN pip install --no-cache-dir paddleocr fastapi uvicorn pillow
COPY ocr_server.py /ocr_server.py
CMD ["uvicorn","ocr_server:app","--host","0.0.0.0","--port","8866","--workers","1"]
