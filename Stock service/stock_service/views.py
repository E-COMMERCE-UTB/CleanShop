from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(id=id)
            product_serilizer = ProductSerializer(product, many=True)
            return JsonResponse(product_serilizer.data[0], safe=False)
        else:
            products = Product.objects.all()
            product_serilizer = ProductSerializer(products, many=True)
            return JsonResponse(product_serilizer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serilizer = ProductSerializer(data=product_data)
        if product_serilizer.is_valid():
            product_serilizer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=product_data['id'])
        product_serilizer = ProductSerializer(product, data=product_data)
        if product_serilizer.is_valid():
            product_serilizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False)

