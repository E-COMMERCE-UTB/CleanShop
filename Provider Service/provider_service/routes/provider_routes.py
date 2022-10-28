from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.provider_schema import providersEntity
from ..models.models import Provider, Product
from bson import ObjectId

provider = APIRouter()



#get methods
@provider.get('/providers')
async def get_providers():
    providers = providersEntity(collection_name.find())
    return {"status":"ok", "data": providers}


@provider.get('/provider/{id}')
async def get_provider_by_id(id: str):
    provider = providersEntity(collection_name.find({'_id':ObjectId(id)}))
    return {"status":"ok", "data": provider}

#post method
@provider.post('/provider')
async def add_provider(name:str):
    providerObj = Provider(name=name, items=[])
    _id = collection_name.insert_one(dict(providerObj))
    provider = providersEntity(collection_name.find({'_id':_id.inserted_id}))
    return {"status":"ok", "data": provider}

#put methods
@provider.put('/provider/add_product/{id}')
async def add_product_to_provider(id:str):
    product_ex = Product(id_prod= 2, name="Mop", description="Something", type_prod="M", quantity=40, price=40000)

    collection_name.update_many({'_id':ObjectId(id)}, { "$push": {"items":dict(product_ex)} }, upsert = True)

    provider = providersEntity(collection_name.find({'_id':ObjectId(id)}))
    return {"status":"ok", "data": provider}

@provider.put('/provider/remove_product/{id}/{id_prod}')
async def remove_product_from_provider(id:str, id_prod:int):

    collection_name.update_many({'_id':ObjectId(id)}, { "$pull": { "items":{ "id_prod":id_prod } } }, upsert = True)

    provider = providersEntity(collection_name.find({'_id':ObjectId(id)}))
    return {"status":"ok", "data": provider}

@provider.put('/provider/{id}')
async def change_name_provider(name:str, id: str):
    
    collection_name.find_one_and_update({'_id':ObjectId(id)}, { "$set": {"name" : name }})

    provider = providersEntity(collection_name.find({'_id':ObjectId(id)}))
    return {"status":"ok", "data": provider}

@provider.delete('/provider_delete/{id}')
async def delete_provider(id:str):
    collection_name.find_one_and_delete({'_id':ObjectId(id)})
    
    return {"status":"ok", "data": []}



