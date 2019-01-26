import json
#from django.views.generic import View
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404

from status.models import Status

from status.api.slz import StatusSerializer

#from accounts.api.permissions import IsOwnerOrReadOnly


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid



#CreateModelMixin---->POST method
#UpdateModelMixin----> PUT method
#DestroyModelMixin---> DELETE


class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes          = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()
    lookup_field                = 'id'


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None



# Login required Mixin / decorator
class StatusAPIView(
    mixins.CreateModelMixin,
    # mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication] #Oauth, JWT
    serializer_class = StatusSerializer
    passed_id  = None

    #lookup_field = 'id' #'slug'

    def get_queryset(self):
        request = self.request
        #print('jjjjjjjjjjj', request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content_icontains=query)
        return qs

    def get_object(self, request, *args, **kwargs):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    # def get(self,request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     #print(request.body)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)



    def post(self,request, *args, **kwargs):
        return self.create(request,  *args, **kwargs)

    def put(self,request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        #print(request.body)
        print(request.data)
        requested_id = None # request.data.get('id')
        passed_id = url_passed_id or new_passed_id or requested_id or None
        self.passed_id = passed_id
        return self.update(request,  *args, **kwargs)

    def patch(self,request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        #print(request.body)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        return self.update(request,  *args, **kwargs)


    def delete(self,request, *args, **kwargs):
        #url_passed_id = request.GET.get('id', None)
        #json_data = {}
        body_ = str(request.body.decode("utf-8"))
        print('hhhhhhhhhhhhhhhhhhhhhhhooooooooooooooooooo',body_)
        if is_json(body_):
            json_data = json.loads(body_)
            print('GGGGOOOOODDDDD WWWOOORRRRKKKK')
        new_passed_id = json_data.get('id', None)
        print('CCCCOOOOOOLLLLLLLLLLL',new_passed_id)
        #print(request.body)
        #passed_id = url_passed_id or new_passed_id or None
        passed_id = new_passed_id
        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


























#CreateModelMixin---->POST method
#UpdateModelMixin----> PUT method
#DestroyModelMixin---> DELETE

# class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content_icontains=query)
#         return qs
#
#     def post(self,request, *args, **kwargs):
#         return self.create(request,  *args, **kwargs)
#
#
#
# class StatusAPIDetailView(mixins.DestroyModelMixin,mixins.UpdateModelMixin ,generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#
#     def put(self,request, *args, **kwargs):
#         return self.update(request,  *args, **kwargs)
#
#
#     # def patch(self,request, *args, **kwargs):
#     #     return self.update(request,  *args, **kwargs)
#
#
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(request,  *args, **kwargs)
#
#     def post(self,request, *args, **kwargs):
#         return self.create(request,  *args, **kwargs)
#


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#
#         return Response(serializer.data)



#
# class StatusAPIView(generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content_icontains=query)
#         return qs




# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# class StatusAPIDetailView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     #lookup_field = 'id' #'slug'
#     #Note will show only for those id which exist in database
#     #
#     # def get_object(self, *args, **kwargs):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)


# class StatusAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer





#
# class StatusAPIUpdateView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#
#
#
# class StatusAPIDeleteView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


###################################################################################################################
###################################################################################################################
# #from django.views.generic import View
# from rest_framework import generics, mixins
# from rest_framework.views import APIView
# from rest_framework.response import Response
# #from rest_framework.generics import ListAPIView
# from django.shortcuts import get_object_or_404
#
# from status.models import Status
#
# from status.api.slz import StatusSerializer
# import json
#
#
# # #CreateModelMixin---->POST method
# # #UpdateModelMixin----> PUT method
# # #DestroyModelMixin---> DELETE
#
#
# # def is_json(json_data):
# #     try:
# #         real_json = json.loads(json_data)
# #         is_valid = True
# #     except ValueError:
# #         is_valid = False
# #     return is_valid
# #
# #
# # class StatusAPIView(
# #     mixins.CreateModelMixin,
# #     mixins.RetrieveModelMixin,
# #     mixins.UpdateModelMixin,
# #     mixins.DestroyModelMixin,
# #     generics.ListAPIView):
# #
# #     permission_classes = []
# #     authentication_classes = []
# #     serializer_class = StatusSerializer
# #     lookup_field = 'id'  # 'slug'
# #     passed_id = None
# #
# #     def get_queryset(self):
# #         qs = Status.objects.all()
# #         query = self.request.GET.get('q')
# #         if query is not None:
# #             qs = qs.filter(content_icontains=query)
# #         return qs
# #
# #     def get_object(self):
# #         request = self.request
# #         passed_id = request.GET.get('id', None) or self.passed_id
# #         queryset = self.queryset()
# #         obj = None
# #         if passed_id is not None:
# #             obj = get_object_or_404(queryset, id = passed_id)
# #             self.check_object_permissions(request, obj)
# #
# #         return obj
# #
# #     def perform_destroy(self, instance):
# #         if instance is not None:
# #             return instance.delete()
# #         return None
# #
# #     def get(self, request , *args, **kwargs):
# #         url_passed_id = request.GET.get('id', None)
# #         json_data = {}
# #         body_ = request.body
# #         if is_json(body_):
# #             json_data = json.loads(request.body)
# #
# #         #passed_id = request.GET.get('id', None)
# #
# #         new_passed_id  = json_data.get('id', None)
# #         #print(request.body)
# #         #request.data
# #         #return self.get(request , *args, **kwargs)
# #         passed_id = url_passed_id or new_passed_id or None
# #         if passed_id is not None:# or passed_id is not "":
# #             return self.retrieve(request, *args, **kwargs)
# #         return super().get(request, *args, **kwargs)
# #
# #
# #
# #     def post(self,request, *args, **kwargs):
# #         return self.create(request,  *args, **kwargs)
# #
# #     def put(self,request, *args, **kwargs):
# #         url_passed_id = request.GET.get('id', None)
# #         json_data = {}
# #         body_ = request.body
# #         if is_json(body_):
# #             json_data = json.loads(request.body)
# #
# #         # passed_id = request.GET.get('id', None)
# #
# #         new_passed_id = json_data.get('id', None)
# #         # print(request.body)
# #         # request.data
# #         # return self.get(request , *args, **kwargs)
# #         passed_id = url_passed_id or new_passed_id or None
# #         if passed_id is not None:  # or passed_id is not "":
# #             return self.retrieve(request, *args, **kwargs)
# #         return super().get(request, *args, **kwargs)
# #
# #         return self.update(request,  *args, **kwargs)
# #
# #
# #     def patch(self,request, *args, **kwargs):
# #         url_passed_id = request.GET.get('id', None)
# #         json_data = {}
# #         body_ = request.body
# #         if is_json(body_):
# #             json_data = json.loads(request.body)
# #
# #         # passed_id = request.GET.get('id', None)
# #
# #         new_passed_id = json_data.get('id', None)
# #         # print(request.body)
# #         # request.data
# #         # return self.get(request , *args, **kwargs)
# #         passed_id = url_passed_id or new_passed_id or None
# #         if passed_id is not None:  # or passed_id is not "":
# #             return self.retrieve(request, *args, **kwargs)
# #         return super().get(request, *args, **kwargs)
# #
# #         return self.update(request,  *args, **kwargs)
# #
# #
# #     def delete(self,request, *args, **kwargs):
# #         url_passed_id = request.GET.get('id', None)
# #         json_data = {}
# #         body_ = request.body
# #         if is_json(body_):
# #             json_data = json.loads(request.body)
# #
# #         # passed_id = request.GET.get('id', None)
# #
# #         new_passed_id = json_data.get('id', None)
# #         # print(request.body)
# #         # request.data
# #         # return self.get(request , *args, **kwargs)
# #         passed_id = url_passed_id or new_passed_id or None
# #         if passed_id is not None:  # or passed_id is not "":
# #             return self.retrieve(request, *args, **kwargs)
# #         return super().get(request, *args, **kwargs)
# #
# #         return self.destroy(request,  *args, **kwargs)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # class StatusListSearchAPIView(APIView):
# #     permission_classes = []
# #     authentication_classes = []
# #
# #     def get(self, request, format=None):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #
# #         return Response(serializer.data)
# #
# #     def post(self, request, format=None):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #
# #         return Response(serializer.data)
# #
# #
# #
# # #
# # # class StatusAPIView(generics.ListAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     serializer_class = StatusSerializer
# # #
# # #     def get_queryset(self):
# # #         qs = Status.objects.all()
# # #         query = self.request.GET.get('q')
# # #         if query is not None:
# # #             qs = qs.filter(content_icontains=query)
# # #         return qs
# #
# #
# # #CreateModelMixin---->POST method
# # #UpdateModelMixin----> PUT method
# # #DestroyModelMixin---> DELETE
# #
# # # class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     serializer_class = StatusSerializer
# # #
# # #     def get_queryset(self):
# # #         qs = Status.objects.all()
# # #         query = self.request.GET.get('q')
# # #         if query is not None:
# # #             qs = qs.filter(content_icontains=query)
# # #         return qs
# # #
# # #     def post(self,request, *args, **kwargs):
# # #         return self.create(request,  *args, **kwargs)
# #
# #
# #
# #
# #
# # # class StatusCreateAPIView(generics.CreateAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
# # #
# # #     # def perform_create(self, serializer):
# # #     #     serializer.save(user=self.request.user)
# #
# # # class StatusCreateAPIView(generics.CreateAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
# # #
# # #     # def perform_create(self, serializer):
# # #     #     serializer.save(user=self.request.user)
# #
# #
# # # class StatusAPIDetailView(generics.RetrieveAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
# # #     #lookup_field = 'id' #'slug'
# # #     #Note will show only for those id which exist in database
# # #     #
# # #     # def get_object(self, *args, **kwargs):
# # #     #     kwargs = self.kwargs
# # #     #     kw_id = kwargs.get('id')
# # #     #     return Status.objects.get(id=kw_id)
# #
# #
# # # class StatusAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
# #
# #
# #
# # class StatusAPIDetailView(mixins.DestroyModelMixin,mixins.UpdateModelMixin ,generics.RetrieveAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerializer
# #
# #
# #     def put(self,request, *args, **kwargs):
# #         return self.update(request,  *args, **kwargs)
# #
# #
# #     def patch(self,request, *args, **kwargs):
# #         return self.update(request,  *args, **kwargs)
# #
# #
# #     def delete(self,request, *args, **kwargs):
# #         return self.destroy(request,  *args, **kwargs)
# #
# #     # def post(self,request, *args, **kwargs):
# #     #     return self.create(request,  *args, **kwargs)
# #
# # #
# # # class StatusAPIUpdateView(generics.UpdateAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
# # #
# # #
# # #
# # #
# # # class StatusAPIDeleteView(generics.DestroyAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer