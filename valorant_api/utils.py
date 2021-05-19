import re
from typing import Dict, Any
from valorant_api.exceptions import AttributeExistsError


def snakeit(string: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


class Mapper(object):
    raw_data: Dict[str, Any]

    def __init__(self):
        pass

    def map(self, childclasses={}, childdata=None):
        raw_data = childdata if childdata is not None else self.raw_data
        for key, value in raw_data.items():
            key_snake = snakeit(key)
            if hasattr(self, key_snake):
                raise AttributeExistsError(f"{self} already has '{key_snake}' attribute.")
            if isinstance(value, dict):
                child = childclasses[key.title()](value)
                child.map()
                setattr(self, key_snake, child)
            elif isinstance(value, list):
                lst = []
                for x in value:
                    child = childclasses[key]()
                    child.map(childdata=x)
                    lst.append(child)
                    setattr(self, key_snake, lst)
            else:        
                setattr(self, key_snake, value)
