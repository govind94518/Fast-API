from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None



@app.get("/")
def home():
    return [ 
                {
                    "place1":"Mathura",
                    "place2":"Kailash0"

                }
            ]

@app.get("/about")
def about():
    return {
            "govind":"Believe Yourself you can do it",
            "Jai Guru dev":"will help you",
            "Shiv":"in your heart"
        }

# inventory={
#     1:{
#         "name":"milk",
#         "price":"80",
#         "company":"amul"
#     }
# }
inventory={}
# @app.get("/get_item/{item_id}/{name}")
#  def get_item(item_id:int,name:str):
#      return inventory[item_id][name]

# @app.get("/get_item/{item_id}")
# def get_item(item_id:int):
#     return inventory[item_id]

# PATH PARAMETER 
@app.get("/get_item/{item_id}")
def get_item(item_id:int=Path(None,description="The ID of the item you like to view",gt=0)):
    return inventory[item_id]

#QUERY PARAMETER
#is to be given after the question marks (?test=1& str=govind)
# @app.get("/get-by-name")
# def get_item(*,name:Optional[str]=None,test:int):
#     for item_id in inventory:
#         if inventory[item_id]["name"]==name:
#             return inventory[item_id]["name"]
#     return {"Data":"Not Found"}
    
# combining Query Parameter and Path Parameter

# @app.get("/get-by-name/{item_id}")
# def get_item(*,item_id:int,name:Optional[str]=None,test:int):
#     for item_id in inventory:
#         if inventory[item_id].name == name:# if inventory[item_id]["name"]==name:
#             return inventory[item_id]
#     return {"Data":"Not Found"}
    
@app.get("/get-by-name")
def get_item(name:str):
    for item_id in inventory:
        if inventory[item_id].name==name:
            return inventory[item_id]
    return  {"Data":"Not Found"}


@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return {
            "Eroor":"Item_id is already exists."
        }
    # inventory[item_id]={"name":item.name,"brand":item.brand,"price":item.price}
    inventory[item_id]=item
    return inventory[item_id]

    
@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        return {"Eroor":"Item does  not Exist ."}

    if item.name!=None:
          inventory[item_id].name=item.name
    
    if item.price!=None:
          inventory[item_id].price=item.price
    
    if item.brand!=None:
          inventory[item_id].name=item.brand
    
    return inventory[item_id]

# @app.delete("/delete-item")
# def delete_item(item_id:int = Query(..., description("the id of the item to delete"),gt=0)):
#     if item_id not in inventory:
#         return {"Error":"Id does not exist"}
#     del inventory[item_id]
#     return {"Success":"Item deleted"}
