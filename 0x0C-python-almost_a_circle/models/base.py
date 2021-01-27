#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """dictionary to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs=None):
        """saves json string to file"""
        dicti = []
        if list_objs is not None:
            for obj in list_objs:
                output.append(cls.to_dictionary(obj))
        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(output))

    def from_json_string(json_string):
        """json to dictionary"""
        if type(json_string) is not str and json_string is not None:
            raise TypeError("must be a string")
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new instance"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        instances = []
        try:
            with open("{}.json".format(cls.__name__)) as file:
                loaded = cls.from_json_string(file.read())
                for item in loaded:
                    instances.append(cls.create(**item))
                return instances
        except:
            return instances
