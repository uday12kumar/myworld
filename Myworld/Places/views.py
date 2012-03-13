import json
from django.http import HttpResponse

def home(request):
    hello = json.dumps("hello")
    return HttpResponse(hello,mimetype="application/json")
