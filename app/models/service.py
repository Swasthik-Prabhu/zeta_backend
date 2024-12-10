from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Any


# class PyObjectId(ObjectId):
#     """Custom ObjectId type to handle serialization for Pydantic"""
#     @classmethod
#     def __get_pydantic_json_schema__(cls, core_schema, handler):
#         # Customizing the JSON schema to properly represent ObjectId
#         return {
#             "type": "string",
#             "pattern": "^[0-9a-fA-F]{24}$",
#         }







    
# Schema for creating a service
class ServiceCreate(BaseModel):
    name: str
    category: str  # e.g., "Electrical", "Plumbing", etc.
    description: str
    price: float
    availability: bool = True
    provider_id: str               #PyObjectId = Field(default_factory=PyObjectId)  # ID of the service 
    

# class Config:
#         arbitrary_types_allowed = True

# Schema for searching services
class ServiceSearch(BaseModel):
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    availability: Optional[bool] = None

# Schema for service responses
class ServiceResponse(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    category: str
    description: str
    price: float
    availability: bool
    provider_id: str

    class Config:
        orm_mode = True
