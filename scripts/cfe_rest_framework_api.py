import json
import requests
import os

# def is_json(json_data):
#     try:
#         real_json = json.loads(json_data)
#         is_valid = True
#     except ValueError:
#         is_valid = False
#     return is_valid

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = 'http://127.0.0.1:8000/api/status/'

image_path = os.path.join(os.getcwd(),"flower.jpg")

#
headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'harsh',
    'password': 'sudhansu'
}


# r = requests.post(AUTH_ENDPOINT, data=data)
#print(r.json())
#
# token = r.json()['token']

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print('token is :',token)
#
#
# print('old_token is :',token)
# refresh_data = {
#     'token': token
# }
#
#
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']
#
# print('new_token is :',new_token)


headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT" + token,
}

post_data = json.dumps({"content": "Some random content"})
posted_response = requests.post(ENDPOINT, data=post_data, headers=headers)
print((posted_response.text))


# get_endpoint = ENDPOINT + str(22)
# post_data = json.dumps({"content": "Some random content"})
#
# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(get_endpoint)
# print(r2.status_code)
#
# post_header = {
#     'content-type':'application/json'
# }
#
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_header)
#
# print(post_response.text)
#
#



# def do_img(method='get', data = {}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if image_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image':image
#             }
#
#             r = requests.request(method, ENDPOINT, data=data, files = file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
# def do(method='get', data = {}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT , data = data)
#     print(r.text)
#     print(r.status_code)
#     return r


# do(data = {'id': 20})


#do(method='delete', data = {"id": 22, 'content':'yyggg'})
# do(method='put', data = {'id': 20, "content":"Some cool hhhhhhcdss new content", 'user':1})
# do(method='post', data = {"content":"Some cool hhhhhhcdss new content"})


#do_img(method='post', data={'user':1, 'content':""}, is_json=False, image_path=image_path)