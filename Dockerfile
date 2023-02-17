FROM python:3.10-alpine

RUN pip install fastapi uvicorn starlette-prometheus


COPY main.py .
CMD ["uvicorn","main:app","--host","0.0.0.0"]