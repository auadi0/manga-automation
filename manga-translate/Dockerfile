FROM python:3.10-slim
RUN apt-get update
RUN pip install --no-cache-dir transformers torch sentencepiece fastapi uvicorn
COPY translate_server.py /translate_server.py
CMD ["uvicorn","translate_server:app","--host","0.0.0.0","--port","7000","--workers","1"]
