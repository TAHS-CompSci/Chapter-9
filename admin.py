from user import User

class Admin(User):
    def __init__(self, first_name, last_name, password, username, gender):
        super().__init__(first_name, last_name, password, username, gender)
        priviliges = ['can add post', 'can delete post', 'can ban user', 'can un-ban user']
        self.priviliges = Priviliges()

class Priviliges():
    def __init__(self, priviliges = ['can add post', 'can delete post', 'can ban user', 'can un-ban user']):
        self.priviliges = priviliges
    def show_priviliges(self):
        print(str(self.priviliges))