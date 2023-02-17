from fastapi import FastAPI
# from starlette.applications import Starlette
from starlette_prometheus import metrics, PrometheusMiddleware

app=FastAPI()

@app.get('/')
def home():
    return {"message":"hello-world"}

app.add_middleware(PrometheusMiddleware)
# app.add_route("/metrics/", metrics)