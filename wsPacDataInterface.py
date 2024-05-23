from fastapi import FastAPI
from pydantic import BaseModel


class WSResponse(BaseModel):
    code: int
    result: bool
    data: str
    message: str


class PackageInfo(BaseModel):
    ticketsNum: str
    weight: float
    lenght: float
    width: float
    height: float
    volumne: float
    workConsole: str
    extend: str


app = FastAPI()

@app.get("/")
async def root():
    return {"code": 1, "message": "Access prohibited"}


@app.post("/item/")
async def insert_item(newItem: PackageInfo) -> WSResponse:
    result = WSResponse
    
    result.code = 0
    result.result = True
    result.data = "1"
    result.message = ""

    return result


#http://localhost:8000/items/?skip=2&limit=1
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10) -> list[PackageInfo]:

    exampla_items = list[PackageInfo]
    exampla_items.add(
        {"ticketsNum": "0000000000000",
            "weight": 0.35,
            "volume": 1,
            "height": 0.5,
            "length": 0.5,
            "width": 0.5,
            "workConsole": "No. 1"})
    
    exampla_items.add(
        {"ticketsNum": "0000000000000",
            "weight": 1.15,
            "volume": 2.5,
            "height": 1,
            "length": 1,
            "width": 1,
            "workConsole": "No. 2"})
    
    exampla_items.add(
        {"ticketsNum": "0000000000000",
            "weight": 2.00,
            "volume": 2,
            "height": 1,
            "length": 2,
            "width": 1.5,
            "workConsole": "No. 1"})
    
    return exampla_items[skip: skip + limit]

