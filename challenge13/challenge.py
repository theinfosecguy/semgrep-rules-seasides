from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

subprocess.run(command, shell=True)

@app.post("/unsafe_subprocess")
async def unsafe_subprocess(request: Request):
    user_input = await request.json()
    command = user_input + "la"
    subprocess.run(command, shell=True)