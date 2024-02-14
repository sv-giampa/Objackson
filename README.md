# Objackson
This is a JSON serializer for Python that supports deep serialization of objects and full reconstruction of object structure on deserialization.
Circular references are supported too.

# How to install
Install latest version of Objackson from PyPI:

    python3 -m pip install objackson

# How to use

    from objackson import obj2json, json2obj

    class MyClass:

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y
        
        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        def __eq__(self, obj)
            return self.x == obj.x and self.y = obj.y
        
    def main():
        obj1 = TestClass(2, 3)
        json = obj2json(obj1)
        obj2 = json2obj(json)

        # obj2 is a copy of obj1. Test it:
        if obj1 == obj2:
            print("SUCCESS")
        else:
            print("FAIL")

    if __name__ == "__main__"
        main()


For a class to be serializable, it must have a constructor that allows zero-arguments initialization.
