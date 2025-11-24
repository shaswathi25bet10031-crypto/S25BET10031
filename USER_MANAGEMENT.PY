class User:
    def __init__(self, name):
        self.name = name

def create_user():
    name = input("Enter your name: ")
    return User(name)
