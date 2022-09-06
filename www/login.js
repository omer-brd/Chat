var check2 = false;
var check3 = false;
function Valid() {
//checks if all the inputs are valid
    var check = true;
    check = Username() && check;
    check = Password() && check;
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
function UsernameExist(exist) {
//checks if the username is already exists
    if (exist == "True") {
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        document.getElementById("username_alert").innerHTML = "";
        eel.match(username, password)(Match);
    }
    else {
        document.getElementById("username_alert").innerHTML = "username does not exist";
    }
}
function Match(match) {
//checks if the username and the password matches
    if (!(match == "True")) {
        document.getElementById("username_alert").innerHTML = "username and password does not match";
        document.getElementById("password_alert").innerHTML = "username and password does not match";
    }
    else {
        document.getElementById("username_alert").innerHTML = "";
        document.getElementById("password_alert").innerHTML = "";
        window.open("client.html", "_self");
        eel.start(document.getElementById("username").value);
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
function SignUp() {
//redirects to the signup page
    window.open("sign_up.html", "_self");
}
function Reset() {
//redirects to the reset password page
    window.open("forgot.html", "_self");
}