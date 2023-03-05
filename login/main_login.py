from dotenv import load_dotenv
load_dotenv()
import os

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username=os.getenv('USERNAME'), password=os.getenv('PASSWORD')))