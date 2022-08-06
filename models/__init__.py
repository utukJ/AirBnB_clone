#!/usr/bin/python3

"""init file storage module"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
