import requests
import json
from flask import Flask
# server
app = Flask(__name__)

@app.after_request
def stamp(response): 
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

# annotation / decorator
@app.route("/")
def root():
    return "ROOT WEBPAGE!"

"""create 1 post for each button in app, 4 total"""
@app.route("/see_fire")
def see_fire():
    see_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_see_fire", json = {"button_press": "yes_alarm_see_fire"})
    return "I SEE FIRE!"
    # TODO: validate

@app.route("/get_see_fire_count")
def get_see_fire_count():
    # get the information in each of the posts store each post's version into separate variable for use
    get_see_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_see_fire")
    see_fire_version = get_see_fire.json().get("_version", 0)
    return json.dumps(see_fire_version)

@app.route("/fire_drill")
def fire_drill():
    fire_drill = requests.post("http://localhost:9200/button_press/button/fire_drill", json = {"button_press": "fire_drill"})
    return "DRILL!!"

@app.route("/get_fire_drill_count")
def get_fire_drill_count():
    get_fire_drill = requests.get("http://localhost:9200/button_press/button/fire_drill")
    fire_drill_version = get_fire_drill.json().get("_version", 0)
    return json.dumps(fire_drill_version)

@app.route("/no_fire")
def no_fire():
    no_fire = requests.post("http://localhost:9200/button_press/button/yes_alarm_no_fire", json = {"button_press": "yes_alarm_no_fire"})
    return "DON'T SEE FIRE"

@app.route("/get_no_fire_count")
def get_no_fire_count():
    get_no_fire = requests.get("http://localhost:9200/button_press/button/yes_alarm_no_fire")
    no_fire_version = get_no_fire.json().get("_version", 0)
    return json.dumps(no_fire_version)

@app.route("/no_alarm")
def no_alarm():
    no_alarm = requests.post("http://localhost:9200/button_press/button/no_alarm", json = {"button_press": "no_alarm"})
    return "DON'T HEAR ALARM!"

@app.route("/get_no_alarm_count")
def get_no_alarm_count():
    get_no_alarm = requests.get("http://localhost:9200/button_press/button/no_alarm")
    no_alarm_version = get_no_alarm.json().get("_version", 0)
    return json.dumps(no_alarm_version)
