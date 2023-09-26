
class Stringclass:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())


def test_string_class1():
    class1 = Stringclass()
    class1.getString()

    class1.printString()

if __name__ == "__main__":
    test_string_class1()

