FROM python:3.9.5-slim-buster

RUN apt update && apt upgrade -y && apt clean

COPY src/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY src/ /app/

CMD ["streamlit", "run", "/app/main.py", "--server.port", "8501", "--server.maxUploadSize", "1"]