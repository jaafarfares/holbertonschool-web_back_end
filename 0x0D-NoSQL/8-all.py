#!/usr/bin/python3
""" mongodb
 Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    return mongo_collection.find()
