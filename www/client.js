var displayed_friends = "";
var displayed_groups = "";
var curr_chat = "everyone";
var curr_type = "group";
function Join() {
//starts the groups when loading the page
    start_groups();
}
function quit() {
//notifies the client when leaving the page
    eel.quit();
}
function PrintMessage(name, clr, time, data, command){
//prints a message
    var msg;
    var color;
    if (name == "You") {
        color = "#A0A0A0";
    }
    else {
        color = clr;
    }
    if (command == "alert") {
        msg = " " + data;
    }
    else if (command == "message") {
        var data = data.replaceAll("\\\\n", "\n")
        data = data.replaceAll("\\n", "\n")
        msg = data;
        date = document.createElement("d");
        var date_text = document.createTextNode(" " + time);
        date.appendChild(date_text);
        date.style.color = "#9b9b9b";
        date.style.fontSize = "10px";
        date.style.fontFamily = "Lucida Console, Courier New, monospace";
    }
    var first = document.createElement("f");
    var last = document.createElement("l");
    var space1 = document.createElement("br");
    var space2 = document.createElement("br");
    var space3 = document.createElement("br");
    var first_text = document.createTextNode(name);
    var last_text = document.createTextNode(msg);
    first.appendChild(first_text);
    last.appendChild(last_text);
    first.style.color = color;
    first.style.fontFamily = "Arial";
    last.style.fontFamily = "Arial";
    first.style.fontSize = "18px";
    last.style.fontSize = "15px";
    last.style.color = "white";
    last.style.whiteSpace = "pre-wrap";
    document.getElementById("chat").appendChild(first);
    if(command == "message") {
        document.getElementById("chat").appendChild(date);
        document.getElementById("chat").appendChild(space1);
    }
    document.getElementById("chat").appendChild(last);
    document.getElementById("chat").appendChild(space2);
    if(command == "alert") {
        document.getElementById("chat").appendChild(space3);
    }
    scroll();
}
function send_msg() {
//sends a message
    var receiver = curr_chat;
    var d = new Date();
    var time = " " + d.getDate() + "/" + (d.getMonth() + 1) + "/" + d.getFullYear() + " " + d.getHours() + ":" + d.getMinutes();
    var raw = document.getElementById("input").value.replaceAll("|", "").match(/.{1,130}/g);
    var data = "";
    for (i = 0; i < raw.length; i++) {
        data += raw[i] + "\n";
    }
    document.getElementById("input").value = "";
    eel.send_msg(data);
    PrintMessage("You", "", time, data, "message");
}
function scroll() {
//scrolls the chat down
     var scroll_div = document.getElementById("chat");
     scroll_div.scrollTop = scroll_div.scrollHeight;
}
function start_friends() {
//loads the friends window
    document.getElementById("friends_btn").style.borderColor = "#3971b0";
    document.getElementById("friends_btn").style.borderWidth = "4px";
    document.getElementById("groups_btn").style.borderColor = "";
    document.getElementById("groups_btn").style.borderWidth = "";
    document.getElementById("groups").style.display = "none";
    document.getElementById("friends").style.display = "block";
    document.getElementById("manage_groups").style.display = "none";
    document.getElementById("manage_friends").style.display = "inline-block";
    document.getElementById("bar").style.backgroundColor = "#3971b0";
    eel.get_friends()(InsertFriends);
    curr_type = "friend";
    while (document.getElementById("chat").firstChild) {
        document.getElementById("chat").removeChild(document.getElementById("chat").firstChild);
    }
}
function start_groups() {
//loads the groups window
    document.getElementById("groups_btn").style.borderColor = "#e34c67";
    document.getElementById("groups_btn").style.borderWidth = "4px";
    document.getElementById("friends_btn").style.borderColor = "";
    document.getElementById("friends_btn").style.borderWidth = "";
    document.getElementById("friends").style.display = "none";
    document.getElementById("groups").style.display = "block";
    document.getElementById("manage_groups").style.display = "inline-block";
    document.getElementById("manage_friends").style.display = "none";
    document.getElementById("bar").style.backgroundColor = "#e34c67";
    curr_type = "group";
    eel.get_groups()(InsertGroups);
}
function open_friends() {
//opens the friends popup
    var win = document.getElementById("friends_window");
    var back = document.getElementById("container");
    var dis = document.getElementsByClassName("dis");
    win.style.display = "block";
    back.style.opacity = "0.4";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = true;
    }
    eel.get_friends()(InsertFriends);
}
function open_groups() {
//opens the groups popup
    var win = document.getElementById("groups_window");
    var back = document.getElementById("container");
    var dis = document.getElementsByClassName("dis");
    win.style.display = "block";
    back.style.opacity = "0.4";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = true;
    }
    eel.get_groups()(InsertGroups);
}
function open_profile() {
//opens the profile popup
    var win = document.getElementById("profile_window");
    var back = document.getElementById("container");
    var dis = document.getElementsByClassName("dis");
    win.style.display = "block";
    back.style.opacity = "0.4";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = true;
    }
}
function close_friends() {
//closes the friends popup
    var win = document.getElementById("friends_window");
    var back = document.getElementById("container");
    document.getElementById("friend_username_alert").innerHTML = "";
    document.getElementById("friend_username").value = "";
    var dis = document.getElementsByClassName("dis");
    win.style.display = "none";
    back.style.opacity = "1";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = false;
    }
}
function close_groups() {
//closes the groups popup
    var win = document.getElementById("groups_window");
    var back = document.getElementById("container");
    var dis = document.getElementsByClassName("dis");
    win.style.display = "none";
    back.style.opacity = "1";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = false;
    }
}
function close_profile() {
//closes the profile popup
    var win = document.getElementById("profile_window");
    var back = document.getElementById("container");
    document.getElementById("username_alert").innerHTML = "";
    document.getElementById("username").value = "";
    document.getElementById("confirm_alert").innerHTML = "";
    document.getElementById("confirm").value = "";
    document.getElementById("password_alert").innerHTML = "";
    document.getElementById("password").value = "";
    var dis = document.getElementsByClassName("dis");
    win.style.display = "none";
    back.style.opacity = "1";
    for (var i = 0; i < dis.length; i++) {
        dis[i].disabled = false;
    }
}
function add_friend() {
//adds a friend
    document.getElementById("user_friends_alert").innerHTML = "";
    if (Username()) {
        var username = document.getElementById("friend_username").value;
        eel.exist(username)(UsernameExist);
    }
}
function remove_friend() {
//removes a friend
    var list = document.getElementById("user_friends");
    var friend = list.value;
    eel.remove_friend(friend);
    list.remove(list.selectedIndex);
    document.getElementById("user_friends_alert").innerHTML = "friend removed";
    document.getElementById("user_friends_alert").style.color = "green";
    document.getElementById("friend_username_alert").innerHTML = "";
    displayed_friends = displayed_friends.replace(friend + ",", "");
    document.getElementById(friend).remove();
    document.getElementById(friend + "_label").remove();
    document.getElementById(friend + "_br").remove();
}
function Username() {
//checks if the username is valid
    document.getElementById("friend_username_alert").style.color = "red";
    var username = document.getElementById("friend_username").value;
    var verify = /^[a-zA-Z0-9_-]+$/.test(username);
    if (username == "") {
        document.getElementById("friend_username_alert").innerHTML = "this field is required";
        return false;
    }
    else if (username.length < 3) {
        document.getElementById("friend_username_alert").innerHTML = "username must be at least 3 digits long";
        return false;
    }
    else if (!verify) {
        document.getElementById("friend_username_alert").innerHTML = "not a valid username";
        return false;
    }
    else {
        document.getElementById("friend_username_alert").innerHTML = "";
        return true;
    }
}
function UsernameExist(exist) {
//checks if the username is already exists
    if (exist == "True") {
        var friend = document.getElementById("friend_username").value;
        document.getElementById("friend_username_alert").innerHTML = "";
        eel.friend_exist(friend)(FriendExist);
    }
    else {
        document.getElementById("friend_username_alert").innerHTML = "username does not exist";
    }
}
function FriendExist(exist) {
//checks if the friend's username is already exists
    if (exist == "True") {
        document.getElementById("friend_username_alert").innerHTML = "user is already your friend";
    }
    else {
        var friend = document.getElementById("friend_username").value;
        eel.get_name(friend)(FinalFriendCheck);
    }
}
function FinalFriendCheck(yourself) {
//checks if the friend's username is not the client's name
    var friend = document.getElementById("friend_username").value;
    if (yourself == "True") {
        document.getElementById("friend_username_alert").innerHTML = "you can't add yourself";
    }
    else {
        var list = document.getElementById("user_friends");
        eel.add_friend(friend);
        document.getElementById("friend_username").value = "";
        document.getElementById("friend_username_alert").innerHTML = "friend added";
        document.getElementById("friend_username_alert").style.color = "green";
        var option = document.createElement("option");
        option.text = friend;
        list.add(option);
        var label = document.createElement("label");
        var input = document.createElement("input");
        var text = document.createTextNode(friend);
        label.htmlFor = friend;
        label.className = "checks";
        input.type = "checkbox";
        input.id = friend + "_box";
        label.id = friend + "_label";
        label.appendChild(input);
        label.appendChild(text);
        document.getElementById("checkboxes").appendChild(label);
        DisplayFriend(friend);
    }
}
function InsertFriends(friends) {
//insert friends to main screen, select list and member list
    var option;
    var exist;
    var list = document.getElementById("user_friends");
    var options = document.getElementById("user_friends").options;
    //insert to select list and member list
    for (var i = 0; i < friends.length - 1; i++) {
        exist = false;
        for (var j = 0; j < options.length; j++) {
            if(friends[i] == options[j].text) {
                exist = true;
            }
        }
        if(!exist) {
            var friend = friends[i];
            option = document.createElement("option");
            option.text = friend;
            list.add(option);
            var label = document.createElement("label");
            var input = document.createElement("input");
            var text = document.createTextNode(friend);
            label.htmlFor = friend;
            label.className = "checks";
            input.type = "checkbox";
            input.id = friend + "_box";
            label.id = friend + "_label";
            label.appendChild(input);
            label.appendChild(text);
            document.getElementById("checkboxes").appendChild(label);
        }
    }
    //display on main screen
    friends_split = displayed_friends.split(",");
    for (var i = 0; i < friends.length - 1; i++) {
        exist = false;
        for (var j = 0; j < friends_split.length - 1; j++) {
            if(friends[i] == friends_split[j]) {
                exist = true;
            }
        }
        if(!exist) {
            DisplayFriend(friends[i]);
        }
    }
}
function DisplayFriend(name) {
//displays a friend on the main screen
    var friend = document.createElement("div");
    var friend_name = document.createTextNode(name);
    var space = document.createElement("br");
    friend.setAttribute("onclick", "specific_friend('" + name + "')");
    space.id = name + "_br";
    friend.appendChild(friend_name);
    friend.id = name;
    friend.style.color = "black";
    friend.style.fontFamily = "Arial";
    friend.style.fontSize = "30px";
    friend.style.textAlign = "center";
    friend.style.width = "90%";
    friend.style.margin = "auto";
    friend.style.padding = "5px";
    friend.style.border = "3px solid #575757";
    friend.style.borderRadius = "15px";
    friend.style.backgroundColor = "#a3a3a3";
    document.getElementById("friends").appendChild(friend);
    document.getElementById("friends").appendChild(space);
    displayed_friends += name + ",";
}
function EnterSend(event) {
//sends a message by pressing enter
    if (event.keyCode == 13 && !event.shiftKey) {
        send_msg();
    }
}
function ShowCheckboxes() {
//shows the members select checkboxes
    if (document.getElementById("checkboxes").style.display == "none") {
        document.getElementById("checkboxes").style.display = "block";
    }
    else {
        document.getElementById("checkboxes").style.display = "none";
    }
}
function leave_group() {
//leaves a group
    var list = document.getElementById("user_groups");
    var group = list.value;
    eel.leave_group(group);
    list.remove(list.selectedIndex);
    document.getElementById("leave_group_alert").innerHTML = "left group";
    document.getElementById("leave_group_alert").style.color = "green";
    document.getElementById("create_group_alert").innerHTML = "";
    displayed_groups = displayed_groups.replace(group + ",", "");
    document.getElementById(group).remove();
}
function create_group() {
//creates a group
    document.getElementById("leave_group_alert").innerHTML = "";
    if (GroupName()) {
        var name = document.getElementById("group_name").value;
        eel.group_exist(name)(GroupExist);
    }
}
function GroupName() {
//checks if the group name is valid
    document.getElementById("create_group_alert").style.color = "red";
    var name = document.getElementById("group_name").value;
    var verify = /^[a-zA-Z0-9_-]+$/.test(name);
    if (name == "") {
        document.getElementById("create_group_alert").innerHTML = "this field is required";
        return false;
    }
    else if (name.length < 3) {
        document.getElementById("create_group_alert").innerHTML = "group name must be at least 3 digits long";
        return false;
    }
    else if (!verify) {
        document.getElementById("create_group_alert").innerHTML = "not a valid group name";
        return false;
    }
    else {
        document.getElementById("create_group_alert").innerHTML = "";
        return true;
    }
}
function GroupExist(exist) {
//checks if the group name is already exists
    if (exist == "True") {
        document.getElementById("create_group_alert").innerHTML = "group name is taken";
    }
    else {
        var name = document.getElementById("group_name").value;
        var friends_split = displayed_friends.split(",");
        var members = "";
        for (var i = 0; i < friends_split.length - 1; i++) {
            if(document.getElementById(friends_split[i] + "_box").checked){
                members += friends_split[i] + ",";
            }
        }
        eel.create_group(name, members);
        document.getElementById("group_name").value = "";
        document.getElementById("create_group_alert").innerHTML = "group created";
        document.getElementById("create_group_alert").style.color = "green";
        var option = document.createElement("option");
        var list = document.getElementById("user_groups");
        option.text = name;
        list.add(option);
        DisplayGroup(name);
    }
}
function DisplayGroup(name) {
//displays a group on the main screen
    var group = document.createElement("div");
    var group_name = document.createTextNode(name);
    var space = document.createElement("br");
    group.setAttribute("onclick", "specific_group('" + name + "')");
    group.appendChild(group_name);
    group.id = name;
    group.style.color = "black";
    group.style.fontFamily = "Arial";
    group.style.fontSize = "30px";
    group.style.textAlign = "center";
    group.style.width = "90%";
    group.style.margin = "auto";
    group.style.padding = "5px";
    group.style.border = "3px solid #575757";
    group.style.borderRadius = "15px";
    group.style.backgroundColor = "#a3a3a3";
    document.getElementById("groups").appendChild(group);
    document.getElementById("groups").appendChild(space);
    displayed_groups += name + ",";
}
function InsertGroups(groups) {
//insert groups to main screen and select list
    var option;
    var exist;
    var list = document.getElementById("user_groups");
    var options = document.getElementById("user_groups").options;
    //insert to select list
    for (var i = 0; i < groups.length - 1; i++) {
        exist = false;
        for (var j = 0; j < options.length; j++) {
            if(groups[i] == options[j].text) {
                exist = true;
            }
        }
        if(!exist && groups[i] != "everyone") {
            var group = groups[i];
            option = document.createElement("option");
            option.text = group;
            list.add(option);
        }
    }
    //display on main screen
    groups_split = displayed_groups.split(",");
    for (var i = 0; i < groups.length - 1; i++) {
        exist = false;
        for (var j = 0; j < groups_split.length - 1; j++) {
            if(groups[i] == groups_split[j]) {
                exist = true;
            }
        }
        if(!exist) {
            DisplayGroup(groups[i]);
        }
    }
    specific_group("everyone");
}
function change_password() {
//changes the client's password the the new password
    document.getElementById("username_alert").innerHTML = "";
    var check = true;
    check = Password() && check;
    check = Confirm() && check;
    alert(check)
    if (check) {
        var password = document.getElementById("password").value;
        eel.change_password(password)();
        document.getElementById("password").value = "";
        document.getElementById("confirm").value = "";
        document.getElementById("confirm_alert").innerHTML = "password changed";
        document.getElementById("confirm_alert").style.color = "green";
        document.getElementById("password_alert").innerHTML = "password changed";
        document.getElementById("password_alert").style.color = "green";
    }
}
function Password() {
//checks if the password is valid
    document.getElementById("password_alert").style.color = "red";
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
    document.getElementById("confirm_alert").style.color = "red";
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
function change_username() {
//changes the client's username the the new username
    document.getElementById("password_alert").innerHTML = "";
    document.getElementById("confirm_alert").innerHTML = "";
    if (Username2()) {
        var username = document.getElementById("username").value;
        eel.exist(username)(UsernameExist2);
    }
}
function Username2() {
//checks if the username is valid
    document.getElementById("username_alert").style.color = "red";
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
function UsernameExist2(exist) {
//checks if the username is already exists
    if (exist == "True") {
        document.getElementById("username_alert").innerHTML = "username is taken";
    }
    else {
        var username = document.getElementById("username").value;
        eel.change_username(username)();
        document.getElementById("username").value = "";
        document.getElementById("username_alert").innerHTML = "username changed";
        document.getElementById("username_alert").style.color = "green";
    }
}
function specific_group(group) {
//chooses a specific group to show its chat
    document.getElementById(curr_chat).style.color = "black";
    document.getElementById(curr_chat).style.backgroundColor = "#a3a3a3";
    document.getElementById(curr_chat).style.border = "3px solid #575757";
    curr_chat = group;
    curr_type = "group";
    document.getElementById(curr_chat).style.color = "white";
    document.getElementById(curr_chat).style.backgroundColor = "black";
    document.getElementById(curr_chat).style.border = "3px solid #e34c67";
    eel.get_chat("group", group)(UploadChat);
}
function specific_friend(friend) {
//chooses a specific friend to show its chat
    document.getElementById(curr_chat).style.color = "black";
    document.getElementById(curr_chat).style.backgroundColor = "#a3a3a3";
    document.getElementById(curr_chat).style.border = "3px solid #575757";
    curr_chat = friend;
    curr_type = "friend";
    document.getElementById(curr_chat).style.color = "white";
    document.getElementById(curr_chat).style.backgroundColor = "black";
    document.getElementById(curr_chat).style.border = "3px solid #3971b0";
    eel.get_chat("friend", friend)(UploadChat);
}
function UploadChat(chat) {
//uploads the chat of the selected friend/group
    while (document.getElementById("chat").firstChild) {
        document.getElementById("chat").removeChild(document.getElementById("chat").firstChild);
    }
    self_name = chat[1];
    chat = chat[0].split("<--->");
    for(i = 0; i < chat.length - 1; i+=1) {
        message = chat[i];
        message = message.split("!@");
        name = message[0];
        color = message[1];
        time = message[2];
        data = message[3];
        if(name == self_name) {
            name = "You";
        }
        command = "message";
        if (time == "--") {
            command = "alert";
        }
        PrintMessage(name, color, time, data, command);
    }
}
function update_chat() {
//updates the chat of the selected friend/group
    eel.get_chat(curr_type, curr_chat)(UploadChat);
}
function update_friend() {
//updates the friend list
    eel.get_friends()(InsertFriends);
}
function update_group() {
//updates the group list
    eel.get_groups()(InsertGroups);
}
eel.expose(update_chat);
eel.expose(update_friend);
eel.expose(update_group);
