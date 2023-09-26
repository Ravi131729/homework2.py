

class MyClass:
    class_param = "I am a class parameter"

    def __init__(self, instance_param):
        self.instance_param = instance_param

obj = MyClass("I am an instance parameter")

print(MyClass.class_param)
print(obj.instance_param)
