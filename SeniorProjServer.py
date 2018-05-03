import requests
import json
from flask import Flask
# server
app = Flask(__name__)

""" not sure what these two lines below do
res = requests.get('htttp://localhost:9200')
print(res.content)
"""

# annotation / decorator
@app.route("/")
def root_mstarch():
    return "Root webpage"

"""create 1 post for each button in app, 4 total"""
@app.route("/see_fire")
def see_fire():
    see_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_see_fire", json = {"button_press": "yes_alarm_see_fire"})
    return "work!"
    # TODO: validate

@app.route("/get_see_fire_count")
def get_see_fire_count():
    # get the information in each of the posts store each post's version into separate variable for use
    get_see_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_see_fire")
    see_fire_version = get_see_fire.json()["_version"]
    return json.dumps({"count": see_fire_version})

"""
no_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_no_fire", json = {"button_press": "yes_alarm_no_fire"})
no_alarm = requests.post("http://localhost:9200/button_press/button/no_alarm", json = {"button_press": "no_alarm"})
fire_drill = requests.post("http://localhost:9200/button_press/button/fire_drill", json = {"button_press": "fire_drill"})

get_no_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_no_fire")
see_no_fire = get_no_fire.json()["_version"]

get_no_alarm = requests.get("http://localhost:9200/button_press/button/no_alarm")
see_no_alarm = get_no_alarm.json()["_version"]

def get_drill_count():
    get_fire_drill = requests.get("http://localhost:9200/button_press/button/fire_drill")
    see_fire_drill = get_fire_drill.json()["_version"]
    return {"count": see_fire_drill}

annonobj["count"]
# supposed to update user responses
def update_user_responses(which_button):


def main():
    

main()
"""