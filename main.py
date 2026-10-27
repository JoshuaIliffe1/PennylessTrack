import subprocess

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/calc")
def calc(expr: str):
    return {"result": eval(expr)}


@app.get("/ping")
def ping(host: str):
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return {"output": result.stdout.decode()}
