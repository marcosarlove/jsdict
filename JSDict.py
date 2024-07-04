from collections import abc

class JSDict:
    def __new__(cls, obj = {}):
        if isinstance(obj, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(obj, abc.MutableSequence):
            return [cls(item) for item in obj]
        else: return obj

    def __init__(self, obj = {}):
        self.__dict__["_JSDict__data"] = dict(obj)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
           return getattr(self.__data, name)
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __setitem__(self, name, value):
        self.__data.update({name: value})
    
    def __getitem__(self, key):
        return JSDict(self.__data[key])

    def __repr__(self):
        return f"JSDict({repr(self.__data)})"

    def __str__(self):
        return str(self.__data)
    
    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data.keys())

    def copy(self):
        return JSDict(self.__data.copy())
