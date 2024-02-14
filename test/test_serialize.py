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

from objackson import obj2json, json2obj, JSONObject
from unittest import TestCase

class TestClass:
    def __init__(self, x=3, y=5):
        self.x = x
        self.y = y
        
    def __eq__(self, __value: object) -> bool:
        __value: TestClass
        return self.x == __value.x and self.y == __value.y
    
class TestSerialize(TestCase):
    
    def test_obj2json(self):
        obj1 = TestClass()
        json1 = obj2json(obj1)
        
        obj2 = json2obj(json1)
        self.assertEqual(obj2, obj1)
        
        json2 = obj2json(obj2)
        self.assertEqual(json2, json1)
        
        obj3 = json2obj(json2)
        self.assertEqual(obj3, obj1)
    
    def test_custom_object(self):
        
        custom_object = {
            "x": 3,
            "y": 5
        }
        dumped_json = obj2json(custom_object)
        test_obj = json2obj(dumped_json)
        
        self.assertIsInstance(test_obj, JSONObject)
        
        self.assertEqual(
            TestClass(3,5),
            test_obj
        )
        
        
    def test_encode_refs(self):
        class ClassEncodeRef:
            def __init__(self):
                self.x = None
                self.y = None
                
        value = 5        
        
        obj1 = ClassEncodeRef()
        obj2 = ClassEncodeRef()
        obj3 = ClassEncodeRef()
        obj1.x = obj2
        obj1.y = obj3
        obj2.x = obj3
        obj1.x.x.x = value
        
        json = obj2json(obj1)
        self.assertGreaterEqual(json.find("__json_type_ref__"), 0)
        print(json)
        
        result_obj = json2obj(json)
        
        self.assertEqual(result_obj.x.x.x, value)
        
    def test_noencode_refs(self):
        class ClassNoEncodeRef:
            def __init__(self):
                self.x = None
                self.y = None
                
        value = 5        
        
        obj1 = ClassNoEncodeRef()
        obj2 = ClassNoEncodeRef()
        obj3 = ClassNoEncodeRef()
        obj1.x = obj2
        obj1.y = obj3
        obj2.x = obj3
        obj1.x.x.x = value
        
        json = obj2json(obj1, encode_refs=False)
        self.assertLess(json.find("__json_type_ref__"), 0)
        print(json)
        
        result_obj = json2obj(json)
        
        self.assertEqual(result_obj.x.x.x, value)
        
    
    def test_circular(self):
        class ClassCircular:
            def __init__(self):
                self.x = None
        
        ref1 = ClassCircular()
        ref2 = ClassCircular()
        ref1.x = ref2
        ref2.x = ref1
        
        json = obj2json(ref1)
        print(json)
        
        obj = json2obj(json)