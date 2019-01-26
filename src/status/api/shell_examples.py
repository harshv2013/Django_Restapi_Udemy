
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from status.api.slz import StatusSerializer
from status.models import Status


'''
Serialize a single object
'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serialize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)



'''
Create obj
'''
data = {'user':1}
sl = StatusSerializer(data = data)  # sl for serializer
sl.is_valid()
sl.save()

if sl.is_valid():
    sl.save()

'''
Update obj
'''
obj = Status.objects.first()
data = {'content': 'some new content3', 'user':1}
update_sl = StatusSerializer(obj, data=data)
update_sl.is_valid()
update_sl.save()


'''
Delete Obj
'''
#first create an object
data = {'user':1, 'content':'please delete me'}
create_obj_sl = StatusSerializer(data = data)
create_obj_sl.is_valid()

create_obj=create_obj_sl.save() # instance of object
print(create_obj)


obj = Status.objects.last()
get_data_sl = StatusSerializer(obj)
# update_sl = StatusSerializer(obj, data=data)
# update_sl.is_valid()
# update_sl.save()
#print(get_data_sl.data)

print(obj.delete)

#####################################################

from rest_framework import serializers
class CustomSerializer(serializers.Serializer):
    content =      serializers.CharField()
    email       =  serializers.EmailField()


data = {'email': 'hello@teamcfe.com', 'content': "please delete me"}
create_obj_serializer = CustomSerializer(data=data)
if create_obj_serializer.is_valid():
    valid_data = create_obj_serializer.data
    print(valid_data)


