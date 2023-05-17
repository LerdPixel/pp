from getpass import getpass
from mysql.connector import connect, Error
from datetime import datetime


db = connect(
        host="localhost",
        user="root",
        password="jojotop12345",
        database="projectPP"
)

mycursor = db.cursor()

class Server:
    def Login(login, password):
        return mycursor.execute("CALL log_in({1}, {2});".format(login, password))
    def SignUp(login, password):
        return mycursor.execute("CALL sign_up({1}, {2});".format(login, password))
    def CreateChat(id1, id2):
        return mycursor.execute("CALL create_chat({1}, {2});".format(id1, id2))
    def NewMessage(chat_ID, str):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        return mycursor.execute("CALL create_message({1}, {2}, {3});".format(chat_id, message, formatted_date))
    def GetMessages(chat_id):
        return mycursor.execute("SELECT message_id, message, time FROM message WHERE chat_id={};".format(chat_id))
    
