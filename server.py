import socket
import select
import database
from cryptography.fernet import Fernet


class Server:
    """
    represents the server
    :ivar server_socket: server's socket
    :type server_socket: socket
    :ivar client_sockets: connected clients
    :type client_sockets: list
    :ivar read_list: sockets that the server can read from
    :type read_list: list
    :ivar write_list: sockets that the server can write to
    :type write_list: list
    :ivar error_list: errors list
    :type error_list: list
    :ivar to_send_list: messages that need to be sent
    :type to_send_list: list
    :ivar key: encryption/decryption key
    :type key: Fernet
    """
    def __init__(self):
        """
        creates new server
        :return: nothing
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("0.0.0.0", 5555))
        self.server_socket.listen()
        self.client_sockets = []
        self.read_list = []
        self.write_list = []
        self.error_list = []
        self.to_send_list = []
        self.key = Fernet(b'SgVhKk7otbEjAtpEoGyn1dq87dEIPNjC4A0u9JGDqFY=')

    def add_client(self, current_socket):
        """
        adds client to the clients list and connects him to the server
        :param current_socket: client's socket
        :type current_socket: socket
        :return: nothing
        """
        connection, client_address = current_socket.accept()
        self.client_sockets.append(connection)

    def encode(self, raw):
        return self.key.encrypt(bytes(str(raw), 'utf-8'))

    def decode(self, raw):
        return self.key.decrypt(raw)

    def recv_raw(self, current_socket):
        """
        receives message from the client and handles it
        :param current_socket: client's socket
        :type current_socket: socket
        :return: nothing
        """
        raw = str(self.decode(current_socket.recv(1024)))[2:-1]
        raw = raw.split("|")
        id = raw[0]
        command = raw[1]
        print(command)
        if command == "quit":
            self.remove_client(current_socket)
        elif command == "exist":
            username = raw[2]
            raw = database.exist(username)
            current_socket.send(self.encode(str(raw)))
        elif command == "friend_exist":
            friend = raw[2]
            raw = database.friend_exist(id, friend)
            current_socket.send(self.encode(str(raw)))
        elif command == "match":
            username = raw[2]
            password = raw[3]
            raw = database.match(username, password)
            current_socket.send(self.encode(str(raw)))
        elif command == "insert":
            username = raw[2]
            password = raw[3]
            question = raw[4]
            answer = raw[5]
            database.insert(username, password, question, answer)
        elif command == "add_friend":
            friend = raw[2]
            database.add_friend(id, friend)
            self.to_send_list.append((current_socket, "", "friend2"))
        elif command == "get_friends":
            raw = database.get_friends(id)
            if raw == "":
                raw = "None"
            current_socket.send(self.encode(str(raw)))
        elif command == "remove_friend":
            friend = raw[2]
            database.remove_friend(id, friend)
            self.to_send_list.append((current_socket, "", "friend2"))
        elif command == "group_exist":
            group = raw[2]
            raw = database.group_exist(group)
            current_socket.send(self.encode(str(raw)))
        elif command == "create_group":
            group = raw[2]
            members = raw[3]
            database.create_group(group, members)
            self.to_send_list.append((current_socket, "", "group2"))
        elif command == "get_groups":
            raw = database.get_groups(id)
            if raw == "":
                raw = "None"
            current_socket.send(self.encode(str(raw)))
        elif command == "leave_group":
            group = raw[2]
            database.leave_group(id, group)
            self.to_send_list.append((current_socket, "", "group2"))
        elif command == "get_id_by_name":
            name = raw[2]
            raw = database.get_id_by_name(name)
            current_socket.send(self.encode(str(raw)))
        elif command == "change_password":
            password = raw[2]
            database.change_password(id, password)
        elif command == "change_username":
            username = raw[2]
            database.change_username(id, username)
        elif command == "match_question":
            question = raw[2]
            answer = raw[3]
            username = raw[4]
            raw = database.match_question(username, question, answer)
            current_socket.send(self.encode(str(raw)))
        elif command == "change_password2":
            username = raw[2]
            password = raw[3]
            database.change_password2(username, password)
        elif command == "get_chat":
            type = raw[2]
            name = raw[3]
            if type == "friend":
                raw = database.get_chat_friend(id, name)
                current_socket.send(self.encode(str(raw)))
            else:
                raw = database.get_chat_group(name)
                current_socket.send(self.encode(str(raw)))
        elif command == "send_message":
            chat = raw[2]
            data = raw[3]
            type = raw[4]
            if type == "friend":
                database.send_msg_friend(id, chat, data)
                self.to_send_list.append((current_socket, database.get_name(id), type))
            else:
                database.send_msg_group(id, chat, data)
                self.to_send_list.append((current_socket, chat, type))

    def send_msg(self, message):
        """
        send message to the clients
        :param message: list that contains the chat's name and type
        :type message: list
        :return: nothing
        """
        current_socket = message[0]
        chat = message[1]
        type = message[2]
        command = "update_chat"
        if type == "friend2":
            command = "update_friend"
        elif type == "group2":
            command = "update_group"
        for rec_socket in self.client_sockets:
            if rec_socket != current_socket:
                raw = command + "|" + chat + "|" + type
                rec_socket.send(self.encode(str(raw)))

    def remove_client(self, current_socket):
        """
        removes client from the clients list and disconnects him from the server
        :param current_socket: client's socket
        :type current_socket: socket
        :return: nothing
        """
        self.client_sockets.remove(current_socket)
        current_socket.close()

    def manager(self):
        """
        manages the sending and receiving of messages
        :return: nothing
        """
        self.read_list, self.write_list, self.error_list = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
        for current_socket in self.read_list:
            if current_socket is self.server_socket:
                self.add_client(current_socket)
            else:
                self.recv_raw(current_socket)
        for message in self.to_send_list:
            current_socket = message[0]
            if current_socket in self.write_list:
                self.send_msg(message)
            self.to_send_list.remove(message)


def main():
    server = Server()
    database.main()
    database.print_tables()
    while True:
        server.manager()


if __name__ == "__main__":
    main()
