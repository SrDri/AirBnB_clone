#!/usr/bin/python3
""" Packages init - aplication """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
