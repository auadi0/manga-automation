FROM python:3.10-slim
RUN apt-get update && apt-get install -y fonts-dejavu-core
RUN pip install --no-cache-dir pillow flask arabic-reshaper python-bidi
COPY server.py /server.py
CMD ["python","/server.py"]
