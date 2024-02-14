
class JSONObject:
    def __init__(self):
        pass

    def __str__(self):
        return type(self).__name__ + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self)