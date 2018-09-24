from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

@csrf_exempt 
def asset(request):
    if request.method == 'POST:
    # print(request.POST)
    # print(request.GET)
        print(request.body)
        host_info = json.loads(str(request.body, encoding='utf-8'))
        print(host_info)
    return HttpResponse('....')