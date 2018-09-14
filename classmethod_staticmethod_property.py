import  random
class Animal:
    """
    This is Animal class for test
    """
    def __init__(self, name, legs=None, color="white", sound=""):
        if legs is None:
            legs = random.choice(range(2, 6))
        self.name = name
        self.legs = legs
        self.color = color
        self.sound = sound

    def speak(self):
        """
        return instance sound
        """
        return self.sound

    def getcolor(self):
        return self.color

    def change_color(self, color):
        self.color = color

    @staticmethod
    def test(message):
        print('this is test:{}'.format(message))

    def __repr__(self):
        return  "Class Animal instance name: {} and legs: {}".format(self.name, self.legs)


if __name__ == "__main__":
    a = Animal('cow', sound='bow')
    print(a)
    print(a.speak())
    a.test('neew')
    Animal.test('hello')
    print(a.getcolor())
    print(a.color)
    a.change_color('green')
    print(a.color)



# from classmethod_staticmethod_property import Animal
