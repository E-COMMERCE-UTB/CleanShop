from pydantic import BaseModel
from typing import Union, List

class Product(BaseModel):
    id_prod:int
    name:str
    description:str
    type_prod:str
    quantity:int
    price:int

    

class Provider(BaseModel):
    name:str
    items:Union[List[Product], None] = None