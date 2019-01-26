import json

import requests  # http request


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(): # --> List all this out
    r  = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 404: # 404 for page not found, 200 for good sign
        print('Probably good sign ?')
    data = r.json()  # here data type is list
    #print(type(json.dumps(data)))  # print str, data type becomes str
    for obj in data:
        print('Harshhhhhhhh')
        print(obj['id'])
        print(type(obj))
        print(obj)
        if obj['id'] == 1: # --> User Interaction
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print('WOOOOOOOOOOW')
            print(r2)
            print(r2.json())

    return r.json()


def create_update():
    new_data = {
        'user': 1,
        #'content':"Some more cool content"
        'content': "Another more cool content"
    }

    #r = requests.post(BASE_URL + ENDPOINT, data=new_data) # Since we are creating so using post method
    #r = requests.delete(BASE_URL + ENDPOINT, data=new_data)  # Since we are deletinging so using delete method
    r = requests.post(BASE_URL + ENDPOINT  + '1' , data=json.dumps(new_data))  # Since we are creating so using post method

    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text


#print(get_list())

## WE CAN HAVE TEST IF SERVER IS RUNNING

#get_list()

#print(create_update())

def do_obj_update():
    new_data = {
        #'id': 1,
        #'content':"Some more cool content"
        'content': "New obj data"
    }
    # new_data = {
    #     'id': 1,
    #     #'content':"Some more cool content"
    #     'content': "Another more cool content"
    # }
    #r = requests.post(BASE_URL + ENDPOINT, data=new_data) # Since we are creating so using post method
    #r = requests.delete(BASE_URL + ENDPOINT, data=new_data)  # Since we are deletinging so using delete method
    r = requests.put(BASE_URL + ENDPOINT  + "1/" , data=json.dumps(new_data))  # ??????Since we are creating so using post method

    r = requests.put(BASE_URL + ENDPOINT + "1/",
                     data= new_data)
    print(r.headers)
    print(r.status_code)
    print('hasssssssssssssmmmtttt')
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text


print(do_obj_update())

def do_obj_delete():
    new_data = {
        'id': 1,
        #'content':"Some more cool content"
        'content': "New obj data"
    }
    # new_data = {
    #     'id': 1,
    #     #'content':"Some more cool content"
    #     'content': "Another more cool content"
    # }
    #r = requests.post(BASE_URL + ENDPOINT, data=new_data) # Since we are creating so using post method
    #r = requests.delete(BASE_URL + ENDPOINT, data=new_data)  # Since we are deletinging so using delete method
    r = requests.delete(BASE_URL + ENDPOINT  + '11' )  # Since we are deleting so no need to send any data

    print(r.headers)
    print(r.status_code)
    print('hasssssssssssssmmmtttt')
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text

#print(do_obj_delete())