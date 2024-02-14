#    Copyright 2024 Salvatore Giampà
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

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