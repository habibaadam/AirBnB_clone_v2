#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str):  string - path to the JSON file (ex: file.json)
        __objects (dict): dictionary - empty but will store all objects by
        class.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If `cls` is provided, it returns a dictionary containing only objects
        of the specified class.
        """
        if cls is None:
            return FileStorage.__objects
        else:
            objs = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    objs[key] = value
            return objs

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        data = {k: obj.to_dict() for k, obj in
                self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(self.__file_path) as f:
                data = f.read()
                if not data:  # empty file
                    return
                obj_dict = json.loads(data)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()