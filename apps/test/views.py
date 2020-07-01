from django.http import HttpResponse
from django.shortcuts import render
import pprint

def test(request):
    d = {}
    d["test"] = "test"
    d["my_list"] = ["fff","zzz","ddd"]
    return render(request, "test/test.html", d)

def hi(request, name):
    print(request)
    pprint.pprint(request.META)
    return HttpResponse(f"Hello {name}")