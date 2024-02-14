from objackson.serializer import json2obj


if __name__ == "__main__":

    class Test1:
        def __init__(self, x=3, y=5):
            self.x = x
            self.y = y

        def __str__(self):
            return "Test1{test1_field1=" + self.test1_field1 + "}"

        def __repr__(self):
            return str(self)

    loaded_json = json2obj(
        "{"
        '"test2_field1": "test2", '
        '"test2_field2": {"test1_field1": "test1", "__json_object_type_name__": "Test1"}, '
        '"__json_object_type_name__": "Test2"'
        "}"
    )
    print("loaded_json:", loaded_json)

    dumped_json = obj2json(loaded_json)
    print("dumped_json:", dumped_json)