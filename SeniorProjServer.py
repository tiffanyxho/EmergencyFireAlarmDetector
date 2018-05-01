import requests

""" not sure what these two lines below do
res = requests.get('htttp://localhost:9200')
print(res.content)
"""

see_fire = requests.post("http://localhost:9200/buttonPress/button/yesAlarmSeeFire"), json = {"buttonPress": "yesAlarmSeeFire"}
no_fire = requests.post("http://localhost:9200/buttonPress/button/yesAlarmNoFire"), json = {"buttonPress": "yesAlarmNoFire"}
no_alarm = requests.post("http://localhost:9200/buttonPress/button/noAlarm"), json = {"buttonPress": "noAlarm"}
fire_drill = requests.post("http://localhost:9200/buttonPress/button/fireDrill"), json = {"buttonPress": "fireDrill"}

