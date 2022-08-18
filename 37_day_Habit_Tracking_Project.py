import requests
from datetime import datetime

USERNAME="nirupam"
TOKEN="hgiuyui67khgvk7"
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Reading Graph",
    "unit":"hour",
    "type":"float",
    "color":"ajisai",
}
headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

today=datetime.now()
# print(today.strftime('%Y%m%d'))
pixel_config={
    "date":today.strftime('%Y%m%d'),
    "quantity":input("How many hours did you read today?"),
}
pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

response=requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)
print(response.text)

update_config={
    "quantity": "12.0",
}
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20211124"

# response=requests.put(url=update_endpoint, json=update_config,headers=headers)
# print(response.text)


delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20211124"

# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)
