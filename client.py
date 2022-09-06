import socket
import select
import threading
import eel
from cryptography.fernet import Fernet


@eel.expose
def exist(username):
    """
    checks if the username exists
    :param username: the wanted name of the client
    :type username: string
    :return: username exist?
    :rtype: bool
    """
    return c.exist(username)


@eel.expose
def friend_exist(friend):
    """
    checks if the username is already a friend
    :param friend: the friend's username
    :type friend: string
    :return: already friend?
    :rtype: bool
    """
    return c.friend_exist(friend)


@eel.expose
def match(username, password):
    """
    checks if the username and password matches
    :param username: the name of the client
    :type username: string
    :param password: the password of the client
    :type password: string
    :return: username and password match?
    :rtype: bool
    """
    return c.match(username, password)


@eel.expose
def insert(username, password, question, answer):
    """
    adds the new user into the database
    :param username: the name of the client
    :type username: string
    :param password: the password of the client
    :type password: string
    :param question: the question of the client
    :type question: string
    :param answer: the answer of the client
    :type answer: string
    :return: nothing
    """
    c.insert(username, password, question, answer)


@eel.expose
def add_friend(friend):
    """
    adds a friend
    :param friend: the name of the friend
    :type friend: string
    :return: nothing
    """
    c.add_friend(friend)


@eel.expose
def get_friends():
    """
    returns the client's friends
    :return: client's friends
    :rtype: list
    """
    return c.get_friends()


@eel.expose
def remove_friend(friend):
    """
    removes a friend
    :param friend: the name of the friend
    :type friend: string
    :return: nothing
    """
    c.remove_friend(friend)


@eel.expose
def group_exist(group):
    """
    checks if the group exists
    :param group: the wanted name of the group
    :type group: string
    :return: group exist?
    :rtype: bool
    """
    return c.group_exist(group)


@eel.expose
def create_group(group, members):
    """
    creates a group
    :param group: the name of the group
    :type group: string
    :param members: the members of the group
    :type members: string
    :return: nothing
    """
    c.create_group(group, members)


@eel.expose
def get_groups():
    """
    returns client's groups
    :return: client's groups
    :rtype: list
    """
    return c.get_groups()


@eel.expose
def leave_group(group):
    """
    leaves group
    :param group: the name of the group
    :return: nothing
    """
    c.leave_group(group)


@eel.expose
def get_name(friend):
    """
    returns if the friend is the client
    :param friend: wanted friend name
    :return: if the friend is the client
    :rtype: bool
    """
    return c.name == friend


def run_eel():
    """
    runs eel and opens the login screen
    :return: nothing
    """
    global c
    c = Client("defualt")
    manager = threading.Thread(target=c.manager)
    manager.start()
    eel.init("www")
    eel.start("login.html", port=0)


@eel.expose
def start(name):
    """
    assign the name to the client
    :param name: client's name
    :return: nothing
    """
    c.start(name)


@eel.expose
def start2(username, password, question, answer):
    """
    adds the new user into the database
    :param username: the name of the client
    :type username: string
    :param password: the password of the client
    :type password: string
    :param question: the question of the client
    :type question: string
    :param answer: the answer of the client
    :type answer: string
    :return: nothing
    """
    c.insert(username, password, question, answer)
    c.start(username)


@eel.expose
def change_password(password):
    """
    changes the password of the client
    :param password: new password
    :type password: string
    :return: nothing
    """
    c.change_password(password)


@eel.expose
def change_password2(username, password):
    """
    changes the password of the client
    :param username: username of the client
    :type username: string
    :param password: new password
    :type password: string
    :return: nothing
    """
    c.change_password2(username, password)


@eel.expose
def change_username(username):
    """
    changes the name of the client
    :param username: new name
    :type username: string
    :return: nothing
    """
    c.change_username(username)


@eel.expose
def match_question(question, answer, username):
    """
    checks if the question and answer matches
    :param question: the question of the client
    :type question: string
    :param answer: the answer of the client
    :type answer: string
    :param username: the username of the client
    :type username: string
    :return: question and answer match?
    :rtype: bool
    """
    return c.match_question(question, answer, username)


@eel.expose
def quit():
    """
     disconnects from the server
     :return: nothing
     """
    c.quit()


@eel.expose
def get_chat(type, name):
    """
    returns the chat history
    :param type: the type of the chat
    :type type: string
    :param name: the name of the chat
    :type name: string
    :return: chat history
    :rtype: list
    """
    return c.get_chat(type, name), c.name


