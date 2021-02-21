from typing import Union, Optional, Any, Generic, TypeVar

T = TypeVar('T')


class BaseList(list, Generic[T]):
    _list: list

    def __init__(self, data: list):
        self._list = data
        super(BaseList, self).__init__(self._list)
        self._index = -1

    def __iter__(self):
        for x in self._list:
            yield x

    def find_first(self, **kwargs) -> Union[Optional[Any], None]:
        """:returns None if not found else first matching result"""
        kwargs = dict((k.lower(), v.lower()) for k, v in kwargs.items())  # to lower case key/value
        searchkeys = [x for x in list(kwargs.keys())]
        x: dict[str, str]
        for datacls in self._list:
            x = datacls.raw_data
            for key, val in x.items():
                key = key.lower()
                if isinstance(val, str):
                    val = val.lower()

                if key in searchkeys:
                    if val == kwargs[key].lower():
                        return datacls

        return None

    def find_where(self, **kwargs) -> Union[list, None]:
        """:returns empty list if not found else list of matching result"""
        result = []
        kwargs = dict((k.lower(), v.lower()) for k, v in kwargs.items())  # to lower case key/value
        searchkeys = [x for x in list(kwargs.keys())]
        x: dict[str, str]
        for datacls in self._list:
            x = datacls.raw_data
            for key, val in x.items():
                key = key.lower()
                if isinstance(val, str):
                    val = val.lower()

                if key in searchkeys:
                    if val == kwargs[key].lower():
                        result.append(datacls)
        return result