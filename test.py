import requests
url ="http://localhost:8000"

userdata={
    "sepal_length": 5.0,
    "sepal_width": 3.6,
    "petal_length": 1.4,
    "petal_width": 0.2
}
ans = requests.post(url,json=userdata)
print(ans.text)