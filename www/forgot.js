function ColorFix() {
//fixes the text question color after picking an option
  document.getElementById("question").style.color = "black";
}
function Valid() {
//checks if all the inputs are valid
    var check = true;
    check = Username() && check;
    check = Password() && check;
    check = Question() && check;
    check = Answer () && check;
    if (check) {
        var username = document.getElementById("username").value;
        eel.exist(username)(UsernameExist);
    }
}
function Username() {
//checks if the username is valid
    var username = document.getElementById("username").value;
    var verify = /^[a-zA-Z0-9_-]+$/.test(username);
    if (username == "") {
        document.getElementById("username_alert").innerHTML = "this field is required";
        return false;
    }
    else if (username.length < 3) {
        document.getElementById("username_alert").innerHTML = "username must be at least 3 digits long";
        return false;
    }
    else if (!verify) {
        document.getElementById("username_alert").innerHTML = "not a valid username";
        return false;
    }
    else {
        document.getElementById("username_alert").innerHTML = "";
        return true;
    }
}
function Password() {
//checks if the password is valid
    var password = document.getElementById("password").value;
    if (password == "") {
        document.getElementById("password_alert").innerHTML = "this field is required";
        return false;
    }
    else if (password.length < 6) {
        document.getElementById("password_alert").innerHTML = "password must be at least 6 digits long";
        return false;
    }
    else {
        document.getElementById("password_alert").innerHTML = "";
        return true;
    }
}
function Question() {
//checks if the question is valid
    var question = document.getElementById("question").value;
    if (question == "Select Question") {
        document.getElementById("question_alert").innerHTML = "this field is required";
        return false;
    }
    else {
        document.getElementById("question_alert").innerHTML = "";
        return true;
    }
}
function Answer() {
//checks if the answer is valid
    var answer = document.getElementById("answer").value;
    var verify = /^[a-zA-Z0-9 ]+$/.test(answer);
    if (answer == "") {
        document.getElementById("answer_alert").innerHTML = "this field is required";
        return false;
    }
    else if (!verify) {
        document.getElementById("answer_alert").innerHTML = "answer must contain only numbers, letters and hyphens";
        return false;
    }
    else {
        document.getElementById("answer_alert").innerHTML = "";
        return true;
    }
}
function EyePassword() {
//toggles between the open eye - type text, and the closed eye - type password
    var toggle = document.querySelector('#toggle_password');
    var password = document.querySelector('#password');
    var type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    if (type == "password"){
        toggle.className = "show-password fas fa-eye-slash";
    }
    else {
        toggle.className = "show-password fas fa-eye";
    }
}
function EyeConfirm() {
//toggles between the open eye - type text, and the closed eye - type password
    var toggle = document.querySelector('#toggle_confirm');
    var confirm = document.querySelector('#confirm');
    var type = confirm.getAttribute('type') === 'password' ? 'text' : 'password';
    confirm.setAttribute('type', type);
    if (type == "password"){
        toggle.className = "show-confirm fas fa-eye-slash";
    }
    else {
        toggle.className = "show-confirm fas fa-eye";
    }
}
function UsernameExist(exist) {
//checks if the username is already exists
    if (exist == "True") {
        var question = document.getElementById("question").value;
        var answer = document.getElementById("answer").value;
        var username = document.getElementById("username").value;
        eel.match_question(question, answer, username)(Match);
    }
    else {
        document.getElementById("username_alert").innerHTML = "username does not exist";
    }
}
function Match(match) {
//checks if the question and the answer matches
    if (!(match == "True")) {
        document.getElementById("question_alert").innerHTML = "question and answer does not match";
        document.getElementById("answer_alert").innerHTML = "question and answer does not match";
    }
    else {
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        eel.change_password2(username, password)();
        window.open("login.html", "_self");
    }
}
function Login() {
//redirects to the login page
    window.open("login.html", "_self");

}
function SignUp() {
//redirects to the signup page
    window.open("sign_up.html", "_self");
}