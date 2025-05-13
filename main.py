from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

@app.get("/hardware")
async def read_root():
    # Read the JSON file
    json_path = Path(__file__).parent / "data.json"
    with open(json_path) as f:
        data = json.load(f)
    return data 