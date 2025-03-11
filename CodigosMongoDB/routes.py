from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson import ObjectId
 
from model import Traveler

router = APIRouter()


@router.get("/", response_description="Get the reasons or the stays", response_model=List)
def list_reasons(request: Request, option: str):
    if option == "reasons":
      group = [
            { "$match": { "reason": "Business/Work" } },
            { "$group": { "_id": { "day": "$day", "month": "$month" }, "count": { "$sum": 1 }, "from_": { "$first": "$from_" } } },
            { "$group": { "_id": "$_id.month", "totalPersons": { "$sum": "$count" }, "airport": { "$first": "$from_" } } },
            { "$addFields": { "num_month": "$_id" } },
            { "$project": { "_id": 0, "airport": "$airport", "totalPersons": 1, "num_month": 1 } },
            { "$sort": { "totalPersons": -1 } }
        ]    
    elif option == "stays":
         group = [
            { "$match": { "stay": "Hotel" } },
            { "$group": { "_id": { "day": "$day", "month": "$month" }, "count": { "$sum": 1 }, "from_": { "$first": "$from_" } } },
            { "$group": { "_id": "$_id.month", "totalPersons": { "$sum": "$count" }, "airport": { "$first": "$from_" } } },
            { "$addFields": { "num_month": "$_id" } },
            { "$project": { "_id": 0, "airport": "$airport", "totalPersons": 1, "num_month": 1 } },
            { "$sort": { "totalPersons": -1 } }
        ]
   
    pipeline = list(request.app.database["travelers"].aggregate(group))
    return pipeline

@router.post("/", response_description="New traveler added", status_code=status.HTTP_201_CREATED, response_model=Traveler)
def create_traveler(request: Request, traveler: Traveler = Body(...)):
    traveler = jsonable_encoder(traveler)
    new_traveler = request.app.database["travelers"].insert_one(traveler)
    created_traveler = request.app.database["travelers"].find_one(
        {"_id": new_traveler.inserted_id}
    )
    return created_traveler