@eel.expose
def send_msg(data):
    """
    sending a message from the client
    :param data: the content of the message
    :return: nothing
    """
    c.send_msg(data)


class Client:
    """
    represents the client
    :ivar client_socket: client's socket
    :type client_socket: socket
    :ivar name: client's name
    :type name: string
    :ivar color: client's color
    :type color: string
    :ivar connected: is the client connected
    :type connected: bool
    :ivar read_list: sockets that the client can read from
    :type read_list: list
    :ivar write_list: sockets that the client can write to
    :type write_list: list
    :ivar error_list: errors list
    :type error_list: list
    :ivar curr_chat: the current chat
    :type curr_chat: string
    :ivar curr_type: the current type of the chat
    :type curr_type: string
    :ivar key: encryption/decryption key
    :type key: Fernet
    """
    def __init__(self, name):
        """
        creates new client
        :param name: client's name
        :type name: string
        :return: nothing
        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 5555))
        self.name = name
        self.id = 0
        self.read_list = []
        self.write_list = []
        self.error_list = []
        self.connected = True
        self.color = "#A0A0A0"
        self.curr_chat = ""
        self.curr_type = ""
        self.key = Fernet(b'SgVhKk7otbEjAtpEoGyn1dq87dEIPNjC4A0u9JGDqFY=')

    def quit(self):
        """
        disconnects from the server
        :return: nothing
        """
        command = "quit"
        raw = str(self.id) + "|" + command
        self.client_socket.send(self.encode(str(raw)))
        self.connected = False

    def encode(self, raw):
        return self.key.encrypt(bytes(str(raw), 'utf-8'))

    def decode(self, raw):
        return self.key.decrypt(raw)

    def recv(self):
        """
        receives message from the server
        :return: nothing
        """
        raw = str(self.decode(self.client_socket.recv(1024)))[2:-1]
        raw = raw.split("|")
        command = raw[0]
        chat = raw[1]
        type = raw[2]
        if command == "update_chat" and chat == self.curr_chat and type == self.curr_type:
            self.update_chat()
        elif command == "update_friend" and self.curr_type == "friend":
            self.update_friend()
        elif command == "update_group" and self.curr_type == "group":
            self.update_group()

    def start(self, name):
        """
        starts the client
        :param name: the name of the client
        :type name: string
        :return: nothing
        """
        self.name = name
        command = "get_id_by_name"
        raw = str(self.id) + "|" + command + "|" + self.name
        self.client_socket.send(self.encode(str(raw)))
        self.id = int(str(self.decode(self.client_socket.recv(1024)))[2:-1])

    def exist(self, username):
        """
        checks if the username exists
        :param username: the wanted name of the client
        :type username: string
        :return: username exist?
        :rtype: bool
        """
        command = "exist"
        raw = str(self.id) + "|" + command + "|" + username
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(1024)))[2:-1]

    def friend_exist(self, friend):
        """
        checks if friend exist
        :param friend: the name of the friend
        :type friend: string
        :return: friend exist?
        :rtype: bool
        """
        command = "friend_exist"
        raw = str(self.id) + "|" + command + "|" + friend
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(1024)))[2:-1]

    def add_friend(self, friend):
        """
        adds a friend
        :param friend: the name of the friend
        :type friend: string
        :return: nothing
        """
        command = "add_friend"
        raw = str(self.id) + "|" + command + "|" + friend
        self.client_socket.send(self.encode(str(raw)))

    def get_friends(self):
        """
        returns friends
        :return: friends
        :rtype: list
        """
        self.curr_type = "friend"
        command = "get_friends"
        raw = str(self.id) + "|" + command
        self.client_socket.send(self.encode(str(raw)))
        friends = str(self.decode(self.client_socket.recv(1024)))[2:-1]
        if friends == "None":
            return ""
        return friends.split(",")

    def remove_friend(self, friend):
        """
        removes a friend
        :param friend: the name of the friend
        :type friend: string
        :return: nothing
        """
        command = "remove_friend"
        raw = str(self.id) + "|" + command + "|" + friend
        self.client_socket.send(self.encode(str(raw)))

    def group_exist(self, group):
        """
        checks if the group exists
        :param group: the wanted name of the group
        :type group: string
        :return: group exist?
        :rtype: bool
        """
        command = "group_exist"
        raw = str(self.id) + "|" + command + "|" + group
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(1024)))[2:-1]

    def get_groups(self):
        """
        returns groups
        :return: groups
        :rtype: list
        """
        self.curr_type = "group"
        command = "get_groups"
        raw = str(self.id) + "|" + command
        self.client_socket.send(self.encode(str(raw)))
        groups = str(self.decode(self.client_socket.recv(1024)))[2:-1]
        if groups == "None":
            return ""
        return groups.split(",")

    def leave_group(self, group):
        """
        leaves group
        :param group: the name of the group
        :type group: string
        :return: nothing
        """
        command = "leave_group"
        raw = str(self.id) + "|" + command + "|" + group
        self.client_socket.send(self.encode(str(raw)))

    def match(self, username, password):
        """
        checks if the username and password matches
        :param username: the name of the client
        :type username: string
        :param password: the password of the client
        :type password: string
        :return: username and password match?
        :rtype: bool
        """
        command = "match"
        raw = str(self.id) + "|" + command + "|" + username + "|" + password
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(1024)))[2:-1]

    def match_question(self, question, answer, username):
        """
        checks if the question and answer matches
        :param question: the name of the client
        :type question: string
        :param answer: the answer of the client
        :type answer: string
        :param username: the username of the client
        :type username: string
        :return: question and answer match?
        :rtype: bool
        """
        command = "match_question"
        raw = str(self.id) + "|" + command + "|" + question + "|" + answer + "|" + username
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(1024)))[2:-1]

    def create_group(self, group, members):
        """
        creates a group
        :param group: the name of the group
        :type group: string
        :param members: the members of the group
        :type members: string
        :return: nothing
        """
        command = "create_group"
        raw = str(self.id) + "|" + command + "|" + group + "|" + members + self.name + ","
        self.client_socket.send(self.encode(str(raw)))

    def insert(self, username, password, question, answer):
        """
        adds the new user into the database, currently without color
        :param username: the name of the client
        :type username: string
        :param password: the password of the client
        :type password: string
        :param question: the question of the client
        :type question: string
        :param answer: the answer of the client
        :type answer: string
        :return: nothing
        """
        command = "insert"
        raw = str(self.id) + "|" + command + "|" + username + "|" + password + "|" + question + "|" + answer
        self.client_socket.send(self.encode(str(raw)))

    def change_password(self, password):
        """
        changes the password of the client
        :param password: new password
        :type password: string
        :return: nothing
        """
        command = "change_password"
        raw = str(self.id) + "|" + command + "|" + password
        self.client_socket.send(self.encode(str(raw)))

    def change_password2(self, username, password):
        """
        changes the password of the client
        :param username: username of the client
        :type username: string
        :param password: new password
        :type password: string
        :return: nothing
        """
        command = "change_password2"
        raw = str(self.id) + "|" + command + "|" + username + "|" + password
        self.client_socket.send(self.encode(str(raw)))

    def change_username(self, username):
        """
        changes the name of the client
        :param username: new name
        :type username: string
        :return: nothing
        """
        command = "change_username"
        raw = str(self.id) + "|" + command + "|" + username
        self.client_socket.send(self.encode(str(raw)))
        self.name = username

    def get_chat(self, type, name):
        """
        returns the chat history
        :param type: the type of the chat
        :type type: string
        :param name: the name of the chat
        :type name: string
        :return: chat history
        :rtype: string
        """
        self.curr_chat = name
        self.curr_type = type
        command = "get_chat"
        raw = str(self.id) + "|" + command + "|" + type + "|" + name
        self.client_socket.send(self.encode(str(raw)))
        return str(self.decode(self.client_socket.recv(6400)))[2:-1]

    def send_msg(self, data):
        """
        sending a message from the client
        :param data: content of the message
        :return: nothing
        """
        command = "send_message"
        raw = str(self.id) + "|" + command + "|" + self.curr_chat + "|" + data + "|" + self.curr_type
        self.client_socket.send(self.encode(str(raw)))

    def update_chat(self):
        """
        updates the chat
        :return: nothing
        """
        eel.update_chat()

    def update_friend(self):
        """
        displays / undisplayes friend
        :return: nothing
        """
        eel.update_friend()

    def update_group(self):
        """
        displays / undisplayes group
        :return: nothing
        """
        eel.update_group()

    def manager(self):
        """
        manages the sending and receiving of messages
        :return: nothing
        """
        while self.connected:
            self.read_list, self.write_list, self.error_list = select.select([self.client_socket], [self.client_socket], [])
            if len(self.read_list) != 0:
                self.recv()
        self.client_socket.close()


def main():
    run = threading.Thread(target=run_eel)
    run.start()


if __name__ == "__main__":
    main()
