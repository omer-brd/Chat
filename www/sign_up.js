function ColorFix() {
//fixes the text question color after picking an option
    document.getElementById("question").style.color = "black";
}
function Valid() {
//checks if all the inputs are valid
    var check = true;
    check = Username() && check;
    check = Password() && check;
    check = Confirm() && check;
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
        document.getElementById("username_alert").innerHTML = "username must contain only numbers, letters and hyphens";
        return false;
    }
    else {
        document.getElementById("username_alert").innerHTML = "";
        return true;
    }
}
function UsernameExist(exist) {
//checks if the username is already exists
    if (exist == "True") {
        document.getElementById("username_alert").innerHTML = "this username is taken";
    }
    else {
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        var question = document.getElementById("question").value;
        var answer = document.getElementById("answer").value;
        document.getElementById("username_alert").innerHTML = "";
        eel.start2(username, password, question, answer);
        window.open("client.html", "_self");
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
function Confirm() {
//checks if the confirm password is valid
    var confirm = document.getElementById("confirm").value;
    if (confirm == "") {
        document.getElementById("confirm_alert").innerHTML = "this field is required";
        return false;
    }
    else if (confirm != document.getElementById("password").value) {
        document.getElementById("confirm_alert").innerHTML = "confirm does not match password";
        return false;
    }
    else {
        document.getElementById("confirm_alert").innerHTML = "";
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
function Login() {
//redirects to the login page
    window.open("login.html", "_self");
}
function Reset() {
//redirects to the reset password page
    window.open("forgot.html", "_self");
}