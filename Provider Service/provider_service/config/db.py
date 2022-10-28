from pymongo import MongoClient
import certifi

client = MongoClient("mongodb+srv://david:TyuI1705$@cluster0.qqb9bkj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db = client.provider_db

collection_name = db["provider_app"]