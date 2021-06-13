FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="Tempuss"

COPY ./app /app
RUN chmod +x /app/prestart.sh
WORKDIR /app/

ENV PORT 8000

RUN pip install -r requirements.txt
