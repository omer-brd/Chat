import sqlite3
import os
import time


def print_tables():
    """
    print the tables
    :return: nothing
    """
    database.print_tables()


def exist(username):
    """
    checks if the username exists
    :param username: the wanted name of the client
    :type username: string
    :return: username exist?
    :rtype: bool
    """
    return database.exist(username)


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
    return database.match(username, password)


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
    database.insert(username, password, question, answer)


def get_id_by_name(username):
    """
    returns id by name
    :param username:
    :return: id
    :rtype: int
    """
    return database.get_id_by_name(username)


def get_color_by_id(id):
    """
    returns color by id
    :param id: id
    :return: color
    :rtype: string
    """
    return database.get_color_by_id(id)


def get_name(id):
    """
    returns name by id
    :param id: id
    :return: name
    :rtype: string
    """
    return database.get_name(id)


def add_friend(id, friend):
    """
    adds a friend
    :param friend: the name of the friend
    :type friend: string
    :return: nothing
    """
    database.add_friend(id, friend)


def remove_friend(id, friend):
    """
    removes a friend
    :param id: the id of the client
    :type id: int
    :param friend: the name of the friend
    :type friend: string
    :return: nothing
    """
    database.remove_friend(id, friend)


def friend_exist(id, friend):
    """
    checks if friend exist
    :param id: the id of the friend
    :type id: int
    :param friend: the name of the friend
    :type friend: string
    :return: friend exist?
    :rtype: bool
    """
    return database.friend_exist(id, friend)


def get_friends(id):
    """
    returns friends
    :param id: the id of the client
    :type id: int
    :return: friends
    :rtype: list
    """
    return database.get_friends(id)


def group_exist(group):
    """
    checks if the group exists
    :param group: the wanted name of the group
    :type group: string
    :return: group exist?
    :rtype: bool
    """
    return database.group_exist(group)


def create_group(group, members):
    """
    creates a group
    :param group: the name of the group
    :type group: string
    :param members: the members of the group
    :type members: string
    :return: nothing
    """
    database.create_group(group, members)


def get_groups(id):
    """
    returns client's groups
    :param id: the id of the client
    :type id: int
    :return: client's groups
    :rtype: list
    """
    return database.get_groups(database.get_name(id))


def leave_group(id, group):
    """
    leaves group
    :param id: the id of the client
    :type id: int
    :param group: the name of the group
    :return: nothing
    """
    database.leave_group(database.get_name(id), group)


def change_password(id, password):
    """
    changes the password of the client
    :param id: the id of the friend
    :type id: int
    :param password: new password
    :type password: string
    :return: nothing
    """
    database.change_password(id, password)


def change_password2(username, password):
    """
    changes the password of the client
    :param username: username of the client
    :type username: string
    :param password: new password
    :type password: string
    :return: nothing
    """
    database.change_password2(username, password)


def change_username(id, username):
    """
    changes the name of the client
    :param id: the id of the friend
    :type id: int
    :param username: new name
    :type username: string
    :return: nothing
    """
    database.change_username(id, username)


def match_question(username, question, answer):
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
    return database.match_question(username, question, answer)


def get_chat_group(name):
    """
    returns the chat history
    :param name: the name of the chat
    :type name: string
    :return: chat history
    :rtype: string
    """
    return database.get_chat_group(name)


def get_chat_friend(id, friend):
    """
    returns the chat history
    :param id: the id of the friend
    :type id: int
    :param friend: the name of the chat
    :type friend: string
    :return: chat history
    :rtype: string
    """
    return database.get_chat_friend(database.get_name(id), friend)


def send_msg_group(id, chat, data):
    """
    sending a message from the client
    :param id: the id of the client
    :type id: int
    :param chat: the name of the chat
    :type chat: string
    :param data: content of the message
    :return: nothing
    """
    database.send_msg_group(id, chat, data)


