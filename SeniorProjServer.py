import requests

""" not sure what these two lines below do
res = requests.get('htttp://localhost:9200')
print(res.content)
"""

see_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_see_fire", json = {"button_press": "yes_alarm_see_fire"})
no_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_no_fire", json = {"button_press": "yes_alarm_no_fire"})
no_alarm = requests.post("http://localhost:9200/button_press/button/no_alarm", json = {"button_press": "no_alarm"})
fire_drill = requests.post("http://localhost:9200/button_press/button/fire_drill", json = {"button_press": "fire_drill"})

