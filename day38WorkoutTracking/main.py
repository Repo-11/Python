import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
basic = HTTPBasicAuth('dylan1699', 'sheety_hello1699')

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 168
AGE = 23



APP_ID ="27da535d"
API_KEY ="a39213879bab416f64b2c868c451357e"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2658c77738c4c9f61f9f9e00fabef8f4/myWorkouts/workouts"
exercise_text = input("Tell me which exercise you did: ")

headers = {

    "x-app-id":APP_ID,
    "x-app-key":API_KEY,

}

parameters ={
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age":AGE

}



response = requests.post(exercise_endpoint, json=parameters, headers = headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise": exercise["name"].title(),
            "duration" :exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            "dylan1699",
            "sheety_hello1699",
        )

    )