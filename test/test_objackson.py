from objackson import obj2json, json2obj, JSONObject
from unittest import TestCase

class TestClass:
    def __init__(self, x=3, y=5):
        self.x = x
        self.y = y
        
    def __eq__(self, __value: object) -> bool:
        __value: TestClass
        return self.x == __value.x and self.y == __value.y
class ObjacksonTest(TestCase):
    
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