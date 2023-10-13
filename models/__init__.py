#!/usr/bin/python3

"""
=> FileStorage Initialization:

storage = FileStorage(): This creates an instance of
the FileStorage class. FileStorage is a class
responsible for managing the serialization and
deserialization of objects to and from a JSON file.

=> Unique Instance:

This initialization is intended to create a unique
instance for the application. This means that this particular
FileStorage instance will be used throughout
your application's lifecycle. It will be the
central point for handling the storage and
retrieval of objects.

=> reload() Method:

storage.reload(): This method is presumably
responsible for deserializing any existing
data from the JSON file. This is crucial for
restoring the previous state of objects if the
application has been run before.

For example, if the application was run
previously and some objects were stored in the
JSON file, calling reload() would load those
objects back into the FileStorage instance.

"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
