#!/usr/bin/python3
"""class"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        if attrs is None or type(attrs) is not list:
            return vars(self)
        else:
            new = {}
            for x in attrs:
                if type(x) is str:
                    try:
                        new[x] = self.__dict__[x]
                    except:
                        pass
            return new

    def reload_from_json(self, json):
        """replaces  with json"""
        for x in json:
            try:
                self.__dict__[x] = json[x]
            except:
                pass
