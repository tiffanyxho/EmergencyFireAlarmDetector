import requests

""" not sure what these two lines below do
res = requests.get('htttp://localhost:9200')
print(res.content)
"""

see_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_see_fire", json = {"button_press": "yes_alarm_see_fire"})
no_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_no_fire", json = {"button_press": "yes_alarm_no_fire"})
no_alarm = requests.post("http://localhost:9200/button_press/button/no_alarm", json = {"button_press": "no_alarm"})
fire_drill = requests.post("http://localhost:9200/button_press/button/fire_drill", json = {"button_press": "fire_drill"})

get_see_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_see_fire")
see_fire_version = get_see_fire.json()["_version"]

get_no_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_no_fire")
see_no_fire = get_no_fire.json()["_version"]

get_no_alarm = requests.get("http://localhost:9200/button_press/button/no_alarm")
see_no_alarm = get_no_alarm.json()["_version"]

get_fire_drill = requests.get("http://localhost:9200/button_press/button/fire_drill")
see_fire_drill = get_fire_drill.json()["_version"]
