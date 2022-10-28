from django.http.response import JsonResponse

def home(request):
     return JsonResponse({"server":"running successfully"}, safe = False)