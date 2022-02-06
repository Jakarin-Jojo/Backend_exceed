from msilib.schema import tables
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import uvicorn


class Reservation(BaseModel):
    name : str
    time: int
    table_number: int
    
client = MongoClient('mongodb://localhost', 27017)

db = client["restaurants"]


collection = db["reservation"]

app = FastAPI()




@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    result = collection.find_one({"name": name}, {"_id":0, "time":1, "table_number": 1})
    if result != None:
        return {
            "result": result 
        }
    else:
        raise HTTPException(404, f"I can't find anyone who reserved this name.")

@app.get("reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    pass

@app.post("/reservation")
def reserve(reservation : Reservation):
    pass

@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    pass