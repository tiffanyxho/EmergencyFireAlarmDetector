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
function display_responses(){
    document.getElementById("real_fire_text").innerHTML = "HIIII!!!";
}