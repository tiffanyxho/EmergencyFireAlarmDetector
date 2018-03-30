// anchor links - may be handy later

// This link may be handy for solving the below problem: https://stackoverflow.com/questions/1947263/using-an-html-button-to-call-a-javascript-function?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
/* This link was used for the below commented code: https://www.w3schools.com/js/js_htmldom_nodes.asp
document.getElementById("real_fire_button").addEventListener("click", display_responses);

function display_responses(){
    var para = document.createElement("p");
    var node = document.createTextNode("TEXT:!!!");
    para.appendChild(node);
    var element = document.getElementsById("notification_text");
    element.appendChild(para);
}
*/

// Should display how many people pressed which button to users

var real_fire_button_clicks = 0, fire_drill_button_clicks = 0;
var dont_see_fire_button_clicks = 0, dont_hear_alarm_button = 0;


function display_responses(){
    if (document.getElementById("real_fire_text")){
        real_fire_button_clicks += 1;
        document.getElementById("real_fire_text").innerHTML = "Real fire: " + real_fire_button_clicks;
    }else if (document.getElementById("fire_drill_button")){
        fire_drill_button_clicks += 1;
        document.getElementById("fire_drill_button").innerHTML = "It's a drill: " + fire_drill_button_clicks;
    }else if (document.getElementById("dont_see_fire_button")){
        dont_see_fire_button_clicks += 1;
        document.getElementById("dont_see_fire_button").innerHTML = "Don't see fire: " + dont_see_fire_button_clicks;
    }else if (document.getElementById("dont_hear_alarm_button")){
        dont_hear_alarm_button += 1;
        document.getElementById("dont_hear_alarm_button").innerHTML = "Real fire: " + dont_hear_alarm_button;
    }
}