def providerEntity(provider) -> dict:
    return {
        "id": str(provider["_id"]),
        "name": provider["name"],
        "items": [{
            "id_prod":provider["items"][i]["id_prod"],
            "name":provider["items"][i]["name"],
            "description":provider["items"][i]["description"],
            "type_prod":provider["items"][i]["type_prod"],
            "quantity":provider["items"][i]["quantity"],
            "price":provider["items"][i]["price"],
        }for i in range(len(provider["items"]))],
    }

def providersEntity(providers) -> list:
    return [providerEntity(provider) for provider in providers]