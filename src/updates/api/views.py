import json
from django.views.generic.base import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

from updates.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin

from updates.forms import UpdateModelForm

from .utils import is_json


#Creating, Updating, Deleting, Retriving (1) --Update Model

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    Retrive, Update, Delete --> because it one is an object
    """
    is_json = True

    def get_boject(self, id= None):
        #1st method
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None

        """
        Below handles a does not Exist Exception too
        """
    #2nd method

        qs = UpdateModel.objects.filter(id=id)
        print('dttttttttttttt')
        print(type(qs))
        if qs.count()==1:
            return qs.first()
        return None

    def get(self, request, id,  *arge, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *arge, **kwargs):
        data = {'message': 'Not allowed, please use the /api/updates/  endpoints. '}
        json_data = json.dumps(data)

        #return HttpResponse({}, content_type='application/json')
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *arge, **kwargs):
        obj  = self.get_boject(id=id)
        #obj = UpdateModel.objects.get(id=id)
        #obj = None

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        #print(dir(request))
        print(type(request.body))
        print('ggggggggggggg')
        # valid_json =  is_json(request.body)
        # if not valid_json:
        #     error_data = json.dumps({"message": "Invalid data sent, please send using JSON"})
        #     return self.render_to_response(error_data, status=400)

        #print(request.data)
        print('ddddddddllllg')
        # new_data = json.dumps(request.body)
        # print(new_data['content'])
        json_data = json.dumps({"message":"Something"})


        # return HttpResponse({}, content_type='application/json')
        return self.render_to_response(json_data, status=403)

    def delete(self, request, id, *arge, **kwargs):
        obj = self.get_boject(id=id)

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        json_data = {}

        # return HttpResponse({}, content_type='application/json')
        return self.render_to_response(json_data, status=403)




class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin, View):

    """
    List View
    Create View

    """
    is_json = True
    # def render_to_response(data,status=200):
    #     return HttpResponse(data, content_type='application/json', status_code=400)

    def get(self, request, *arge, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()

        #return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)


    def post(self, request, *arge, **kwargs):
        print('hhhhhhkkkkkkkkkkkk', request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message":"Not Allowed"}

        #data = json.dumps({"message":"Unknown data"})

        # return HttpResponse(data, content_type='application/json',status_code=400)
        return self.render_to_response(data,status=400)


    def delete(self, request, *arge, **kwargs):
        data = json.dumps({"message": "you can not delete an entire list"})
        status_code = 403 #Not Allowed
        #return HttpResponse(data, content_type='application/json')
        return self.render_to_response(data, status=403)






