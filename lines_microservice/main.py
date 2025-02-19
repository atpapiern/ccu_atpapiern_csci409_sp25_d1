from fastapi import FastAPI
import requests

API_KEY = "be5ec94292c64bfabc8ae27290df855c"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

@app.get("/lines")
def get_lines():
    lines_list = list()
    response = requests.get(ENDPOINT_URL + f"/lines?&api_key={API_KEY}")
    lines = response.json()["data"]
    for line in lines:
        lines_list.append({
            "id": line["id"],
            "text_color": line["attributes"]["text_color"],
            "short_name": line["attributes"]["short_name"],
            "long_name": line["attributes"]["long_name"],
            "color": line["attributes"]["color"],
        })
    return {"lines": lines_list}

@app.get("/lines/{line_id}")
def get_line(line_id: str):
    response = requests.get(ENDPOINT_URL + f"/lines/{line_id}?api_key={API_KEY}")
    line_data = response.json()["data"]
    line = {
        "id": line_data["id"],
        "text_color": line_data["attributes"]["text_color"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
    }
    return {"lines": line}