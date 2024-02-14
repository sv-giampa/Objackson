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

import json
from typing import Dict
import sys

from objackson.json_object import JSONObject

def obj2json(obj) -> str:
    def default(obj) -> Dict:
        obj_type: type = type(obj)
        json_repr = dict(obj.__dict__) if hasattr(obj, "__dict__") else {}
        if isinstance(obj, JSONObject):
            if "__json_object_type_name__" in json_repr:
                json_repr["__json_object_type_name__"] = obj.__dict__[
                    "__json_object_type_name__"
                ]
            if "__json_object_type_module__" in json_repr:
                json_repr["__json_object_type_module__"] = obj.__dict__[
                    "__json_object_type_module__"
                ]
        else:
            json_repr["__json_object_type_name__"] = obj_type.__qualname__
            json_repr["__json_object_type_module__"] = obj_type.__module__

        return json_repr

    return json.dumps(obj, default=default)


def json2obj(json_str: str) -> object:
    def object_hook(json_dict: Dict):
        obj_dict = dict(json_dict)
        obj = None
        if (
            "__json_object_type_name__" in json_dict
            and "__json_object_type_module__" in json_dict
        ):
            obj_class_name = json_dict["__json_object_type_name__"]
            obj_class_module = json_dict["__json_object_type_module__"]
            try:
                obj_class = getattr(sys.modules[obj_class_module], obj_class_name)
                obj = obj_class()
                del obj_dict["__json_object_type_name__"]
                del obj_dict["__json_object_type_module__"]
            except AttributeError:
                pass
        #                print('WARNING: class \'' + obj_class_name + '\' was not found in the Python environment. ' +
        #                       'Loading as a '+GenericObject.__name__+'...')
        else:
            pass
        #            print('WARNING: field __json_object_type_name__ was not found in for a JSON object. '
        #                  'Loading as a JsonObject...')

        if obj is None:
            obj = JSONObject()

        obj.__dict__ = obj_dict
        return obj

    return json.loads(json_str, object_hook=object_hook)