def send_msg_friend(id, chat, data):
    """
    sending a message from the client
    :param id: the id of the client
    :type id: int
    :param chat: the name of the chat
    :type chat: string
    :param data: content of the message
    :return: nothing
    """
    database.send_msg_friend(id, chat, data)


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.groups = self.conn.cursor()
        self.path = '/Cyber 11th 2021/Chat Project/Groups'
        self.path2 = '/Cyber 11th 2021/Chat Project/Friends'
        self.users.execute("""CREATE TABLE IF NOT EXISTS USERS (
            USERNAME TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL,
            QUESTION TEXT NOT NULL,
            ANSWER TEXT NOT NULL,
            COLOR TEXT NOT NULL,
            FRIENDS TEXT
            );""")
        self.groups.execute("""CREATE TABLE IF NOT EXISTS GROUPS (
            NAME TEXT NOT NULL UNIQUE,
            MEMBERS TEXT
            );""")
        self.COLORS = ["#d21212", "#FF8000", "#FFFF00", "#139113", "#0ed7d7", "#4040d1", "#a861ee", "#c54cc5", "#f25d31", "#4dd0e1"]
        self.conn.commit()
        self.conn.close()
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if not os.path.exists(self.path2):
            os.mkdir(self.path2)
            self.create_group("everyone", "")

    def print_tables(self):
        """
        prints the tables
        :return: nothing
        """
        self.print_users()
        self.print_groups()

    def exist(self, username):
        """
        checks if the username exists
        :param username: the wanted name of the client
        :type username: string
        :return: username exist?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}'""")
        num = len(self.users.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

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
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}' AND PASSWORD = '{password}'""")
        num = len(self.users.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def get_id_by_name(self, username):
        """
        returns id by name
        :param username:
        :return: id
        :rtype: int
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}'""")
        id = self.users.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return id

    def get_name(self, id):
        """
        returns name by id
        :param id: id
        :return: name
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT USERNAME FROM USERS WHERE ROWID = '{id}'""")
        name = self.users.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return name

    def get_color(self, id):
        """
        returns color by id
        :param id: id
        :return: color
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT COLOR FROM USERS WHERE ROWID = '{id}'""")
        color = self.users.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return color

    def get_color_by_id(self, id):
        """
        returns color by id
        :param id: id
        :return: color
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT COLOR FROM USERS WHERE ROWID = '{id}'""")
        color = self.users.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return color

    def insert(self, username, password, question, answer):
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
        color = self.get_color()
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"INSERT INTO USERS VALUES ('{username}', '{password}', '{question}', '{answer}', '{color}', '')")
        self.conn.commit()
        self.conn.close()
        self.add_member(username)

    def change_password(self, id, password):
        """
        changes the password of the client
        :param id: the id of the friend
        :type id: int
        :param password: new password
        :type password: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""UPDATE USERS SET PASSWORD = '{password}' WHERE ROWID = '{id}'""")
        self.conn.commit()
        self.conn.close()

    def change_password2(self, username, password):
        """
        changes the password of the client
        :param username: username of the client
        :type username: string
        :param password: new password
        :type password: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""UPDATE USERS SET PASSWORD = '{password}' WHERE USERNAME = '{username}'""")
        self.conn.commit()
        self.conn.close()

    def change_username(self, id, username):
        """
        changes the name of the client
        :param id: the id of the friend
        :type id: int
        :param username: new name
        :type username: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.groups = self.conn.cursor()
        self.users.execute(f"""SELECT USERNAME FROM USERS WHERE ROWID = '{id}'""")
        old_username = self.users.fetchone()[0]
        self.users.execute(f"""UPDATE USERS SET USERNAME = '{username}' WHERE ROWID = '{id}'""")
        self.users.execute(f"""SELECT * FROM USERS""")
        raw_users = self.users.fetchall()
        for user in raw_users:
            curr_name = user[0]
            self.users.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{curr_name}'""")
            curr_id = self.users.fetchone()[0]
            self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{curr_id}'""")
            friends = self.users.fetchone()[0]
            friends = friends.replace(old_username + ",", username + ",")
            self.users.execute(f"""UPDATE USERS SET FRIENDS = '{friends}' WHERE ROWID = '{curr_id}'""")
            if os.path.isfile(self.path2 + "/" + old_username + "-" + curr_name + ".txt"):
                os.rename(self.path2 + "/" + old_username + "-" + curr_name + ".txt", self.path2 + "/" + username + "-" + curr_name + ".txt")
            elif os.path.isfile(self.path2 + "/" + curr_name + "-" + old_username + ".txt"):
                os.rename(self.path2 + "/" + curr_name + "-" + old_username + ".txt", self.path2 + "/" + curr_name + "-" + username + ".txt")
        self.groups.execute(f"""SELECT * FROM GROUPS""")
        raw_groups = self.groups.fetchall()
        for group in raw_groups:
            curr_name = group[0]
            self.groups.execute(f"""SELECT MEMBERS FROM GROUPS WHERE NAME = '{curr_name}'""")
            members = self.groups.fetchone()[0]
            members = members.replace(old_username + ",", username + ",")
            self.groups.execute(f"""UPDATE GROUPS SET MEMBERS = '{members}' WHERE NAME = '{curr_name}'""")
        self.conn.commit()
        self.conn.close()

    def add_friend(self, id, friend):
        """
        adds a friend
        :param friend: the name of the friend
        :type friend: string
        :return: nothing
        """
        friend_id = self.get_id_by_name(friend)
        user_name = self.get_name(id)
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{id}'""")
        friends = self.users.fetchone()[0]
        self.users.execute(f"""UPDATE USERS SET FRIENDS = '{friends + friend},' WHERE ROWID = '{id}'""")
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{friend_id}'""")
        friends = self.users.fetchone()[0]
        self.users.execute(f"""UPDATE USERS SET FRIENDS = '{friends + user_name},' WHERE ROWID = '{friend_id}'""")
        self.conn.commit()
        self.conn.close()
        open(self.path2 + "/" + user_name + "-" + friend + ".txt", "a").close()
        file = open(self.path2 + "/" + user_name + "-" + friend + ".txt", "a")
        file.write(str(id) + "!@joined the chat!@--" + "<--->\n")
        file.write(str(friend_id) + "!@joined the chat!@--" + "<--->\n")
        file.close()

    def remove_friend(self, id, friend):
        """
        removes a friend
        :param id: the id of the client
        :type id: int
        :param friend: the name of the friend
        :type friend: string
        :return: nothing
        """
        friend_id = self.get_id_by_name(friend)
        user_name = self.get_name(id)
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{id}'""")
        friend += ","
        friends = self.users.fetchone()[0]
        friends = friends.replace(friend, "")
        self.users.execute(f"""UPDATE USERS SET FRIENDS = '{friends}' WHERE ROWID = '{id}'""")
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{friend_id}'""")
        user_name += ","
        new_friends = self.users.fetchone()[0]
        new_friends = new_friends.replace(user_name, "")
        self.users.execute(f"""UPDATE USERS SET FRIENDS = '{new_friends}' WHERE ROWID = '{friend_id}'""")
        self.conn.commit()
        self.conn.close()
        try:
            if os.path.isfile(self.path2 + "/" + user_name[:-1] + "-" + friend[:-1] + ".txt"):
                os.remove(self.path2 + "/" + user_name[:-1] + "-" + friend[:-1] + ".txt")
            elif os.path.isfile(self.path2 + "/" + friend[:-1] + "-" + user_name[:-1] + ".txt"):
                os.remove(self.path2 + "/" + friend[:-1] + "-" + user_name[:-1] + ".txt")
        except:
            pass

    def friend_exist(self, id, friend):
        """
        checks if friend exist
        :param id: the id of the friend
        :type id: int
        :param friend: the name of the friend
        :type friend: string
        :return: friend exist?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{id}'""")
        fr_exist = False
        friends = self.users.fetchone()[0].split(",")
        for curr_friend in friends:
            if curr_friend == friend:
                fr_exist = True
        self.conn.commit()
        self.conn.close()
        return fr_exist

    def get_friends(self, id):
        """
        returns client's groups
        :param id: the id of the client
        :type id: int
        :return: client's groups
        :rtype: list
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT FRIENDS FROM USERS WHERE ROWID = '{id}'""")
        friends = self.users.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return friends

    def get_color(self):
        """
        returns current color
        :return: color
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT ROWID FROM USERS""")
        num = len(self.users.fetchall())
        self.conn.commit()
        self.conn.close()
        return self.COLORS[num % 10]

    def create_group(self, name, members):
        """
        creates a group
        :param name: the name of the group
        :type name: string
        :param members: the members of the group
        :type members: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute(f"INSERT INTO GROUPS VALUES ('{name}', '{members}')")
        self.conn.commit()
        self.conn.close()
        open(self.path + "/" + name + ".txt", "a").close()
        file = open(self.path + "/" + name + ".txt", "a")
        members = members.split(",")
        members.pop()
        for member in members:
            file.write(str(self.get_id_by_name(member)) + "!@joined the chat!@--" + "<--->\n")
        file.close()

    def group_exist(self, group):
        """
        checks if the group exists
        :param group: the wanted name of the group
        :type group: string
        :return: group exist?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute(f"""SELECT ROWID FROM GROUPS WHERE NAME = '{group}'""")
        num = len(self.groups.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def get_groups(self, name):
        """
        returns client's groups
        :param name: the name of the client
        :type name: string
        :return: client's groups
        :rtype: list
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute(f"""SELECT * FROM GROUPS""")
        raw_groups = self.groups.fetchall()
        user_groups = ""
        for group in raw_groups:
            members = group[1].split(",")
            for member in members:
                if member == name:
                    user_groups += group[0] + ","
        self.conn.commit()
        self.conn.close()
        return user_groups

    def leave_group(self, name, group):
        """
        leaves group
        :param name: the name of the client
        :type name: string
        :param group: the name of the group
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute(f"""SELECT * FROM GROUPS WHERE NAME = '{group}'""")
        curr_group_members = self.groups.fetchone()[1].split(",")
        curr_group_members.remove(name)
        new_members = ""
        for new_member in curr_group_members:
            new_members += new_member + ","
        if new_members == ",":
            self.groups.execute(f"DELETE from GROUPS WHERE NAME = '{group}'")
        else:
            self.groups.execute(f"""UPDATE GROUPS SET MEMBERS = '{new_members[:-1]}' WHERE NAME = '{group}'""")
        self.conn.commit()
        self.conn.close()
        if new_members == ",":
            os.remove(self.path + "/" + group + ".txt")
        else:
            file = open(self.path + "/" + group + ".txt", "a")
            file.write(str(self.get_id_by_name(name)) + "!@left the chat!@--" + "<--->\n")
            file.close()

    def match_question(self, username, question, answer):
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
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}' AND QUESTION = '{question}' AND ANSWER = '{answer}'""")
        num = len(self.users.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def add_member(self, member):
        """
        adds member to everybody group
        :param member: new member
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute(f"""SELECT * FROM GROUPS WHERE NAME = 'everyone'""")
        fetch = self.groups.fetchone()
        if fetch == None:
            curr_group_members = ""
        else:
            curr_group_members = fetch[1]
        curr_group_members += member + ","
        self.groups.execute(f"""UPDATE GROUPS SET MEMBERS = '{curr_group_members}' WHERE NAME = 'everyone'""")
        self.conn.commit()
        self.conn.close()
        file = open(self.path + "/everyone.txt", "a")
        file.write(str(self.get_id_by_name(member)) + "!@joined the chat!@--" + "<--->\n")
        file.close()

    def get_chat_group(self, name):
        """
        returns the chat history
        :param name: the name of the chat
        :type name: string
        :return: chat history
        :rtype: string
        """
        file = open(self.path + "/" + name + ".txt", "r")
        raw_messages = file.read().split("<--->\n")
        raw_messages.pop()
        messages_list = ""
        for message in raw_messages:
            id = message.split("!@")[0]
            data = message.split("!@")[1]
            time = message.split("!@")[2]
            color = self.get_color_by_id(id)
            name = self.get_name(id)
            messages_list += name + "!@" + color + "!@" + time + "!@" + data + "<--->"
        return messages_list

    def get_chat_friend(self, user, friend):
        """
        returns the chat history
        :param user: the user of the friend
        :type user: string
        :param friend: the name of the chat
        :type friend: string
        :return: chat history
        :rtype: string
        """
        try:
            if os.path.isfile(self.path2 + "/" + user + "-" + friend + ".txt"):
                file = open(self.path2 + "/" + user + "-" + friend + ".txt", "r")
            else:
                file = open(self.path2 + "/" + friend + "-" + user + ".txt", "r")
        except:
            pass
        raw_messages = file.read().split("<--->\n")
        raw_messages.pop()
        messages_list = ""
        for message in raw_messages:
            id = message.split("!@")[0]
            data = message.split("!@")[1]
            time = message.split("!@")[2]
            color = self.get_color_by_id(id)
            name = self.get_name(id)
            messages_list += name + "!@" + color + "!@" + time + "!@" + data + "<--->"
        return messages_list

    def send_msg_group(self, id, chat, data):
        """
        sending a message from the client
        :param id: the id of the client
        :type id: int
        :param chat: the name of the chat
        :type chat: string
        :param data: content of the message
        :return: nothing
        """
        t = time.strftime(" %m/%d/%Y %H:%M", time.localtime())
        file = open(self.path + "/" + chat + ".txt", "a")
        file.write(id + "!@" + data + "!@" + t + "<--->\n")
        file.close()

    def send_msg_friend(self, id, chat, data):
        """
        sending a message from the client
        :param id: the id of the client
        :type id: int
        :param chat: the name of the chat
        :type chat: string
        :param data: content of the message
        :return: nothing
        """
        user_name = self.get_name(id)
        t = time.strftime(" %m/%d/%Y %H:%M", time.localtime())
        try:
            if os.path.isfile(self.path2 + "/" + user_name + "-" + chat + ".txt"):
                file = open(self.path2 + "/" + user_name + "-" + chat + ".txt", "a")
                file.write(id + "!@" + data + "!@" + t + "<--->\n")
            elif os.path.isfile(self.path2 + "/" + chat + "-" + user_name + ".txt"):
                file = open(self.path2 + "/" + chat + "-" + user_name + ".txt", "a")
                file.write(id + "!@" + data + "!@" + t + "<--->\n")
        except:
            pass
        file.close()

    def print_users(self):
        """
        prints the users table
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.users = self.conn.cursor()
        self.users.execute("SELECT * FROM USERS")
        users = self.users.fetchall()
        print("-----USERS-----")
        for user in users:
            print("/>>Name: " + user[0])
            print("|--Password: " + user[1])
            print("|--Question: " + user[2])
            print("|--Answer: " + user[3])
            print("|--Color: " + user[4])
            print("|--Friends: " + user[5])
            print()
        self.conn.commit()
        self.conn.close()

    def print_groups(self):
        """
        prints the groups table
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.groups = self.conn.cursor()
        self.groups.execute("SELECT * FROM GROUPS")
        groups = self.groups.fetchall()
        print("-----GROUPS-----")
        for group in groups:
            print("/>>Name: " + group[0])
            print("|--Members: " + group[1])
            print()
        self.conn.commit()
        self.conn.close()


def main():
    global database
    database = DataBase()
