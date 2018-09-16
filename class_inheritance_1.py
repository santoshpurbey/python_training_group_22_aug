class User:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name  = " + self.name)

class Programmer(User):
    def __init__(self, name, email):
        self.email = email
        super().__init__(name)

    def doPython(self):
        print("Programming Python")

if __name__ == "__main__":
    brian = User("brian")
    brian.printName()

    diana = Programmer("Diana", 'sa@hh.com')
    diana.printName()
    diana.doPython()
    print(diana.email)
