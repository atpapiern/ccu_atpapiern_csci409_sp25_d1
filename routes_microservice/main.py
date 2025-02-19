from fastapi import FastAPI
import requests

API_KEY = "be5ec94292c64bfabc8ae27290df855c"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

@app.get("/routes")
def get_routes():
    routes_list = list()
    response = requests.get(ENDPOINT_URL + f"/routes?&api_key={API_KEY}")
    routes = response.json()["data"]
    for route in routes:
        routes_list.append({
            "id": route["id"],
            "type": route["type"],
            "color": route["attributes"]["color"],
            "text_color": route["attributes"]["text_color"],
            "description": route["attributes"]["description"],
            "long_name": route["attributes"]["long_name"],
            "type": route["attributes"]["type"],
        })
    return {"routes": routes_list}

@app.get("/routes/{route_id}")
def get_route(route_id: str):
    response = requests.get(ENDPOINT_URL + f"/routes/{route_id}?api_key={API_KEY}")
    route_data = response.json()["data"]
    route = {
        "id": route_data["id"],
        "type": route_data["type"],
        "color": route_data["attributes"]["color"],
        "text_color": route_data["attributes"]["text_color"],
        "description": route_data["attributes"]["description"],
        "long_name": route_data["attributes"]["long_name"],
        "type": route_data["attributes"]["type"],
    }
    return {"routes": route}