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

// BEFORE PUSHING TO GITHUB, MAKE SURE TO HAVE FLASK = "server";
var FLASK = "http://localhost:5000" //--> for testing on computer; for testing on web --> "server"; 
var real_fire_button_clicks = 0, fire_drill_button_clicks = 0;
var dont_see_fire_button_clicks = 0, dont_hear_alarm_button = 0;
var last_button_clicked_id = "";

/* Links to help with adding back HTML for buttons... - might need to make a div to hold all of the removed content in the first div
 * https://www.abeautifulsite.net/adding-and-removing-elements-on-the-fly-using-javascript

 */

/**Server code - retrieving data to make usable - starts here*/
/**get method (equivalent of get method in requests library in python) */
function get(theUrl){
    var xmlHttp  =  new XMLHttpRequest();
    xmlHttp.open(  "GET", theUrl,false);  // false for synchronous request
    xmlHttp.send(  null  );
    return xmlHttp.responseText;
}

/*JS see_fire func*/
function see_fire(){
    var see_fire = get(FLASK + "/see_fire");
    change_screen();
    return "JAVASCRIPT: I SEE FIRE!";
}

/*Get data from the python server to get the see fire count*/
function get_see_fire_count(){
    var see_fire = get(FLASK + "/get_see_fire_count");
    return see_fire;
}

/*JS fire_drill func */
function fire_drill(){
    var fire_drill = get(FLASK + "/fire_drill");
    change_screen();
    return "IT'S A FIRE DRILL";
}

/*get the fire_drill count */
function get_fire_drill_count(){
    var fire_drill = get(FLASK + "/get_fire_drill_count");
    return fire_drill;
}

/*JS no_fire func*/
function no_fire(){
    var no_fire = get(FLASK + "/no_fire");
    change_screen();
    return "DON'T SEE FIRE";
}

/*get the no_fire count */
function get_no_fire_count(){
    var no_fire = get(FLASK + "/get_no_fire_count");
    return no_fire;
}

/**JS no_alarm func */
function no_alarm(){
    var no_alarm = get(FLASK + "/no_alarm");
    change_screen();
    return "DON'T HEAR ALARM!";
}

/**get no_alarm count */
function get_no_alarm_count(){
    var get_no_alarm = get(FLASK + "/get_no_alarm_count");
    return get_no_alarm;
}

/**TODO: make the prints only print the version number 
 * Updates the version numbers when user presses buttons
*/
function get_count(){
    real_fire_button_clicks = get_see_fire_count();
    fire_drill_button_clicks = get_fire_drill_count();
    dont_see_fire_button_clicks = get_no_fire_count();
    dont_hear_alarm_button = get_no_alarm_count();

    document.getElementById("real_fire_text").innerHTML = "Real fire: " + real_fire_button_clicks;
    document.getElementById("fire_drill_text").innerHTML = "It's a drill: " + fire_drill_button_clicks;
    document.getElementById("dont_see_fire_text").innerHTML = "Don't see fire: " + dont_see_fire_button_clicks;
    document.getElementById("dont_hear_alarm_text").innerHTML = "Don't hear alarm: " + dont_hear_alarm_button;
}

/**if you want a button that deletes the count and restarts it at 0, then you can make similar function as get one
 * for the url part, reference picture taken to know what to put in
 */

/** changes screen from buttons to display user responses/counts */
 function change_screen(){
    get_count();
    document.getElementById("end_screen").style.display = "inline";
    document.getElementById("buttons_id").style.display = "none";
 }

 /**calls get_count every 10s */
 setInterval(get_count, 10000);