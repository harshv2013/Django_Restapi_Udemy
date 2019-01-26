import json # from python library

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.generic import View


#def detail_view(request):
    #return render(request, template, {})# return JSON data --> JS Object Notation
    #return HttpResponse(get_template().render({}))

from .mixins import JsonResponseMixin
# from ..cfeapi.mixins import JsonResponseMixin
from .models import Update


def json_example_view(request):
    """
    URI -- Uniform Resource Locator--> for a REST API
    GET --Retrive (all we are using here)
    """
    data = {
        "count":1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data) # old method to dump JSON
    #return JsonResponse(data) # dictionary can be directly
                               # converted into JSON using Jsonresponce
                               #Newly introduced in Django
    return HttpResponse(json_data, content_type='application/json')

## We want to convert above example in class based voew

class JsonCBV(View):
    def get(self,request, *args, **kwargs):

        """
        URI -- for a REST API
        GET --Retrive
        """
        data = {
            "count":1000,
            "content": "Some new content"
        }
        json_data = json.dumps(data) # old method to dump JSON
        return JsonResponse(data)
        #return HttpResponse(json_data, content_type='application/json')





class JsonCBV2(JsonResponseMixin,View):
    def get(self,request, *args, **kwargs):

        data = {
            "count":1000,
            "content": "Some new content"
        }
        #return JsonResponse(data)
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self,request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # data = serialize('json', [obj,], fields= ('user','content'))

        # data = {
        #     "count":1000,
        #     "content": "Some new content"
        # }
        # json_data = json.dumps(data)  ## one of the method of Python Inbuilt Json
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self,request, *args, **kwargs): # In class based view we write like this see _
        #                                     # _> https://docs.djangoproject.com/en/2.1/topics/class-based-views/intro/
        # qs = Update.objects.all()
        # data = serialize('json',qs, fields=('user', 'content'))
        # json_data = data

        json_data = Update.objects.all().serialize() # will give serialize version of queryset
        return HttpResponse(json_data, content_type='application/json')


