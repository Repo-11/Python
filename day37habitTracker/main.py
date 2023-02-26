import requests
from datetime import datetime


USERNAME = "saanclay"
TOKEN = "afj3dl5a8jad9osh3lj3k4k3n4"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":"afj3dl5a8jad9osh3lj3k4k3n4",
    "username":"saanclay",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime(year=2022,month=8, day = 4)
pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity" :"15.6"


}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220804"
pixel_update ={
    "quantity":"9.6"
}
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220804"


response = requests.put(url = pixel_update_endpoint,json = pixel_update ,headers=headers )
print(response.text)
