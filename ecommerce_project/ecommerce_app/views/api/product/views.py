from django.http import JsonResponse
import json
from ecommerce_app.models import Product

def productsData(request):
    productIds = json.loads(request.GET.get("productIds"))
    productsData = Product.objects.filter(id__in=productIds)
    response = []
    for product in productsData:
        response.append({
            'id': product.id,
            'title': product.title,
            'price': str(product.price),
            'imageUrl': product.image.url,
            
        })
    return JsonResponse({
        "status": "success",
        "code": 200,
        "response": json.dumps(response)
    })
