class User():
    def __init__(self, first_name, last_name, password, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ' is ' + self.gender.title())
        print('password = '+  self.password)
        print('Username = ' + self.username)
    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + " thank you for visiting.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
       