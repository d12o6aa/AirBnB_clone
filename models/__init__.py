#!/usr/bin/python3

"""
Update for models/__init__.py: to create a
unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
