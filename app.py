from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# Tank model (POST)
class Tank(BaseModel):
    location: str
    lat: float
    long: float

# Tank (PATCH) for optional fields
class UpdateTank(BaseModel):
    location: Optional[str] = None
    lat: Optional[float] = None
    long: Optional[float] = None

tanks = []

# GET all tanks
@app.get("/tank", response_model=List[dict])
def get_tanks():
    return tanks

# GET single tank by ID
@app.get("/tank/{id}")
def get_tank(id: str):
    tank = next((t for t in tanks if t["id"] == id), None)
    if tank is None:
        raise HTTPException(status_code=404, detail="Tank not found")
    return tank

# POST create a new tank
@app.post("/tank", response_model=dict, status_code=201)
def create_tank(tank: Tank):
    new_tank = {
        "id": str(uuid.uuid4()),
        "location": tank.location,
        "lat": str(tank.lat),
        "long": str(tank.long)
    }
    tanks.append(new_tank)
    return new_tank

# PATCH update tank (now allows partial updates)
@app.patch("/tank/{id}")
def update_tank(id: str, updated_tank: UpdateTank):
    for tank in tanks:
        if tank["id"] == id:
            if updated_tank.location is not None:
                tank["location"] = updated_tank.location
            if updated_tank.lat is not None:
                tank["lat"] = str(updated_tank.lat)
            if updated_tank.long is not None:
                tank["long"] = str(updated_tank.long)
            return tank
    raise HTTPException(status_code=404, detail="Tank not found")

# DELETE tank
@app.delete("/tank/{id}", status_code=204)
def delete_tank(id: str):
    global tanks
    tanks = [tank for tank in tanks if tank["id"] != id]
    return  # No response body
