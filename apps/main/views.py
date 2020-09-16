import json
import datetime
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse


def hello(request):
    data = {'hello': '1'}
    
    return JsonResponse(data)
