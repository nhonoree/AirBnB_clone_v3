class FileStorage:
    # ... existing code ...

    def get(self, cls, id):
        """Retrieve one object based on class and ID."""
        if cls and id:
            key = f"{cls.__name__}.{id}"
            return self.__objects.get(key, None)
        return None

    def count(self, cls=None):
        """Count the number of objects in storage, optionally filtered by class."""
        if cls:
            return len([obj for obj in self.__objects.values() if isinstance(obj, cls)])
        else:
            return len(self.__objects)
