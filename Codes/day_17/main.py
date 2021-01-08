class User:
    # name = "Anushka"
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("Hello from Class")

    def follow(self, user):
        user.followers += 1
        self.following += 1


usr1 = User("001", "User One")
usr2 = User("002", "User Two")

usr1.follow(usr2)

print(usr1.followers)
print(usr1.following)
print(usr1.followers)
print(usr1.following)
# usr.followers = 100
# print(usr.followers)
# print(usr.id + " " + usr.username)
# print(usr)
