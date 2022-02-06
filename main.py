from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class Reservation(BaseModel):
    name: str
    time: int
    table_number: int


client = MongoClient('mongodb://localhost', 27017)
db = client["restaurants"]
collection = db["reservation"]
app = FastAPI()


# TODO complete all endpoint.
@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name: str):
    pass


@app.get("/reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    r = collection.find({"table_number": table}, {"_id": 0, "name": 1, "time": 1})
    my_result = []
    for i in r:
        my_result.append(i)
    return {
        "result": my_result
    }


@app.post("/reservation")
def reserve(reservation: Reservation):
    already_reservation = collection.find()
    for already in already_reservation:
        if reservation.table_number == already['table_number'] and reservation.time == already['time']:
            return {
                "result": "already reserved"
            }
    collection.insert_one(jsonable_encoder(reservation))
    return {
        "result": "Done"
    }


@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass


@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number: int):
    query = {"name": name, "table_number": table_number}
    collection.delete_many(query)
    return {
        "result": "done"
    }
