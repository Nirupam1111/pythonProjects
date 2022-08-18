import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "90"
HEIGHT_CM = "180"
AGE = 19
APP_ID = '8e2f2486'
API_KEY = '3ecabfd55d462ba0e290ebf325845d71'
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


shetty_endpoint='https://api.sheety.co/6f932cb935bb5af9b4509e5d84644f2e/copyOfMyWorkoutTracking/workouts'
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime('%X')

headers = {
    'Authorization': 'Basic bmlydXBhbTpjdmJubUAxamhqNzg2Njdi'
}

for exercise in result['exercises']:
    body = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise':exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],

        }
    }
    response2 = requests.post(shetty_endpoint, json=body, headers=headers)
    print(response2.text)
