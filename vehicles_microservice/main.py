from fastapi import FastAPI, Depends
import httpx

API_KEY = "be5ec94292c64bfabc8ae27290df855c"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

async def get_all_vehicles(route: str = None, revenue: str = None):
    params = {}
    if route:
        params["filter[route]"] = route
    if revenue:
        params["filter[revenue]"] = revenue

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles", params=params)
        response.raise_for_status()
        return response.json()

@app.get("/vehicles")
async def read_vehicles(route: str = None, stop: str = None, vehicles=Depends(get_all_vehicles)):
    return vehicles

async def get_vehicle_by_id(vehicle_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{vehicle_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@app.get("/vehicles/{vehicle_id}")
async def read_vehicle(vehicle_id: str, vehicle=Depends(get_vehicle_by_id)):
    return vehicle