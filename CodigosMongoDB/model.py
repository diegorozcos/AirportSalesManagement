import uuid
from typing import Optional
from pydantic import BaseModel, Field
 
class Traveler(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    airline: str = Field(...)
    from_: str = Field(...)
    to_: str = Field(...)
    day: int = Field(...)
    month: int = Field(...)
    year: int = Field(...)
    age: int = Field(...)
    #gender: str = Field(...)
    reason: str = Field(...)
    stay: str = Field(...)
    #transit: str = Field(...)
    #connection: str = Field(...)
    #wait: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "airline": "Volaris",
                "from_": "GDL",
                "to_": "SJC",
                "day": 28,
                "month": 1,
                "year": 2014,
                "age": 12,
                "reason": "Back Home",
                "stay": "Home",
            }
        }

