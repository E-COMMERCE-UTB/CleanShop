def cartEntity(cart) -> dict:
    return {
        "id_client": cart["id_client"],
        "total": sum([cart["items"][i]["cart_quantity"] * cart["items"][i]["price"] for i in range(len(cart["items"]))]),
        "items": [{
            "id_prod":cart["items"][i]["id_prod"],
            "name":cart["items"][i]["name"],
            "description":cart["items"][i]["description"],
            "type_prod":cart["items"][i]["type_prod"],
            "quantity":cart["items"][i]["quantity"],
            "price":cart["items"][i]["price"],
            "product_pic":cart["items"][i]["product_pic"],
            "cart_quantity":cart["items"][i]["cart_quantity"],
            "total_item":cart["items"][i]["cart_quantity"] * cart["items"][i]["price"],
        }for i in range(len(cart["items"]))],
    }

def cartsEntity(carts) -> list:
    return [cartEntity(cart) for cart in carts]